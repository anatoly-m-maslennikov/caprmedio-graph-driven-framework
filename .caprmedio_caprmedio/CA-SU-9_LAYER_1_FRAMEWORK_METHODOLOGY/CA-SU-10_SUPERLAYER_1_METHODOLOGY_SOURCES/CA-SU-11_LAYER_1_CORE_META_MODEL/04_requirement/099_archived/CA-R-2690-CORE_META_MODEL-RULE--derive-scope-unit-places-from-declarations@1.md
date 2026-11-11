---
atom_id: CA-R-2690
ref_id: CA-R-2690
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier/Directory
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:17:40 +0400
---
## Summary

Derive Scope Unit places from Declarations

## Claim

Each non-Project Scope Unit has Authority and Delivery folders derived from its Scope Unit Declaration. Delivery Atoms govern representation, placement, and general Carrier conventions without repeating a unit's selected paths.
