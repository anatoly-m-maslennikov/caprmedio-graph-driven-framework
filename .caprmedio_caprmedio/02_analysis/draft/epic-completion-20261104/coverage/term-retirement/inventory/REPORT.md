# Current Term retirement inventory

**Read-only inventory; no source changes.**

Published 1,159-source frontier used as index. 105 relevant Current carriers pinned by actual file bytes; 9 differ from the published hashes.

## Current model items

- Direct Term kind Declaration: CA-R-1318@33.
- Method Term Definition atoms: CA-M-449@3, CA-M-450@4, CA-M-451@4, CA-M-452@3, CA-M-453@3, CA-M-454@5, CA-M-455@4, CA-M-458@3 (8).
- Requirement Term Definition atoms: CA-R-2275@2 (separate form/role).
- Typed incoming Method-form Subjects: CA-D-655, CA-E-382, CA-E-444, CA-E-472, CA-E-659, CA-M-114, CA-M-439, CA-M-449, CA-M-450, CA-M-451, CA-M-452, CA-M-453, CA-M-454, CA-M-455, CA-R-1319, CA-R-1454.
- Typed incoming Requirement-form Subjects: CA-R-2275.

The exact paths, hashes, typed Subject references (including `Term.Name`), and incoming Atom-ID mentions are in `inventory.json`. Ordinary prose “term” and CFEL grammar references are excluded.

The Method form is present in current atom metadata and Subject selectors; no active Requirement Declaration directly targets that exact selector. `CA-D-404` is the current Method-form carrier. This is an inventory result, not an authority conclusion.

## CCE naming dependency

`CA-R-2276@6` is the current Rule “require one-to-one canonical entity names with reusable terms.” Keeping this naming rule unchanged while removing the Term branch is a direct conflict. Resolve this before any retirement. Current pin and actual hash are in `inventory.json`.

## Safe order if the user confirms retirement

- Confirm the drop scope and reconcile it with CA-R-2276’s reusable-Term requirement.
- Preserve CCE naming and Declaration Semantics; identify mixed-carrier clause boundaries.
- Resolve typed Subject and exact Atom-ID references to form/registration consumers; retire only confirmed Term-specific clauses.
- Retire the eight Method Term Definition atoms and separate Requirement Term Definition atom only if both are confirmed for retirement.
- Retire Term and Term.Name declarations after inbound refs are resolved. Keep archived, Draft, release and applicable copies untouched.

## Changed source pins

- `CA-D-485@27`: `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-485-CORE_META_MODEL-ENG_DECISION--carry-defaulted-atom-values-without-copying-inherited-overrides.md`, current SHA `197b21393908781c448ff0713e38045e11fb244fe26511503989ad6db3073b6e` (published SHA `5e4f75cef43a1d37d2111aaa176fb2abe0d5d132165f4eab7cf9fe5d78c511f8`).
- `CA-E-522@19`: `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-522-CORE_META_MODEL-EVAL_CASE--storage-boundary-classification-interpretability.md`, current SHA `5550f842418739f0947a1e4cef3e0f71b1c1313494e262f144f4d7e34e9b8b28` (published SHA `2eeb2ca1d3eed36413fa28d6197463467b3a108308269e4f484dda70455664cc`).
- `CA-M-006@31`: `.caprmedio_caprmedio/05_method/CA-M-006-CAPRMEDIO-SCOPE_CONTRACT-ENG-POLICY--keep-the-whole-project-coherent.md`, current SHA `57777a88746b31d16e60ddf8adc2c87441333a1b422f1db77567134c10522736` (published SHA `38fd34e55ed223fa7950520bbc47138c76e2fe3a0f84461018f5cb00371d223d`).
- `CA-M-277@34`: `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/05_method/CA-M-277-PROJECT_CONFIGURATION-IMPLEMENTATION_METHOD--report-in-silent-mode.md`, current SHA `fced0df43e6ed7efc4f1da701dbc0c2bd0e3668877f083ac5c172395773e4384` (published SHA `18380d048dae6c357bb4071c33717272dcc574f28029b01daf71fe575fba67e1`).
- `CA-M-278@31`: `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/05_method/CA-M-278-PROJECT_CONFIGURATION-IMPLEMENTATION_METHOD--report-in-verbose-mode.md`, current SHA `3f2621fb97fce654e03a7f1ed46c7f951cff5f24757fa20b09ce4904e73161b8` (published SHA `d204168180771af9d07f98225dc524fe1d77d8957a94c4fc90fbf3715cd704b8`).
- `CA-R-1568@26`: `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1568-CORE_META_MODEL--permit-projections-as-implementation-outputs.md`, current SHA `693b9f373d3ffbaa6d06c93ce59856e6cb46ba39674a33fc9173e2bb62e01fa1` (published SHA `22bc7a73f5bb154e70128978a07ffbfa208301771315664599e8bd2ffc27fd28`).
- `CA-R-1703@40`: `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1703-CORE_META_MODEL-RULE--use-implementation-overview-as-a-projection.md`, current SHA `20dbd89fa31f9c349013127c64a527b53840f5c01b5fead0f6927ac6dd468290` (published SHA `5f8ae47413affdaf940598d8cc3ae283e4678103e4af367d7ecc77b986d99801`).
- `CA-R-1720@38`: `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1720-CORE_META_MODEL-RULE--use-one-project-journal-for-governed-provenance.md`, current SHA `2b8f8698154fc9d627ee4a78258881835ebc2c23f41906f8b34b65d4086e0c11` (published SHA `e4e23f42ce0818131075826ba67c94f95ea0e1c9b01aed2b2803aadd5a2baa21`).
- `CA-R-622@35`: `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-622-PROJECT_CONFIGURATION-RULE--keep-selected-settings-in-their-authoritative-settings-artifact.md`, current SHA `f5a631daa14b0b4af665d1d0d36f68c5f6b97fea69766195fd089d8f02139a98` (published SHA `eadcdf57ad54e3ef5aeefd0c760d36a19581322b869d1ae0d3b6b9ac24c0d36e`).

Five later-index IDs were compared; 0 had direct typed Term/Term Definition Subject or Atom-ID references. Details are in `inventory.json`.
