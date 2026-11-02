---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Content
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - Entity/Object/Continuant/Governing Objects/Atom.Subjects.Governs
  - Entity/Term//Property
  - Entity/Graph Syntax <+ Relation//IS_ALLOWED_VALUE_OF
version: 33
updated_at: 2026-10-30 14:55:21 +0400
relations:
  evaluation_for:
  - CA-R-1358
  - CA-R-1359
atom_id: CA-E-403@33
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Eval Policy
tier: 4
---
## Summary

Report Exact Claim Value-Set Consolidation Candidates

## Claim scope

Claim Value Set consolidation candidates.

## Claim

the Evaluation **must** report **`=1`** Claim Value Set consolidation candidate **only** **if** **every** contributing active Atom has the same Atom Scope, Atom Governed Subject, Claim Target Scope Unit, textual Claim Scope, Property, **and** exact qualifiers, has **`=1`** mechanically parseable single-value Claim, **and** differs **only** by **`=1`** unique value proven through IS_ALLOWED_VALUE_OF for that Property; it **must not** mutate, merge, archive, replace, compile, **or** change a Source Atom by another operation, use semantic **or** LLM inference, **or** cause Applicable Methodology compilation **to** fail.
