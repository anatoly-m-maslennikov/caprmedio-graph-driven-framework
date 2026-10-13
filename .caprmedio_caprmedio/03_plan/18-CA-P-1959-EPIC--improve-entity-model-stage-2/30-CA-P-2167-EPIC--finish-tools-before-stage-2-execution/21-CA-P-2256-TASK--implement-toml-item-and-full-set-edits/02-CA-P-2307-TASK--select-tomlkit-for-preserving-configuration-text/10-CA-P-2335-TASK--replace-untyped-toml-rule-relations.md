---
atom_id: CA-P-2335
content_role: Plan
type: Plan
label: Task
work_sequence_number: 10
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Relation, Plan]
version: 1
updated_at: "2026-10-13 20:11:07 +0400"
relations:
  is_decomposition_of: [CA-P-2307]
---
# Summary

Replace untyped TOML rule relations

## Objective

M383, D632 and E635 carry meaningful admitted typed relations instead of relates_to.

## Details

Estimated own work: up to 15 minutes. The Operator rejected a context-only workaround and requires typed relations. Review every existing broad link against source content and the admitted Relation Kind definitions. Do not substitute a generic related_to alias, invent a kind, or force an incorrect type just to preserve an edge. Identify inverse relations already owned by another Atom and ask about unclear or removed links before mutation.

Independently review the mapping first, then narrowly update the three source relation collections with exact predecessor archives, Version +1 and actual Updated At. Keep Summary, Subjects and body content unchanged unless a concrete approved correction requires otherwise. Independently check the final sources and run actual finite PRMEDO admission. Keep C/A, live publication and Core migration outside this task.

### Definition of Done

The Plan is not Done if a relation is untyped, an endpoint is silently lost or guessed, current source admission fails, exact predecessor history is missing, or independent semantic and final-source review is absent.
