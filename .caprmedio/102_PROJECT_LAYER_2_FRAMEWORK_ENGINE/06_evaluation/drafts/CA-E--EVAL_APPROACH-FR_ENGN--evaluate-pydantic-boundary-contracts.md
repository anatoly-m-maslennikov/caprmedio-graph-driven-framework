---
subject_scopes:
  - framework-engine-python
version: 2
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Evaluate Pydantic boundary contracts

For each admitted Pydantic boundary, evaluate accepted input, missing required fields, undeclared extra fields, wrong types, violated constraints, nested failures, and serialization behavior. Exercise Python-object and JSON input separately when both are supported because their strict-mode behavior can differ.

Verify that strict boundaries reject unintended coercion, deliberately lax boundaries perform only their declared conversions, and every rejected input returns stable machine-readable error locations and types without exposing secrets. Compare generated JSON Schema when it is part of the public contract, and treat an intentional schema change as a compatibility change requiring explicit acceptance.

Candidate alignment: CA-E-001, CA-E-002, CA-D-001, CA-D-002, CA-R-861.

## Sources

- [Pydantic: strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
- [Pydantic: error handling](https://docs.pydantic.dev/latest/errors/errors/)
- [Pydantic: JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/)
