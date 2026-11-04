---
atom_id: CA-E-677
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Active
author: Anatoly Maslennikov
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
version: 8
role: Evaluation
form: Eval Case
tier: 5
carrier_destination:
  file:
    name: CA-E-677-WORKBENCH_BACKEND-EVAL_CASE--reconcile-source-lifecycle-and-invalid-repair-state.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
relations:
  evaluation_for: [CA-R-2723, CA-R-2725, CA-M-465, CA-D-672, CA-D-675]
updated_at: 2026-11-04 23:19:17 +0400
---
## Summary

Reconcile source lifecycle changes and repaired validity

## Claim scope

Atomic file-backed refresh of governed sources and Current declarations.

## Claim

### Prose Claim

The indexer atomically replaces `atoms` and `scope_units` state from selected governed sources and Current declarations. Current and Draft Atom carriers are included, including Done and Canceled Current statuses; Archived carriers are excluded. Only Current Scope Unit Declarations establish `scope_units`; Draft Declarations remain Atom rows. No reader schema is compiled. Each public row hash is SHA-256 of deterministic canonical row JSON excluding `hash`, with materialized relations in the Atom payload. Failures go to stderr, are skipped, and are not retried. The database, internal results and spill data stay under the owned Workbench runtime directory; no intermediate source or schema file is created. Saved SQL files are separate UTF-8 runtime artifacts and are not removed or changed by source refresh.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Repository parent folder is named `archive` or `draft` | Classify each source relative to the selected repository, without inheriting lifecycle from the parent mount path. |
| Plain review Markdown without a closed Atom Header; or a role-mismatched proof copy | Ignore it without reporting a malformed Atom. Canonical Atom filename candidates still report invalid source content. |
| Current Active, Done, Canceled; Draft; and Archived carrier | The first four have Current/Draft `atoms` rows; Archived is absent. |
| Current and Draft Scope Unit Declarations | Only Current produces Scope Unit structure; Drafts remain queryable Atom rows. No reader-schema state is created. |
| Saved SQL while source refresh fails or skips a source | The saved SQL file remains unchanged; the query response reports the source error separately and does not retry or roll back the saved file. |
| Valid Task edit adding or removing `IS_CONTAINED_BY Epic` | One published state refreshes the Task row, Epic outgoing derived Relations, their hashes, and DuckPGQ mappings. The unchanged Epic source bytes and Version stay unchanged. |
| Direct-fact source becomes invalid or is removed | Its row and every supported derived counterpart disappear or refresh together; unrelated valid rows remain queryable. |
| Current Scope Unit Declaration becomes invalid | The invalid structural input is reported to stderr and does not establish Current structure; no reader-schema fallback or automatic retry is introduced. |
| Ambiguous relation key or inverse metadata | Warn on stderr, omit ambiguous facts without choosing a winner, keep valid rows and unambiguous facts, and change no model declaration. |
| Index or graph refresh fails | The owner reports stderr and becomes unavailable; it does not retry, restore old rows, swap databases, or run application rollback. |
| Current Scope Unit or literal Relation-inverse Declaration changes | Relevant structural/materialized rows and their hashes refresh with the graph; no generic CFEL or schema compilation occurs. |
| Invalid, unreadable, or unstable source | Its rows are absent; stderr identifies it; unrelated valid rows remain; no retry is queued. |
| Move, deletion, or later repair | A later refresh reflects observed selected state without prescribing fingerprint algorithm or event workflow classification. |
| Filesystem observation during indexing | The database, internal results and spill data stay under the owned Workbench runtime directory; no intermediate source or schema file is created. |
