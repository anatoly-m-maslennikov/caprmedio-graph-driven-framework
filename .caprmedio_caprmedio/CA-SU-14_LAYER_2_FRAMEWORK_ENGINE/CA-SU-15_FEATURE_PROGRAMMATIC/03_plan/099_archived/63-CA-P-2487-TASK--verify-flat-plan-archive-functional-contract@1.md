---
atom_id: CA-P-2487
content_role: Plan
type: Plan
label: Task
work_sequence_number: 63
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
updated_at: "2026-10-20T19:57:02.969Z"
---
# Summary

Verify flat Plan archive functional contract

## Objective

Independently verify the integrated flat Plan archive behavior and exact retained-history contract.

## Details

At most 15 minutes own work; split before extending. Depends on reviewed P2484-P2486 frozen source. Synthetic frozen-authority filesystem functional tests only: root Plan, nested leaf Plan, empty optional matching directory, independently current descendant refusal, flat collision, exact predecessor bytes, retained decomposition and unrelated incoming links, and unchanged legacy nested archive/ bytes. No production-port tests, live-project migration or deployment. Review exact code and focused regression evidence; do not require tests of private helper shapes.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.
