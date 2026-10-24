---
atom_id: CA-P-2301
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Action, Workflow, Plan]
version: 1
updated_at: "2026-10-13 04:40:03 +0400"
relations:
  is_decomposition_of: [CA-P-2294]
  blocks: [CA-P-2259]
---
# Summary

Bind selected Read receivers

## Objective

Existing selected execution supplies concrete request, source, schema and permission bindings to the implemented Atom and Scope Unit Read/Query adapters.

## Details

Estimated own work: 15 minutes. Split larger work before execution. Reopen the accepted O046/O047/O201/O207/O211/O212 and Delivery contracts. Reuse genuine RunExecutionSession context and ProjectSelection, preserving exact current source pins and complete original-identity frontiers. Do not substitute the unrelated Artifact/Journal Query bindings. Find and Read remain independent; effects are empty.

Implement only the smallest source-only receiving connection with isolated actual-admission fixtures. Preserve existing CLI interfaces and registered routes. A descriptor or ProjectSelection is not permission. Do not force a fabricated mutation authorization onto ordinary direct reads. If the accepted sources cannot establish a concrete receiving map, report that gap instead of inventing a public protocol or claiming connected runtime capability. No live registration, new publication mechanism or Core migration is included.

### Definition of Done

Not Done until actual receiving callers, source/schema/view mapping and independent positive/refusal/currentness fixtures are pinned and accepted. Generic injected callbacks or descriptor-only compilation are preparation, not completion. Full selected-manifest/placement/runtime acceptance remains with CA-P-2269–2278.
