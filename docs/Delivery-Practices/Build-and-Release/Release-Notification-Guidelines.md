---
title: Release Notofication Guidelines
authors: 
- Helen Duriez
reviewed: 
reviewer:
next-review: 2022-06-01
---

When carrying out a release, it is good practice to let stakeholders know the release is about to happen, and what it will mean for them. 

## What types of work require notification? 

Any work that involves a release, including:
- Product features and changes, regardless of platform
- Bug fixes that involve code changes
- Technical improvements and infrastructure changes

## How to notify colleagues of a release

- Delivery team member posts to the Release Announcements channel (in the Platform Support team) ahead of release.
- Use team tags to alert stakeholders identified in your Release Plan.
- Confirm when the release has been completed successfully, or if there’s been an issue and you have to change course/roll back. 

!!! Note "Who are your stakeholders?"
Ensure that you are clear on [who the stakeholders are]().

## What to communicate
When communicating to stakeholders, think about their perspective and what they might need to know. Be sure to:
-	Provide a short summary of the change, including the area of the platform and whether it is part of a larger suite of changes.
-	Provide context behind the change. Stakeholders may not know the change is coming, or why! A brief note on practical applications can be useful. 
-	Whether there are any visible changes they’ll see as a result, including whether the change has been feature flagged. Even if there are no visible changes, letting stakeholders know that a release is taking place can help manage expectations in the event that there’s an issue. 
-	Note if any actions are required by the user in order to see the desired changes, e.g. re-promote or re-publish. 
If the release is part of a larger set of changes, the Product Manager should be in discussions with stakeholders throughout development, and will prepare accompanying Feature Notes . 

## Examples
 
###	A good level of detail:

> Hi \[Specific Tag(s)] we are about to release the fix for font colours in high contrast mode. 
> This should fix a few instances where font was not sufficiently contrasting when using the high contrast mode toggle. 
> This will require a republish for sites that’s users are using a screen reader.

###	Poor detail: Valuable information is missing

> Hi \[Specific Tag(s)] \[Product Delivery Team] are releasing a change that will improve accessibility when using keyboard focus visibility on video player. 
> This is a visual change and will effect everybody. Will notify when release is complete.

In this scenario, a stakeholder had to ask what the visual change was.
 
### Poor detail: Contextual information is missing:
> Morning \[Specific Tag(s)] we are planning to perform an update to the Export Asset Metadata feature today. This will add an Asset ID column to any newly generated asset exports.

In this scenario, a stakeholder had to ask what the Asset ID was/how it was different from other IDs. They benefitted from a response that told them the reason for the change, and how it could be applied to their own use cases. 


