---
atom_id: CA-P-2515
content_role: Plan
type: Plan
label: Task
work_sequence_number: 75
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
updated_at: "2026-10-21 05:01:19 +0400"
---
# Summary

Repair Plan bundle ownership and flat history fixtures

## Objective

Close the bounded C557 full-release fixture gap without changing production semantics.

## Details

At most15 minutes own work; split before extending. Depends on the current failed full suite finishing and independent diagnosis. Own only201_TOOLS/tests/test_status_bundle_publication.py and test_status_bundle_publication_independent.py. Declare the exact synthetic amber Scope Unit in the primary fixture, preserving strict production ownership validation. Route only Plan predecessor assertions, collision targets and fault-injection history variables to the owning Scope Unit shared03_plan/archived; keep nested current Done paths and Operations/Step local history unchanged. Preserve all injection-reached assertions, exceptions, snapshots, exact bytes and foreign-state safety. No production/test source edits while that suite collects results. Acceptance: Both named suites plus test_flat_plan_archive pass; independent exact-diff review confirms no weakened recovery checks or production changes. After completion review and update dependent P2513 before a fresh complete normal local release; no waived checks, live corpus fallback, production mutation testing or held/uncertain replay.
