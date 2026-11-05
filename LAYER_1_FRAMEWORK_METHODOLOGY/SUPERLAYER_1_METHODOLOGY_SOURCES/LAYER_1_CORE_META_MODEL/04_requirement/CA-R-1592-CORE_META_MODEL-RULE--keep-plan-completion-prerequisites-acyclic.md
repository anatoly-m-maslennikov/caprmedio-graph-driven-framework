---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Status: Done'
version: 23
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1592
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Keep Plan completion prerequisites acyclic

## Claim

### Prose Claim


Plan execution.


Plan execution **must not** contain a cycle of completion prerequisites, including one formed jointly by `BLOCKS` **and** the requirement **to** complete directly contained Plan work **before** its containing Plan can be Done **or** Canceled.
