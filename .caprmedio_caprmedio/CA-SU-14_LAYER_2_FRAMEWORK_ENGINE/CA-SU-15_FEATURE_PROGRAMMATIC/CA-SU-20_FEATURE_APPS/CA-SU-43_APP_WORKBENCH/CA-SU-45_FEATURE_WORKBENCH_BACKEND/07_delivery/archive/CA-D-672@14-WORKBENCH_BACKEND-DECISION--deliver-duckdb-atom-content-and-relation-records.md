---
identity:
  atom_id: CA-D-672@14
  ref_id: CA-D-672@14
context:
  container:
    scope_unit: CA-SU-45
  role: Delivery
  form: Decision
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 4
relations:
  delivery_for:
  - CA-R-2723
  - CA-R-2726
  - CA-R-2724
  depends_on:
  - CA-M-509
state:
  status: Archived
  version: 14
  updated_at: 2026-11-08 23:52:13 +0400
destination:
  file:
    name: CA-D-672@14-WORKBENCH_BACKEND-DECISION--deliver-duckdb-atom-content-and-relation-records.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/07_delivery/archive
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---

## Summary

Deliver DuckDB Atom, Content Property, and relation records

## Claim scope

The derived `atoms` and `scope_units` tables and their complete parsed Header, Markdown heading paths, nested values, and materialized outgoing Relations.

## Claim

### Prose Claim

The Workbench Projection must read governed source files directly with the Current model parser into a file-backed DuckDB reader. It exposes exactly two public source tables, `atoms` and `scope_units`; a separate technical `change_log` table may be exposed for watcher observations, but it is not a graph source or source of truth. Internal graph mappings and materialized query results remain derived implementation state under the Workbench runtime directory. Source bytes are transient parser input only; do not store source-byte copies, raw frontmatter or intermediate source files. Retain successful parsed-row snapshots and filesystem signatures for incremental refresh under the admitted indexing Method. Database and spill files are allowed under the owned runtime directory.

Parse complete YAML Headers and Markdown Content, including nested Header mappings and complete heading paths. The parser preserves native distinctions between a missing key, null, empty value, scalar, list, map, false, and zero. It keeps the original Markdown body and mapped section occurrences. It applies the Current model directly. At cold start, select exactly one schema mode. Mode 1 exposes only current-model-declared Header Properties and current-model-declared Markdown Properties. Mode 2 exposes every observed raw Header Property path and current-model-declared Markdown Properties; Mode 2 is enabled now. The schema is a rebuildable derived asset under `.caprmedio_runtime/workbench` and regenerates during image build from the complete valid source inventory; the reader does not evaluate generic CFEL or arbitrary prose. Current legacy Scope Unit Declarations and Current Scope Delegations define `scope_units`; accept both sources without changing the existing Declaration tree. Applicable Current structural Declaration or Scope Delegation changes that govern scope or Relations refresh the actual indexed facts.

Header and Markdown SQL column names use dots between path levels and lowercase snake_case within each segment, for example `header.identity.atom_id`, `header.context.container` and `content.claim.formal_claim`. The generated schema asset, public SQL interface, MCP results and `query_schema` use the same names; do not replace path separators with underscores.

Under Mode 1, bind Current model-declared Header Properties through the existing grouped Header carrier adapter: use its canonical carrier paths for column naming and its accepted aliases only for value reads through `header_value`, rejecting conflicts. Do not create additional alias columns, rewrite source Headers or add another property list. Header Relations remain one `header.relations` JSON projection. Use existing declared Header formats, including the existing timestamp delivery rules for offset-bearing Updated At values as `TIMESTAMPTZ`, without UTC or naive-local normalization or a full Form validator.

Under Mode 2, expose every observed raw Header Property path found in valid source Atoms using its complete dot-separated Header path as a SQL column name, including paths with null or empty values. Use dots between path levels and lowercase snake_case within each segment, replacing spaces within a segment with underscores. `Header.Context.Plan` becomes `header.context.plan`; a serialized `context.plan.work_sequence_number` is exposed as `header.context.plan.work_sequence_number`. Header is the logical frontmatter root, not an extra YAML wrapper. Preserve the source Header's nesting and values; no second authored flat copy is created.

