---
atom_id: CA-R-2555
ref_id: CA-R-2555
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Package.structural_level
tier: 3
status: Active
version: 3
updated_at: 2026-11-10 14:38:45 +0400
carrier_destination:
  file:
    name: CA-R-2555-CORE_META_MODEL-DECLARATION--declare-package-structural-level.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2555-CORE_META_MODEL-DECLARATION--declare-package-structural-level.md
  source_atom_id: CA-R-2555
  source_atom_revision: 3
  source_sha256: fe224486264a6703447cedbc5929cc84dafa90fe614a851ac73fb66a064b3584
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Package.structural_level

## Claim

### Formal Claim

```CFEL
# model
Package.structural_level{::1}:: [int]{::1};

Package.structural_level.*[]{::0};

Package.structural_level >= 0;

# instances
Package/Project Package//$implementation.structural_level = 0;

IF (Package//$contained ((IS_CONTAINED_BY)) Package//$container)
THEN ($contained.structural_level = $container.structural_level + 1)
```

