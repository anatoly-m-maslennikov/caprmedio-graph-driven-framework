---
subject_scopes:
  - framework-engine-apps
version: 1
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Reject interface bypass of governed Doers

Given an operator-interface request that would change project authority, attempt the change through the frontend, service API, and direct derived-database path. Verify that only the governed Doer path can apply it and that every bypass is rejected without changing source, derived state, or Runtime evidence.

Candidate alignment: CA-E-001, CA-E-002, CA-R-004, CA-R-827, CA-R-861.

## Sources

- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/02-checklist/05-checklist)
- [Python documentation: unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
