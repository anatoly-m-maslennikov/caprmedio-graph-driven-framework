---
subject_scopes:
  - framework-engine-python
version: 2
updated_at: 2026-08-22 01:50:50
relations: {}
---
# Validate untrusted Python data with Pydantic at boundaries

Use Pydantic when untrusted structured data crosses an admitted Python boundary in a Tool, App, or MCP component, such as a CLI payload, Hook event, configuration carrier, Journal record, protocol message, or external adapter. Validate once at the boundary, return structured validation diagnostics, and pass accepted typed values into the deterministic core without making Pydantic the universal internal object model.

Use strict validation when coercion could hide a contract defect. Admit lax conversion only for a declared interoperability need and make the conversion observable. Reject undeclared extra fields for closed machine contracts. Prefer field types and constraints over custom validators, and add Pydantic as a runtime dependency only where its validation and schema value justifies the dependency cost.

Candidate alignment: CA-M-002, CA-M-005, CA-D-001, CA-D-002, CA-E-002.

## Sources

- [Pydantic: models](https://docs.pydantic.dev/latest/concepts/models/)
- [Pydantic: strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
- [Pydantic: model configuration](https://docs.pydantic.dev/latest/concepts/config/)
