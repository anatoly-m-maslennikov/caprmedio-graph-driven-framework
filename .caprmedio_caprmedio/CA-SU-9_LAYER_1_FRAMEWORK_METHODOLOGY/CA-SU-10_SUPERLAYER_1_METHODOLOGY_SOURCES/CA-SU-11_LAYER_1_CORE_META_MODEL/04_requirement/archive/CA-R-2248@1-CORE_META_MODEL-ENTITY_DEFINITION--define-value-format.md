---
atom_id: CA-R-2248@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Syntax > Format
version: 1
relations: {}
tier: 1
updated_at: 2026-10-29 07:32:39 +0400
---
## Summary

Define Value Format

## Claim

A Value Format defines the admissible type of each direct property value,
separately from its cardinality. Neither list nor map is a value Format: YAML
sequences carry multiple values and mappings carry declared child properties.
`ref` is not a value Format; identifying values use string while their
Definitions state what they identify. Nested properties have independent value
formats and counts.

Data Type names the value domain. Uniqueness Selection identifies the
comparison population. YAML null and an empty string each count as one direct
value when present; Format and prose conditions determine admissibility.

### Formal claim

```text
Format.Data Type[string]{1}
Format.Uniqueness Selection[string]{0..1}
```

## Semantics

In `atom.version_number[int]`, `int` identifies the integer value Format. A
format annotation does not itself impose uniqueness. Markdown, YAML, TOML, and
JSON are Carrier representation formats, not members of this value-type branch.

## Details

The initial vocabulary—bool, datetime, decimal, float, int, and string—is
provisional rather than a closed catalog. Formula expressions, function-style
uniqueness notation, and bracketed conditions remain separate proposals.
