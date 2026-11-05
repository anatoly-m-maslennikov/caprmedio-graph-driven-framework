---
atom_id: CA-R-2428
ref_id: CA-R-2428
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Tier
  dependencies:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Goal)
  - CAPRMEDIO_MODEL <+ Atom.Header.Topics.Main Subject
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
tier: 3
relations:
  child_of:
  - CA-R-917
status: Active
version: 3
updated_at: 2026-11-04 09:19:08 +0400
carrier_destination:
  file:
    name: CA-R-2428-CORE_META_MODEL-RULE--admit-numeric-tiers-in-scope-units.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2428-CORE_META_MODEL-RULE--admit-numeric-tiers-in-scope-units.md
  source_atom_id: CA-R-2428
  source_atom_revision: 3
  source_sha256: c8f442d5b904107bdd9c9312661d5e2e336b12345c8c69f53100f99a15764574
  original_relations_sha256: 07ff186ea0a321d7fb069e80e411ab3df2f1dd583be9f06f09fb9bef084dac4b
---
## Summary

Admit Numeric Tiers in Scope Units

## Claim

### Prose Claim


ordinary Atoms owned by Scope Units in the Project.


a Scope Unit in the Project **must** admit an integer Tier **>=0** for every ordinary Atom it owns, except an Atom of Form Goal whose active Subject resolves to the Project Scope Unit root. That exact predicate carries Tier `-1` under CA-R-2132 regardless of its Container or owner. Higher integer Tiers remain admissible without an upper bound and may be assigned or raised when required by the approved governing-relation ordering.

This range rule imposes no Content-Role or Type-to-Tier restriction.
