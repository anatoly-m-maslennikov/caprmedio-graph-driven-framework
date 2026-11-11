---
atom_id: CA-M-500
ref_id: CA-M-500@2
container:
  scope_unit: CA-SU-45
role: Method
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 4
relations:
  method_for:
  - CA-R-2726
status: Archived
version: 2
updated_at: 2026-11-07 02:02:14 +0400
carrier_destination:
  file:
    name: CA-M-500@2-WORKBENCH_BACKEND-ENG_DECISION--rebuild-workbench-schema-from-source-atoms.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method/archived
author: Anatoly Maslennikov
---

## Summary

Rebuild the Workbench schema from source Atoms.

## Claim scope

The schema asset and source tables used by WORKBENCH_BACKEND.

## Claim

### Prose Claim

Keep the Workbench schema outside handwritten code as a rebuildable asset. The asset provides the column names and formats needed by the query projection. Do not hardcode the list of Atom properties in Python modules.

For Header columns, use every observed raw Header Property path found in valid source Atoms, including paths whose observed values are null or empty. Flatten every path segment; grouping nodes without an observed direct Property do not add whole-object columns. For Content columns, use only model-declared Properties. Read all valid Current and Draft Atoms with the existing readers for filenames, paths, YAML, Markdown and Declarations. Use those sources to build the schema asset. Header Relations retain their existing special projection: expose one `header_relations` JSON column from the native direct-and-derived graph facts, not a second raw mapping or per-link columns.

The asset is derived data under `.caprmedio_runtime/workbench`, not another source of truth. Rebuild it from the source Atoms when it is missing or the source schema changes.

If the complete valid-source inventory finds a new observed Header path, a removed last Header path, a Header format/type change, or a previously populated Header path globally empty:

- Rebuild the schema asset and the affected DuckDB source tables.
- Reread the source Atoms into those tables.

Check global emptiness across the complete valid source inventory, not one result page. NULL, empty strings and empty collections are empty. Zero and false are values. Observed empty Header paths remain columns; only removal of the last observed path removes a column.

An ordinary value edit that leaves the schema unchanged remains an incremental update. Rebuilding the schema is not a fallback for an unrelated indexing failure.

Generate Content columns from Current model Declarations. Keep dots between path levels and use snake_case within every segment, for example `content.claim.prose_claim` and `content.claim.formal_claim`. Do not maintain a separate handwritten property list in Python.


Build Header schema contributions once from the complete accepted inventory. On an ordinary delta, update only changed or removed source contributions. Aggregate observations preserve every current path, format, populated flag and normalized-name collision rule without recursively scanning unchanged Headers. Retain observations at parent mapping paths too: a parent may become a direct column because another source uses an empty mapping. Remove a column only when its last observed direct path disappears. Equality preserves YAML types, including date versus quoted string and Boolean versus integer.

Reuse the reader's compiled Content schema while declaration contributions are unchanged. Retain per-source Content rules with their exact provenance; reparse only changed declaration sources. Same-shape changes still refresh source ID, version and path provenance. Actual shape changes retain the existing full reread/revalidation boundary. Pass the compiled schema from the reader to the query store rather than compiling every cached Atom again on each ordinary update.

Candidate Header and Content schema state is owner-local derived state. Preserve invalid-content exclusion, duplicate filtering, Header Relation projection, asset regeneration and the existing full rebuild conditions. Do not add a second source, handwritten property list, public query parameter or background schema service.
