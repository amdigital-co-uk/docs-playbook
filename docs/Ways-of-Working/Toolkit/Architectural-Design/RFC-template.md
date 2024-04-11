
# RFC: [Your Title Here]

The title should be prefixed with 'RFC' and should be succinct and explanatory. e.g. `RFC: Implementation of a new Impact Function plugin loader`. Using the 'RFC' acronym in the title will allow us to easily search for past and present RFC's.

## Problem

The problem statement should be labeled with the Markdown heading # Problem. It should be followed by a single paragraph that concisely describes the issue the RFC aims to address. The language used should be factual and devoid of emotional undertones. Additionally, it's crucial to describe the business context for the proposed change, elucidating why it is necessary.

For instance, an inappropriate problem statement might be: The new Impact Function loader is broken and sucks and makes me look bad at training courses. While this statement might capture the author's feelings, it's not suitable for an RFC.

A more suitable problem statement would be: During training courses, we have faced reputational issues due to the performance of the Impact Function loader. The existing loader consistently fails (refer to Issues #1, #2, #5). A new, robust plugin loading mechanism is needed to ensure reliable performance across all platforms.

## Duration

The duration section should be annotated with the markdown heading `# Duration`. Each RFC should express a duration during which the commenting period can take place. At the end of this deadline the decision may be made to extend the deadline if time is needed for further investigation  or discussion. When an RFC is extended the extension should be appended and annotated as per the example below:

   ```text
   # Duration

   1 August 2014 (extended by @timlinux)
   30 July 2014
   ```

## Current state

 This section should be annotated by the `# Current state` heading. It should be contain if the RFC is in draft, awaiting feedback, closed etc.

## Proposers

This section should be annotated by the `# Proposer` heading. It should be followed by a bullet list of one or more persons who have developed the RFC. e.g.

   ```text
   # Proposers

   * Tim Sutton
   * Charlotte Morgan
   ```

## Detail

This is a free-form section that should be annotated with the `# Detail` heading. The detail section should extend the initial problem statement with additional details that describe the situations in which the problems arise, which the current situation is in fact a problem and so on.

## Proposal

This should be annotated with the `# Proposal` markdown section header. It should contain a detailed breakdown of how the problem should be resolved including detailed code listings, diagrams and other supporting materials needed to present the case and implementation roadmap for the proposed changes.The effective use of diagrams, screenshots and sample code listings cannot be over emphasized - the reader should be able to fully understand the proposal and its implications of the current software architecture. This section should be broken up using `##` subsections as needed.

## Resolution

This section should be annotated with a `# Resolution` markdown section header. Here you should indicate whether the RFC is in draft, submitted for approval, approved, denied or shelved to be retabled at a future date.
