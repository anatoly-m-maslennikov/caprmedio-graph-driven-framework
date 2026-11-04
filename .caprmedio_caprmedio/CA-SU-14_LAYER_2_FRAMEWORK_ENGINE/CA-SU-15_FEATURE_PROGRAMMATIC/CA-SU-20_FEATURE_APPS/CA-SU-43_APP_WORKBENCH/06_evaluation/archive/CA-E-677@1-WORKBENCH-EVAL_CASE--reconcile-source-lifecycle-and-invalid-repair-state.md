---
atom_id: CA-E-677
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
author: Anatoly Maslennikov
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
version: 1
role: Evaluation
form: Eval Case
tier: 5
carrier_destination:
  file:
    name: CA-E-677@1-WORKBENCH-EVAL_CASE--reconcile-source-lifecycle-and-invalid-repair-state.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/archive
relations:
  evaluation_for:
  - CA-R-2723
  - CA-R-2725
  - CA-M-465
  - CA-D-672
  - CA-D-675
updated_at: 2026-11-03 23:17:14 +0400
---
## Summary

Reconcile source lifecycle changes and repaired validity

## Claim scope

The background synchronizer's committed source-to-Projection state for a bounded
governed Atom fixture inventory.

## Claim

### Prose Claim

The synchronizer passes when every committed state reflects the complete selected
fixture inventory without half-updated Atom records, nested Content Properties or relations, or derived Scope Unit records. Creates,
edits, moves, renames, and confirmed deletes update only the affected source
records. A move changes the indexed locator and does not invent a new source
Version. Startup reconciliation includes changes made while the service was
stopped. An invalid or ambiguous carrier has no indexed Atom or owned derived
rows until it is repaired, while valid unrelated carriers remain available.
Each source error names the path and error and includes available line or column
information on stderr. A source error is not treated as a confirmed deletion,
and an old valid row is not exposed for an invalid, unreadable, or
changed-during-capture source.

## Details

### Fixtures and expected outcomes

| Fixture | Expected outcome |
| --- | --- |
| New valid carrier | Its `atoms` record, including nested Content Properties and relations, becomes queryable; a valid Current Scope Unit Declaration also supplies its `scope_units` record. |
| Edited valid carrier | Its Atom, Properties, and owned relations change together in one committed state; no mixed old/new state is visible. |
| Renamed or moved carrier | The indexed source locator changes once, the source identity remains stable, and no old locator row remains. |
| Carrier removed after absence is confirmed | Its source record and owned derived rows disappear; unrelated valid rows remain. |
| Carrier that is unreadable while its path still exists | Its old rows and owned derived rows are omitted, the error is on stderr, it is not treated as a deletion, and unrelated valid rows remain queryable. |
| Source that changes during stable capture | Its old rows and owned derived rows are omitted, the error is on stderr, and the capture is not automatically resubmitted. |
| Invalid YAML, duplicate key, undecodable text, normalized heading collision, or ambiguous Current identity | The affected carrier and its owned derived rows are excluded, the error is on stderr with path and available location, and no stale valid row is returned for that source. |
| Same failed source state after a source-file error | No retry queue, persisted failed-attempt record, or automatic resubmission is created. |
| Actual later file edit, move, or new observed source state | It is a new input; if valid, its rows return together and the earlier error does not remain as a successful row. |
| Valid edits made while the service is stopped, followed by restart | The complete governed inventory is reconciled before the Projection is exposed; no pre-stop stale row survives. |
| Technical query-index maintenance | Technical output uses Docker stdout/stderr and errors use stderr. Valid rows remain queryable, failed inputs are skipped with no automatic retry, and no business Journal entry is written. |
