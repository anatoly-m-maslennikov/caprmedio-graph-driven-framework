---
atom_id: CA-R-2969
ref_id: CA-R-2969@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Step.Content.Claim.Mermaid Scheme
  dependencies:
  - CAPRMEDIO_MODEL <+ Workflow.Content.Claim.Mermaid Scheme
tier: 3
status: Draft
version: 1
updated_at: 2026-11-05 21:46:20 +0400
carrier_destination:
  file:
    name: CA-R-2969@1-draft-CORE_META_MODEL-DECLARATION--declare-step-content-claim-mermaid-scheme.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---

## Summary

Declare Step.Content.Claim.Mermaid Scheme

## Claim

### Prose Claim

Mermaid Scheme semantics: [Workflow Mermaid Scheme declaration](CA-R-2962@1-draft-CORE_META_MODEL-DECLARATION--declare-workflow-content-claim-mermaid-scheme.md#semantics).

### Formal Claim

```CFEL
# model
Step.Content.Claim.Mermaid Scheme{::0..1} :: [markdown]{::1};

Step.Content.Claim.Mermaid Scheme.*[]{::0}
```
