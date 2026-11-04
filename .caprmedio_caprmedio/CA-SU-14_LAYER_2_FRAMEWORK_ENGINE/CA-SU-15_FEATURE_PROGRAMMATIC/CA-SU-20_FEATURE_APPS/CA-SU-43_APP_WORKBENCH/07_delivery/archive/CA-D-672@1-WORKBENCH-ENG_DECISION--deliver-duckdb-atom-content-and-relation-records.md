---
atom_id: CA-D-672
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 1
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
    name: CA-D-672@1-WORKBENCH-ENG_DECISION--deliver-duckdb-atom-content-and-relation-records.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/archive
updated_at: 2026-11-03 23:17:14 +0400
---

## Summary

Deliver DuckDB Atom, Content Property, and relation records

## Claim scope

The derived `atoms` and `scope_units` records of the DuckDB Projection for governed canonical Atom carriers and Current Scope Unit Declarations.

## Claim

### Prose Claim

The DuckDB Projection must expose exactly two public tables: `atoms` and
`scope_units`. It delivers one source-bound `atoms` record for each valid
canonical Atom carrier and keeps status groups distinct. A Current group is
not reduced to Active. An ambiguous identity or other invalid source is not
published as a valid record.

The mapping retains the source locator and source bytes, Atom identity and Version, status group, convenient Header columns derived from the complete Header, the original frontmatter text, and the unchanged Markdown body.

| Projection records | Delivered representation |
| --- | --- |
| `atoms` | One source record with the retained Header and Markdown source data. |
| `scope_units` | One Current declared Scope Unit, including its declared parent and declaration source binding. |

Mapped Content Property occurrences and registered typed Relation facts are
nested values in their owning `atoms` row. They are not public tables, views,
or another schema.

The parsed Header preserves native YAML distinctions: an absent key, explicit null, empty string, empty list or mapping, scalar, one-item list, false, and zero remain distinct. Duplicate mapping keys are rejected. A reference value remains a reference; it does not become an inline copy of the referenced object. No reserved model Property such as `$value` is introduced.

Content Property paths are stored as segments, not only as a dotted string. A direct Markdown value remains separate from a complete section value; the latter includes its heading and descendants. Real heading structure is used: skipped levels create no empty Properties, heading-like text in a code fence creates no section, and colliding normalized keys under one parent are rejected rather than merged.

The RMED `Claim` container remains a container with its declared `Formal Claim` and/or `Prose Claim` children. `Formal Claim` retains its CFEL-labelled fence, and `Prose Claim` retains ordinary Markdown; a heading inside Prose Claim remains its value unless an applicable declaration admits it as a child Property. The Projection does not add a custom CFEL parser or execute Formal Claims.

Relation facts retain typed references rather than inline dereference objects. A direct relation fact is stored once; a declared derived counterpart is resolved from that fact and is not another source relation or a new model entity.

### Public SQL schema

This is the complete public SQL surface for the first version. The Projection is
per Project, so `source_path` needs no Project-prefix column and is unique in
that Project's database. `NULL` is a real SQL null; it is never a replacement
for an absent, explicit-null, empty, false, or zero Header value in
`header_json`.

#### `atoms`

