---
atom_id: CA-R-1728
ref_id: CA-R-1728
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 1
relations:
  child_of:
  - CA-M-544
status: Active
version: 30
updated_at: 2026-11-11 15:00:27 +0400
carrier_destination:
  file:
    name: CA-R-1728-CORE_META_MODEL--record-every-projection-rebuild-in-a-journal.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Record every Projection rebuild in a Journal

## Claim

### Prose Claim


Business Projection rebuild attempts. Technical read-only queries and maintenance of rebuildable query indexes are runtime activities, not Projection rebuild attempts under this Rule.


**every** business Projection rebuild attempt **must** produce append-only Journal provenance from its start through **`=1`** terminal outcome, binding the target Projection, exact source Atom revisions **and** Journal records, generator, configuration, **and** produced revision **when** successful. Programmatic generation **and** LLM generation are provenance facts **only**; the two generation forms grant the Projection no authority.

## Details

technical read-only queries and maintenance of rebuildable query indexes report normal output through runtime stdout and failures through runtime stderr. these activities create no Journal provenance obligation under this Rule.
