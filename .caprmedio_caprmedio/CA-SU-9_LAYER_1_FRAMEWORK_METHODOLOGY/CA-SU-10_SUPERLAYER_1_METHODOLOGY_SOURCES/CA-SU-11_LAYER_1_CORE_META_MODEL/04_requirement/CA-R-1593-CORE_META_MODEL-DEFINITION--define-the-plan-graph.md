---
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
  passive:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)'
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ CFEL > Relation
  - CAPRMEDIO_MODEL <+ Carrier
version: 25
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1593
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Define the Plan Graph

## Claim

### Prose Claim


the Plan Graph.


the Plan Graph **means** a Projection whose nodes reference authoritative Plan Atoms **and** whose graph-owned Relations represent Plan containment **and** blocking. explicit once-owned Plan Relation declarations are the sources of those facts; optional directory placement represents them **without** becoming another declaration.
