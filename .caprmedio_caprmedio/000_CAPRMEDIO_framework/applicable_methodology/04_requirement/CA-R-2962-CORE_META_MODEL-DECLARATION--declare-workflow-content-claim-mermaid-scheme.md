---
atom_id: CA-R-2962
ref_id: CA-R-2962
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Workflow.Content.Claim.Mermaid Scheme
tier: 3
status: Active
version: 1
updated_at: 2026-11-05 21:06:57 +0400
carrier_destination:
  file:
    name: CA-R-2962-CORE_META_MODEL-DECLARATION--declare-workflow-content-claim-mermaid-scheme.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2962-CORE_META_MODEL-DECLARATION--declare-workflow-content-claim-mermaid-scheme.md
  source_atom_id: CA-R-2962
  source_atom_revision: 1
  source_sha256: a6c083c84fc149c6b64dff4b6cd4499638a957f2a81311fd0e6c3e3531ba4634
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Workflow.Content.Claim.Mermaid Scheme

## Claim

### Prose Claim

The scheme shows all Workflow Steps, including nested Steps.

### Formal Claim

```CFEL
# model
Workflow.Content.Claim.Mermaid Scheme{::1} :: [markdown]{::1};

Workflow.Content.Claim.Mermaid Scheme.*[]{::0}
```

## Semantics

The value is exactly one `mermaid`-labelled fenced Markdown block. A Mermaid Scheme is a visual Minto summary of its owning Claim's text: removing it must leave that text's specification complete and unchanged. It may repeat the text.