Remove old short Header convenience-column names such as `id`, `status` and `role`; do not keep them as aliases. Existing queries that use those names need updating. Under Mode 2, infer Header column formats from the parsed values across valid sources and preserve collection values. Content Properties keep their declared meaning. Under Mode 2, grouping nodes with no direct value do not add duplicate JSON buckets. The Mode 2 explicit exception is the observed Header.Context.Container mapping: expose `header.context.container` JSON alongside its observed descendant columns. This adds no whole-Header bucket or other grouping-node exception. Distinct source paths must not share one dot-separated SQL column name; reject an ambiguous schema mapping through the existing runtime error boundary rather than merge values or invent an alias. Content Property SQL names keep dots between path levels and use snake_case within every segment, replacing spaces with underscores.

The public SQL interface uses the following columns. Private parsed Header and Markdown data may remain available to the reader and graph pipeline, but it is not exposed as raw JSON or whole-body public columns.

Under Mode 2, generate Header columns from the actual raw paths: a flat `atom_id` becomes `header.atom_id`, while nested `identity.atom_id` becomes `header.identity.atom_id`. These are source paths, not duplicate aliases. Under Mode 1, generate Header columns only from current-model-declared Header Properties. Keep Content columns model-declared in both modes. Store the rebuildable schema asset under `.caprmedio_runtime/workbench` and regenerate it during image build. Under Mode 2, a new observed Header path, removed last Header path, Header format/type change, or previously populated Header path globally empty across the complete valid source inventory triggers a schema/table rebuild and full source reread. In Mode 1, a changed declared Header or Markdown schema does the same. Observed empty Header paths remain columns under Mode 2; ordinary edits with unchanged schema remain incremental.

#### `atoms`

| Column | DuckDB type | Nullability and key | Meaning |
| --- | --- | --- | --- |
| `relative path` | `VARCHAR` | NOT NULL; part of primary key | Governed canonical carrier directory relative to the Project root; uniqueness is with `filename`. |
| `filename` | `VARCHAR` | NOT NULL; part of primary key | Governed canonical carrier filename. |
| `status_group` | `VARCHAR` | NOT NULL | `Current` or `Draft` only; all Current statuses and Drafts are included, while Archived sources are excluded. |
| `reference` | `VARCHAR` | NULL; unique when non-null | Exact Current or Draft identity, including Draft `ID@Version-draft`. |
| `header.*` | declared DuckDB types in Mode 1; inferred DuckDB types in Mode 2 | NULL when the source value is absent | Mode 2: one column per observed raw Header Property path found in valid source Atoms, using its complete dot-separated path; examples include `header.identity.atom_id`, `header.context.role` and `header.state.status`. Mode 1: one column per current-model-declared Header Property. |
| `content.*` | declared DuckDB types | NULL | One column for each declared Content Property. Names are dot-separated paths with snake_case segments, such as `content.summary`, `content.claim.prose_claim`, `content.claim.formal_claim` and `content.details`. Parent direct values and declared nested values remain separate; arbitrary prose headings stay inside the value. |
| `header.relations` | `JSON` | NOT NULL | Outgoing direct and derived Relations as a native JSON object. Each present Relation Type maps to `[{"kind": "...", "reference": "...", "derived": false}]`; no outgoing Relations are `{}` and no empty placeholder key is added. |
| `hash` | `VARCHAR` | NOT NULL | SHA-256 of deterministic canonical row JSON with this column excluded. |


The reader retains the complete mapped Content Property occurrences privately. `section_markdown` includes the heading and full subtree; the public parent column keeps the direct value while each declared child path is a separate public column. Heading mapping follows the actual CommonMark heading tree: skipped levels create no synthetic segments, fenced heading-like text creates no section, and colliding normalized declared Content Property headings under one parent are rejected; repeated arbitrary prose headings are allowed and remain inside the value. The public table preserves complete prose and nested headings without exposing a raw Markdown or property JSON bucket.

