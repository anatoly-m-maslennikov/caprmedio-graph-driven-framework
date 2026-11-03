---
atom_id: CA-R-2556
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

State assertions about the active Subject

## Claim

- For an Atom with an active Subject, all assertions and prescriptions concern that active Subject.
- References to other Subjects describe the active Subject's endpoints, inputs, outputs, conditions or dependencies.
- Independent assertions about another Subject belong in an Atom with that active Subject.
- For an Atom whose active Subject is a Node, each Relation count constrains that active Subject's own outgoing Relations.
