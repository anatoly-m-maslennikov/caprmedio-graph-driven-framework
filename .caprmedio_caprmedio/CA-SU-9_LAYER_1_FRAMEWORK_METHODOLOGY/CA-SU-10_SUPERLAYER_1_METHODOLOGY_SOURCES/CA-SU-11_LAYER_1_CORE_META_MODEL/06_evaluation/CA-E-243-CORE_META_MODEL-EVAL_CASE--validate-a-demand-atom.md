---
atom_id: CA-E-243
ref_id: CA-E-243
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form := Demand)'
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit.order.number
tier: 7
relations:
  evaluation_for:
  - CA-R-932@37
  - CA-R-933
  - CA-R-916
  - CA-R-944
  - CA-R-1293
  - CA-R-934
  - CA-R-954
status: Active
version: 39
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-E-243-CORE_META_MODEL-EVAL_CASE--validate-a-demand-atom.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Validate a Demand Atom

## Claim

### Prose Claim


Demand Atoms and their Consumer-owned Producer-result constraints.


a Demand is owned by its Consumer **and** constrains **only** one Producer result authorized by the Consumer's accepted Goal.

### Test case

create valid Demand Atoms with Consumer **and** Producer Scope Unit references **in** permitted branches **and** with a later ordered sibling as Consumer **and** an earlier ordered sibling as Producer. **then** remove the Goal-authorized need for the Producer result, change ownership, target an ancestor, direct child, deeper descendant, **or** later ordered sibling, use equal Producer **and** Consumer Local Order, target two results, constrain Producer authority outside the selected result, fully define Producer Scope, **and** add a separate Demand-direction relation Kind.

### Acceptance criteria

**only** fixtures with Consumer ownership, a permitted direction, one exact Goal-authorized need for the Producer result, one exact Implementation result, **and** no additional direction relation pass.

### Failure disposition

record a Concern naming the invalid Demand fact.
