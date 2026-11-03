---
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
  passive:
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History/Journal > Event Record
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - CAPRMEDIO_MODEL <+ Project
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/Type: Artifact Change Log'
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/Type: Process Log'
version: 26
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1463
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Derive log views from the shared Journal

## Claim

### Prose Claim


Artifact Change Log and Process Log log Projection Types derived from the same Project Journal.


the Core Meta-Model **must** provide Artifact Change Log **and** Process Log as **`=2`** log Projection Types derived from the same Project Journal, under CA-R-1467@19-CORE_META_MODEL-DEFINITION--define-artifact-change-log-projection **and** CA-R-1468@20-CORE_META_MODEL-REQUIREMENT--define-process-log-projection. these Types organize recorded history **without** introducing independent Journals; additional Projection Types remain governed by the open Projection model.

**every** represented historical fact **must** remain traceable **to** its canonical source event record **and** Event identity. the same source event **may** appear **in** both views **without** becoming two authoritative records. a read-only execution requires no fictitious Artifact change; membership **and** execution associations **must** come from recorded source evidence rather than invented events **or** inferred success. a view **must** remain rebuildable from its declared Journal selection, disclose known incomplete **or** stale source coverage **without** claiming complete current history, **and** obtain corrections through the owning source authority rather than independent log edits.
