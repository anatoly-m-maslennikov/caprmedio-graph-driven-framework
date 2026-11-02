---
subjects:
  governs: "Entity/Node/Continuant/Projection"
  depends_on:
    ["Entity/Node/Continuant/History/Journal", "Entity/Node/Continuant/History/Journal.Record", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow", "Entity/Node/Continuant/Project", "Entity/Node/Continuant/Projection/Type: Artifact Change Log", "Entity/Node/Continuant/Projection/Type: Process Log"]
version: 12
updated_at: "2026-10-19 15:53:10 +0400"
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
  source_atom_revision: 12
  source_sha256: 77f4ac687846cec0202b15c4d492b73eda2f85c54bba300f3db88c567d2d362d
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
