---
atom_id: CA-P-949
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: Operator
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Selection//Methodology Conflict Disposition Set
  depends_on:
  - Subject/Graph Node/Engineering/Methodology
  - Subject/Graph Node/Domain/Continuant/Projection
version: 6
updated_at: 2026-10-25 17:32:27 +0400
autonomous_confidence_threshold: 99
relations:
  depends_on:
  - CA-P-948
status: Done
current_scope_unit: caprmedio
content_role: Plan
type: Plan
label: Task
tier: 3
---
# Approve Exact Methodology Conflict Dispositions

**when** CA-P-948 is Done, **then** the Operator **must** assign **`=1`** exact disposition to every reported methodology conflict that requires a semantic choice **before** that conflict changes source authority **or** Applicable Methodology output.

## Scope

`(all CA-P-948 findings whose required resolution class is Operator disposition)`

## Definition of Done

the Task is **not done if** (**any** in-scope conflict lacks **`=1`** explicit disposition **or** a disposition omits its conflict identity, source-frontier digest, selected semantic result, affected Carrier paths, **and** authorized action **or** a disposition rewrites Core authority through an Extension **or** Local Configuration **or** a disposition relies on unstated precedence, confidence, filename order, **or** compiler preference **or** a stale disposition is reused **after** its source frontier changes **or** a conflict-free report is not recorded explicitly as requiring **`=0`** dispositions).

## Details

bind every disposition to the exact CA-P-948 frontier. reject any proposed resolution that makes an Extension **or** Local Configuration rewrite Core authority.
