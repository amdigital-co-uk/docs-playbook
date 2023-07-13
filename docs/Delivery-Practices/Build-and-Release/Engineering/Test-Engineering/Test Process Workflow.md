---
title: Test Process WorkFlow
authors: 
- James Perry
reviewed: [yyyy-mm-dd]
reviewer:
next-review:
---

--- ![Test Process Work Flow Diagram](BLI_Test_WorkFlow.png)
---

The above diagram outlines the different Test phases and what is involved for each of those individual phases. For a more granular breakdown, please see below and for a much more simplified version, please see [Test Workflow Diagram](Test-Engineering\Test Workflow Diagram.md) 

## What is Test monitoring and control?
Test monitoring involves:
- comparing actual progress to the plan
- using metrics defined in the plan
- Checking scheduled End to End regression tests

Test control involves:
- taking actions to meet the plan’s objectives
- Evaluate [results against] exit criteria (Agile = Definition of Done)
- checking test results and logs against coverage criteria
assessing the level of component or system quality based on test results and logs
- Determining if more tests are needed
- PR Reviews on code commits (automation)

- work products: test progress reports, test summary reports (internal or external), test rail reports / dashboard


## What is Test Planning?
Test planning activities define:

- The scope of testing and the approach for meeting them, e.g.
test activities and tasks
- feedback from monitoring and control may cause re-planning
- Estimations of test effort for Backlog Items, as a spart of readying sessions
- Prioritizing of test activities
- Defining entry criteria

- work products include: Information about test basis on which to build traceability, exit criteria, schedules etc. for monitoring and control


## What is Test analysis
Test analysis is intended to:

- identify testable features of the test object
- define test conditions for them
- determines what to test in a way that gives us a measure of how much we have tested – “coverage”
- define full scope of test coverage

Major activities include:
- collect the test basis
- evaluate the test basis – testable? 
- ambiguities, omissions, inconsistencies etc.
- Test analysis is a form static testing, delivers early testing
- identify features to be tested
- define and prioritise test conditions
- capture bi-directional traceability: test basis test conditions
- Test preparation 


### What is test design?
- Test design involves elaborating test conditions
- turning them into prioritized test cases
- creating other “testware”

major activities include:
- design and prioritize test cases and sets of test cases (suites)
- identify test data needed to support these test cases
- Collecting test data
- Test preparation for different types of tests 
- identify any required infrastructure and tools
- extend bi-directional traceability to the test cases
- test design can use same techniques as test analysis
- Can find defects in test basis
- Define further techniques to be used – Boundary value analysis, state transitioning, error guessing


### What is Test Implementation?
- Test implementation involves finalizing testware
- turning test cases into test procedures / scripts
- completing / creating all other testware needed

major activities include:
- develop and prioritize test procedures – may include sequencing >1 test case into one test procedure
- may include creating and reviewing automated test scripts
- create test suites from test procedures &/or automated test scripts
- arrange test suites in efficient test execution schedule
- build test environment, verify it’s set up correctly
- Load test data into test environment
- verify / update bi-directional traceability test basis, test suites
- test implementation often combined with test design and both done together with test execution in exploratory testing



### What is test execution?
Test execution involves running the tests according to the test execution schedule

major activities include:
- execute tests, manually / with test execution tools
- compare actual results with expected ones
- analyze anomalies (differences) to establish likely causes
- failure due to defect, or false positive?
- report defects based on failures observed or suspected if not yet clear
- log outcomes
- repeat test activities as needed
- verify & update bi-directional traceability test results


### What is test execution?
Test completion involves tidying up after:
- a test level is completed
- an Agile iteration is finished
- a test project is completed (or cancelled)
- a new system or maintenance release goes live

major activities include:
- check that all defect reports are closed
- reate change requests or product backlog items for any not closed
- create test summary report for stakeholders
- finalise / archive testware for later reuse &/or audit trail
- hand over testware to maintenance teams / project teams /
- analyse lessons learned from completed test activities
- use information gathered to improve test process maturity

