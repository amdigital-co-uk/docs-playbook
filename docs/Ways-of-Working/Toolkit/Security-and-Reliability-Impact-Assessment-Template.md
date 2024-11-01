---
title: Security and Reliability Impact Assessment Template
tags:
- SRIA
- Default
---

This template is the default template for [Security and Reliability Impact Assessment](../Governance/Technology-Governance/Security-and-Reliability-Impact-Assessment.md) documents. 

## How to use

Make a copy of this template in a branch in the Knowledgebase, ensuring that it is placed alongside the solution's other design documentation.
Submit a Pull request and ensure that appropriate stakeholders are requested to review. If risks or concerns are raised, ensure that senior technical stakeholders such as the VP of Engineering and Principal Engineer are informed. 

It is the responsibility of the [Engineering Owner](../Governance/Problem-Ownership/Engineering-Owner.md) to ensure that the SRIA is performed accurately and that the correct technical stakeholders are informed. 

---

## Solution Project/Feature:

[_link to design documents / tickets_]

## Engineering Owner:

[_name of engineering owner_]

---

## 1. Security Impact Assessment

### 1.1 Overall Impact
   1. [ ] No perceived impact on security. No further assessment is required.
   2. [ ] There is a likely impact on security.

If **No** skip to 2.0. If **Yes**, continue to section 1.2.

### 1.2. General Security Concerns

1. Does this solution introduce new data storage or transmission techniques or systems?  
   
     - [ ] Yes  
     - [ ] No
        
    If Yes, describe the type of data and associated risks:

       
2. Will sensitive or personally identifiable information (PII) be stored, processed, or transmitted?  
     - [ ] Yes  
     - [ ] No
        
    If Yes, specify types of data:
   
3. Does the solution expose any external interfaces (e.g., APIs, web services)?  
     - [ ] Yes  
     - [ ] No 
        
    If Yes, reference relevant parts of technical design covering exposed interfaces:
   
1. Are there any authentication or authorization mechanisms being used or implemented?  
     - [ ] Yes  
     - [ ] No
        
    If No, and 1.2.3 is Yes, specify reasons:

### 1.3. Threat Modelling & Known Vulnerabilities

1. Have you created or updated a threat model for this solution?  
     - [ ] Yes  
     - [ ] No
        
    If no, specify reasons:

2. Does the solution mitigate known vulnerabilities in line with OWASP guidelines (see [OWASP top 10 vulnerabilities](https://owasp.org/www-project-top-ten/){:target="_blank"})?  
     - [ ] Yes  
     - [ ] No
        
    If No, specify reasons:

3. Are there any third-party dependencies that could introduce security risks?  
     - [ ] Yes  
     - [ ] No
        
    If Yes, reference relevant parts of technical design covering relevant third-party dependencies and mitigations:

### 1.4. Maintenance & Security Tests

8. Will this solution impact existing security test strategies (e.g., penetration testing, vulnerability scans)?  
     - [ ] Yes  
     - [ ] No 
        
    If Yes, reference solution test strategy regarding security:

9. Will this solution deviate from any existing maintenance strategy, or require changes to the existing maintenance strategy?  
     - [ ] Yes  
     - [ ] No
        
    If Yes, or if no maintenance strategy exists, describe maintenance strategy:

10. Will a penetration test be performed by a third party prior to deploying this solution?  
     - [ ] Yes  
     - [ ] No  

    If No, specify reasons:

## 2. Reliability Impact Assessment

### 2.1 Overall Impact
   1. [ ] No perceived impact on reliability. No further assessment is required.
   2. [ ] There is a likely impact on reliability.

If **No** skip to 3. If **Yes**, continue to section 2.2.

### 2.2. Performance Under Load

1. Will this solution change the system's ability to handle user or data load?  
     - [ ] Yes  
     - [ ] No  

     If Yes, reference relevant parts of technical design covering performance:

2. Are performance testing be performed for this solution?  
     - [ ] Yes  
     - [ ] No

    If No, specify reasons:

### 2.3. Failure & Recovery

3. Does the design include mechanisms for failing gracefully?  
     - [ ] Yes  
     - [ ] No   

     If No, outline key failure points and reasons:

3. Does the design include mechanisms for recovery from error/failure?  
     - [ ] Yes  
     - [ ] No   

     If No, specify reasons:

4. Will this solution affect the system's disaster recovery (DR) capabilities, or is additional DR required in order to meet defined Restore Point and Recovery Time Objectives (RPO/RTO)?  
     - [ ] Yes  
     - [ ] No 

     If Yes, reference relevant parts of technical design covering DR processes:

### 2.4. Observability & Monitoring

5. Does this solution modify logging, monitoring, or alerting strategies?  
     - [ ] Yes  
     - [ ] No  

   If Yes, reference relevant parts of technical design covering observability:

6. Are metrics or logs being created?  
     - [ ] Yes  
     - [ ] No   

   If No, specify reasons:

7. Are there new alerts that need to be introduced?  
     - [ ] Yes  
     - [ ] No  

   If Yes, reference relevant parts of technical design covering alerting strategy:


## 3. Summary of Mitigations

1. The solution and architectural designs effectively mitigate necessary security and reliability concerns: 
     - [ ] Yes  
     - [ ] No  

