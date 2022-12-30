---
title: Functional Test Strategy
authors: 
- Karen Farrell
reviewed: [yyyy-mm-dd]
reviewer:
next-review:
---

## **Introduction**
This document defines the overarching functional test strategy followed at AM to accompany and support the SDLC.  Further strategies are available to cover exploratory testing, automated testing etc in more detail.

## **Test Objectives**
We use both static and dynamic testing as a means for achieving test objectives.  Both provide information to improve the Backlog Item under test, and our development and testing processes. 

Our main testing objectives are to: 
- Verify documentation in order to prevent defects
- Detect defects existing in the software under test
- Determine the solution satisfies our Stakeholders needs 
- Demonstrate the software is fit for purpose
- Gain confidence in and provide information about the level of quality

## **Test Approach**
### **Test Levels - Responsibility & Tools**
This section details the test levels frequently applied and who has responsibility for performing this testing  

| Test Level | Objective | Tools Used | Responsibility |
|:---        |:---       |:---        |:---            |
|Unit Testing|Focus on individual components||Delivery Team|
|Integration Testing|Focus on interactions between components or systems||Delivery Team|
|System Testing|Focus on behaviour and capability of the whole system are as designed and specified|TestPad / Playwright / BrowserStack / Azure DevOps|Delivery Team|
Business Acceptance Testing (BAT)|Focus on validating the fitness of use of the system in a real or simulated operational environment||Stakeholders|

### **Test Types**
Static Testing 
- Testing at specification level without execution of the software e.g. reviewing Backlog Items 

Functional Testing 
- Functional testing is based on the analysis of the behaviour of the component / system i.e. ‘what it does’ 
- Ensures the product meets our stakeholders' requirements and doesn’t have any major bugs 

Confirmation Testing 
- When a test fails and a defect reported, we can expect a new version of the software that has had the defect fixed.  In this case, we will need to execute the test again to confirm the defect has indeed been resolved 

Regression Testing 
- Verify that modifications in the software or environment have not caused unintended adverse side effects and that the system still meets its requirements

Smoke Testing 
- These are basic tests that are quick to execute with the goal of ensuring the major features of the system are working as expected 
- Smoke tests are useful following a new build/release:
  - To verify a successful build/release
  - To decide whether more expensive testing can commence

Business Acceptance Testing (BAT) 
- This tends to be the last phase of testing.  During BAT, our Stakeholders test to make sure the software can handle required tasks in real-world scenarios, according to requirements

### **Test Design Techniques**
There are many different types of software testing techniques, each with its own strengths and weaknesses.  At AM, we are not limited to which technique is used and it is therefore left to the judgement of the Engineer.  Following is a list of common test techniques: 

Specification Based 
- Equivalence Partitioning 
- Boundary Value Analysis 
- Decision Tables 
- Pairwise 

Experience Based 
- Error Guessing 
- Checklist-Based 
- Exploratory 

### **Supported Browsers & Devices**
Please refer to the [Supported Browsers, Devices & Operating Systems](/docs\6.-Engineering\Test-Engineering\Supported-Browsers,-Devices-&-Operating-Systems.md) documentation 

## **Test Process**
### **Readying**
Consider how the team will approach testing the backlog Item and note a high-level strategy 

### **Planning**
In the planning phase, we aim to: 
- Identify test scenarios  
- Define the test approach, including:
  - Assess which scenarios can be automated  
  - Define approach to manual testing 
  - Identify test data required  

### **Execution**
Once development of the Backlog Item is available on a test environment, the test approach is executed.  Further details on assessing results can be found in the relevant test strategy (e.g. Manual Test Strategy / Automation Test Strategy) 

### **Exit Criteria**
Exit Criteria is discussed on a per Backlog Item basis.  Points to consider: 
- Number of Test Scenarios executed  
- Desired and sufficient coverage of the requirements  
- Software delivered has not regressed 
- Identified defects are addressed 
- Any high priority/severity defects outstanding  

## **Defect/Bug Management**
Defects are raised in Azure DevOps as a child task of the relevant Backlog Item. 

Production Bugs are raised in Azure DevOps as a Backlog Item. 

As a minimum, the following data is logged: 
- Test Data 
- Steps to replicate the defect or bug 
- Expected Results 
- Actual Results 
- Test Evidence, where possible 

## **Release Control**
Please refer to the Release Management documentation //TO DO 

## **Other strategies**
The following strategies are an extension to this Functional Test Strategy: 
- Manual Testing Strategy //TO DO
- Automation Testing Strategy //TO DO
- Testing Package Dependencies //TO DO