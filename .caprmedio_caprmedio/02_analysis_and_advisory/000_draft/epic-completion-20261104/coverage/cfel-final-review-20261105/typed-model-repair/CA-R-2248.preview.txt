---
atom_id: CA-R-2248
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Format
version: 6
updated_at: 2026-11-05 03:25:14 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 1
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2248@6-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-value-format.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Define Value Format

## Claim

### Formal Claim

```CFEL
# model
CFEL / Format
```

### Prose Claim


Format defines the admissible value domain of each direct Property value,
separately from its cardinality. In CFEL, `Format` is the language element for
expressing that value domain. Data Type names the value domain. Uniqueness
Selection names the comparison population. List and map are Carrier
structures, not Value Formats. A YAML sequence carries multiple values, and a
mapping carries dependent Properties. `ref` is not a Value Format. Identifying
values use the `string` Format; their Definition identifies the referenced
object. Nested Properties have independent Formats and cardinalities. A Model object kind referenced as `<Kind>` may also supply an object Format alongside primitive Formats such as `int`; a Format specifies the admissible domain and does not create an instance or turn a literal into a Node. `[<Workflow Run> OR <Step Run>]` admits either declared Model kind as one union domain; a participant selected from it is one binding. Bracketed Format conditions constrain values in that domain. In `p{::occ} :: [<Kind>]{::valuecount}`, the bounds count Property occurrences and direct values respectively, not every instance of Kind in the Project. YAML
null and an empty string each count as one direct value when present; Format
and prose conditions determine admissibility.



## Semantics

Format annotations constrain direct values. Markdown, YAML, TOML and JSON are
Carrier representation formats, not value Formats. The initial scalar
vocabulary—bool, datetime, decimal, float, int and string—is provisional. A
format annotation selects a value domain; it does not impose uniqueness.

