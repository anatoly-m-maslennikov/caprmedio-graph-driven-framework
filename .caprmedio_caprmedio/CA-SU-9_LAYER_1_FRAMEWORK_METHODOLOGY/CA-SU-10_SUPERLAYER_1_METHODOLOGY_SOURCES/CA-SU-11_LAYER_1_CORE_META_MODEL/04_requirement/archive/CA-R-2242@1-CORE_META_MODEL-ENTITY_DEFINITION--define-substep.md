---
atom_id: CA-R-2242@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Atom/Content Role: Operations/Type: Step >{0+} Atom/Content Role: Operations/Type: Sub-step'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Atom/Content Role: Operations/Type: Step'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
version: 1
updated_at: 2026-10-29 07:32:39 +0400
relations: {}
tier: 1
---
## Summary

Define Sub-step

## Claim

A Sub-step is a distinct leaf unit contained in exactly one Step. It specifies a call to exactly one reusable Action with parameters and input bindings. It cannot call a Workflow or contain further Sub-steps.

### Formal claim

```text
Atom/Content Role: Operations/Type: Step >{0+} Atom/Content Role: Operations/Type: Sub-step
```

## Semantics

A Sub-step is not another name for a nested Step. Its Action is referenced and reusable, not structurally contained by the Sub-step. The call and its eventual execution are distinct; this definition creates neither a Run nor a record.

## Details

A1262–A1264 resolve further nesting and call targets. Containment supplies no inheritance. Exact Atom-Type admission and any properties requiring separate definitions remain uncompleted; no Sub-step Run kind or numeric Atom ID is invented here.

CA-A-1279 confirms the already-settled container hierarchy; no separate Type-catalog decision is inferred from it.

CA-A-1280 adopts the compact cardinality spelling without changing the counts.
