---
atom_id: CA-E-443
ref_id: CA-E-443
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Decision Confidence"
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Plan)/(.Header.Form: Plan)'
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern)
  - CAPRMEDIO_MODEL <+ Carrier
tier: 4
relations:
  evaluation_for:
  - CA-R-1587
  - CA-R-1044
  - CA-R-1045
  - CA-R-1427@17
  - CA-R-1428
  - CA-M-271
  - CA-R-1591
  - CA-D-472
  - CA-D-485
  - CA-R-1713
status: Active
version: 34
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-E-443-CORE_META_MODEL-EVAL_CASE--validate-confidence-threshold-precedence-and-inheritance.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-443-CORE_META_MODEL-EVAL_CASE--validate-confidence-threshold-precedence-and-inheritance.md
  source_atom_id: CA-E-443
  source_atom_revision: 34
  source_sha256: 46635910f345c3baec1029cc1e355395f54905d7040e9b4425936a31f8b14b56
  original_relations_sha256: 4e594913288aae00ff2d31dc5ab5e3127ae4729ea3688f3d2d108e9e7e942fe4
---
## Summary

Validate confidence-threshold precedence **and** inheritance

## Claim

### Prose Claim


the confidence-threshold Evaluation.


the confidence-threshold Evaluation **must** preserve CA-M-271-CORE_META_MODEL-IMPLEMENTATION_METHOD--resolve-confidence-thresholds-by-source-precedence precedence **and** CA-R-1591-CORE_META_MODEL-RULE--apply-autonomous-confidence-thresholds-to-plan-execution authorization gates.

- supply distinct valid values through Operator input, a Plan, nested Hubs, **and** Framework Instance Settings; omit sources successively **and** confirm nearest explicit source selection.
- scope direct input **to** one execution; retain the unrelated execution's setting.
- omit the inner Hub's optional confidence override while retaining its mandatory file **and** a retry override: inherit confidence **without** copying it. reject a missing mandatory file.
- supply a Hub file with explicit values: require the same Atom identity as its folder **and** its DoD; reject a separate Objective, `epic_overrides`, **or** a nearby unrelated file as an inherited source.
- use a current Plan Revision **without** taking values from its Archived copies; reject an ambiguous Bundle **or** invalid reached source **without** silent fallback.
- preserve an explicit override equal **to** the inherited value **after** the upstream source changes; an omitted override follows that change.
- accept permitted integer values including **`=0`**, **`=87`**, **`=99`**, **and** **`=100`**; reject out-of-range, non-integer, missing effective, **or** ambiguous values.
- confidence below the effective value requests Operator disposition; equal **or** greater confidence grants no additional authority.

report the selected source, context, expected value, **and** failed condition **without** mutating source values.
