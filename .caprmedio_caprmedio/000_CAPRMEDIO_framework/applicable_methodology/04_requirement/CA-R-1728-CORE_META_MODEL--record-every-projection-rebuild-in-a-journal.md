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
  - CA-R-007
status: Active
version: 29
updated_at: 2026-11-03 23:17:14 +0400
carrier_destination:
  file:
    name: CA-R-1728-CORE_META_MODEL-RULE--record-every-projection-rebuild-in-a-journal.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1728-CORE_META_MODEL--record-every-projection-rebuild-in-a-journal.md
  source_atom_id: CA-R-1728
  source_atom_revision: 29
  source_sha256: 39586b952a2f0255df8ec29f3a3066a1306e51f53ea995f86bc17351a6b1afd4
  original_relations_sha256: edef9085fddd1e905afd02423e8d88f5300a99b1f0a711703db5055e0c42a859
---
## Summary

Record every Projection rebuild in a Journal

## Claim

### Prose Claim


Business Projection rebuild attempts. Technical read-only queries and maintenance of rebuildable query indexes are runtime activities, not Projection rebuild attempts under this Rule.


**every** business Projection rebuild attempt **must** produce append-only Journal provenance from its start through **`=1`** terminal outcome, binding the target Projection, exact source Atom revisions **and** Journal records, generator, configuration, **and** produced revision **when** successful. Programmatic generation **and** LLM generation are provenance facts **only**; the two generation forms grant the Projection no authority.

## Details

technical read-only queries and maintenance of rebuildable query indexes report normal output through runtime stdout and failures through runtime stderr. these activities create no Journal provenance obligation under this Rule.
