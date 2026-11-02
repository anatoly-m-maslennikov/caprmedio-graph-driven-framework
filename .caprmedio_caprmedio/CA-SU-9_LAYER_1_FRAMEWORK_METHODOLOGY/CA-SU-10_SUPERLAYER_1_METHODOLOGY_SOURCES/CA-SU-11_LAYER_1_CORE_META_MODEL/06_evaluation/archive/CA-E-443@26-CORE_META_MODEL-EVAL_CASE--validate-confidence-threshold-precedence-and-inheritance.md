---
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control/Decision Confidence
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan/Type: Plan'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Domain/Continuant/Term//Property
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Concern'
  - Subject/Graph Node/Carrier
version: 26
updated_at: 2026-10-27 06:04:45 +0400
relations:
  evaluation_for:
  - CA-R-1587
  - CA-R-1044
  - CA-R-1045
  - CA-R-1427
  - CA-R-1428
  - CA-M-271
  - CA-R-1591
  - CA-D-472
  - CA-D-485
  - CA-R-1713
atom_id: CA-E-443@26
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Eval Case
tier: 4
---
# Summary

Validate confidence-threshold precedence **and** inheritance

## Scope

the confidence-threshold Evaluation.

## Claim

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

## Details
