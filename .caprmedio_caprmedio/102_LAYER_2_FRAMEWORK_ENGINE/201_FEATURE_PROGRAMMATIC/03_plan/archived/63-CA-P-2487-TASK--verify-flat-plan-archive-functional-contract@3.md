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
status: Active
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 3
updated_at: "2026-10-20T20:36:20.780Z"
---
# Summary

Verify flat Plan archive functional contract

## Objective

Independently verify the integrated flat Plan archive behavior and exact retained-history contract.

## Details

At most 15 minutes own work; split before extending. Depends on reviewed P2484-P2486 frozen source. Synthetic frozen-authority filesystem functional tests only: root Plan, nested leaf Plan, empty optional matching directory, independently current descendant refusal, flat collision, exact predecessor bytes, retained decomposition and unrelated incoming links, and unchanged legacy nested archive/ bytes. No production-port tests, live-project migration or deployment. Review exact code and focused regression evidence; do not require tests of private helper shapes.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Test preparation and Evaluation selection

Independent functional-test preparation starts now against the existing public lifecycle/publication boundary; final integrated acceptance waits for reviewed P2484-P2486 source. The Task may own its test file before dependent production changes, without claiming implementation acceptance.

E637@1/E389@12 select the least-cost stable observable boundary per declared predicate: disposable frozen-authority filesystem lifecycle cases expose root/nested flat placement, @Version filenames, exact N predecessor versus changed N+1, identity/relations/content preservation and withdrawal from Current authority. Before/after snapshots expose stale/collision/symlink/unauthorized bundle refusal and unchanged old history/assets/references. Injected filesystem failures verify only the admitted within-Action recovery boundary, not mock choreography or automatic cross-Atom rollback. Source-bound deterministic validator cases expose accepted flat Archived Plan placement and rejected nested/wrong-Version placement while preserving historical Status bytes; Subject preview/publication checks expose identical intended and actual predecessor destinations and mutation-free no-op. Existing non-Plan/non-Archived functional cohorts provide justified regression defense for shared owners. Installed/Docker E2E is not selected: the governed local path/byte predicates are fully observable at this narrower real-filesystem boundary, with no runtime-activation claim.

Keep the portfolio predicate-driven rather than fixed test counts/ratios. Pin exact current governing authority and test source; no mutable live Atom fixture. Report unresolved predicates explicitly. Every Task retains at most 15 minutes own work; split test preparation or acceptance if that budget is exceeded.

### Prepared fixture checkpoint and remaining decomposition

The independent preparation lane stopped at its bounded own-work split point. New tests/test_flat_plan_archive.py SHA-256 7048b55de7fdaf9ffbe7af0e4a84d7b82a26362c2fadeca44bc65d630f89fcab contains seven fixture methods covering root/nested placement, byte-exact predecessor/relations, empty/asset bundles, collision, non-Plan/Done controls, legacy bytes without a location assumption and Current withdrawal. Unintended inherited test collection was removed. The targeted Current withdrawal case passed; the final full file and Ruff have not yet run after the last fixture adjustment. This is preparation evidence, not final integrated success.

P2492 owns the additional Draft promotion/current-descendant predicates after reviewed dependencies; P2493 owns final independent frozen acceptance. Each is a separate at-most-15-minute Task before extending the preparation budget. This parent remains an Active roll-up until its admitted predicates have actual evidence and C549 limits are explicit.
