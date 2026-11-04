---
atom_id: CA-R-2503
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content.Details
version: 5
updated_at: 2026-11-04 05:21:15 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2503-CORE_META_MODEL-DECLARATION--declare-atom-content-details.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2503-CORE_META_MODEL-DECLARATION--declare-atom-content-details.md
  source_atom_id: CA-R-2503
  source_atom_revision: 5
  source_sha256: 8017db55ea1a7606166ccf33731c523e7518a1d51665fd975fb228e7006b64d1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Content.Details

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role in RMED).Content.Details: {:0..1};

Atom/(.Header.Role in RMED).Content.Details.*[string]{:0+}
```

