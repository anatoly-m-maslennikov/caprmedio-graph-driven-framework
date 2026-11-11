---
atom_id: CA-R-2961
ref_id: CA-R-2961
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Workflow.Content.Claim
tier: 3
status: Active
version: 1
updated_at: 2026-11-05 21:06:57 +0400
carrier_destination:
  file:
    name: CA-R-2961-CORE_META_MODEL-DECLARATION--declare-workflow-content-claim.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2961-CORE_META_MODEL-DECLARATION--declare-workflow-content-claim.md
  source_atom_id: CA-R-2961
  source_atom_revision: 1
  source_sha256: cb7791a774c23a62b838583a3dffa35685eed2617bea0200535d6cfc702506c7
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Workflow.Content.Claim

## Claim

### Formal Claim

```CFEL
# model
Workflow.Content.Claim{::1} :: []{::0};

Workflow.Content.Claim.*[in (Mermaid Scheme, Prose Claim, Formal Claim)]{::1..3};

Workflow.Content.Claim.Mermaid Scheme ;> Workflow.Content.Claim.Prose Claim;

Workflow.Content.Claim.Prose Claim ;> Workflow.Content.Claim.Formal Claim
```

## Semantics

Workflow Claim has unique child Property names. At least one of Prose Claim and Formal Claim is present, and their text together specifies the Workflow completely without reliance on the Mermaid Scheme.
