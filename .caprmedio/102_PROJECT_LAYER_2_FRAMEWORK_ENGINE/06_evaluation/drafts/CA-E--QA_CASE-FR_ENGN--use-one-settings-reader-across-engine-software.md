---
subject_scopes:
  - framework-engine-software
  - project-settings
version: 1
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Use one Settings Reader across Engine software

Given representative Tool, App, and MCP consumers, replace the centralized Settings Reader with a recording fake and execute each consumer once. Verify that each obtains exactly one immutable validated snapshot, passes it into its decision or service boundary, and performs no direct settings-file read, environment fallback, private default selection, or settings mutation.

The case passes only when all consumers use the same versioned snapshot contract and identify its carrier and digest provenance.

Candidate alignment: CA-E-001, CA-E-002, CA-M-002, CA-D-001, CA-R-861.

## Sources

- [Python documentation: unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [Pydantic: strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
