---
subjects:
  governs: "Entity/Continuant/Node/Projection"
  depends_on:
    ["Entity/Continuant/Node/History/Journal", "Entity/Continuant/Node/History/Journal.Record", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Workflow", "Entity/Continuant/Node/Project", "Entity/Continuant/Node/Projection/Type: Artifact Change Log", "Entity/Continuant/Node/Projection/Type: Process Log"]
version: 11
updated_at: "2026-10-18 03:33:33 +0400"
relations: {}
atom_id: "CA-R-1463"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1463-CORE_META_MODEL-GENERAL-REQUIREMENT--derive-log-views-from-the-shared-journal.md
  source_atom_id: CA-R-1463
  source_atom_revision: 11
  source_sha256: a46832a0b47a894907195505f7d667aab445b0dff67f379e4378e20d109799d7
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive log views from the shared Journal

## Scope

Artifact Change Log and Process Log log Projection Types derived from the same Project Journal.

## Claim

the Core Meta-Model **must** provide Artifact Change Log **and** Process Log as **`=2`** log Projection Types derived from the same Project Journal, under CA-R-1467-CORE_META_MODEL--define-artifact-change-log-projection **and** CA-R-1468-CORE_META_MODEL-REQUIREMENT--define-process-log-projection. these Types organize recorded history **without** introducing independent Journals; additional Projection Types remain governed by the open Projection model.

**every** represented historical fact **must** remain traceable **to** its canonical source event record **and** Event identity. the same source event **may** appear **in** both views **without** becoming two authoritative records. a read-only execution requires no fictitious Artifact change; membership **and** execution associations **must** come from recorded source evidence rather than invented events **or** inferred success. a view **must** remain rebuildable from its declared Journal selection, disclose known incomplete **or** stale source coverage **without** claiming complete current history, **and** obtain corrections through the owning source authority rather than independent log edits.

## Details
