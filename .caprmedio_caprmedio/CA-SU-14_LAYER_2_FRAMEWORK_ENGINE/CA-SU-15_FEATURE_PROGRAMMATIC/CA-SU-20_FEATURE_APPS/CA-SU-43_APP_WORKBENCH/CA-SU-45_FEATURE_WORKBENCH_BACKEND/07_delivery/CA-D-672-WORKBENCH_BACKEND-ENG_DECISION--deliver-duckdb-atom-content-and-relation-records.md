---
atom_id: CA-D-672
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Active
version: 9
author: Anatoly Maslennikov
role: Delivery
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  delivery_for:
  - CA-R-2723
  - CA-R-2726
  - CA-R-2724
carrier_destination:
  file:
    name: CA-D-672-WORKBENCH_BACKEND-ENG_DECISION--deliver-duckdb-atom-content-and-relation-records.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/07_delivery
updated_at: 2026-11-04 21:06:25 +0400
---

## Summary

Deliver DuckDB Atom, Content Property, and relation records

## Claim scope

The derived `atoms` and `scope_units` tables and their complete parsed Header, Markdown heading paths, nested values, and materialized outgoing Relations.

## Claim

### Prose Claim

The Workbench Projection must read governed source files directly with the Current model parser into a file-backed DuckDB reader. It exposes exactly two public tables, `atoms` and `scope_units`; internal graph mappings and materialized query results remain derived implementation state under the Workbench runtime directory. Source bytes are transient parser input only; do not store source-byte copies, raw frontmatter, intermediate source files or schema files. Release successful parsed-row caches after refresh. Database and spill files are allowed under the owned runtime directory.

Parse complete YAML Headers and Markdown Content, including nested Header mappings and complete heading paths. The parser preserves native distinctions between a missing key, null, empty value, scalar, list, map, false, and zero. It keeps the original Markdown body and mapped section occurrences. It applies the Current model directly; Declarations do not produce a second schema artifact, and the reader does not evaluate generic CFEL or arbitrary prose. Current Scope Unit Declarations alone define `scope_units`. Applicable Current Declaration changes that govern scope or Relations refresh the actual indexed facts.

The public SQL interface uses the following columns. Private parsed Header and Markdown data may remain available to the reader and graph pipeline, but it is not exposed as raw JSON or whole-body public columns.

#### `atoms`

| Column | DuckDB type | Nullability and key | Meaning |
| --- | --- | --- | --- |
| `relative path` | `VARCHAR` | NOT NULL; part of primary key | Governed canonical carrier directory relative to the Project root; uniqueness is with `filename`. |
| `filename` | `VARCHAR` | NOT NULL; part of primary key | Governed canonical carrier filename. |
| `status_group` | `VARCHAR` | NOT NULL | `Current` or `Draft` only; all Current statuses and Drafts are included, while Archived sources are excluded. |
| `id` | `VARCHAR` | NULL | Raw Header Atom ID; never synthesized from filename or path. |
| `reference` | `VARCHAR` | NULL; unique when non-null | Exact Current or Draft identity, including Draft `ID@Version-draft`. |
| `version` | `BIGINT` | NULL | Convenient mapped Header Version; complete parsed Header data remains private to the reader. |
| `status` | `VARCHAR` | NULL | Convenient mapped Header Status. |
| `current_scope_unit` | `VARCHAR` | NULL | Convenient mapped Header Current Scope Unit. |
| `claim_target_scope_unit` | `VARCHAR` | NULL | Convenient mapped Header Claim Target Scope Unit. |
| `role` | `VARCHAR` | NULL | Convenient mapped Header Role. |
| `form` | `VARCHAR` | NULL | Convenient mapped Header Form. |
| `tier` | `BIGINT` | NULL | Convenient mapped Header Tier. |
| `updated_at` | `TIMESTAMPTZ` | NULL | Convenient mapped Header Updated At. |
| `content.*` | declared DuckDB types | NULL | One column for each declared Content Property. Names are lowercase business-language paths with dots and spaces, such as `content.summary`, `content.claim.prose claim`, `content.claim.formal claim` and `content.details`. Parent direct values and declared nested values remain separate; arbitrary prose headings stay inside the value. |
| `relations` | `JSON` | NOT NULL | Outgoing direct and derived Relations as a native JSON object. Each present Relation Type maps to `[{"kind": "...", "reference": "...", "derived": false}]`; no outgoing Relations are `{}` and no empty placeholder key is added. |
| `hash` | `VARCHAR` | NOT NULL | SHA-256 of deterministic canonical row JSON with this column excluded. |

