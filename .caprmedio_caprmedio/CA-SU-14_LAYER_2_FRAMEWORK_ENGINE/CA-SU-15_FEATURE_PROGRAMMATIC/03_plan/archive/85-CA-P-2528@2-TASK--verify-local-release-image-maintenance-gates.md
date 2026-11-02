---
atom_id: CA-P-2528@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 85
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 2
updated_at: '2026-10-21T10:13:48Z'
---
# Summary

Verify Local release image maintenance gates

## Objective

Verify Local release image maintenance gates.

## Details

Prepare focused functional regressions with the existing disposable fixtures: green suite before candidate resolve/tag maintenance; exact installed-image verification and --no-build launch; failed suite skips candidate/cleanup/deployment; tag/preparation refusal preserves installation; image removal follows verified launch. Retention cases wait for the P2526 scope and P2527 API freeze. Candidate preparation failure is fatal; obsolete-image cleanup failure retains the existing pending/nonzero disposition. Use selected uv Python 3.14, Project Temporary State, and write-free AST checks. At most 15 minutes own work; split before extending. No Docker, production MCP, release, Atom or Git effects.

### Current reviewed checkpoint

Focused ordering/proof-guard increment accepted. Worker explicit32/32 in7.082s and discovery40/40 in10.831s are overlapping portfolios, not72unique tests. Root independent7-module gate59/59 passed6.330s in selected Python3.14/Project TMPDIR; AST/Ruff/diff and independent review APPROVE. Positive order: green suite → canonical candidate resolve → installed exact SHA resolve → --no-build launch → image cleanup. Negative cases cover failed suite, candidate/tag preparation and first installation without a verified launcher. No Docker daemon, production MCP or real release was run; printed release-phase lines came from synthetic fixtures. Test hashes: simplef8aa2548efbd78a6a943dca246bc4053a7eac78032fe94bdf80e677905e42306; cleanupd924a0940414e33124ac3fd634400da8a1f29cc1b3254665c3b8a21340c2b702. Existing619-line simple fixture remains its canonical owner; bounded modified portion, no broad style-clean claim. Retention-count/scope acceptance remains P2529, not this Task.
