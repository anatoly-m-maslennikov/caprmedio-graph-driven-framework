---
atom_id: CA-C-551
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: high
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-R-1521, CA-O-127, CA-O-128, CA-P-2494, CA-P-2495]
version: 3
updated_at: 2026-10-23 03:06:32 +0400
---
# Summary

Compose mandatory container lifecycle Runs

## Concern

The always-recursive container lifecycle rule is source-defined but lacks an implemented calling Workflow that composes the independently admitted single-Atom Runs. Archive must include all contained latest Atoms, including Done descendants; requesting Done must leave contained latest Plans already Done unchanged and request Canceled for every other contained latest Plan. There is no optional descendant mode.

## Evidences

Independent read-only call-path inspection found contained_atom_targets.py discovery unconnected to lifecycle execution. selected_execution.py freezes one Workflow Run, and change_status_atom_action must remain single-Atom. run_visit_limits repeats frozen Step inputs rather than freshly binding each target; the Subjects-only batch is a different expressly scoped exception. Current singleton publication can move matching bundles without performing descendant Status Actions; P2485 adds a guard against silently moving independent current children, not the missing recursive composition. This is source evidence, not a production MCP probe or deployed incident.

### Implementation review checkpoint

P2497 pure planner is reviewed and accepted, but the first P2499 mocked composition pass was rejected. Real-boundary gaps include original root authorization validation, ordinary fresh member receipts, canonical requested-Run IDs, parent descriptor shape, member frontier/effect bindings, canonical terminal evidence and request-bound uncertain progress. P2503 repairs these before acceptance; no recursive caller completion is claimed. P2500 preview sealing, P2501 actual entrypoint/status wiring and P2502 functional test preparation remain independently owned. C553/P2504 separately repair the frozen fixture and full source-context admission.

## Blast radius

P2494 owns a narrow O127-specific calling-Workflow composition above SelectedExecution.freeze/dispatch; P2495 owns frozen functional acceptance. Reuse governed containment discovery, process descendants before parent relocation, freshly bind each target after prior effects, stop on first failure and retain earlier successes. Preserve exact old history and external references. Do not add a mode, per-child human confirmation, hidden multi-target Action, generic orchestrator or cross-Atom rollback. Installed-runtime adoption, migration, replay and Stage 2 Scope Unit operations remain separately scoped.
