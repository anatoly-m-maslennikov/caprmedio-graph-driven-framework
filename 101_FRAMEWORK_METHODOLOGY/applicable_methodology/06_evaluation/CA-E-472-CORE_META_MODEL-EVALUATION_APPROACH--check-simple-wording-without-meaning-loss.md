---
version: 10
updated_at: "2026-10-19 15:55:07 +0400"
relations:
  evaluation_for:
    - CA-M-294
subjects:
  governs: "language"
  depends_on:
    ["Author", "Entity/Node/Continuant/Atom.Substance", "Entity/Node/Continuant/Atom.Summary", "Governed Term", "CCE Operator"]
atom_id: "CA-E-472"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-472-CORE_META_MODEL-EVALUATION_APPROACH--check-simple-wording-without-meaning-loss.md
  source_atom_id: CA-E-472
  source_atom_revision: 10
  source_sha256: 62a2879eb4e04ad27f6729019925322a67a0811ca19eb4a4df4c484d3d3e47d5
  original_relations_sha256: ccb03e34d5bbafefb098233b0471b4098c19f040a0d2e15825b6bcb20d5f949f
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
