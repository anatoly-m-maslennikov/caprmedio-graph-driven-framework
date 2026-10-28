---
version: 22
updated_at: 2026-10-27 19:59:35 +0400
relations:
  evaluation_for:
  - CA-M-294
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Actor
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Controlled English
atom_id: CA-E-472
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
type: Policy
tier: 4
---
# Summary

Check simple wording without meaning loss

## Scope

wording evaluated under CA-M-294.

## Claim

wording evaluated under CA-M-294 fails **if** **any** of the following holds:

- a demonstrated simpler, more familiar alternative preserves the intended meaning, but unnecessary jargon **or** specialized wording is retained.
- a simplification removes **or** changes a necessary participant, obligation, permission, quantity, condition, boundary, **or** logical distinction.
- a simplification adds ambiguity **or** substitutes an unregistered synonym for a canonical Term, CCE Operator, **or** reference.
- a simplified Summary adds **to**, broadens, narrows, **or** contradicts its source Claim **or** Claim Scope.

## Details

necessary specialized wording **must not** fail merely because it is technical. shorter wording **must not** pass merely because it uses fewer words. uncertain meaning preservation remains unevaluated, **not** passed.
