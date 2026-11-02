---
subjects:
  governs: Entity/Object/Occurrent/Execution/Workflow Run
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - Entity/Object/Occurrent/Execution/Step Run
  - Entity/Object/Continuant/History/Journal > Event Record
  - Entity/Graph Syntax > Relation//IS_EXECUTION_OF
version: 18
updated_at: 2026-10-29 07:32:39 +0400
relations: {}
atom_id: CA-R-1510@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Workflow Run

## Claim scope

the Workflow Run entity.

## Claim

A Workflow Run means one actual execution of exactly one Workflow against the inputs and parameters supplied for that run. The execution follows the Workflow's typed Relations and retains its actual Step Runs, outcomes and applicable retry allowance. A Workflow Run is distinct from the reusable Workflow and from the Journal Records that describe its execution; a reference to the definition does not prove that a run occurred.

### Formal claim

```text
Workflow Run ((IS_EXECUTION_OF)) Workflow
```

## Details

CA-A-1260 makes the existing one-Workflow binding formal. The run remains distinct from the definition and any Event Record about it.
