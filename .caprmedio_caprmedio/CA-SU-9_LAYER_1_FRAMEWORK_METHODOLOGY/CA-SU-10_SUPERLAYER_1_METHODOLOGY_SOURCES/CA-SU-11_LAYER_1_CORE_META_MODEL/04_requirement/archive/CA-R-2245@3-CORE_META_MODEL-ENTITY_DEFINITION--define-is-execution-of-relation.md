---
atom_id: CA-R-2245@3
content_role: Requirement
type: Relation Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Syntax > Relation//IS_EXECUTION_OF
  depends_on:
  - Entity/Object/Occurrent/Execution/Workflow Run
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
version: 3
relations: {}
tier: 1
updated_at: 2026-10-29 10:13:49 +0400
---
## Summary

Define IS_EXECUTION_OF Relation

## Claim

IS_EXECUTION_OF connects an actual execution to the reusable definition being
executed. The stored direction is Workflow Run to Workflow. HAS_EXECUTION is
its declared derived inverse, not a second stored fact.

## Semantics

Workflow Run ((IS_EXECUTION_OF)) Workflow

The reusable definition is not the execution itself. Workflow Run's binding to
one Workflow belongs in the Workflow Run Entity Definition, not in every use
of this Relation Type.

## Details

This named Type uses the general `((RELATION_TYPE))` form. It creates neither
a Current registration nor a runtime fact.
