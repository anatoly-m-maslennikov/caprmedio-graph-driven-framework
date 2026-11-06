---
atom_id: CA-R-2543
ref_id: CA-R-2543
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Aspect
tier: 3
status: Active
version: 4
updated_at: 2026-11-02 18:21:51 +0400
carrier_destination:
  file:
    name: CA-R-2543-CORE_META_MODEL-DECLARATION--declare-aspect.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2543-CORE_META_MODEL-DECLARATION--declare-aspect.md
  source_atom_id: CA-R-2543
  source_atom_revision: 4
  source_sha256: 176f02f688ed13b10bf09ac7c926e072d4223f2d2e36406df5141de9e5b2c779
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Aspect

## Claim

### Prose Claim



- MODEL declares the generic Aspect.
- All concrete Aspects are instances in the applicable PROJECT STRUCTURE tree.

### Formal Claim

```CFEL
# model
Aspect;

Aspect ((NARROWER_THAN)) Node
```

## Semantics

An Aspect is a topic through which an Atom addresses its Subject.
