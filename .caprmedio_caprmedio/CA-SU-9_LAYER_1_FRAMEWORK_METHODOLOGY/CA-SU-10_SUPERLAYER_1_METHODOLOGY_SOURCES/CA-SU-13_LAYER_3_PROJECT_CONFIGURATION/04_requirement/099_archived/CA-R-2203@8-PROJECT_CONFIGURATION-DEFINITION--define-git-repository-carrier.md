---
atom_id: CA-R-2203
ref_id: CA-R-2203@8
container:
  scope_unit: CA-SU-13
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/Git Repository
tier: 1
status: archived
version: 8
updated_at: 2026-11-11 16:04:42 +0400
carrier_destination:
  file:
    name: CA-R-2203@8-PROJECT_CONFIGURATION-DEFINITION--define-git-repository-carrier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/099_archived
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Define Git Repository Carrier

## Claim

### Prose Claim

A Git Repository is a Carrier of versioned content and Git references.

### Formal Claim

```CFEL
# model
Carrier/Git Repository ((NARROWER_THAN)) Carrier;
```

## Semantics

Git Repository contains Git Branches; this is containment, not specialization.
