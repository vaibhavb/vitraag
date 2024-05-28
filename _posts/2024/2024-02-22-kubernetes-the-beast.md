---
author: vitraag
comments: true
date: 2024-02-22 18:41:42+00:00 
layout: post
slug: kubernetes-the-beast
title: Kubernetes The Beast
categories:
    - cloud
    - code
---
Over last week I ended up creating a kubernetes setup with following:
 
- React Frontend
- Flask Backend with flask-sqlalchemy
- Postgres Database
- Nginx reverse proxy
- Hosted in Google cloud

The setup was inspired by (this repo)[]. I learnt to use k9s and kubectl.

Here is how I did the containers, and kubernetes over 3-4 days.

## frontend

### Dockerfile
```
FROM --platform=linux/amd64 node:16-alpine

ADD . /frontend
WORKDIR /frontend
RUN npm install --silent

EXPOSE 3000

RUN npm run build
CMD ["npm", "start"]
```

### Kubernetes
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend
  labels:
    app: frontend
spec:
  replicas: 1
  selector:
    matchLabels:
      app: frontend
  template:
    metadata:
      labels:
        app: frontend
    spec:
      containers:
      - name: react-frontend
        image: vaibhavb/frontend:23
        imagePullPolicy: Always
        ports:
        - containerPort: 3000
        env:
        - name: HOST
          value: 0.0.0.0
        - name: DANGEROUSLY_DISABLE_HOST_CHECK
          value: "true"
---
apiVersion: v1
kind: Service
metadata:
  name: react-service
  labels:
    app: frontend
spec:
  type: ClusterIP
  selector:
    app: frontend
  ports:
  - port: 3000
    targetPort: 3000
```

## backend
### Dockerfile
```
FROM --platform=linux/amd64 python:3.7 as build

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

ENV DATABASE_URI="localhost"
ENV FLASK_APP=main.py

EXPOSE 5000
CMD ["python", "/app/main.py"]
```

### kubernetes
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
  labels:
    app: backend
spec:
  replicas: 1
  selector:
    matchLabels:
      app: backend
  template:
    metadata:
      labels:
        app: backend
    spec:
      containers:
      - name: flask-backend
        image: vaibhavb/backend:12
        imagePullPolicy: Always
        ports:
        - containerPort: 5000
        env:
        - name: DATABASE_URI
          value: pg-service
---
apiVersion: v1
kind: Service
metadata:
  name: flask-service
  labels:
    app: backend
spec:
  type: ClusterIP
  selector:
    app: backend
  ports:
  - port: 5000
    targetPort: 5000
```
## postgres
### Dockerfile
None

### kubernetes
```
apiVersion: v1
data:
  CreateDB.sql: |-
    CREATE TABLE text (
        id serial PRIMARY KEY,
        text VARCHAR ( 100 ) UNIQUE NOT NULL
    );
    INSERT INTO text (text) VALUES ('List of questions below!');
    CREATE TABLE quiz_question (
    id INT PRIMARY KEY,
    question TEXT NOT NULL,
    answer1 TEXT NOT NULL,
    answer2 TEXT NOT NULL,
    answer3 TEXT NOT NULL,
    answer4 TEXT NOT NULL,
    correct_answer INT NOT NULL CHECK(correct_answer BETWEEN 1 AND 4)
    );
    INSERT INTO quiz_question (id, question, answer1, answer2, answer3, answer4, correct_answer) VALUES
      (1, 'What does OSINT stand for?', 'Open System Intelligence', 'Operational Security Intelligence', 'Open Source Intelligence', 'Operational Source Integration', 3),

kind: ConfigMap
metadata:
  name: pg-init-script
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: postgres
  labels:
    app: database
spec:
  replicas: 1
  selector:
    matchLabels:
      app: database
  template:
    metadata:
      labels:
        app: database
    spec:
      containers:
      - name: postgres
        image: postgres
        ports:
        - containerPort: 5432
        volumeMounts:
        - name: sqlscript
          mountPath: /docker-entrypoint-initdb.d
        env:
          - name: POSTGRES_USER
            value: "postgres"
          - name: POSTGRES_PASSWORD
            value: "postgres"
      volumes:
        - name: sqlscript
          configMap:
            name: pg-init-script
---
apiVersion: v1
kind: Service
metadata:
  name: pg-service
  labels:
    app: database
spec:
  type: ClusterIP
  selector:
    app: database
  ports:
  - port: 5432
```

## ingress controller
### Dockerfile
```
helm install ingress-nginx ingress-nginx/ingress-nginx \
                                      --set controller.ingressClass="ingress-nginx"
```

### kubernetes
```
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: kubectlpython-ingress
spec:
  ingressClassName: nginx
  tls:
  rules:
  - host: kubectl.vitraag.com
    http:
      paths:
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: flask-service
            port:
              number: 5000
      - path: /
        pathType: Prefix
        backend:
          service:
            name: react-service
            port:
              number: 3000
```
## google cloud
I use the following script to bring the cluster up and down:

```bash
#!/bin/bash

if [[ "$1" == "down" ]]; then
    gcloud container clusters resize [[CLUSTER_NAME]] --node-pool default-pool --num-nodes 0 --zone [[ZONE_NAME]] --project [[PROJECT_NAME]]
elif [[ "$1" == "up" ]]; then
    gcloud container clusters resize [[CLUSTER_NAME]] --node-pool default-pool --num-nodes 1 --zone [[ZONE_NAME]] --project [[PROJECT_NAME]]
else
    echo "Usage: ./cluster.sh down|up"
fi

```
## bugs

1. I still can't get the containers to use the latest tag
2. Multi-platform build for Docker 
