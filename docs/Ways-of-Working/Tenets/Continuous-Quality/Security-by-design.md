---
title: Secure by Design
---

## 10 Key Principles

These principles are essential for creating robust, secure software that can withstand various threats and protect user data and privacy throughout the software development lifecycle.

## 1. Minimize Attack Surface Area
Reduce the number of entry points and exposed interfaces in your software. By limiting the points of interaction, you decrease the potential vulnerabilities that attackers can exploit.

## 2. Establish Secure Defaults
Ensure that your software is secure by default. Out-of-the-box configurations should be set to the most secure settings, requiring users to deliberately reduce security if they choose to.

## 3. The Principle of Least Privilege
Grant the minimum level of access necessary for users and processes to perform their tasks. This limits the potential damage in case of a breach by restricting access to critical systems and data.

## 4. The Principle of Defence in Depth
Implement multiple layers of security controls throughout the system. This strategy ensures that if one layer is compromised, additional layers provide continued protection.

## 5. Fail Securely
Design systems to handle failures gracefully and securely. Ensure that when errors occur, the system defaults to a secure state to prevent unintended access or data leakage.

## 6. Don’t Trust Services
Assume that external services and components are not secure. Validate and sanitize all inputs and outputs, and implement additional security measures to protect against compromised third-party services.

## 7. Separation of Duties
Divide tasks and privileges among multiple users or systems to prevent any single entity from having too much control. This reduces the risk of insider threats and unauthorized access.

## 8. Avoid Security by Obscurity
Do not rely on secrecy of design or implementation as a primary security measure. Ensure that your security mechanisms are robust and can withstand public scrutiny and attacks.

## 9. Keep Security Simple
Design security measures that are straightforward and easy to understand. Complex systems are more prone to errors and harder to manage, increasing the risk of vulnerabilities.

## 10. Fix Security Issues Correctly
Address security vulnerabilities thoroughly and correctly the first time. Implement proper fixes and avoid temporary patches that could lead to recurring issues or new vulnerabilities.
