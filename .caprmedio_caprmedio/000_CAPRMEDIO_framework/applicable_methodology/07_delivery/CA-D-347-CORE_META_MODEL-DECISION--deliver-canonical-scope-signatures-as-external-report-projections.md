---
subjects:
  active: CAPRMEDIO_MODEL <+ Projection/(.Form:=Canonical Scope Signature)
  passive:
  - CAPRMEDIO_MODEL <+ Projection/(.Form:=Canonical Scope Signature)
  - CAPRMEDIO_MODEL <+ Carrier
version: 29
updated_at: 2026-11-02 08:06:47 +0400
relations:
  child_of:
  - CA-D-266
atom_id: CA-D-347
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-347-CORE_META_MODEL-DECISION--deliver-canonical-scope-signatures-as-external-report-projections.md
  source_atom_id: CA-D-347
  source_atom_revision: 29
  source_sha256: bae57a3b5d71a39868d391ef59350d1f60dc815385380592434ad2aae3f7b711
  original_relations_sha256: 05d305e1056e99459d521dea634c2a5bc7d31356258feae4f6c9491320e90591
---
## Summary

Deliver Canonical Scope Signatures as External Report Projections

## Claim

### Prose Claim


external report Projections that deliver Canonical Scope Signatures.


**every** Canonical Scope Signature Projection **must** be delivered as **`=1`** non-authoritative JSON report under its Project's `.caprmedio_<project_name>/_projection/` Directory Carrier with the selected source frontier digest, **every** source Atom identity **and** revision, source Carrier digest, source Scope Expression occurrence, Canonical Scope Signature, **and** exclusion diagnostic; the Projection **must not** become an Atom Carrier, modify a selected source Carrier, establish Claim equivalence, **or** create a dependency relation.
