---
subject_scopes:
  - framework-engine-apps
  - security
version: 1
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Render untrusted project content only as data

Given project text containing HTML, script, URL, style, and bidirectional-control payloads, render every supported App view. Verify that each value is encoded for its exact output context, executes no active content, gains no additional capability, and remains inspectable as project data.

Candidate alignment: CA-E-001, CA-E-002, CA-D-001, CA-R-827, CA-R-861.

## Sources

- [OWASP Cross Site Scripting Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/02-checklist/05-checklist)
