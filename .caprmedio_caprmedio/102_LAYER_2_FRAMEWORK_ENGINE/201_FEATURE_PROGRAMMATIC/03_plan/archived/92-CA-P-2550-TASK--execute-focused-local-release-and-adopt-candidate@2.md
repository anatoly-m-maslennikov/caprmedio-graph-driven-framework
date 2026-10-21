---
atom_id: CA-P-2550
content_role: Plan
type: Plan
label: Task
work_sequence_number: 92
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2536]
  depends_on: [CA-P-2549]
version: 2
updated_at: "2026-10-21T16:29:30Z"
---
# Summary

Execute focused Local release and adopt candidate

## Objective

After P2549's focused proof, execute one fresh Operator-authorized Local release continuation, install the candidate and verify the observed Project MCP adoption.

## Details

At most 15 minutes own work excluding passive release wait; do not start until P2549 is Done and its exact module list, source-currentness/no-diff proof and focused receipt are reviewed. Use a fresh Run ID and the existing canonical host PROJECT_TOOLS/release.py local entrypoint with the recorded repeated --test-module arguments; do not replay a failed Run or invoke the no-argument complete-suite path for this continuation. Reuse the prior 53-test Docker/related proof only under P2549's exact no-diff binding; execute the focused changed/related host modules, then retain the normal source/product/version/candidate/install/Project-MCP smoke and selected-Project cleanup safeguards. Root owns Git, Docker and runtime effects. Preserve foreign/unowned/referenced resources, stop on any failed or uncertain gate, and report focused-versus-full scope honestly. CA-O-188 public release remains a separate full-suite gate; C564 remains unresolved. No Stage 2 Scope Unit operations or whole-Epic closure.

### Definition of Done

Fresh observed evidence records the focused module results, source/currentness and reused Docker-proof binding, version/product/image identities, installed package and actual MCP health/discovery smoke, candidate ownership and cleanup disposition. Only then may P2536's Local release/adoption continuation be marked complete; absent complete evidence, leave it pending and do not claim release success, full-suite green, public release or whole-Epic completion.
