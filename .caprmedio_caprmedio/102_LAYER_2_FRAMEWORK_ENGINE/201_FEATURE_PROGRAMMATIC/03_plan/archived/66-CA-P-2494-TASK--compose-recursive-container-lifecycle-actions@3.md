---
atom_id: CA-P-2494
content_role: Plan
type: Plan
label: Task
work_sequence_number: 66
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
  is_decomposition_of: [CA-P-2401]
version: 3
updated_at: "2026-10-20T21:23:49.583Z"
---
# Summary

Compose recursive container lifecycle Actions

## Objective

Apply the latest always-recursive container lifecycle rule without adding an optional mode.

## Details

At most 15 minutes own work; split before extending. Depends on reconciled R1521/D461/E502 and the P2485 carrier-safety guard. Implement only the existing source-admitted calling-Workflow composition above SelectedExecution.freeze/dispatch for O127; no such cascade caller exists in the current implementation. Reuse discover_contained_atom_targets and freshly admit separate O127 Runs: resolve containment once from latest Atom revisions, compose independent guarded child Actions before a parent relocation would silently move a current child, and stop truthfully on first failure without cross-Atom rollback. Archive all contained latest Atoms, including Done Plans. For a requested parent Status Done, leave Done Plan descendants unchanged and request Canceled for other contained latest Plans. Preserve older history and external references; do not infer carried Status from paths. Inspect existing implementation boundaries first and split before exceeding the estimate. No per-child human confirmation or new generic orchestrator.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Dependency review

Read-only caller mapping found no implemented cascade caller. Keep change_status_atom_action and each O127 Run single-Atom; do not hide multiple effects inside that Action, reuse run_visit_limits with stale parameters, or borrow the Subjects-only batch exception. Bind original O127@15/O128@15 after Core R1521@10/D461@16/E502@14. Prefer a narrow request-composition addition, deepest descendants first with fresh exact binding between effects; do not add a generic orchestrator or optional mode. This is still Backlog planning, not an implemented capability.

### Execution admission and bounded lane plan

Operator requested continuation. Dependencies are accepted: P2484-P2487/P2496 mechanical paths, source-aligned R1521@10/D461@16/E502@14 and O127@15/O128@15, with C551 explicitly retaining the missing caller. The selected locked managed Python3.14 environment is synchronized. Fresh MCP route discovery succeeds, but context still has no current Step or inner parameter contract; use the standing manual planning fallback, without an invented effect packet or Run replay.

Four initial independent read-only lanes map actual request ingress, existing containment discovery, frozen functional fixtures and source/child-method constraints. Root owns planning, source authority, integration and Git; each writer receives a separate file scope only after its interface is reviewed. Implement only mandatory source-admitted separate-Run composition, no modes, generic orchestrator, automatic retry or extra per-child confirmation. Each own-work Task stays at most15minutes and is split before extending. P2495 remains dependent Backlog acceptance; no production MCP traffic, release, deployment, migration or held-batch replay.
