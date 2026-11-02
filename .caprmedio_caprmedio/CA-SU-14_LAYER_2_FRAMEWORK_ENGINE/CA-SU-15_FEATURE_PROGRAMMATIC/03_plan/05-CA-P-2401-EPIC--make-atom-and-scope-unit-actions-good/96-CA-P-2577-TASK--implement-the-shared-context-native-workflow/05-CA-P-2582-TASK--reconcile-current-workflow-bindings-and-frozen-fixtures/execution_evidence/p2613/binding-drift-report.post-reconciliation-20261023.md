# Current Source Pin Inventory — Post Migration

- Recorded: `2026-10-23T09:19:30+00:00`
- Historical checkpoint: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/03_plan/05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/96-CA-P-2577-TASK--implement-the-shared-context-native-workflow/05-CA-P-2582-TASK--reconcile-current-workflow-bindings-and-frozen-fixtures/execution_evidence/p2613/current-source-pins.review.json`
- Historical checkpoint pins: **50**; routes **15**; query admissions **2**
- Fresh current-source revalidation: **PASS**
- Fresh pins: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/03_plan/05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/96-CA-P-2577-TASK--implement-the-shared-context-native-workflow/05-CA-P-2582-TASK--reconcile-current-workflow-bindings-and-frozen-fixtures/execution_evidence/p2613/current-source-pins.post-reconciliation-20261023.json`
- Fresh pins SHA256: `f0acd20b450b056f61312eb560cd1c742d6fd0cf9a8972de8dfd41db7bf6ed8f`
- Verification: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/03_plan/05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/96-CA-P-2577-TASK--implement-the-shared-context-native-workflow/05-CA-P-2582-TASK--reconcile-current-workflow-bindings-and-frozen-fixtures/execution_evidence/p2613/source-review-verification.post-reconciliation-20261023.json`
- Verification SHA256: `b7a98738e69ea2e982eae089fd965acf5fba2eb12c95ab7e8e4a9cabd938a348`

## Delta

{
  "changed_pin_count": 48,
  "unchanged_pin_count": 2,
  "version_delta_counts": {
    "2": 26,
    "3": 17,
    "4": 4,
    "1": 1,
    "0": 2
  },
  "path_changed_ids": [
    "CA-O-159",
    "CA-O-160"
  ],
  "body_comparison": {
    "receipt_or_archive_checked": 48,
    "body_equal_count": 37,
    "body_unknown_count": 2,
    "raw_body_delta_count": 11,
    "archive_conversion_only_self_reference_count": 2,
    "semantic_body_change_count": 0,
    "semantic_body_change_unresolved_without_exact_receipt_count": 9
  }
}

## Current O016 compatibility

The current canonical Project Workflow is `CA-O-016@20`, entry `CA-O-231`.
The current runtime explicitly profiles O016 versions 17 (legacy projection),
18 and 20 (direct Methods). Unknown future versions are not accepted by a
numeric `>=` comparison.

The legacy Engine manifest remains a separate historical 13-route manifest;
the detached candidate remains exact-15-route plus two query admissions.

## Scope and blockers

- Source paths are resolved with the existing current-source reader/locator;
  stale historical path hints are not rejected solely because their hashes changed.
- Metadata and body comparisons use archived predecessors or receipt evidence
  where available; equality is never inferred from Version alone. Raw body
  deltas are not semantic-change claims when only an older archive baseline is
  available. O011/O127 self-ID substitutions are classified as archive
  conversion only. O160's exact receipt declares `body_changed=false` for
  its @3 predecessor; the archived carrier's bytes differ from the receipt
  preimage, so the result is recorded as receipt-backed body equivalence
  without treating the archive carrier as that preimage.
- `CA-O-188` remains a held identity collision.
- P2620/C583-specific detached-candidate compiler decision remains unresolved.
- No live manifest, A1142 registry, runtime, Docker, release, or Git state was changed.
