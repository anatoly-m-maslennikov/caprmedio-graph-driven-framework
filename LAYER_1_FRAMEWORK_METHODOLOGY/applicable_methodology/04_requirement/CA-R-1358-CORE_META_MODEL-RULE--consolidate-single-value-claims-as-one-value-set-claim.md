---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ CFEL<+Operator//AllowedValue
version: 35
updated_at: 2026-11-02 08:06:47 +0400
relations:
  child_of:
  - CA-R-2102
  - CA-R-1596
atom_id: CA-R-1358
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1358-CORE_META_MODEL-RULE--consolidate-single-value-claims-as-one-value-set-claim.md
  source_atom_id: CA-R-1358
  source_atom_revision: 35
  source_sha256: fb90a002ecb1f78b3ce59c02e46f9e91007bb44263fc110f4e73efcc230ed317
  original_relations_sha256: e5ef375fa10a5f7fff5563acdf3d28805f5472119b8d66cdd96b86a22f04cbd8
---
## Summary

Consolidate Single-Value Claims as One Value-Set Claim

## Claim

### Prose Claim


multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X.


multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X **must** be consolidated as **`=1`** Claim Value Set **if** they differ **only** by one allowed value of X.
