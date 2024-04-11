---
title: DevOps 3 Ways
authors: 
  - Ed Earle
reviewed: 2023-09-06
reviewer: Ed Earle
next-review: 2024-09-01
---

## Intro

This is a simplified summary of the 3 ways. It is highly recommended that all team members read ["The Phoenix Project"](https://itrevolution.com/product/the-phoenix-project/) or ["The DevOps Handbook"](https://itrevolution.com/product/the-devops-handbook-second-edition/) both by Gene Kim.

Additionally, you can learn about the 5 ideals, in ["The Unicorn Project"](https://itrevolution.com/product/the-unicorn-project/)

## First Way: Understanding and optimising flow

Understanding and optimising *flow* means improving the rate at which we deliver work: i.e. **maximising our net effectiveness**.

When we talk about "flow" or "flow of work", we mean entire system or "whole". Often software delivery teams only evaluate their effectiveness within one part of the system, for example the bit when engineers write and test code. In fact the system is much larger and than this. Looking at just one part of the whole may allow us to make that part more efficient, and yet the whole system could become less effective.

Evaluating a whole system is often known as systems thinking. When we look at an entire system we can see the interactions between system components, and where there are bottlenecks, also known as **constraints**. This helps us improve our system.

For example: understanding system interactions helps clarify the impact of quality on subsequent parts of the system, and understanding constraints helps us discover which parts of the system are the slowest and make improvements.

Technology teams are often expected to just "get it done" and discouraged from understanding the dynamics of the system in which they play a critical role. This approach impacts autonomy and reduces the ability of rapid decision making and learning.

## Second Way: Shortening and Amplifying Feedback Loops

Equipped with a good understanding of flow and a desire to improve it, we need to ensure we have feedback.

!!! note "Feedback and _Feedback_"

    Feedback may refer to the practice of providing an individual with your opinion of their performance, either relating to a specific action they have taken or their day to day duties. 

    Feedback in the context of the _Second Way_ refers more broadly to any information going upstream (right to left). This includes the  feedback described above, automated processes (e.g. integration test, build errors), or manual workflow information. 

Feedback loops are a critical part of improvement in iterative delivery environments. Each time a process or action is executed, there is an opportunity to provide information back "upstream", so that the next iteration can adapt.

Shortening feedback loops means reducing the time it takes for feedback to be given.

Amplifying feedback loops means ensuring that we pay enough attention to the information that is being created by the feedback loop.

### Feedback loop examples

1. A team following Scrum delivery practices have a 4 week sprint. They start the sprint with a set of deliverables and set to work. 4 weeks later they present their output to stakeholders. What could be done to shorten this loop?

1. A software engineer is working on a task as part of a deliverable which will create various modules of code and new functionality. Once he has completed the work he passes it on to a tester who tests that the new functionality, and existing functionality works. The tester completes the testing then provides a list of defects back to the developer. What could be done to shorten this loop? How many loops could be created here?

1. A junior software engineer is working on a task. They identify that the acceptance criteria for the backlog item is ambiguous and that the test plan is has not accounted for this. The senior test engineer that created the plan reviews it and determines that the plan and acceptance criteria are fine. How might this feedback be amplified?

## Third Way: A Culture of Continuous Experimentation and Learning

Feedback is coming thick and fast. What do we do with it? Experiment,  learn, and improve.

Successful experimentation - experiments that result in improving our net effectivenes - lead us to improve our value stream: our delivery practices.

Being brave and taking risks is how we ensure we are experimenting and able to learn.