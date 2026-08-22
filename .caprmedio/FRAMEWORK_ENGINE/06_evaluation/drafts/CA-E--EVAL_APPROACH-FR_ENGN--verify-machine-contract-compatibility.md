---
subject_scopes:
  - framework-engine-software
version: 2
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Verify machine-contract compatibility

Evaluate every public Tool, App, and MCP input or output, Journal event, Hook handoff, settings snapshot, and persisted Runtime record against its declared Pydantic or JSON Schema contract. Cover valid values, required and forbidden fields, strict types, constraints, nesting, serialization, version recognition, backward-compatible consumers, and rejection of unsupported versions.

Run producer-consumer contract fixtures across every supported adjacent boundary. A schema-valid value is insufficient when its semantic invariants or compatibility promise fail; report structural and semantic failures separately.

Candidate alignment: CA-E-001, CA-E-002, CA-M-002, CA-D-001, CA-R-861.

## Sources

- [Pydantic: strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
- [Pydantic: JSON Schema](https://docs.pydantic.dev/latest/concepts/json_schema/)
- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12)
