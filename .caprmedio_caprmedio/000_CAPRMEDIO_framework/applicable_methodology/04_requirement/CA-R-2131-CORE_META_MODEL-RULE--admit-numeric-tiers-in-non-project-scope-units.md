---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Tier
  passive:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Goal)
  - CAPRMEDIO_MODEL <+ Atom.Header.Subjects.Active
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
version: 11
updated_at: 2026-11-04 09:19:08 +0400
relations: {}
atom_id: CA-R-2131
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 2
status: Active
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2131-CORE_META_MODEL-RULE--admit-numeric-tiers-in-non-project-scope-units.md
  source_atom_id: CA-R-2131
  source_atom_revision: 11
  source_sha256: f4655c925426a600444cdde8a7bec0ce2d52b49a62cf90eda35caf9894c6f192
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Admit Numeric Tiers in Non-Project Scope Units

## Claim

### Prose Claim


ordinary Atoms owned by non-Project Scope Units.


a non-Project Scope Unit **must** admit an integer Tier **>=0** for every ordinary Atom it owns, except an Atom of Form Goal whose active Subject resolves to the Project Scope Unit root. That exact predicate carries Tier `-1` under CA-R-2132 regardless of its Container or owner. Higher integer Tiers remain admissible without an upper bound and may be assigned or raised when required by the approved governing-relation ordering.

This range rule imposes no Content-Role or Type-to-Tier restriction.