| Column | DuckDB type | Nullability and key | Meaning |
| --- | --- | --- | --- |
| `source_path` | `VARCHAR` | NOT NULL; primary key | Governed canonical carrier path, unique within the Project. |
| `source_bytes` | `BLOB` | NOT NULL | Exact carrier bytes. |
| `status_group` | `VARCHAR` | NOT NULL | The inventory's distinct `Current`, `Draft`, or `Archived` group; it is not a reduction of `status`. |
| `id` | `VARCHAR` | NULL | Raw Header Atom ID. It is not synthesized from the filename or source path. |
| `ref` | `VARCHAR` | NULL; unique when non-null | Computed canonical address: Current base ID; Draft `ID@Version-draft`; Archived `ID@Version`. It is NULL when the required raw ID or Version is absent, including an ID-less legacy Draft. |
| `version` | `BIGINT` | NULL | Convenient mapped Header Version; the raw Header value remains in `header_json`. |
| `status` | `VARCHAR` | NULL | Convenient mapped Header Status. |
| `current_scope_unit` | `VARCHAR` | NULL | Convenient mapped Header Current Scope Unit. |
| `claim_target_scope_unit` | `VARCHAR` | NULL | Convenient mapped Header Claim Target Scope Unit. |
| `role` | `VARCHAR` | NULL | Convenient mapped Header Role. |
| `form` | `VARCHAR` | NULL | Convenient mapped Header Form. |
| `tier` | `BIGINT` | NULL | Convenient mapped Header Tier. |
| `updated_at` | `TIMESTAMPTZ` | NULL | Convenient mapped Header Updated At. |
| `header_raw` | `VARCHAR` | NOT NULL | Original YAML frontmatter text. |
| `header_json` | `JSON` | NOT NULL | Complete parsed Header, retaining nested mappings and the distinctions between absence, null, empty values, scalar/list shape, false, and zero. |
| `content_markdown` | `VARCHAR` | NOT NULL | Unchanged Markdown body after the frontmatter. |
| `content_properties_json` | `JSON` | NOT NULL | JSON array of mapped Content Property occurrences, defined below. |
| `relation_edges_json` | `JSON` | NOT NULL | JSON array of direct registered Relation facts, defined below. |

`content_properties_json` is an array whose objects have exactly these fields:
`property_path` (array of strings, non-empty), `parent_property_path` (array
of strings or null), `heading` (string), `heading_level` (integer), `position`
(integer, one-based heading occurrence order within `content_markdown`),
`direct_markdown` (string or null), and `section_markdown` (string). Paths are
segments, not dotted strings. `section_markdown` includes the heading and its
full subtree; `direct_markdown` excludes child Properties. The normal mapped
heading rules remain in force: no synthetic intermediate segment for a skipped
level, no section inside a code fence, and no merged sibling keys.

For `ref`, the raw `id` is preserved unchanged. The computation first
normalizes an already admitted version-qualified raw ID to its base ID, then
applies the row's `status_group`; it never appends an `@Version` suffix twice.

`relation_edges_json` is an array whose objects have exactly these fields:
`source_kind` (string), `source_ref` (string), `target_kind` (string),
`target_ref` (string), and `relation_type` (string). The enclosing row's
`source_path` owns every object in the array and is not repeated inside it.
Only direct registered facts whose endpoints resolve to typed references enter
this array. A canonical-less source can remain in `atoms` but cannot contribute
such an edge. An inverse or other declared derived counterpart is computed from
that one fact; it is not stored as another object.

#### `scope_units`

| Column | DuckDB type | Nullability and key | Meaning |
| --- | --- | --- | --- |
| `name` | `VARCHAR` | NOT NULL; primary key | Scope Unit base reference and the value used by scope queries. |
| `scope_unit_id` | `VARCHAR` | NULL; unique when non-null | Declared Scope Unit ID. The Project-root declaration may have no Scope Unit ID. |
| `parent_name` | `VARCHAR` | NULL | Direct parent's declared name. It is NULL for the Project root. |
| `declared_label` | `VARCHAR` | NULL | Declared Scope Unit Label. |
| `ordered` | `BOOLEAN` | NOT NULL | Declared `order.ordered`; false for an unordered Scope Unit or the Project root. |
| `order_number` | `BIGINT` | NULL | Declared `order.number`; NULL when the declaration has no order number. |
| `declaration_source_path` | `VARCHAR` | NOT NULL; unique | `source_path` of the Current Scope Unit Declaration that establishes this row. |
| `declaration_version` | `BIGINT` | NOT NULL | Version of that declaration carrier. |

`scope_units` is derived only from Current carriers whose Form is `Scope Unit
Declaration` and the existing governed inventory. It does not read retired
Project Structure TOML, mine arbitrary CFEL or prose, or invent a Scope Unit
Status. Its only structural interpretation is the declaration's explicit
Scope-Unit name, optional ID, direct parent, label and ordering. The Project root is
represented only when such a Current declaration establishes it; no synthetic
root row is added.


