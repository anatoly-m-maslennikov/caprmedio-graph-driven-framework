---
atom_id: CA-P-2515@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 75
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
version: 4
updated_at: 2026-10-24 06:04:46 +0400
tier: 3
---
# Summary

Repair Plan bundle ownership and flat history fixtures

## Objective

Close the bounded C557 full-release fixture gap without changing production semantics.

## Details

At most15 minutes own work; split before extending. Depends on the current failed full suite finishing and independent diagnosis. Own only201_TOOLS/tests/test_status_bundle_publication.py and test_status_bundle_publication_independent.py. Declare the exact synthetic amber Scope Unit in the primary fixture, preserving strict production ownership validation. Route only Plan predecessor assertions, collision targets and fault-injection history variables to the owning Scope Unit shared03_plan/archived; keep nested current Done paths and Operations/Step local history unchanged. Preserve all injection-reached assertions, exceptions, snapshots, exact bytes and foreign-state safety. No production/test source edits while that suite collects results. Acceptance: Both named suites plus test_flat_plan_archive pass; independent exact-diff review confirms no weakened recovery checks or production changes. After completion review and update dependent P2513 before a fresh complete normal local release; no waived checks, live corpus fallback, production mutation testing or held/uncertain replay.

### Complete gate result and execution review

The full run local-20261021-mcp-health-verified-env has finished:424 modules,3796 tests,zero skips,six failed modules; launcher integration passed. No install/startup phase ran. Source repair may now begin under the exclusive scope below, followed by independent diff review and fresh focused/full checks. No failed receipt is reused as acceptance.

### Verified completion and next dependency review

Frozen two-file fixture repair declares exact amber ownership under a distinct synthetic Project identity, re-resolves/rebinds current selection and corrects only Plan predecessor/collision/fault history targets to owning shared03_plan/archived. Release virtualenv checks:24/24 status-bundle and14/14 flat archive pass. Independent final setup/diff review APPROVE; all fault reachability, exact recovery/foreign-state, Operations-local and legacy-byte checks remain. Hashesd6da940b0d62cebe4435ae1f985da7ea467104bf45670304c493be36a03f9a66 andc6c34cd1608bcd522fa1a62407076cf1f256e1c29b71165b4cac2711f64e733f. Review dependent P2513; no deployed/full-release claim.
