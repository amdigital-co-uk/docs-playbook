---
title: Security, privacy and accessibility
authors:
  - Ed Earle
reviewed: 2026-10-02
next-review: 2027-04-01
---

Security, privacy and accessibility are designed in. Each is assessed during design, built by the team, and checked by review and automated tests. None of them is a specialist's job to add at the end.

## Secure by design

Ten principles guide how we design systems:

1. **Minimise the attack surface.** Fewer entry points and exposed interfaces mean fewer things to defend.
2. **Secure by default.** Out of the box, everything is set to its most secure configuration; weakening it is a deliberate act.
3. **Least privilege.** People and processes get the minimum access they need.
4. **Defence in depth.** Several layers of control, so that one failure is not a breach.
5. **Fail securely.** When something goes wrong, the system falls back to a safe state, not an open one.
6. **Trust no service.** Validate what comes in from, and goes out to, every external component.
7. **Separate duties.** No single person or system holds enough control to cause serious harm alone.
8. **No security by obscurity.** Our controls survive scrutiny; secrecy of design is not one of them.
9. **Keep it simple.** Complicated security is hard to get right and easy to get wrong.
10. **Fix it properly.** A vulnerability is fixed at its root, not patched over.

In practice: every engineer knows the OWASP Top 10 and follows its secure coding guidance; every new endpoint and page has the right authentication and authorisation; frameworks, libraries and infrastructure are kept current and configured securely; and secrets never appear in code, configuration files or documentation.

## Impact assessments

Security and reliability are assessed where the choices that affect them are made. Every architectural, design and scope decision record carries a **security and reliability impact assessment**, so that the impact is weighed as part of deciding rather than audited afterwards. The security half covers threat analysis and modelling, personal and sensitive data stored or transmitted, and external interfaces and third-party dependencies. It also covers authentication and authorisation, the effect on existing security tests and known vulnerabilities, and whether penetration testing is needed. The Engineering Owner is accountable for it and raises any significant risk with technology leadership. Most features inherit their assessment from the decisions they rest on. Where a decision has no security or reliability impact, the assessment says so in a line; it is never skipped.

A security vulnerability found in a live system is handled through the service desk as its own type of work, prioritised on its severity. A security incident follows our incident response plan, which is separate from the normal issue process.

## Privacy by design

Seven principles, from the framework of the same name, shape how we handle personal data:

1. **Proactive, not reactive.** Anticipate privacy problems and prevent them.
2. **Privacy as the default.** Nobody should have to act to protect their own data.
3. **Embedded in design.** Privacy is part of the system's core, not a layer on top.
4. **Full functionality.** Privacy and capability are not a trade-off.
5. **End-to-end protection.** Data is protected from collection to deletion.
6. **Visible and transparent.** How we handle data is clear and open to scrutiny.
7. **Respect for the individual.** People have control over their own data.

## Accessibility

Our platforms are used by students, researchers and librarians with a wide range of needs, and our customers rightly expect us to meet them. Every user interface conforms to WCAG AA: usable with a screen reader, with keyboard alone, with the right semantic structure and labelling. Accessibility is a requirement of every feature that touches an interface, and the designer owns the accessibility impact assessment for it. Automated accessibility checks run alongside our end-to-end suites, and accessibility issues reported by customers are a distinct type of service desk work, so that we can see and act on the trend.
