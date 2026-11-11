---
subjects:
  active: 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Status'
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
  - CAPRMEDIO <+ MODEL <+ Atom.Status
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1539
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Register Core Plan Status Values

## Claim scope

Core Plan Status values.

## Claim

the Core Plan Status model **must** inherit the allowed values of Atom.Status and add (Backlog, Done, Canceled). Planned **must not** be a distinct Plan Status.
