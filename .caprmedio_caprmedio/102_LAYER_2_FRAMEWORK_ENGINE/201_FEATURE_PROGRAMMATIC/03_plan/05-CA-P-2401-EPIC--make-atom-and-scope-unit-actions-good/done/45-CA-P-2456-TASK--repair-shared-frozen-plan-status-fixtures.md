---
atom_id: CA-P-2456
content_role: Plan
type: Plan
label: Task
work_sequence_number: 45
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2401
version: 5
updated_at: 2026-10-25 17:32:27 +0400
tier: 3
---
# Summary

Repair shared frozen Plan-status fixtures

## Objective

Align the three directly affected frozen Plan-status fixtures with the approved current status corpus, without weakening validation or changing intentional legacy fixtures.

## Details

Own only the shared frozen inputs and directly affected test consumers for `test_proposed_relation_admission`, `test_relation_fixture_isolation`, and `test_status_bundle_publication_independent`. Preserve inherited Plan-status authority, exact source provenance and legacy-domain boundaries. Run focused checks for these three modules and record actual results; do not broaden into the full local release or infer a production guard defect.

At most15minutes ownwork, split before extending. Preserve unrelated concurrent changes and the exact second-attempt failure receipt.

### Definition of Done

The three affected modules accept the current frozen Plan-status fixture with focused checks passing and no validation weakening or legacy-fixture rewrite. This narrow Task claims fixture alignment only, not production, full-suite, deployment or release acceptance.

### Completion checkpoint

The focused receipt records 25/25 fixture checks passing (`relation` 8, `isolation` 2, `status` 15) plus 2 current Plan-placement checks. Only `tests/test_proposed_relation_admission.py` was edited; strict validation and current D461 placement are unchanged, no production guard changed, and independent review remains pending. No installed deployment, full-release or Epic completion is claimed.
