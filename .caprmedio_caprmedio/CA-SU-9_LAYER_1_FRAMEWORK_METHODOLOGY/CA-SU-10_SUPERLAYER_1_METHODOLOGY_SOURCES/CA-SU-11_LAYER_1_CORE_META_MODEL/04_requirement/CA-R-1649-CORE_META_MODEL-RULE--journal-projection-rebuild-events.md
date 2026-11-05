---
atom_id: CA-R-1649
ref_id: CA-R-1649
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
  dependencies:
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_MODEL <+ Projection
tier: 2
status: Active
version: 34
updated_at: 2026-11-03 23:17:14 +0400
carrier_destination:
  file:
    name: CA-R-1649-CORE_META_MODEL-RULE--journal-projection-rebuild-events.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Journal Projection Rebuild Events

## Claim

### Prose Claim


Business Projection Rebuilds and their Work Journal Actions and terminal Events. Technical read-only queries and maintenance of rebuildable query indexes are runtime activities outside this Rule.


**every** business Projection Rebuild **must** have **`=1`** Work Journal Action whose terminal Event records the rebuild outcome.

## Details

technical read-only queries and maintenance of rebuildable query indexes report normal output through runtime stdout and failures through runtime stderr. these activities require no Work Journal Action or terminal Event under this Rule.

acceptance of that Event into the Journal does **not**, by itself, make the Projection current. currentness remains subject **to** the Projection's applicable source **and** validation requirements; the accepted Event preserves the observed outcome **without** replacing those requirements.
