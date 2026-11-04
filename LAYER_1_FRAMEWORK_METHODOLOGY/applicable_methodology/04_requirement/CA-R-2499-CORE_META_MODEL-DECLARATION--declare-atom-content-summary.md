---
atom_id: CA-R-2499
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content.Summary
version: 5
updated_at: 2026-11-04 05:21:15 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2499-CORE_META_MODEL-DECLARATION--declare-atom-content-summary.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2499-CORE_META_MODEL-DECLARATION--declare-atom-content-summary.md
  source_atom_id: CA-R-2499
  source_atom_revision: 5
  source_sha256: aea7e0d55fa357a067585331d8798af8422b04da64c467b6105c0669c661bdcf
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Content.Summary

## Claim

### Formal Claim

```CFEL
# model
Atom.Content.Summary{:1}: {:1};

Atom.Content.Summary.*[]{:0};

# instances
DETERMINES(
  Atom//$atom,
  (.ID),
  (.Content.Summary),
  (Atom.Header.Status >| Status Group = Current) OR (Atom.Header.Status >| Status Group = Archived)
)
```

