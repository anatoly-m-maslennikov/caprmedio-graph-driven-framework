---
atom_id: CA-C-544
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: high
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2456]
version: 1
updated_at: "2026-10-20T15:10:43.000Z"
---
# Summary

Repair shared frozen Plan-status fixtures

## Concern

The second full local release terminal failed three independent modules because shared frozen Plan-status fixtures do not match the current status corpus: `test_proposed_relation_admission`, `test_relation_fixture_isolation`, and `test_status_bundle_publication_independent`. This is a bounded frozen-fixture cause, not a production guard bug or deployed failure.

## Evidences

The exact log is `.caprmedio_tmp/simple_local_release/local-20261020-current-target-parser-repair-1438-tests-a71g3vcj.log`; the matching release report is `runtime/reports/runid.md`. The run covered 410 modules and 3555 tests with zero skips and twelve failed modules in total. Root recorded commit checkpoint `ac1952165`; no replacement phase ran.

## Scope and owner

CA-P-2456 owns the bounded fixture repair and focused checks. Preserve the approved inherited Plan-status authority and intentional legacy fixtures; do not weaken validation or infer a production defect from this test-terminal failure. This Concern remains Active until the bounded repair is independently checked.
