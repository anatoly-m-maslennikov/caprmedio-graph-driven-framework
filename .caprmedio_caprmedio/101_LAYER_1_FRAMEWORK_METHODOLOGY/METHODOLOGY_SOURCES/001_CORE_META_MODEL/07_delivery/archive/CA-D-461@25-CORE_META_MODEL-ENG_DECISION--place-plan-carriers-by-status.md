---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Status'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Status'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
version: 25
updated_at: 2026-10-26 17:47:19 +0400
relations: {}
atom_id: CA-D-461@25
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Eng Decision
---
# Summary

Place Plan Carriers by Status

## Scope

Plan Carrier Bundle placement by carried Status.

## Claim

**every** Plan Carrier Bundle **must** represent its carried Status **in** the following locations:

- Draft: **in** the owning Scope Unit's shared `03_plan/draft` area.
- Active: directly **in** its local container.
- Backlog: **in** its `001_backlog` subdirectory.
- Done: **in** its `done` subdirectory.
- Canceled: **in** its `canceled` subdirectory.
- Archived: **in** the owning Scope Unit's shared `03_plan/archived` area.

For a contained Current Plan, the local container for its current-Status placement is the matching Directory Carrier of its declared immediate containing Plan. Draft and Archived areas are shared across the owning Scope Unit, rather than replicated under each Plan container. This rule does **not** decide terminal-Status placement for a Plan without an `IS_CONTAINED_BY` connection. reserved Status directories are **not** Plan nodes. validate folder nesting against the child's direct `IS_CONTAINED_BY` declaration; placement does **not** declare containment.

read Status from the Plan's own Markdown file under CA-D-483 **and** check its local placement; a parent **or** folder name **must not** supply a descendant's Status at read time. **every** admitted parent Status change requires the containment cascade under CA-R-1521: separate single-Atom Actions write the Status prescribed by CA-R-1521 to each selected latest descendant under its own model, without an optional descendant mode. For a containing Plan Atom whose requested Status is Done **or** Canceled, preserve every selected latest contained Plan already Done **or** Canceled and request Canceled for every other selected latest contained Plan. After the cascade, every selected latest contained Plan must be Done **or** Canceled; mixed terminal statuses are allowed, and no contained Plan is forced to match the parent's requested Status merely because the parent is Done **or** Canceled. For other admitted parent Statuses, preserve the applicable cascade. Archive selects all contained latest Atoms; references outside the Carrier tree **and** older archived Revisions are excluded. retain Current descendants inside the parent Carrier tree. Archived Plan Markdown Carriers are placed flat in the owning Scope Unit's shared `03_plan/archived` area, not inside an archived parent's directory.

## Details

- for a contained Plan, apply its current-Status placement relative to its immediate containing Plan's Directory Carrier; for example, a Done child is in `<parent-directory>/done/<child>.md`, using its canonical matching stem. This does **not** specify the parent's own root-level terminal-Status location.
- Place each Archived Plan Markdown Carrier directly in the owning Scope Unit's shared `03_plan/archived` area, without a parent/child Plan directory hierarchy. Apply CA-D-289's Version suffixes **to** Archive Carrier basenames. Preserve exact older version bytes **without** rewriting their Version **or** Status. Retained-history subtrees and non-Atom assets may move byte-for-byte with an authorized matching Directory Carrier move; they are not independent Status targets. This does **not** authorize independent legacy-tree migration.
