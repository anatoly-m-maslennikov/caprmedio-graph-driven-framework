---
subject_scopes:
  - framework-engine-python
version: 2
updated_at: 2026-08-22 01:50:50
relations: {}
---
# Adopt current Python idioms only for declared benefit

Within the declared FRAMEWORK_ENGINE Python runtime boundary, adopt a stable current Python idiom only when it improves a named project quality such as correctness, understandability, safety, or measured performance. Preserve the simpler supported idiom when the newer construct adds no useful distinction.

Use f-strings for immediate trusted string construction. Use t-strings only when a processor needs structured interpolation data. Keep synchronous code synchronous unless related concurrent work creates a demonstrated need for structured concurrency.

Candidate alignment: CA-M-005, CA-D-001, CA-D-002, CA-R-815.

## Sources

- [PEP 750 — Template Strings](https://peps.python.org/pep-0750/)
- [Python documentation: asyncio task groups](https://docs.python.org/3.14/library/asyncio-task.html#task-groups)
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
