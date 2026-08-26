---
subject_scopes:
  - framework-engine-apps
version: 2
updated_at: 2026-08-23 17:40:00 +0400
relations:
  derived_from:
    - CA-A-057
---
# Bind an App interface to declared backend services

Apply this candidate only at an App interface that presents a declared backend-service contract to an Operator. The interface renders an admitted result, submits only the declared command or query, preserves visible request, cancellation, stale-result, and error states, and never becomes an authority or effect owner.

The shared PROGRAMMATIC Methods own state and lifecycle allocation (`CA-M-158`) and typed technical contracts (`CA-M-159`). This App candidate adds only the interface-to-service boundary: frontend code consumes the service contract, does not bypass it to mutate project authority, and does not impose Tool scheduling, Hook, file-mutation, or MCP protocol behavior on another component.

Keyboard operation, untrusted-content rendering, governed-Doer admission, and recoverable service state remain separate App Evaluation candidates rather than becoming acceptance conditions of this Method.

Candidate alignment: CA-M-002, CA-M-005, CA-D-001, CA-D-002, CA-R-861.

## Sources

- [Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/)
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/02-checklist/05-checklist)
- [OWASP Cross Site Scripting Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [Python documentation: task groups](https://docs.python.org/3/library/asyncio-task.html#task-groups)
