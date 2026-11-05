---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Status
  passive:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)'
version: 28
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1312
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary
Separate Governed Transitions from Status Values

## Claim

### Prose Claim

Artifact Revision Status values associated with admission, acceptance, commitment, activation, completion, **or** archival.

an Artifact Revision Status value **must** remain distinct from the Action **or** Workflow whose execution **may** establish that value.

## Details
the same distinction applies **when** a Workflow uses several Steps **to** establish the Status value.
