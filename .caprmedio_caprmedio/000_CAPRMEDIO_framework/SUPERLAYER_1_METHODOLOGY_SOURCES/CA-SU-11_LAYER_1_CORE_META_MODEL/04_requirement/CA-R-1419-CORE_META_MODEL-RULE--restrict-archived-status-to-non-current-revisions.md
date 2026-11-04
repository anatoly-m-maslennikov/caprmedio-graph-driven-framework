---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Status:Archived
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Header.Status
  - CAPRMEDIO_MODEL <+ Atom.Header.Version
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

## Claim

### Prose Claim


the Archived Status of an Atom version.


an Atom version **may** have Status Archived **only** **if** it is a prior version **or** the final version of a replaced, absorbed, **or** retired Atom.
