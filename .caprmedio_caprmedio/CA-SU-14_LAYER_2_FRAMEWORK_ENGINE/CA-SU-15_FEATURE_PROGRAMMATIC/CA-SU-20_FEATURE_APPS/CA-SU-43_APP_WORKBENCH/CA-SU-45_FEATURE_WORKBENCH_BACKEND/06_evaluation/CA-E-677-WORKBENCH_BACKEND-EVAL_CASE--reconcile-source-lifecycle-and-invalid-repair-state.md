---
atom_id: CA-E-677
ref_id: CA-E-677
container:
  scope_unit: CA-SU-45
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 5
relations:
  evaluation_for:
  - CA-R-2723
  - CA-R-2725
  - CA-M-465
  - CA-M-500
  - CA-D-672
  - CA-D-675
status: Active
version: 13
updated_at: 2026-11-07 01:06:28 +0400
carrier_destination:
  file:
    name: CA-E-677-WORKBENCH_BACKEND-EVAL_CASE--reconcile-source-lifecycle-and-invalid-repair-state.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Reconcile source lifecycle changes and repaired validity

## Claim scope

Atomic file-backed refresh of governed sources, Current declarations, and the rebuildable derived schema.

## Claim

### Prose Claim

The indexer transactionally applies selected source changes to `atoms`, `scope_units` and graph facts. An ordinary Atom create, edit, rename, move or removal inserts, updates or removes only the changed rows and affected relation neighbors; unrelated SQL rows are not rebuilt. Initial indexing, explicit full reread, actual structural or relation-registry changes, and a complete-inventory schema change retain the admitted rebuild path. Current and Draft Atom carriers are included, including Done and Canceled Current statuses; Archived carriers are excluded. Only Current Scope Unit Declarations establish `scope_units`; Draft Declarations remain Atom rows.

The rebuildable schema asset is derived state under `.caprmedio_runtime/workbench`, not a source or public table. A complete valid-source inventory supplies one flattened SQL column for every observed raw Header Property path and Content columns generated only from Current model Declarations. Header paths flatten every segment with lowercase snake_case; Content paths retain dots between path levels and use snake_case within segments. The declaration generator compiles declared Content paths and applicability without evaluating arbitrary CFEL formulas or prose. A newly observed Header path, a changed declared Content schema, or a path empty across the complete valid inventory rebuilds the affected schema and source tables and rereads that inventory. An ordinary value change with unchanged schema remains incremental.

Each public row hash is SHA-256 of deterministic canonical row JSON excluding `hash`, with materialized relations in the Atom payload. Ordinary source-capture failures go to stderr, are skipped, and are not retried. An indexing transaction failure or invalid Current Scope Unit Declaration instead makes the owner unavailable and requires explicit restart after correction. The database, schema asset, internal results and spill data stay under the owned Workbench runtime directory; no intermediate source copy is created. Saved SQL files are separate UTF-8 runtime artifacts and are not removed or changed by source refresh.


Verify incremental work on the real project as well as small fixtures. The same schema-preserving temporary Atom operation matrix must be measured before and after the change, with cleanup checked. Report ordinary edits separately from cold indexing and structural/schema rebuilds; fixture timings are not live-project timings.

An unchanged or non-source watcher batch must skip graph, hash and database work. A changed source row must be rehashed; an unchanged inverse-relation neighbour must also be rehashed when its outgoing facts change. Unrelated unchanged rows must retain their materialized values and hashes. Deletion, duplicate exclusion and invalid-source exclusion must remove stale reused state. A Boolean-to-number source change must not be treated as equal.

Verify that full reread, Scope Unit changes and Content-schema changes still rebuild correctly. A failed database write must not publish a new reused state. Relation parsing must occur once per captured inventory in a refresh, with one fresh parse allowed for a schema-triggered recapture. Existing stateless materialization callers must retain their behavior.


## Details

| Fixture | Expected outcome |
| --- | --- |
| Repository parent folder is named `archive` or `draft` | Classify each source relative to the selected repository, without inheriting lifecycle from the parent mount path. |
| Plain review Markdown without a closed Atom Header; or a role-mismatched proof copy | Ignore it without reporting a malformed Atom. Canonical Atom filename candidates still report invalid source content. |
| Current Active, Done, Canceled; Draft; and Archived carrier | The first four have Current/Draft `atoms` rows; Archived is absent. |
| Current and Draft Scope Unit Declarations | Only Current produces Scope Unit structure; Drafts remain queryable Atom rows. |
| Complete valid inventory observes a new raw Header path | Rebuild the derived schema/source tables and reread the inventory; expose the flattened raw Header path without creating a source-header copy. |
| Complete valid inventory loses the last observed raw Header path | Rebuild the derived schema/source tables and reread the inventory; remove that column. |
| A raw Header path changes inferred format/type | Rebuild the derived schema/source tables and reread the inventory. |
| A previously populated raw Header path becomes globally empty | Rebuild the derived schema/source tables and reread the inventory; retain the observed empty Header column. |
| Current model Declaration adds, removes, or changes an applicable Content Property | Regenerate declared Content schema, rebuild affected schema/source tables and reread the inventory; undeclared Content headings do not become SQL columns. |
| Ordinary value edit with unchanged schema | Refresh only changed rows, relation neighbors, mappings and hashes; do not rebuild the schema or reread all Atoms. |
| Saved SQL while source refresh fails or skips a source | The saved SQL file remains unchanged; the query response reports the source error separately and does not retry or roll back the saved file. |
| Valid Task edit adding or removing `IS_CONTAINED_BY Epic` | One published state refreshes the Task row, Epic outgoing derived Relations, their hashes, and DuckPGQ mappings. The unchanged Epic source bytes and Version stay unchanged. |
| Direct-fact source becomes invalid or is removed | Its row and every supported derived counterpart disappear or refresh together; unrelated valid rows remain queryable. |
| Current Scope Unit Declaration becomes invalid | The owner becomes unavailable, reports the invalid structural input to stderr and requires an explicit restart after correction; it does not skip the Declaration, serve partial/stale structure, retry, or resume merely because the file changes. |
| Ambiguous relation key or inverse metadata | Warn on stderr, omit ambiguous facts without choosing a winner, keep valid rows and unambiguous facts, and change no model declaration. |
| Registered Relation names collide by case in DuckPGQ | Warn with every colliding name and available source path; omit every colliding Relation Type and all of its projected links, preserve raw source facts, and retain unrelated graph facts. |
| Index or graph refresh fails | The owner reports stderr and becomes unavailable; it does not retry, restore old rows, swap databases, or run application rollback. |
| Current Scope Unit or literal Relation-inverse Declaration changes | Relevant structural/materialized rows and their hashes refresh with the graph; declared Content-schema generation runs only when its Current model Declarations change. |
| Invalid, unreadable, or unstable source | Its rows are absent; stderr identifies it; unrelated valid rows remain; no retry is queued. |
| Move, deletion, or later repair | A later refresh reflects observed selected state without prescribing fingerprint algorithm or event workflow classification. |
| Filesystem observation during indexing | The database, derived schema asset, internal results and spill data stay under the owned Workbench runtime directory; no intermediate source file is created. |

Verify successful source-index SQL writes emit INFO stdout records with operation, table, affected row count, reference when applicable, and measured elapsed milliseconds after commit. Verify each successful INFO refresh event includes total elapsed milliseconds and source-capture, materialization and database-write phase durations, without a DEBUG setting. All timings use a monotonic timer. A bulk write reports its measured batch timing; it does not invent per-row timings. Existing source warnings and blocking runtime failures remain on stderr.