The reader retains the complete mapped Content Property occurrences privately. `section_markdown` includes the heading and full subtree; the public parent column keeps the direct value while each declared child path is a separate public column. Heading mapping follows the actual CommonMark heading tree: skipped levels create no synthetic segments, fenced heading-like text creates no section, and colliding normalized declared Content Property headings under one parent are rejected; repeated arbitrary prose headings are allowed and remain inside the value. The public table preserves complete prose and nested headings without exposing a raw Markdown or property JSON bucket.

`relations` is read from the same native DuckPGQ graph facts used for traversal. Each present Relation Type contains objects with exactly `kind`, `reference` and `derived`; an Atom or Scope Unit row carries its outgoing direct and derived Relations. For `Task IS_CONTAINED_BY Epic`, store the direct fact in the Task `relations` object and the derived `CONTAINS` fact in the Epic `relations` object. Keep the supporting direct-fact association privately so changing or excluding its source removes or refreshes every affected counterpart and row hash without editing the counterpart's source carrier. Preserve Header relation keys in private parsed data. For materialized facts, resolve its exact registered name or its unique case-folded carrier spelling to the canonical registered name. If that spelling matches more than one declared name, warn on stderr and omit that link. Ambiguous inverse metadata similarly produces no derived fact; it does not authorize repairing source declarations or changing their direction. Direct facts come only from source files. A declared inverse is not synthesized twice. References remain references rather than inline dereference objects. A relation object is non-empty when it has a Relation fact, even when a nested value is null; an absent Relation object is `{}`.

#### `scope_units`

| Column | DuckDB type | Nullability and key | Meaning |
| --- | --- | --- | --- |
| `name` | `VARCHAR` | NOT NULL; primary key | Scope Unit base reference and query value. |
| `scope_unit_id` | `VARCHAR` | NULL; unique when non-null | Declared Scope Unit ID. |
| `parent_name` | `VARCHAR` | NULL | Direct declared parent name. |
| `declared_label` | `VARCHAR` | NULL | Declared Scope Unit Label. |
| `ordered` | `BOOLEAN` | NOT NULL | Declared ordering flag. |
| `order_number` | `BIGINT` | NULL | Declared order number, when present. |
| `declaration_source_path` | `VARCHAR` | NOT NULL; unique | Relative path of the Current Scope Unit Declaration carrier, including its filename. This is the Declaration source, not the Scope Unit's own folder. |
| `declaration_version` | `BIGINT` | NOT NULL | Version of that declaration carrier. |
| `relations` | `JSON` | NOT NULL | This Scope Unit's outgoing direct and derived Relations, using the same native JSON shape as `atoms`; `{}` means no outgoing Relation. |
| `hash` | `VARCHAR` | NOT NULL | SHA-256 of deterministic canonical row JSON with this column excluded. |

`scope_units` contains only Current Scope Unit Declaration rows. A Draft Declaration is an `atoms` row and does not alter the Current Scope Unit structure. Every indexed row, including any internal mapping row, carries the same deterministic row hash; no third public table is created. Each row hash covers the entire indexed row after materialization, including all nested derived Relation facts where present, and excludes only `hash`. No hash is automatically added to arbitrary SQL result rows.

DuckPGQ consumes internal vertex and edge mappings derived from these two tables. Vertex identity retains object kind and reference, distinguishing Atom and Scope Unit references and Current and Draft Atom references. Edge mappings retain Relation Type, direction, and whether the fact is derived. Register only declared Relation Types over valid indexed endpoints. The mappings and registered property graph are disposable implementation state; they add no third public source table or independent source of truth.

The DuckPGQ graph `caprmedio` uses typed reference identities (kind, reference), not fetched object copies. Register source-derived relation labels for traversal. Explicit unresolved reference endpoints remain references; joining them to public tables determines whether a source object is indexed. Current literal, unqualified HAS_INVERSE bindings are relation metadata; arbitrary CFEL formulas and qualified derivation rules are not evaluated.
