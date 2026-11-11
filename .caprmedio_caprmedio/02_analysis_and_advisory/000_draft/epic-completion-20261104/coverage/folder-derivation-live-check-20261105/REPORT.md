# Live Scope Unit folder derivation check

- Current declaration inventory: 46 carriers, all pinned to the live sources; declaration Claims parsed with no missing fields. [Inventory](.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/coverage/scope-declaration-check-20261105/inventory.json) SHA-256 `c3409c927f4427a9e6ffea7eb9fec764caed37867fa245d6332f654b0ace81ee`.
- Governing folder rule: CA-D-667@2, SHA-256 `eb19c71a039a3c3086a9e8ab35f4266eef431579f73065d5f7c088fb007b4ec6`. D442@26 confirms folder names are derived rather than authored in Scope Unit Declarations. D302 governs filename tokens; D466 governs Status placement.
- Project root exception: Project `caprmedio` has no Scope Unit ID, Label, or order number. Authority root is `.caprmedio_caprmedio`; Delivery root is repository `.`. Its declaration is directly inside the Authority root.

## Results

| Tree | Expected nonroot paths | Exact paths present | Absent |
| --- | ---: | ---: | ---: |
| Authority | 45 | 38 | 7 |
| Delivery | 45 | 27 | 18 |

All 45 nonroot Scope Unit Declaration files are under the Authority folder expected for their declared parent. Seven expected Authority folders are absent; see the manifest.

Three present directories at expected Delivery parents use the Authority-form name with an ID, where D667 requires the Delivery form without an ID:

- `CA-SU-11 CORE_META_MODEL`: expected `LAYER_1_FRAMEWORK_METHODOLOGY/SUPERLAYER_1_METHODOLOGY_SOURCES/LAYER_1_CORE_META_MODEL`; observed `LAYER_1_FRAMEWORK_METHODOLOGY/SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL`.
- `CA-SU-12 INSTALLED_EXTENSIONS`: expected `LAYER_1_FRAMEWORK_METHODOLOGY/SUPERLAYER_1_METHODOLOGY_SOURCES/LAYER_2_INSTALLED_EXTENSIONS`; observed `LAYER_1_FRAMEWORK_METHODOLOGY/SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-12_LAYER_2_INSTALLED_EXTENSIONS`.
- `CA-SU-13 PROJECT_CONFIGURATION`: expected `LAYER_1_FRAMEWORK_METHODOLOGY/SUPERLAYER_1_METHODOLOGY_SOURCES/LAYER_3_PROJECT_CONFIGURATION`; observed `LAYER_1_FRAMEWORK_METHODOLOGY/SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION`.

Another 15 expected Delivery paths are absent without that specific alternate directory; they are listed individually in `comparison.json`.

This report distinguishes missing materialization from a name mismatch. D667 defines the derived names but this check does not establish that every declared Scope Unit must have an Authority and Delivery directory. The sibling `000_CAPRMEDIO_framework` and Applicable Methodology trees were not treated as Scope Unit paths; their package/copy status remains outside this comparison.


## After-state verification

Independent read-only review: [`.caprmedio_caprmedio/02_analysis/draft/epic-completion-20261104/permissions/delivery-folder-move-actual-review-20261105.json`](../../../permissions/delivery-folder-move-actual-review-20261105.json), SHA-256 `8da04b22a79f151bd89ec3452c83c47d1b5aaa69d71a03b6c68f6e0e278993db`. The pinned plan and move receipt agree (`e0520e4c10b35849306d8dfe8154d775f2e12dd1c82b7504221bb16810c29ea3`); all 1069 destination files match the plan by relative path and SHA-256, and all three old directories are absent. The three D667 Delivery names now exist exactly. All 1067 Markdown files have byte-identical native Current Authority counterparts.

Current Scope Unit declarations remain unchanged: 46 of 46 source pins match and all declaration carriers remain under their expected parent Authority folders. Authority folders remain 38/45 present; Delivery folders are 30/45 present. The other 15 Delivery paths remain absent and are separate from the three resolved name mismatches. The pre-move mismatch list above is retained unchanged. This review does not cover runtime writer behavior, Workbench, or tests.
