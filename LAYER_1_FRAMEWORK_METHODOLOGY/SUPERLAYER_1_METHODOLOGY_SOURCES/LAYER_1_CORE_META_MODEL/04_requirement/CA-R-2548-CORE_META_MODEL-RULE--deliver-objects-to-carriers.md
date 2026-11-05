---
atom_id: CA-R-2548
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Deliver Objects to Carriers

## Claim

### Prose Claim


- `>>` delivers an Object to the referenced Carrier or Carrier part.
- A selection delivers its selected Objects.
- A bare qualified address refers to its declared target.
- `!(selectors)` excludes those branches from a selection.
- Relative exclusions use the selection's base.
- `=` states an equality condition.
