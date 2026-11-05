---
atom_id: CA-R-draft
status: Draft
topics:
  main_subject: CAPRMEDIO_MODEL <+ Workflow.Content.Claim.Mermaid Scheme
version: 1
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-05 21:06:57 +0400
carrier_destination:
  file:
    name: CA-R-draft-CORE_META_MODEL-DECLARATION--declare-workflow-content-claim-mermaid-scheme.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
container:
  scope_unit: CA-SU-11
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
