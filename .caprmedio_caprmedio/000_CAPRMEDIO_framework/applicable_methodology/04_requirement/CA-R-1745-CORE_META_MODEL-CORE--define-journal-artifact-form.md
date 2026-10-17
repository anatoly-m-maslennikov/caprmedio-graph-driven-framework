---
subjects:
  governs: "Entity/Continuant/History/Journal"
  depends_on:
    ["Entity/Continuant/History", "Entity/Continuant/History/Journal.Record", "Entity/Continuant/Object/Atom.Substance"]
version: 20
updated_at: "2026-10-16 12:08:42 +0000"
relations: {}
atom_id: "CA-R-1745"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1745-CORE_META_MODEL-CORE--define-journal-artifact-form.md
  source_atom_id: CA-R-1745
  source_atom_revision: 20
  source_sha256: d803035fbd0407e284c3da68c11486118dc05c466d6e2f99127701dcd4ead02b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Journal Artifact form

## Scope

Journal Artifacts and their recorded histories, including technical and business runtime logs.

## Claim

a Journal, also called an Event Log, **means** an authoritative Artifact whose recorded history forms **`=1`** logically ordered table of admitted records about events. technical **and** business runtime logs **are** Journals. a record describes an event **and** its recorded evidence; the record is **not** the event itself **or** automatic proof of its asserted outcome. accepted records **must not** be edited, reordered, **or** removed; corrections append new traceable records **without** rewriting accepted history. Journal authority concerns recorded history **and** does **not** independently redefine governing Atom Claims.

## Details

Journal is a logical Artifact classification, not a required storage technology or directory. Its Carrier may be files, a local database, a remote database, or a governed logging sink according to applicable Delivery and configuration. Project-control Journal files use the registered _journal directory; runtime log classification does not force every runtime sink into that directory. Views and queries of a Journal remain Projections.
