---
atom_id: CA-P-2479@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2465
version: 4
updated_at: 2026-10-24 08:06:50 +0400
tier: 3
---
# Summary

Align native promotion parser regression fixture

## Objective

Resolve the three independent ATOM_SEARCH Atom-operation regression failures without weakening production admission or truthful rejection ordering.

## Details

At most 15 minutes own work; split before extending. The frozen full promotion suite passed 22 tests, but ATOM_SEARCH/test_atom_operations ran 30 with two failures and one error: synthetic settings lack Project name before complete-carrier validation, and a temporary carried-marker-unsupported expectation remains after support was implemented. Reuse checked-in frozen authority/current fixture conventions; remove or replace obsolete policy assertions rather than reintroducing a refusal. Retain strict role mismatch, source pins and mutation-free rejection proof.

### Definition of Done

Focused synthetic-project checks and independent review verify the stated behavior without live MCP tests, deployment, migration, or held-batch replay. Review dependent next Task before acceptance execution.

### Verified execution checkpoint

The checked-in frozen fixture now supplies Project name, operators, structure and STATUS_FIXTURE. The obsolete unsupported-marker expectation now checks rejection of an incomplete unsealed request without fresh allocation. Full Atom cohort 30/30 and Ruff passed (15.82s real); independent final fixture review APPROVE confirmed no production guard weakened and unchanged production hashes.
