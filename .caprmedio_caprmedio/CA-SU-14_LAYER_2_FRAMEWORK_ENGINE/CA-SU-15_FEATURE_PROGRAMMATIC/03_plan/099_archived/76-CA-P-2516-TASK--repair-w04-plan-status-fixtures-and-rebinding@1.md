---
atom_id: CA-P-2516
content_role: Plan
type: Plan
label: Task
work_sequence_number: 76
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
  is_decomposition_of: [CA-P-2401]
version: 1
updated_at: "2026-10-21 05:01:44 +0400"
---
# Summary

Repair W04 Plan status fixtures and rebinding

## Objective

Close the bounded C557 full-release fixture gap without changing production semantics.

## Details

At most15 minutes own work; split before extending. Depends on the current failed full suite finishing and independent diagnosis. Own only the W04 synthetic fixture/helper and test_selected_w04_fixture.py/test_selected_w04_status_matrix.py after complete failure-set review. Diagnose the nonexistent old Plan archive target and Plan Draft preview declared-versus-observed selected-binding mismatch before changing the fixture. Use canonical actual Plan paths and fresh fixture source bindings after setup mutations. Preserve matrix totals29 applied/eight no-ops/eight refusals; never change production currentness guards, counts or success criteria merely to pass. No production/test source edits while that suite collects results. Acceptance: W04 fixture and complete29/8/8 matrix plus one adjacent selected-workflow check pass; independent review confirms source-currentness refusal and non-Plan paths remain protected. After completion review and update dependent P2513 before a fresh complete normal local release; no waived checks, live corpus fallback, production mutation testing or held/uncertain replay.
