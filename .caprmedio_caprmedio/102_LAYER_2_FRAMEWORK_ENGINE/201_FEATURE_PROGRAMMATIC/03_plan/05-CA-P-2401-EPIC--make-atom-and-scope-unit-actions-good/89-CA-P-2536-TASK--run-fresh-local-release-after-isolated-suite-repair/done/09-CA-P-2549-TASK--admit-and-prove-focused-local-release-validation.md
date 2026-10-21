---
atom_id: CA-P-2549
content_role: Plan
type: Plan
label: Task
work_sequence_number: 9
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2536]
version: 4
updated_at: "2026-10-21T16:32:40Z"
---
# Summary

Admit and prove focused Local-release validation

## Objective

Bind the Operator-approved one-run --test-module continuation to the existing Local-release workflow and produce release-ready focused proof without rerunning the complete discovered suite.

## Details

At most 15 minutes own work; split before extending. Use the current CA-O-164/CA-O-165/CA-O-169 definitions and the existing host PROJECT_TOOLS/release.py local path. The complete suite remains the default. Freeze the current source, Git/runtime inputs and a fresh Run ID before recording the exact changed/related host-module list for the repaired image-selection, local-release, runner, cleanup and scheduler paths. Reuse the prior 53-test Docker/related proof from .caprmedio_tmp/focused-release-repair-20261021/focused-summary.json only after proving exact Engine/runtime/pyproject/uv.lock/version no-diff; do not rerun the expensive 12 Docker tests. Do not invent a second runner, bypass selection guards, call focused evidence full-suite green, or touch Stage 2 Scope Unit work. Preserve exact logs, source hashes, counts, skips, failures and protected production/resource baselines. No version bump, installed replacement, image cleanup, Docker mutation, public release or push in this Task; P2550 owns actual Local release/adoption. C564 remains Active and unresolved.

The implementation/readiness proof is not the actual gate. The observed canonical admission proof ran exactly 16 reviewer-designated host modules, 131 tests, zero skips and zero failures with exit 0. Durable evidence is retained at .caprmedio_tmp/local-focused-admission-20261021.log with the exact full module list; no complete suite or real Docker tests ran. P2550 may now proceed with the same 16 --test-module arguments, while the actual release/adoption remains a separate observed gate.

### Definition of Done

The existing CLI accepts only the explicitly recorded repository-relative focused modules, the exact command/Run ID/module list/source-currentness and no-diff proof are retained, all selected host modules pass with zero required skips, and independent planning/proof review records validation_scope: focused. The reused Docker proof is bound to the retained P2548 receipt and current no-diff evidence; no stale full-suite claim is made. Review dependent P2550 before execution.
