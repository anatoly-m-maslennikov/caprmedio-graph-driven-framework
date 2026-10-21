---
atom_id: CA-P-2475
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2469]
version: 1
updated_at: "2026-10-20T18:45:40.192Z"
---
# Summary

Bind same-path recovery to published state

## Objective

Prevent recovery from overwriting an unrelated concurrent canonical edit after a same-path promotion effect fails.

## Details

At most 15 minutes own work; split before extending. Root read-only integration found same-path restoration obtains the current fingerprint and overwrites non-predecessor bytes without first proving they are this Action's own publication. Require bound expected published state before restoring; changed or unverified state reports recovery uncertainty and remains untouched. Preserve exact ordinary rollback and mutation-free no-op. Add an injected concurrent-edit regression; do not invent replay or lock protocols.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.
