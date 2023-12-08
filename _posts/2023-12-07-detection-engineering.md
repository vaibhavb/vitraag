---
author: vitraag
comments: true
date: 2023-12-07 05:06:00+00:00
layout: post
slug: starting-detection-engineering-with-datadog
title: Starting Detection Engineering with Datadog
categories:
- security
---
Detection engineering is an essential discipline for identifying and mitigating threats relevant to an organization. It involves understanding these threats in depth and developing reliable strategies for detection. While there's no standardized process, detection engineering typically includes phases such as ideation, research, gathering requirements, development, testing and deployment, and maintenance.

## The Lifecycle of Detection Engineering

1. **Ideation**: Identifying relevant attack techniques for your organization.
2. **Research**: Understanding how an attack works and the logs it generates.
3. **Gathering Requirements**: Determining the necessary logs and visibility for implementing a detection.
4. **Development**: Creating a concrete strategy and crafting detection rules.
5. **Testing and Deployment**: Ensuring the rules work as expected with minimal false positives or negatives.
6. **Maintenance**: Continuously monitoring and adjusting the detection rules.

## Challenges and Solutions in Detection Engineering

The process involves multiple complex elements, such as log collection, centralization, parsing, indexing, and aggregation. A common challenge is to ensure the proper configuration and functioning of these elements, from log delivery to correct rule behavior.

### Using Threatest for End-to-End Testing

Threatest is a CLI and Go framework that aids in writing end-to-end tests for threat detection rules. It allows the definition of test scenarios, detonation of attack techniques, and verification of expected alerts using the Datadog API. Threatest can run both as a CLI and programmatically, providing a robust way to ensure your detection mechanisms are functioning correctly.

## Python Sample for Fetching and Analyzing Datadog Logs

Here's a basic Python example for fetching and analyzing logs from Datadog:

```python
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import logs_api
from datadog_api_client.v1.models import *
from datetime import datetime, timedelta
import pytz

# Calculate time range
now = datetime.now(pytz.UTC)
fifteen_minutes_ago = now - timedelta(minutes=15)

# Format times in ISO 8601 format
time_from = fifteen_minutes_ago.isoformat()
time_to = now.isoformat()

# Datadog API configuration
configuration = Configuration()
configuration.api_key['apiKey'] = 'YOUR_API_KEY'
configuration.api_key['appKey'] = 'YOUR_APP_KEY'

with ApiClient(configuration) as api_client:
    api_instance = logs_api.LogsApi(api_client)
    body = LogsListRequest(
        index="main",
        query="status:error",
        sort=LogsSort.TIME_DESCENDING,
        time=LogsListRequestTime(
            _from=time_from,
            to=time_to
        )
    )

    try:
        # Fetch logs
        api_response = api_instance.list_logs(body=body)
        logs = api_response.data

        # Detection logic
        for log in logs:
            if "specific_keyword" in log.content:
                print("Detection: ", log.content)

    except ApiException as e:
        print("Exception when calling LogsApi->list_logs: %s\n" % e)
```

Replace 'YOUR_API_KEY', 'YOUR_APP_KEY', and 'specific_keyword' with your actual Datadog API key, application key, and the keyword you're monitoring in the logs.


## Real-World Applications and Examples

### Google Cloud Threat Detection

Security analysts can design detections for behaviors like the anomalous creation of GPU-based VMs, indicative of activities such as cryptomining. Using Google Cloud audit logs, one can validate and detect suspicious activities, including service account misuse or the creation of unusual resources.

### AWS CloudTrail Analysis

Understanding common enumeration techniques used by attackers in AWS environments is crucial. By analyzing CloudTrail logs, one can identify patterns like the creation of IAM users or security groups, or instances attempting to create IAM users. Datadog provides several high-confidence detections for these activities, which can be implemented using CloudTrail SQL.

## How Datadog Can Help

Datadog's Cloud SIEM includes several detection rules that help in identifying malicious activities encountered during threat hunting in AWS environments. These rules cover a range of activities, from IAM user creation to the identification of Tor client IP addresses within the AWS environment.

## Conclusion

Detection engineering is a dynamic and crucial field in cybersecurity. Tools like Threatest, along with Datadog’s Cloud SIEM, provide powerful means to develop, test, and maintain detection rules, ensuring robust security for your organization.

## References

- [Introducing Threatest, a CLI and Go framework for end-to-end testing of threat detection rules](https://securitylabs.datadoghq.com/articles/threatest-end-to-end-testing-threat-detection/)
- [An Adventure in Google Cloud threat detection](https://securitylabs.datadoghq.com/articles/google-cloud-threat-detection/)
- [Following attackers’ (Cloud)trail in AWS: Methodology and findings in the wild](https://securitylabs.datadoghq.com/articles/aws-cloudtrail)
- [SOCless Detection System](https://www.linkedin.com/pulse/socless-detection-team-netflix-alex-maestretti/)
- [Writing Good Security Alerts](https://summitroute.com/blog/2016/11/22/how_to_write_security_alerts/)
- [IR Playbook](https://magoo.medium.com/incident-response-writing-a-playbook-773e7920f171)

By leveraging these tools and methodologies, you can effectively start and refine your journey in detection engineering with Datadog, ensuring a robust defense against evolving cybersecurity threats.
