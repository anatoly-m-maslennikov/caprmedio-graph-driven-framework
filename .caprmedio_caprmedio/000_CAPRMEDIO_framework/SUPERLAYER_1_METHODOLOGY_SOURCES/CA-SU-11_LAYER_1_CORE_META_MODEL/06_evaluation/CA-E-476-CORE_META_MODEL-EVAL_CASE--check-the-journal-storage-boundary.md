---
atom_id: CA-E-476
ref_id: CA-E-476
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Journal
  dependencies:
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Project
  - 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/Type: Applicable Methodology'
tier: 3
relations:
  evaluation_for:
  - CA-R-1491
  - CA-D-308
  - CA-D-340
status: Active
version: 23
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-E-476-CORE_META_MODEL-EVAL_CASE--check-the-journal-storage-boundary.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Check the Journal storage boundary

## Claim

### Prose Claim


Journal admission checks event **and** storage integrity **without** becoming a Project-conformance gate.


report a failed Evaluation **if** the Journal loses recordable evidence because of Project defects, accepts corrupted **or** unauthorized writes, silently changes observations, **or** rewrites accepted history.

## Details

### Cases

1. submit a correctly encoded event describing a conforming Project change.
2. keep that event envelope valid while recording a legacy Atom ID, broken filename, invalid placement, malformed Atom Properties, unresolved Relation, **or** invalid lifecycle transition.
3. change the live Project **after** capture while leaving the sealed historical observation intact.
4. submit unreadable event data, missing required Event identity **or** fields, a digest mismatch, unauthorized append access, **or** an attempt **to** rewrite accepted history.
5. resubmit the same Event identity **and** payload; **then** supply a conflicting payload under that identity.
6. record an action whose separate conformance Evaluation failed **or** remained unresolved.

### Acceptance

- cases 1, 2, 3, **and** 6 remain recordable **without** inventing identities, repairing observed values, **or** claiming a successful conformance verdict.
- case 4 fails storage admission, preserves pending evidence safely, **and** leaves accepted history unchanged.
- an identical retry creates no duplicate record. an identity collision with different payload fails **without** overwriting history.
- conformance Evaluations remain independently available; their verdicts do **not** become prerequisites for recording the facts they evaluate.
- Journal acceptance grants no Project-mutation permission **and** does **not** bypass a separate action's preconditions.
