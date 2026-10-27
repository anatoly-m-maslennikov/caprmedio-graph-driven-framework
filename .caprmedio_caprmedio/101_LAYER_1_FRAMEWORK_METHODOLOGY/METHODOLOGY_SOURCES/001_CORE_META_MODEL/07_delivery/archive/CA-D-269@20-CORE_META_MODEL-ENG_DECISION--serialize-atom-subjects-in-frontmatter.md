---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Subjects
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Subjects
  - 'Subject/Graph/Relation/Type: GOVERNS'
  - 'Subject/Graph/Relation/Type: DEPENDS_ON'
  - Subject
  - Subject/Graph/Relation/Type
version: 20
updated_at: 2026-10-24 09:42:52 +0400
relations: {}
atom_id: CA-D-269@20
content_role: Delivery
type: Eng Decision
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Serialize Atom Subjects in Frontmatter

## Scope

New **or** migrated Markdown Atom Carriers.

## Claim

a new **or** migrated Markdown Atom Carrier **may** omit `subjects` when it has no Subject Relations. **when** present, `subjects.governs` **may** contain one scalar Subject Path **and** `subjects.depends_on` an unordered collection of **`>=0`** unique scalar Subject Paths; an absent `governs` key **means** zero governed Subjects **and** an absent dependency collection **means** zero dependencies. the `governs` **or** `depends_on` key encodes the Subject Relation Kind; the source Atom is implicit **and** the scalar value encodes its target's Subject Path, **not** the Subject Relation itself. these values resolve their canonical targets under CA-R-1202-CORE_META_MODEL-CORE-REQUIREMENT--resolve-every-direct-subject-target-once **without** an intermediate Subject/Entity **or** Subject/Reference field **or** a repeated target-kind field.

## Details

an existing unmigrated Carrier **may** temporarily retain `subjects.<governs|depends_on>.<continuant|occurrent>` **only** **until** its explicitly assigned carrier-migration Task is executed. this compatibility is migration-limited, preserves the same direct relation facts **and** target identities, **and** does **not** establish a second canonical representation. legacy temporal-classification authority **and** bulk Carrier conversion require their separately assigned migration Tasks.
