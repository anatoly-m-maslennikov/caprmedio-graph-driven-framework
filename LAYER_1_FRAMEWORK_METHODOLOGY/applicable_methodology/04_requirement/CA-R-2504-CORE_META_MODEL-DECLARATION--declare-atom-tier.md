---
atom_id: CA-R-2504
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom.Tier
version: 2
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2504-CORE_META_MODEL-DECLARATION--declare-atom-tier.md
  source_atom_id: CA-R-2504
  source_atom_revision: 2
  source_sha256: 4a63dfa3612df1ffead39a2b3338a278d7cb177c6677c161df4e20fb447e1cb9
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Tier

## Claim

Goals whose active Subject resolves to the Project use Tier -1. Ordinary Scope Unit-owned non-Goal Atoms use Tier 0 or higher.

```CFEL
Atom.Tier{:1}: [int]{:1};
Atom.Tier.*[in(Label)]{:0..1};
Atom.Tier >= -1
```
