---
author: vitraag
comments: true
date: 2024-08-20T19:18:18Z
layout: post
slug: top-security-controls 
title: Top Security Controls
categories:
    - cybersecurity
---
# InfoSec Controls, Standards, and Implementation Table

Based on my experience as a software security engineer implementing security products, tools, and policies, I've found the following controls to be most relevant. This table outlines how I typically implement these controls, aligning with standards like SOC2, PCI DSS, ISO 27001, CSA STAR-1, and NIST. While not exhaustive, this approach provides a solid foundation for organizations seeking to enhance their security posture across various compliance frameworks.

| Technical Control | Relevant Standards | Implementation with Policies and Standards |
|-------------------|---------------------|---------------------------------------------|
| 1. Identity and Access Management (IAM) | SOC2: CC6.1, CC6.2, CC6.3<br>PCI DSS: Req. 7, 8<br>ISO 27001: A.9<br>CSA STAR-1: IAM-02, IAM-05, IAM-09<br>NIST SP 800-53: AC-2, IA-2, IA-5 | - Implement an IAM policy<br>- Develop access control procedures<br>- Create user provisioning and de-provisioning processes<br>- Establish password policies<br>- Implement multi-factor authentication |
| 2. Network Security | SOC2: CC6.6, CC6.7<br>PCI DSS: Req. 1, 11<br>ISO 27001: A.13<br>CSA STAR-1: IVS-06, IVS-07, IVS-13<br>NIST SP 800-53: SC-7, AC-4, SI-4 | - Develop network security policy<br>- Implement firewall configuration standards<br>- Create IDS/IPS monitoring procedures<br>- Establish VPN usage guidelines<br>- Implement network segmentation |
| 3. Encryption | SOC2: CC6.7<br>PCI DSS: Req. 3, 4<br>ISO 27001: A.10<br>CSA STAR-1: EKM-02, EKM-03<br>NIST SP 800-53: SC-8, SC-13, SC-28 | - Create data classification policy<br>- Develop encryption standards for data at rest and in transit<br>- Establish key management procedures<br>- Implement cryptographic module validation |
| 4. Endpoint Protection | SOC2: CC6.8<br>PCI DSS: Req. 5<br>ISO 27001: A.8<br>CSA STAR-1: MOS-03, MOS-04, MOS-20<br>NIST SP 800-53: SI-3, SI-7, CM-7 | - Implement endpoint security policy<br>- Develop BYOD guidelines<br>- Create malware protection standards<br>- Establish mobile device management procedures<br>- Implement application whitelisting |
| 5. Logging and Monitoring | SOC2: CC7.2, CC7.3<br>PCI DSS: Req. 10<br>ISO 27001: A.12.4<br>CSA STAR-1: IVS-01, LOG-01<br>NIST SP 800-53: AU-2, AU-6, SI-4 | - Develop logging and monitoring policy<br>- Create incident response procedures<br>- Establish alert thresholds and escalation processes<br>- Implement log retention standards<br>- Conduct regular log reviews |
| 6. Patch and Vulnerability Management | SOC2: CC7.1<br>PCI DSS: Req. 6<br>ISO 27001: A.12.6<br>CSA STAR-1: TVM-02, TVM-03<br>NIST SP 800-53: RA-5, SI-2, CM-8 | - Create vulnerability management policy<br>- Develop patch management procedures<br>- Establish vulnerability scanning frequency standards<br>- Implement a responsible disclosure policy<br>- Maintain software/hardware inventory |
| 7. Secure Development Practices | SOC2: CC8.1<br>PCI DSS: Req. 6<br>ISO 27001: A.14<br>CSA STAR-1: AIS-01, AIS-02<br>NIST SP 800-53: SA-8, SA-11, SA-15 | - Implement secure SDLC policy<br>- Develop coding standards<br>- Create change management procedures<br>- Establish security testing requirements<br>- Implement security-focused code reviews |
| 8. Backup and Recovery | SOC2: CC7.4<br>PCI DSS: Req. 9, 12.10<br>ISO 27001: A.12.3, A.17<br>CSA STAR-1: BCR-01, BCR-02, BCR-03<br>NIST SP 800-53: CP-9, CP-10, IR-4 | - Develop backup and recovery policy<br>- Create disaster recovery plan<br>- Establish backup frequency and retention standards<br>- Implement business continuity testing procedures<br>- Conduct regular recovery exercises |
| 9. Cloud Security | SOC2: CC6.6, CC6.7<br>PCI DSS: Req. 1, 2, 4<br>ISO 27001: A.13, A.15<br>CSA STAR-1: IVS-08, IVS-09<br>NIST SP 800-53: AC-20, SA-9, SC-7 | - Develop cloud security policy<br>- Create cloud provider assessment procedures<br>- Establish data residency requirements<br>- Implement cloud configuration standards<br>- Establish cloud service provider oversight |
| 10. Data Loss Prevention (DLP) | SOC2: CC6.7<br>PCI DSS: Req. 3, 4<br>ISO 27001: A.8.2, A.13.2<br>CSA STAR-1: DCS-01, DSI-02<br>NIST SP 800-53: SC-7, AC-4, SI-4 | - Create data handling policy<br>- Develop data classification standards<br>- Establish DLP monitoring procedures<br>- Implement data exfiltration controls<br>- Conduct regular data flow mapping |
