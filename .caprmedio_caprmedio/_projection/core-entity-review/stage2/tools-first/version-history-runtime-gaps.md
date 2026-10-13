# Version and history runtime gaps

Read-only trace, 2026-10-13, following source alignment commit `450a47b04`. This is derived evidence for CA-P-1970, CA-P-2259 and CA-P-2179, not implementation or execution authority.

Investigator: `/root/epic_atom_read`. The source-only acceptance remains in [the narrow rule receipt](version-history-rule-alignment-acceptance.md).

## Two remaining corrections

1. `lifecycle_intents.update_atom_action` preserves Version for `carrier_only` and `equivalent_refinement`; it retains history only for semantic or legacy updates. A fresh native fixture changed bytes while retaining Version 1 and creating no history. Align every admitted real same-ID update with +1 and exact predecessor retention; preserve no-op, identity and assessment checks.
2. `lifecycle_intents.change_status_atom_action` and `replace_atom_action` refresh Status/time without increasing Version. `atom_operations.archive_atom_revision` names the resulting Archived carrier with the old Version. Fresh fixtures for both actions produced changed Archived bytes at Version 1 / `@1`, without exact predecessor history. Retain the original bytes first, then use the resulting incremented Version for the actual Archived revision. Preserve successor-before-archive ordering and existing partial-effect handling.

The registered callers are the selected Workflow Orchestrator lifecycle handlers and `WORKFLOW_OPERATIONS/REVERT_CHANGES/native_revert_provider.py`. These are actual runtime consumers, not unused helpers.

`atom_operations.preserve_atom_revision` already preserves raw predecessor bytes and leaves current bytes unchanged. Its fresh fixture passed; do not rewrite this helper merely to align the surrounding callers.

## Checks and pins

Four fresh scratch-fixture cases reproduced the three mismatches and confirmed exact-history copying. Eight existing targeted tests passed, but some assertions endorse obsolete preserved Versions and old-version archive names. Update those expectations and add independent corrected-behavior cases before claiming runtime alignment.

Paths below are relative to `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/`.

| Source | SHA-256 |
| --- | --- |
| `lifecycle_intents.py` | `d9112f75d68ab37fe01fbb04a9f0be9fa0287dc90f4dad725af047de8ea58662` |
| `atom_operations.py` | `a78f3dea98b5b183fe406192197f399602c12be9919c9abe5a777c02730ffb64` |
| `tests/test_selected_atom_lifecycle.py` | `750580f01300098c9ecb3644f8a961fe7b0d8f81fc7a828be1e55e7d8be656be` |
| `tests/test_model_driven_status_lifecycle.py` | `a6ec5b59069e7574e733573dcbca6fa70ddbd406b9249802e4fd7d7f0cb6b122` |

No implementation, live Atom mutation, connected-runtime verification, FPF acceptance or safe-publication claim is included. The changed-Subject publication guard remains intact. Source-review and publication gates are not bypassed by this diagnosis.
