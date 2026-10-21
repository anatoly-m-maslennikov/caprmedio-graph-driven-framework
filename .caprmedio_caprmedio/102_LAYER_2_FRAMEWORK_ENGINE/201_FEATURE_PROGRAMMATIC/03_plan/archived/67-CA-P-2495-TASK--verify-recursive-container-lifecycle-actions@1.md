---
atom_id: CA-P-2495
content_role: Plan
type: Plan
label: Task
work_sequence_number: 67
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
  is_decomposition_of: [CA-P-2401]
version: 1
updated_at: "2026-10-20T20:50:22.353Z"
---
# Summary

Verify recursive container lifecycle Actions

## Objective

Independently accept Archive and target-Done recursion using disposable frozen Projects.

## Details

At most 15 minutes own work; split before extending. Depends on reviewed P2494 implementation. Use a small functional matrix: nested Archive including Done children, target-Done preserves Done descendants and cancels unfinished descendant Plans, exact old history bytes, external-reference exclusion, unsupported-model or occupied-destination refusal, and partial failure preserving earlier successes. Verify parent carrier relocation never silently carries a still-current child and no optional descendant mode exists. Bind receipts to frozen source and fixture hashes; do not use live Atoms or the production MCP port.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.