`header.relations` is read from the same native DuckPGQ graph facts used for traversal. Each present Relation Type contains objects with exactly `kind`, `reference` and `derived`; an Atom or Scope Unit row carries its outgoing direct and derived Relations. For `Task IS_CONTAINED_BY Epic`, store the direct fact in the Task `header.relations` object and the derived `CONTAINS` fact in the Epic `header.relations` object. Keep the supporting direct-fact association privately so changing or excluding its source removes or refreshes every affected counterpart and row hash without editing the counterpart's source carrier. Preserve Header relation keys in private parsed data. Resolve authored Relation keys through the canonical registry under CA-M-509, accepting exact canonical names and declared inverse alias addresses, or their unique case-folded carrier spellings. Normalize an unambiguous inverse writing once to its canonical direct fact without editing its source. Apply the existing ambiguity warnings and omission rules to names, aliases and inverse bindings. Build inverse views once from canonical direct facts. Direct facts come only from source files. References remain references rather than inline dereference objects. A relation object is non-empty when it has a Relation fact, even when a nested value is null; an absent Relation object is `{}`.

#### `scope_units`

| Column | DuckDB type | Nullability and key | Meaning |
| --- | --- | --- | --- |
| `name` | `VARCHAR` | NOT NULL; primary key | Scope Unit base reference and query value. |
| `scope_unit_id` | `VARCHAR` | NULL; unique when non-null | Declared Scope Unit ID. |
| `parent_name` | `VARCHAR` | NULL | Direct declared parent name. |
| `declared_label` | `VARCHAR` | NULL | Declared Scope Unit Label. |
| `ordered` | `BOOLEAN` | NOT NULL | Declared ordering flag. |
| `order_number` | `BIGINT` | NULL | Declared order number, when present. |
| `declaration_source_path` | `VARCHAR` | NOT NULL; unique | Relative path of the Current legacy Scope Unit Declaration or Current Scope Delegation carrier, including its filename. This is the structural source, not the Scope Unit's own folder. |
| `declaration_version` | `BIGINT` | NOT NULL | Version of that structural-declaration carrier. |
| `relations` | `JSON` | NOT NULL | This Scope Unit's outgoing direct and derived Relations, using the same native JSON shape as `atoms`; `{}` means no outgoing Relation. |
| `hash` | `VARCHAR` | NOT NULL | SHA-256 of deterministic canonical row JSON with this column excluded. |

`scope_units` contains only Current legacy Scope Unit Declarations and Current Scope Delegations; the existing Declaration tree remains unchanged. A Draft Declaration or Scope Delegation is an `atoms` row and does not alter the Current Scope Unit structure. Every indexed source row, including any internal mapping row, carries the same deterministic row hash; these source-row hash rules do not apply to the separate technical watcher `change_log`, and no third public source table is created. Each row hash covers the entire indexed row after materialization, including all nested derived Relation facts where present, and excludes only `hash`. No hash is automatically added to arbitrary SQL result rows.

DuckPGQ consumes internal vertex and edge mappings derived from these two tables. Vertex identity retains object kind and reference, distinguishing Atom and Scope Unit references and Current and Draft Atom references. Edge mappings retain Relation Type, direction, and whether the fact is derived. Register only declared Relation Types over valid indexed endpoints. The mappings and registered property graph are disposable implementation state; they add no third public source table or independent source of truth.

The DuckPGQ graph `caprmedio` uses typed reference identities (kind, reference), not fetched object copies. Register source-derived relation labels for traversal. Explicit unresolved reference endpoints remain references; joining them to public tables determines whether a source object is indexed. Current explicit inverse aliases and literal unqualified inverse bindings are registry metadata under CA-M-509; arbitrary CFEL formulas and qualified derivation rules are not evaluated.

The remaining technical columns—repository-relative path, filename, lifecycle group, canonical graph reference and row hash—are derived query metadata rather than short aliases for Header Properties. Scope Unit columns continue to represent Scope Unit objects, not Atom Headers. Atom `header.relations` retains the admitted direct-and-derived native graph projection; do not expose a second raw Header Relations copy.

Native graph labels must remain unambiguous in the backend. If registered names differ only by case and collide as native labels, warn and omit every colliding type and its projected links; retain raw Header facts privately and keep unrelated graph facts.

Literal CFEL inverse-binding and inverse-alias endpoints are model references and must match their declared addresses exactly. Unique case-folded spelling resolution applies only to carrier/Header Relation keys; do not repair or invent model addresses.
