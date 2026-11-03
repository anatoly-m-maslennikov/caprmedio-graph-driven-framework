---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom
  passive:
  - CAPRMEDIO_MODEL <+ CFEL > Relation
version: 28
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1033
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Define compatible Lineage Impact disposition

## Claim

### Prose Claim


`compatible` Lineage Impact dispositions.



When a Lineage Impact analysis addresses an Atom, `compatible` must mean the child remains valid against the parent Revision required by the gate and traversal stops without a child update; a pinned earlier Revision does not establish compatibility where the new Revision is required.

