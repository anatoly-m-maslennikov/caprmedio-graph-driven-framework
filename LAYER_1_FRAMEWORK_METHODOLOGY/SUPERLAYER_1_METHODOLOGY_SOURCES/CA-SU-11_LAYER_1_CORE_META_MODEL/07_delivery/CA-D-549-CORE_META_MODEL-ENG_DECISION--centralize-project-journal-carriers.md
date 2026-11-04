---
atom_id: CA-D-549
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Journal
  passive:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Projection
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
version: 19
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Delivery
form: Decision
---
## Summary

Centralize Project Journal Carriers

## Claim

### Prose Claim


persistent File Carriers of a Project's shared Work Journal and other project-control Journals.


**all** persistent project-control Journal File Carriers of a Project **must** reside under **`=1`** Directory Carrier: `.caprmedio_<project_name>/_journal/`.

## Details

- Journal segments use this root **or** its subdirectories.
- Artifact Change Log **and** Workflow Execution Log views **are** Projections, **not** separate authoritative Journals.
- Runtime locks, receipts, **and** pending-recording state remain runtime state, **not** canonical Journal Carriers.

Technical and business runtime logs are Journals too, but their configured local database, remote database, or logging sink Carriers are not required to reside in this Directory Carrier. Journal classification does not impose one physical storage technology.
