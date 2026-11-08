---
identity:
  atom_id: CA-M-500
  ref_id: CA-M-500
context:
  container:
    scope_unit: CA-SU-45
  role: Method
  form: Decision
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2726
state:
  status: Active
  version: 3
  updated_at: 2026-11-08 23:52:13 +0400
destination:
  file:
    name: CA-M-500-DECISION--rebuild-workbench-schema-from-source-atoms.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method
author: Anatoly Maslennikov
---

## Summary

Rebuild the Workbench schema from source Atoms.

## Claim scope

The schema asset and source tables used by WORKBENCH_BACKEND.

## Claim

### Prose Claim

Keep the Workbench schema outside handwritten code as a rebuildable asset. The asset provides the column names and formats needed by the query projection. Do not hardcode the list of Atom properties in Python modules.

Header and Markdown SQL column names use dots between path levels and lowercase snake_case within each segment, for example `header.identity.atom_id`, `header.context.container` and `content.claim.formal_claim`. The generated schema asset, public SQL interface, MCP results and `query_schema` use the same names; do not replace path separators with underscores.

Under Mode 1, derive canonical Header column names from the existing grouped Header carrier adapter using empty or Role-selector-only metadata, independently of actual source spellings. Bind the declared logical `Header.ID` to the existing semantic `atom_id` property and its canonical `identity.atom_id` carrier path, producing `header.identity.atom_id`. Derive every other canonical path through the same adapter, without another property list. Read actual source values through the existing `header_value` accepted-alias handling and reject conflicts. Accepted aliases create no additional columns and do not rewrite source Headers. Mode 2 retains distinct actual raw Header paths.

Use the existing declared Header formats in Mode 1, including the existing timestamp delivery rules for offset-bearing Updated At values as `TIMESTAMPTZ`. Do not normalize source timestamps to UTC or naive local time. This schema binding adds no full Form validator.

At cold start, choose exactly one schema mode. Mode 1 exposes only current-model-declared Header Properties and current-model-declared Markdown Properties. Mode 2 exposes every observed raw Header Property path found in valid source Atoms, including paths whose observed values are null or empty, while Content remains only current-model-declared Markdown Properties. Mode 2 is enabled now. Under Mode 2, retain dots between Header path levels and normalize each segment to lowercase snake_case; grouping nodes without an observed direct Property do not add whole-object columns. The explicit exception is the observed Header.Context.Container mapping: expose `header.context.container` as JSON alongside its observed descendant columns. This adds no whole-Header bucket or other grouping-node exception. Read all valid Current and Draft Atoms with the existing readers for filenames, paths, YAML, Markdown and Declarations. Use those sources to build the schema asset. Header Relations retain their existing special projection: expose one `header.relations` JSON column from the native direct-and-derived graph facts, not a second raw mapping or per-link columns.

The asset is derived data under `.caprmedio_runtime/workbench`, not another source of truth. Regenerate it from the source Atoms during image build and rebuild it when it is missing or the selected mode's source schema changes.

Under Mode 2, if the complete valid-source inventory finds a new observed Header path, a removed last Header path, a Header format/type change, or a previously populated Header path globally empty:

- Rebuild the schema asset and the affected DuckDB source tables.
- Reread the source Atoms into those tables.

Under Mode 2, check global emptiness across the complete valid source inventory, not one result page. NULL, empty strings and empty collections are empty. Zero and false are values. Observed empty Header paths remain columns; only removal of the last observed path removes a column. Under Mode 1, a changed current-model-declared Header or Markdown Property schema rebuilds the asset and affected tables from the complete valid source inventory.

An ordinary value edit that leaves the schema unchanged remains an incremental update. Rebuilding the schema is not a fallback for an unrelated indexing failure.

Generate Content columns from Current model Declarations. Keep dots between path levels and use snake_case within every segment, for example `content.claim.prose_claim` and `content.claim.formal_claim`. Do not maintain a separate handwritten property list in Python.


Under Mode 2, build Header schema contributions once from the complete accepted inventory. On an ordinary delta, update only changed or removed source contributions. Aggregate observations preserve every current path, format, populated flag and normalized-name collision rule without recursively scanning unchanged Headers. Retain observations at parent mapping paths too: a parent may become a direct column because another source uses an empty mapping. Remove a column only when its last observed direct path disappears. Equality preserves YAML types, including date versus quoted string and Boolean versus integer.

Reuse the reader's compiled Content schema while declaration contributions are unchanged. Retain per-source Content rules with their exact provenance; reparse only changed declaration sources. Same-shape changes still refresh source ID, version and path provenance. Actual shape changes retain the existing full reread/revalidation boundary. Pass the compiled schema from the reader to the query store rather than compiling every cached Atom again on each ordinary update.

Candidate Header and Content schema state is owner-local derived state. Preserve invalid-content exclusion, duplicate filtering, Header Relation projection, asset regeneration and the existing full rebuild conditions. Do not add a second source, handwritten property list, public query parameter or background schema service.
