---
atom_id: CA-D-672
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Archived
version: 8
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
    name: CA-D-672@8-WORKBENCH_BACKEND-ENG_DECISION--deliver-duckdb-atom-content-and-relation-records.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/07_delivery/archive
updated_at: 2026-11-04 17:55:47 +0400
---

## Summary

Deliver DuckDB Atom, Content Property, and relation records

## Claim scope

The derived `atoms` and `scope_units` tables and their complete parsed Header, Markdown heading paths, nested values, and materialized outgoing Relations.

## Claim

### Prose Claim

The Workbench Projection must read governed source files directly with the Current model parser into a file-backed DuckDB reader. It exposes exactly two public tables, `atoms` and `scope_units`; internal graph mappings and materialized query results remain derived implementation state under the Workbench runtime directory. Source bytes are transient parser input only; do not store source-byte copies, raw frontmatter, intermediate source files or schema files. Release successful parsed-row caches after refresh. Database and spill files are allowed under the owned runtime directory.

Parse complete YAML Headers and Markdown Content, including nested Header mappings and complete heading paths. The parser preserves native distinctions between a missing key, null, empty value, scalar, list, map, false, and zero. It keeps the original Markdown body and mapped section occurrences. It applies the Current model directly; Declarations do not produce a second schema artifact, and the reader does not evaluate generic CFEL or arbitrary prose. Current Scope Unit Declarations alone define `scope_units`. Applicable Current Declaration changes that govern scope or Relations refresh the actual indexed facts.

The public SQL interface uses the following columns.

#### `atoms`

| Column | DuckDB type | Nullability and key | Meaning |
| --- | --- | --- | --- |
| `source_path` | `VARCHAR` | NOT NULL; primary key | Governed canonical carrier path, unique within the Project. |
| `status_group` | `VARCHAR` | NOT NULL | `Current` or `Draft` only; all Current statuses and Drafts are included, while Archived sources are excluded. |
| `id` | `VARCHAR` | NULL | Raw Header Atom ID; never synthesized from filename or path. |
| `ref` | `VARCHAR` | NULL; unique when non-null | Current base ID, or Draft `ID@Version-draft`. |
| `version` | `BIGINT` | NULL | Convenient mapped Header Version; the complete value remains in `header_json`. |
| `status` | `VARCHAR` | NULL | Convenient mapped Header Status. |
| `current_scope_unit` | `VARCHAR` | NULL | Convenient mapped Header Current Scope Unit. |
| `claim_target_scope_unit` | `VARCHAR` | NULL | Convenient mapped Header Claim Target Scope Unit. |
| `role` | `VARCHAR` | NULL | Convenient mapped Header Role. |
| `form` | `VARCHAR` | NULL | Convenient mapped Header Form. |
| `tier` | `BIGINT` | NULL | Convenient mapped Header Tier. |
| `updated_at` | `TIMESTAMPTZ` | NULL | Convenient mapped Header Updated At. |
| `header_json` | `JSON` | NOT NULL | Complete parsed Header, retaining nested mappings and native value distinctions. |
| `content_markdown` | `VARCHAR` | NOT NULL | Unchanged Markdown body after the frontmatter. |
| `content_properties_json` | `JSON` | NOT NULL | Parsed mapped Content Property occurrences defined below. |
| `relation_edges_json` | `JSON` | NOT NULL | All materialized direct and derived Relation facts defined below. |
| `hash` | `VARCHAR` | NOT NULL | SHA-256 of deterministic canonical row JSON with this column excluded. |

`content_properties_json` is an array whose objects have exactly these fields: `property_path` (non-empty array of strings), `heading` (string), `heading_level` (integer), `position` (one-based heading occurrence order), `direct_markdown` (string or null), and `section_markdown` (string). Paths are segments, not dotted strings. `section_markdown` includes the heading and full subtree; `direct_markdown` excludes child Properties. Heading mapping follows the actual CommonMark heading tree: skipped levels create no synthetic segments, fenced heading-like text creates no section, and colliding normalized sibling keys are rejected. The row retains direct values separately from descendant subtrees, including the RMED Claim container with Formal Claim and Prose Claim children.

`relation_edges_json` is an array whose objects have exactly these fields: `source_kind` (string), `source_ref` (string), `target_kind` (string), `target_ref` (string), `relation_type` (string), and `derived` (boolean). Each edge's `source_kind` and `source_ref` identify the object represented by the enclosing row. An Atom row carries its outgoing Relations; a Scope Unit row carries its outgoing Relations. `source_path` is not duplicated inside an edge. For `Task IS_CONTAINED_BY Epic`, store the direct fact in the Task row and the derived `CONTAINS` fact in the Epic row. Keep the supporting direct-fact association in memory so changing or excluding its source removes or refreshes every affected counterpart and row hash without editing the counterpart's source carrier. Preserve each Header relation key unchanged in `header_json`. For materialized facts, resolve its exact registered name or its unique case-folded carrier spelling to the canonical registered name. If that spelling matches more than one declared name, warn on stderr and omit that link. Ambiguous inverse metadata similarly produces no derived fact; it does not authorize repairing source declarations or changing their direction. Direct facts come only from source files. Derived facts are materialized in the derived database from those direct facts, and a declared inverse is not synthesized twice. References remain references rather than inline dereference objects.

#### `scope_units`

| Column | DuckDB type | Nullability and key | Meaning |
| --- | --- | --- | --- |
| `name` | `VARCHAR` | NOT NULL; primary key | Scope Unit base reference and query value. |
| `scope_unit_id` | `VARCHAR` | NULL; unique when non-null | Declared Scope Unit ID. |
| `parent_name` | `VARCHAR` | NULL | Direct declared parent name. |
| `declared_label` | `VARCHAR` | NULL | Declared Scope Unit Label. |
| `ordered` | `BOOLEAN` | NOT NULL | Declared ordering flag. |
| `order_number` | `BIGINT` | NULL | Declared order number, when present. |
| `declaration_source_path` | `VARCHAR` | NOT NULL; unique | Source path of the Current Scope Unit Declaration. |
| `declaration_version` | `BIGINT` | NOT NULL | Version of that declaration carrier. |
| `relation_edges_json` | `JSON` | NOT NULL | This Scope Unit's outgoing direct and derived Relation facts, using the same edge fields as `atoms`. |
| `hash` | `VARCHAR` | NOT NULL | SHA-256 of deterministic canonical row JSON with this column excluded. |

`scope_units` contains only Current Scope Unit Declaration rows. A Draft Declaration is an `atoms` row and does not alter the Current Scope Unit structure. Every indexed row, including any internal mapping row, carries the same deterministic row hash; no third public table is created. Each row hash covers the entire indexed row after materialization, including all nested derived Relation facts where present, and excludes only `hash`. No hash is automatically added to arbitrary SQL result rows.

DuckPGQ consumes internal vertex and edge mappings derived from these two tables. Vertex identity retains object kind and reference, distinguishing Atom and Scope Unit references and Current and Draft Atom references. Edge mappings retain Relation Type, direction, and whether the fact is derived. Register only declared Relation Types over valid indexed endpoints. The mappings and registered property graph are disposable implementation state; they add no third public source table or independent source of truth.

The DuckPGQ graph `caprmedio` uses typed reference identities (kind, reference), not fetched object copies. Register source-derived relation labels for traversal. Explicit unresolved reference endpoints remain references; joining them to public tables determines whether a source object is indexed. Current literal, unqualified HAS_INVERSE bindings are relation metadata; arbitrary CFEL formulas and qualified derivation rules are not evaluated.
