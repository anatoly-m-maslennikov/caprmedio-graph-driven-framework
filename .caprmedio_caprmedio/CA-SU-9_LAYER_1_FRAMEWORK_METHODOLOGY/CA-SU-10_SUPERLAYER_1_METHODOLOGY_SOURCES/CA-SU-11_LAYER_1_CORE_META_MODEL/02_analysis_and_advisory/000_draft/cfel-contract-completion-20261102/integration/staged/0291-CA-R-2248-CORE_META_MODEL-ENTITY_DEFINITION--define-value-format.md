---
atom_id: CA-R-2248
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Format
version: 4
updated_at: 2026-11-02 07:49:21 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
---
## Summary

Define Value Format

## Claim

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


```CFEL
CFEL <+ Format;
Format.Data Type{:1}: [string]{:1};
Format.Data Type.*[]{:0};
Format.Uniqueness Selection{:0..1}: [string]{:1};
Format.Uniqueness Selection.*[]{:0}
```

## Semantics

Format annotations constrain direct values. Markdown, YAML, TOML and JSON are
Carrier representation formats, not value Formats. The initial scalar
vocabulary—bool, datetime, decimal, float, int and string—is provisional. A
format annotation selects a value domain; it does not impose uniqueness.

## Details

Formula expressions, function-style uniqueness notation and bracketed
conditions remain separate proposals.
