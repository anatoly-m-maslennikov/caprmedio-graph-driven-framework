---
atom_id: CA-P-2550
content_role: Plan
type: Plan
label: Task
work_sequence_number: 10
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2536]
  depends_on: [CA-P-2549]
version: 4
updated_at: "2026-10-21T16:32:40Z"
---
# Summary

Execute focused Local release and adopt candidate

## Objective

After P2549's focused proof, execute one fresh Operator-authorized Local release continuation, install the candidate and verify the observed Project MCP adoption.

## Details

At most 15 minutes own work excluding passive release wait; do not start until P2549 is Done and its exact module list, source-currentness/no-diff proof and focused receipt are reviewed. Use a fresh Run ID and the existing canonical host PROJECT_TOOLS/release.py local entrypoint with the recorded repeated --test-module arguments; do not replay a failed Run or invoke the no-argument complete-suite path for this continuation. Reuse the prior 53-test Docker/related proof only under P2549's exact no-diff binding; execute the focused changed/related host modules, then retain the normal source/product/version/candidate/install/Project-MCP smoke and selected-Project cleanup safeguards. Root owns Git, Docker and runtime effects. Preserve foreign/unowned/referenced resources, stop on any failed or uncertain gate, and report focused-versus-full scope honestly. CA-O-188 public release remains a separate full-suite gate; C564 remains unresolved. No Stage 2 Scope Unit operations or whole-Epic closure.

### Definition of Done

Fresh observed evidence records the focused module results, source/currentness and reused Docker-proof binding, version/product/image identities, installed package and actual MCP health/discovery smoke, candidate ownership and cleanup disposition. Only then may P2536's Local release/adoption continuation be marked complete; absent complete evidence, leave it pending and do not claim release success, full-suite green, public release or whole-Epic completion.

### Activation after focused admission

P2549Done@3 records the fresh canonical focused admission: exactly 16 selected host modules, 131 tests, zero skips, zero failures and exit 0, with the exact module list in .caprmedio_tmp/local-focused-admission-20261021.log. The fresh actual-release Run ID is local-20261021-focused-adoption-01 and must use the same 16 --test-module arguments before candidate installation and observed Project-MCP smoke. This activation is not release success; preserve the complete-suite/public-gate distinction and stop on any failed or uncertain effect.
