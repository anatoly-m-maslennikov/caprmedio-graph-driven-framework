---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Concern).Priority
version: 30
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-D-386
  - CA-R-1629
atom_id: CA-E-623
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-623-CORE_META_MODEL-EVAL_CASE--effective-priority-selection.md
  source_atom_id: CA-E-623
  source_atom_revision: 30
  source_sha256: c41e0c309d9775240705d7a2ff4f1af92c6dc4e519644ef1ca5da49c593778a0
  original_relations_sha256: 482ac75541dbf35df7976298b4551596eac5e1a3d27b3579c5d272536b9bd1ee
---
## Summary

Effective-priority selection

## Claim scope

the following effective-priority selection conditions:

1. accept stored priority **only** on Concern Atoms **and** reject it on **every** non-Concern Content Role Atom.
2. accept **only** stored `high`, `medium`, **or** `low`.
3. reject stored `highest`, `critical`, **and** `deferred`.
4. compare Concern Atoms with equal stored Priority under a selected model that gives them equal comparison results. change **only** their Scope Unit ancestry; confirm that no implicit increment, virtual `highest`, **or** ancestry-based winner appears.
5. confirm that comparison follows the selected model, its effective parameters, **and** its active criteria; an unresolved model **or** unjustified selection asks the Operator.
6. confirm `ask_always` always asks.
7. confirm `auto_by_effective_priority` selects **`=1`** unique eligible winner **and** asks on ties, incomparable scopes, uncertainty, **or** multiple winners.
8. confirm unsatisfiable external obligations stop rather than auto-resolve.

## Claim

conflict selection follows the admissible Operator-selected priority model **without** an implicit ancestry bonus **and** never chooses through a tie, incomparable scope, uncertainty, **or** ineligible external obligation.

## Details

### Acceptance criteria

**every** comparison conforms **to** the selected priority model **without** an implicit ancestry bonus **and** never guesses through a non-unique **or** ineligible result. authority-tier precedence remains separate **and** unchanged.

### Failure disposition

stop automatic selection, ask the Operator, **and** record a Concern for **any** incorrect priority **or** unauthorized winner.
