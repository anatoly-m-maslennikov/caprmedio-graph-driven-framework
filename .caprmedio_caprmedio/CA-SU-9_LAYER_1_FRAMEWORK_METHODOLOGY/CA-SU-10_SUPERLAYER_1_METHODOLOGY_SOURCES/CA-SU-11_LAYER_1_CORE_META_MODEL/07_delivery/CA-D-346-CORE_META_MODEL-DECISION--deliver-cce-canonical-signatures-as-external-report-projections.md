---
atom_id: CA-D-346
ref_id: CA-D-346
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection/(.Form:=Canonical Signature)
  dependencies:
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Output Publication
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom.Header.ID
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Carrier/File
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Controlled English
tier: 3
relations:
  child_of:
  - CA-D-266
status: Active
version: 36
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-D-346-CORE_META_MODEL-DECISION--deliver-cce-canonical-signatures-as-external-report-projections.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary
Deliver CCE Canonical Signatures as External Report Projections

## Claim

### Prose Claim

Canonical Signature Projections for selected source frontiers **and** their external reports.


**every** Canonical Signature Projection **must** be delivered as **`=1`** non-authoritative report under its Project's `.caprmedio_<project_name>/_projection/` Directory Carrier with the selected source frontier digest, **every** source Atom Identity **and** Revision, **every** source expression occurrence, **every** Canonical Signature, **and** **every** exclusion diagnostic; the Projection **must not** become an Atom Carrier, modify a selected source Carrier, **or** establish Claim equivalence.
