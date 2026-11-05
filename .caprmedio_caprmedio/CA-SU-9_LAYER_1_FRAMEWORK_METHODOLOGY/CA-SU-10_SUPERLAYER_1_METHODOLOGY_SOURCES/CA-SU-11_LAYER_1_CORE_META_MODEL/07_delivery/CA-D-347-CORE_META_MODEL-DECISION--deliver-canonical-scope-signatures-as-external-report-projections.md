---
atom_id: CA-D-347
ref_id: CA-D-347
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection/(.Form:=Canonical Scope Signature)
  dependencies:
  - CAPRMEDIO_MODEL <+ Projection/(.Form:=Canonical Scope Signature)
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
relations:
  child_of:
  - CA-D-266
status: Active
version: 29
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-D-347-CORE_META_MODEL-DECISION--deliver-canonical-scope-signatures-as-external-report-projections.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Deliver Canonical Scope Signatures as External Report Projections

## Claim

### Prose Claim


external report Projections that deliver Canonical Scope Signatures.


**every** Canonical Scope Signature Projection **must** be delivered as **`=1`** non-authoritative JSON report under its Project's `.caprmedio_<project_name>/_projection/` Directory Carrier with the selected source frontier digest, **every** source Atom identity **and** revision, source Carrier digest, source Scope Expression occurrence, Canonical Scope Signature, **and** exclusion diagnostic; the Projection **must not** become an Atom Carrier, modify a selected source Carrier, establish Claim equivalence, **or** create a dependency relation.
