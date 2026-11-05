---
atom_id: CA-E-511
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Subjects.Active
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Header.Subjects
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Scope Unit
version: 23
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-R-2102
  - CA-D-495
  - CA-R-1271
  - CA-R-1588
  - CA-R-1595@21
  - CA-R-1596
  - CA-R-922
  - CA-R-923
tier: 4
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-511-CORE_META_MODEL-EVAL_CASE--validate-target-scope-unit-and-textual-claim-scope.md
  source_atom_id: CA-E-511
  source_atom_revision: 23
  source_sha256: 638939f5bd755383364af8d1e17dd5bb55fbbcc50c85fe8c9480704be456cc2a
  original_relations_sha256: 62e600ae351ff84ee1edfcb102569c0c97a74a686bf80919f3b4d68e38cdb4b7
---
## Summary

Validate Target Scope Unit **and** textual Claim Scope

## Claim

### Prose Claim

the distinction between an Atom's Claim Target Scope Unit **and** its textual applicability.


**Claim checked.**

**every** Atom has exactly one active Subject; resolve its Claim Target Scope Unit from that Subject under CA-R-2102. Textual applicability belongs in Claim.Prose Claim under CA-D-495 and does not create another structural target.

## Details

### Test case

create an Atom whose active Subject resolves to its current Scope Unit and whose Prose Claim restricts applicability to Python files; repeat with a composite restriction and with an admitted different target. Include a Plan nested in Container Atoms. Then omit or duplicate the active Subject, use an unresolved Subject, or infer a target from the textual restriction alone.

### Acceptance criteria

valid fixtures resolve the target from exactly one active Subject; containment supplies current Scope Unit context. Applicability restrictions and Container Atom nesting do not independently change that target. Invalid fixtures identify the missing, multiple, unresolved, or improperly inferred Subject or target.

### Failure disposition

report the affected Atom **and** target **or** textual-applicability distinction; preserve the source **until** an authorized correction is selected.
