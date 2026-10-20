---
atom_id: CA-P-2477
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2467]
version: 1
updated_at: "2026-10-20T18:51:57.976Z"
---
# Summary

Reduce new Draft path complexity

## Objective

Reduce new configured Ruff C901 findings and avoid worsening touched legacy complexity through small cohesive extractions in the new Draft implementation paths.

## Details

At most 15 minutes own work; split before extending. Root compared the exact HEAD baseline: atom_operations had 8 C901 findings and lifecycle_intents 5. Current output has 17, including new restore/publish/rename/preflight complexity plus increased existing dispatch/update complexity. These are not all pre-existing baseline debt. Preserve every guard, rollback, byte pin, caller and test; no behavior change or broad legacy cleanup. Keep one behavioral owner and extract only coherent new responsibilities.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.
