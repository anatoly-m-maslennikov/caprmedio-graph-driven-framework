---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Status:Archived
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom.Status
  - CAPRMEDIO <+ MODEL <+ Atom.Version
version: 23
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1419
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Restrict Archived Status to Non-Current Revisions

## Claim scope

the Archived Status of an Atom version.

## Claim

an Atom version **may** have Status Archived **only** **if** it is a prior version **or** the final version of a replaced, absorbed, **or** retired Atom.
