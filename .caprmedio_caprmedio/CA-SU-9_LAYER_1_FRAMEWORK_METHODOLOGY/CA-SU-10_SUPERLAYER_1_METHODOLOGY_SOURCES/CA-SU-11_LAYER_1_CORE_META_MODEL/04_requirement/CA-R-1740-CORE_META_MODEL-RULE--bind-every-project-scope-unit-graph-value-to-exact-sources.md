---
atom_id: CA-R-1740
ref_id: CA-R-1740
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection/(.Form:=Scope Unit Graph)
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Journal
tier: 3
relations:
  child_of:
  - CA-R-1052
  - CA-R-007
status: Active
version: 41
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1740-CORE_META_MODEL-RULE--bind-every-project-scope-unit-graph-value-to-exact-sources.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Bind every Project Scope Unit Graph value to exact sources

## Claim

### Prose Claim


Project Scope Unit Graph Projection values.


**every** Project Scope Unit Graph Projection value **must** retain traceability **to** the exact Project Structure state, Settings state, Atom Revisions, Carrier observations, **or** Journal Records actually used **to** derive it. an unavailable **or** contradictory source **must** produce an explicit unresolved result for the affected value **without** erasing independent observations **or** claiming complete source coverage. declared values **and** observed materialization **must not** be conflated.
