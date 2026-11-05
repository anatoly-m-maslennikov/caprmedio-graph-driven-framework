---
atom_id: CA-A-1279
ref_id: CA-A-1279
role: Analysis & Advisory
form: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
topics:
  main_subject: 'Model::CAPRMEDIO::Continuant/Governing Objects/Atom/Content Role: Operations/Type:
    Workflow'
version: 3
tier: 3
updated_at: 2026-11-02 15:49:28 +0400
container:
  scope_unit: CA-SU-00
---
# Summary

Retain the settled Workflow container hierarchy

## Decision

The container hierarchy is already settled:

```text
Workflow >{>=1} Step >{>=0} Substep
```

A Workflow contains at least one Step. A Step may contain zero or more Substeps. Each Step belongs to exactly one immediate Workflow; each Substep belongs to exactly one immediate Step. Containment is not specialization.

Do not reopen this hierarchy as a separate choice between independent entities and embedded content, or introduce extra Operations Types on that basis. The established leaf-call boundaries and permission for recursive Workflow calls remain unchanged.

## State

The Workflow, Step and Substep Definition Drafts and Model proposal use the Operator's latest cardinality spelling. Current source adoption, catalog reconciliation and Engine implementation remain pending.
