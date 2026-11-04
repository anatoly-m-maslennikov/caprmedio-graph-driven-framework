---
atom_id: CA-D-672
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 3
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
    name: CA-D-672@3-WORKBENCH-ENG_DECISION--deliver-duckdb-atom-content-and-relation-records.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/archive
updated_at: 2026-11-04 05:16:33 +0400
---

## Summary

Deliver DuckDB Atom, Content Property, and relation records

## Claim scope

The in-memory `atoms` and `scope_units` tables and their nested parsed values.

## Claim

### Prose Claim

The Workbench Projection must read governed source files directly into an in-memory DuckDB reader. It exposes exactly two public tables, `atoms` and `scope_units`; all Reader Schema Projection, temporary schema, and relation-materialization structures remain in memory. Source bytes may exist transiently while a file is read, but no source-byte or raw-frontmatter value is stored in a row or intermediate file.

Both YAML Header and Markdown Content must be parsed under the Current model and its applicable declarations, including nested Properties. `header_json` retains the complete parsed Header and native distinctions between absence, null, empty values, scalar/list shape, false, and zero. `content_markdown` retains the original Markdown body. `content_properties_json` retains mapped section occurrences with `property_path` segments, heading, heading level, position, `direct_markdown`, and complete `section_markdown`. A parent path is derived from the segments; no separate parent-path field is stored. Direct values remain separate from descendant subtrees, including the declared RMED Claim container with Formal Claim and Prose Claim children.

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

`content_properties_json` is an array whose objects have exactly these fields: `property_path` (non-empty array of strings), `heading` (string), `heading_level` (integer), `position` (one-based heading occurrence order), `direct_markdown` (string or null), and `section_markdown` (string). Paths are segments, not dotted strings. `section_markdown` includes the heading and full subtree; `direct_markdown` excludes child Properties. Heading mapping follows the Current declarations: skipped levels create no synthetic segments, fenced heading-like text creates no section, and colliding normalized sibling keys are rejected.

`relation_edges_json` is an array whose objects have exactly these fields: `source_kind` (string), `source_ref` (string), `target_kind` (string), `target_ref` (string), `relation_type` (string), and `derived` (boolean). Each edge's `source_kind` and `source_ref` identify the object represented by the enclosing row. An Atom row carries its outgoing Relations; a Scope Unit row carries its outgoing Relations. `source_path` is not duplicated inside an edge. For `Task IS_CONTAINED_BY Epic`, store the direct fact in the Task row and the derived `CONTAINS` fact in the Epic row. Keep the supporting direct-fact association in memory so changing or excluding its source removes or refreshes every affected counterpart and row hash without editing the counterpart's source carrier. Direct facts come only from source files. Derived facts are materialized in memory from those direct facts, and a declared inverse is not synthesized twice. References remain references rather than inline dereference objects.

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

`scope_units` contains only Current Scope Unit Declaration rows. A Draft Declaration is an `atoms` row and does not alter the Current Scope Unit structure. Every internal Reader Schema Projection mapping row also carries the same deterministic row hash while in memory; it does not become another public table.

Each row hash covers the entire indexed row after materialization, including all nested derived Relation facts where present, and excludes only `hash`. No hash is automatically added to arbitrary SQL result rows.


DuckPGQ consumes internal in-memory vertex and edge mappings derived from these two tables. Vertex identity retains the object kind and reference, distinguishing Atom and Scope Unit references and Current and Draft Atom references. Edge mappings retain Relation Type, direction, and whether the fact is derived. Register only declared Relation Types over valid indexed endpoints. The mappings and registered property graph are disposable implementation state; they add no third public table, stored intermediate file, or independent source of truth.
