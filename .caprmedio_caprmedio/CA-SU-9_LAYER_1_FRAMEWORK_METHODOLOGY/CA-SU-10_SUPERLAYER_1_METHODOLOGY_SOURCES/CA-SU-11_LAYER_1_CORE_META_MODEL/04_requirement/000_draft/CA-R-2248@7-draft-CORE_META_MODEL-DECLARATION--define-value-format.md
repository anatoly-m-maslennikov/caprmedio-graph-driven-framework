---
atom_id: CA-R-2248
ref_id: CA-R-2248@7-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format
tier: 1
status: draft
version: 7
updated_at: '2026-11-13T06:25:59.530754+00:00'
carrier_destination:
  file:
    name: CA-R-2248@7-draft-CORE_META_MODEL-DECLARATION--define-value-format.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Value Format

## Claim

### Prose Claim


Format defines the admissible value domain of each direct Property value,
separately from its cardinality. In CFEL, `Format` is the language element for
expressing that value domain. Data Type names the value domain. Uniqueness
Selection names the comparison population. List and map are Carrier
structures, not Value Formats. A YAML sequence carries multiple values, and a
mapping carries dependent Properties. `ref` is not a Value Format. Identifying
values use the `string` Format; their Definition identifies the referenced
object. Nested Properties have independent Formats and cardinalities. YAML
null and an empty string each count as one direct value when present; Format
and prose conditions determine admissibility.



### Formal Claim

```python
# model
composition(container='CFEL', parts=('Format',))
```

## Semantics

Format annotations constrain direct values. Markdown, YAML, TOML and JSON are
Carrier representation formats, not value Formats. The initial scalar
vocabulary—bool, datetime, decimal, float, int and string—is provisional. A
format annotation selects a value domain; it does not impose uniqueness.

