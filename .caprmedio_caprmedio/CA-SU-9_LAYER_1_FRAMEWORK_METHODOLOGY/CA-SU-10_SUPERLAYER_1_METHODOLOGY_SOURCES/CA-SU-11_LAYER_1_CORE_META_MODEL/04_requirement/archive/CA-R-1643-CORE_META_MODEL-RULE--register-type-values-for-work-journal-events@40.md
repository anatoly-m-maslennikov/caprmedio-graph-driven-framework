---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File.Main Content
  passive:
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Journal
version: 40
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1643
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Register Type Values for Work Journal Events

## Claim

### Prose Claim


legacy Work Journal execution-observation category labels in serialized Journal Carrier Main Content.


the Main Content of a serialized Journal Carrier **must** preserve a supplied legacy Work Journal execution-observation category label as one of (Started, Progressed, Completed, Failed, Interrupted, Abandoned, Recovered).

this is a Carrier representation constraint. It does **not** create a logical Event Record Property, prescribe an Event Record business Action, or make these legacy observation labels model-level action values.
