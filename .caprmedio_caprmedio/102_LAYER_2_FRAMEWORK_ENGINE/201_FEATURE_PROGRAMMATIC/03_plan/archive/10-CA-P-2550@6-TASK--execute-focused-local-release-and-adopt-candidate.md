---
atom_id: CA-P-2550@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 10
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2536
  depends_on:
  - CA-P-2549
version: 6
updated_at: 2026-10-24 06:04:42 +0400
tier: 3
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

### Actual focused Local release/adoption result

Root observed the fresh Run `local-20261021-focused-adoption-01` complete with
`completed_with_cleanup_pending`, CLI1 and `failed_step: null`. The approved
focused path ran exactly 16 selected host modules: 131 tests, zero skips and
zero failures. It did not rerun the complete suite or the expensive real-Docker
12-test set.

The installed candidate is version `0.4.4.10`, with image tag
`caprmedio-runtime:0.4.4.10-20261021T131557Z-0555ed0be341` (candidate digest
prefix `0555ed0`). Container
`649228a677661439d12d9771d606652525480ab4a2f5ef2131036b451a1cae7e` is
healthy; `/health` returned `ready: true`; connected MCP
`discover_operations` returned O164 v20. The launcher matched image/source
fingerprint `80fc2b4` and the current Project. The durable release receipt is
`.caprmedio_runtime/simple_local_release/reports/local-20261021-focused-adoption-01.md`.

Cleanup removed the old Project container
`e81250f8ed4c39bf08007e05449c63b88d5c96b8f65f94f6fdec8622c6817d84` and
owned images
`00a99705a531c5673fa019b125ac3c473ec16934d36c2ac00cbec9578fe286a6`,
`08f26a9b8b14b6884fb6a8011264ea2e7c99a12f687377c355e50b34c2e4f929`, and
`c189bc1a31fc7da3513249e334b2498a8d4ad9d6ee3e32bb9c67d9b3884b3062`.
Unknown, incomplete or foreign resources were retained, including image
`650023dd711fad2e48a3446b2780733d20881adbe088a8f63a09af48f938fd83`; no
force or broad prune was used. The selected-workflow cleanup Run
`local-release-cleanup-problem-20261021-01` was observed ENQUEUED and then
officially cancelled through the SDK as CANCELLED, with no child cascade and
no observed effect. This is the cleanup-pending disposition, not a claim that
all ownership cleanup is complete; P2551 owns the bounded follow-up.

This observed focused adoption closes P2550 only. It is not a full-suite or
public-release gate, and it does not close P2536, CA-C-571, CA-C-564 or the
whole Epic.
