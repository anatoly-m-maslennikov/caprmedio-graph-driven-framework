---
subjects:
  active: CAPRMEDIO_MODEL <+ Projection/(.Form:=Scope Unit Graph)
  passive:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Journal
version: 41
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-1052
  - CA-R-007
atom_id: CA-R-1740
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
---
## Summary

Bind every Project Scope Unit Graph value to exact sources

## Claim

### Prose Claim


Project Scope Unit Graph Projection values.


**every** Project Scope Unit Graph Projection value **must** retain traceability **to** the exact Project Structure state, Settings state, Atom Revisions, Carrier observations, **or** Journal Records actually used **to** derive it. an unavailable **or** contradictory source **must** produce an explicit unresolved result for the affected value **without** erasing independent observations **or** claiming complete source coverage. declared values **and** observed materialization **must not** be conflated.
