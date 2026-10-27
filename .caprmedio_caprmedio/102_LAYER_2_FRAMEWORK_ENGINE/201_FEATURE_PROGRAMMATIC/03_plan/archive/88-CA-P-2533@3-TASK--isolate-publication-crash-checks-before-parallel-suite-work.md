---
atom_id: CA-P-2533@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 88
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 3
updated_at: 2026-10-24 06:04:46 +0400
tier: 3
---
# Summary

Isolate publication crash checks before parallel suite work

## Objective

Remove the full suite's own interference from its crash-publication check without weakening coverage.

## Details

C565 remains Active. At most15minutes own work per owner, split before extending. Child P2534 exclusively owns PROJECT_TOOLS/run_full_test_suite.py; P2535 exclusively owns PROJECT_TOOLS/tests/test_full_test_suite_parallel.py. Root owns README, contracts/planning, Journal, Git and real release. Reuse the current run_module and result accounting: execute exact test_selected_subject_apply.py once before submitting remaining modules to2ordinary+2Docker pools. Preserve failure continuation/counts/skips, launcher sequencing, cancellation and30second child/1800second module deadlines. No new Workflow/gate, generic scheduler, dependency, public API, production caching change or global lock. Focused synthetic scheduler checks and independent review precede any fresh real release; its complete full suite cannot be substituted by focused checks.

### Acceptance

P2534/P2535 Done after independent review APPROVE and root31focused checks (17scheduler+14adjacent, separate totals); README matches actual source. Exact predecessor carriers retained and children relocated within the Done Task hierarchy. C565 remains Active pending fresh full-suite/release evidence. C564 tracks runner245/test272physical-line debt; clean pinned Ruff is not E539 exception acceptance. New P2536 owns the requested fresh Local release; source boundaries freeze before launch.
