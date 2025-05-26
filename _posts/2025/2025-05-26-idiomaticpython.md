---
author: vitraag
comments: true
date: 2025-05-24T00:18:18Z
layout: post
slug: idiomatic-python
title: Idiomatic Python 
categories:
    - hackathon
    - python
---
Here some simple SQLModel based user table creation code which i find super idiomatic. 

```
from typing import Optional, Dict
from sqlmodel import SQLModel, Field, create_engine, Session, select, JSON
from sqlalchemy import Column, JSON

class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    lastname: str
    prefs: Optional[Dict] = Field(default_factory=dict, sa_column=Column(JSON))

sqlite_url = "sqlite:///users.db"
engine = create_engine(sqlite_url, echo=True)
SQLModel.metadata.create_all(engine)

user = User(id=1, name="Vaibhav", lastname="Bhandari", prefs={"theme": "dark"})
with Session(engine) as session:
    session.add(user)
    session.commit()

print(user)
```

### Why you may ask?
because
1. ```class User(SQLModel, table=True)``` cleanly defines both a Pydantic model and SQL table schema in one class
2. Using ```sa_column=Column(JSON)``` to correctly define a JSON column in SQLite is clean, explicit and robust, and works well with PostGres as well.


