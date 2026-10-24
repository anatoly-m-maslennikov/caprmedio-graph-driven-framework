# Current Source Pin Inventory — Post Migration

- Recorded: `2026-10-23T08:55:11+00:00`
- Historical checkpoint: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/03_plan/05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/96-CA-P-2577-TASK--implement-the-shared-context-native-workflow/05-CA-P-2582-TASK--reconcile-current-workflow-bindings-and-frozen-fixtures/execution_evidence/p2613/current-source-pins.review.json`
- Historical checkpoint pins: **50**; routes **15**; query admissions **2**
- Fresh current-source revalidation: **PASS**
- Fresh pins: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/03_plan/05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/96-CA-P-2577-TASK--implement-the-shared-context-native-workflow/05-CA-P-2582-TASK--reconcile-current-workflow-bindings-and-frozen-fixtures/execution_evidence/p2613/current-source-pins.post-migration-20261023.json`
- Fresh pins SHA256: `e0f71ad9ad9ece1acce4cb228a25afe4600b37de86e507711cdf78274ff00b54`
- Verification: `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/03_plan/05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/96-CA-P-2577-TASK--implement-the-shared-context-native-workflow/05-CA-P-2582-TASK--reconcile-current-workflow-bindings-and-frozen-fixtures/execution_evidence/p2613/source-review-verification.post-migration-20261023.json`
- Verification SHA256: `63c7fdb573ac7213b92e907aa5488cf6c2f98d17039d7b3b7f37ad2740d59177`

## Delta

{
  "changed_pin_count": 48,
  "unchanged_pin_count": 2,
  "version_delta_counts": {
    "2": 29,
    "3": 16,
    "4": 2,
    "1": 1,
    "0": 2
  },
  "path_changed_ids": [
    "CA-O-159",
    "CA-O-160"
  ],
  "body_comparison": {
    "receipt_or_archive_checked": 50,
    "body_equal_count": 41,
    "body_unknown_count": 0
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
  where available; equality is never inferred from Version alone.
- `CA-O-188` remains a held identity collision.
- P2620/C583-specific detached-candidate compiler decision remains unresolved.
- No live manifest, A1142 registry, runtime, Docker, release, or Git state was changed.
