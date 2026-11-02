---
subjects:
  active: Projection/(.Form:=Canonical Scope Signature)
  passive:
  - Projection/(.Form:=Canonical Scope Signature)
  - Carrier
version: 29
updated_at: 2026-11-02 07:52:54 +0400
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
---
## Summary

Deliver Canonical Scope Signatures as External Report Projections

## Claim scope

external report Projections that deliver Canonical Scope Signatures.

## Claim

**every** Canonical Scope Signature Projection **must** be delivered as **`=1`** non-authoritative JSON report under its Project's `.caprmedio_<project_name>/_projection/` Directory Carrier with the selected source frontier digest, **every** source Atom identity **and** revision, source Carrier digest, source Scope Expression occurrence, Canonical Scope Signature, **and** exclusion diagnostic; the Projection **must not** become an Atom Carrier, modify a selected source Carrier, establish Claim equivalence, **or** create a dependency relation.
