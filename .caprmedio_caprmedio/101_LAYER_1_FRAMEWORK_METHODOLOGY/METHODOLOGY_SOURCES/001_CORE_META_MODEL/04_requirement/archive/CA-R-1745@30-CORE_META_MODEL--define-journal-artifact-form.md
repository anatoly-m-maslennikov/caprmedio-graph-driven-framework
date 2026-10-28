---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/History/Journal
  depends_on:
  - Subject/Graph Node/Domain/Continuant/History
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
  - Subject/Graph Node/Domain/Continuant/Atom.Content
version: 30
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-R-1745@30
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define Journal Artifact form

## Scope

Journal Artifacts and their recorded histories, including technical and business runtime logs.

## Claim

a Journal, also called an Event Log, **means** an authoritative Artifact whose recorded history forms **`=1`** logically ordered table of admitted records about events. technical **and** business runtime logs **are** Journals. a record describes an event **and** its recorded evidence; the record is **not** the event itself **or** automatic proof of its asserted outcome. accepted records **must not** be edited, reordered, **or** removed; corrections append new traceable records **without** rewriting accepted history. Journal authority concerns recorded history **and** does **not** independently redefine governing Atom Claims.

## Details

Journal is a logical Artifact classification, not a required storage technology or directory. Its Carrier may be files, a local database, a remote database, or a governed logging sink according to applicable Delivery and configuration. Project-control Journal files use the registered _journal directory; runtime log classification does not force every runtime sink into that directory. Views and queries of a Journal remain Projections.
