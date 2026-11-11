---
atom_id: CA-R-2969
ref_id: CA-R-2969
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Step.Content.Claim.Mermaid Scheme
  dependencies:
  - CAPRMEDIO_MODEL <+ Workflow.Content.Claim.Mermaid Scheme
tier: 3
status: Active
version: 1
updated_at: 2026-11-05 21:46:20 +0400
carrier_destination:
  file:
    name: CA-R-2969-CORE_META_MODEL-DECLARATION--declare-step-content-claim-mermaid-scheme.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2969-CORE_META_MODEL-DECLARATION--declare-step-content-claim-mermaid-scheme.md
  source_atom_id: CA-R-2969
  source_atom_revision: 1
  source_sha256: 04084c93e388b1c398a53d3861ac9b6f7587cc5f6a1f5e5ef4171d8a9941e2a1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Step.Content.Claim.Mermaid Scheme

## Claim

### Prose Claim

Mermaid Scheme semantics: [Workflow Mermaid Scheme declaration](CA-R-2962-CORE_META_MODEL-DECLARATION--declare-workflow-content-claim-mermaid-scheme.md#semantics).

### Formal Claim

```CFEL
# model
Step.Content.Claim.Mermaid Scheme{::0..1} :: [markdown]{::1};

Step.Content.Claim.Mermaid Scheme.*[]{::0}
```
