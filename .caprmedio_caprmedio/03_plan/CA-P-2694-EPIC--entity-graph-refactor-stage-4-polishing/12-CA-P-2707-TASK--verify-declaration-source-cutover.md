---
atom_id: CA-P-2707
role: Plan
form: Plan
label: Task
status: Active
version: 3
updated_at: 2026-11-02 23:30:39 +0400
tier: 4
current_scope_unit: caprmedio
subjects:
  active: Scope Unit
relations:
  IS_CONTAINED_BY:
  - CA-P-2694
author: Anatoly Maslennikov
---
## Summary

Verify the Declaration source cutover

## Objective

Verify Current source readback, the absence of TOML readers/writers, and affected runtime/script tests. Run the complete suite with required integration tests before any release. No release, container restart, commit or push is implied.

## Verification

- Current readback: 44 Declarations, 43 non-root IDs, nine Ordered units; unchanged source digest.
- The live TOML is absent. Production Python has no `project_structure.toml` or `STRUCTURE_FILENAME` dependency.
- Complete run: 517 modules, 4,252 tests, no skips; launcher passed. The run reported 28 failing modules before the targeted corrections.
- The corrected host fixtures passed focused reruns. The fresh Docker query and creation-status matrix passed all nine tests; launcher verification passed again.
- The deferred O016 desired-behavior test remains one explicit expected failure under Engine task P2708.
- The W10 Docker expected-result hash versus real timestamp mismatch remains open for Engine review. Live Project carrier admission also still depends on retired D274.

Keep this verification task Active until the remaining Engine release-gate issue is resolved. Do not expand the completed Declaration migration or claim a green whole-project suite. See [Engine follow-ups](scope-unit-governance-20261031/engine-followups.md) and [verification results](scope-unit-governance-20261031/verification/final-cutover-verification.json).
