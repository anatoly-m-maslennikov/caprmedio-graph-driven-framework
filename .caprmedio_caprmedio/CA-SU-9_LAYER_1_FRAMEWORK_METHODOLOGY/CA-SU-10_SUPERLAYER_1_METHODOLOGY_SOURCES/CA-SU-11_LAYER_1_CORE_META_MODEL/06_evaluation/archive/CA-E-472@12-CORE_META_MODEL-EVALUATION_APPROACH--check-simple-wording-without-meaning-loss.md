---
version: 12
updated_at: 2026-10-23 03:20:06 +0400
relations:
  evaluation_for:
  - CA-M-294
subjects:
  governs: language
  depends_on:
  - Author
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Entity/Node/Continuant/Atom.Summary
  - Governed Term
  - CCE Operator
atom_id: CA-E-472@12
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
status: Archived
author: Anatoly Maslennikov
type: Policy
global_tier: 11
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
