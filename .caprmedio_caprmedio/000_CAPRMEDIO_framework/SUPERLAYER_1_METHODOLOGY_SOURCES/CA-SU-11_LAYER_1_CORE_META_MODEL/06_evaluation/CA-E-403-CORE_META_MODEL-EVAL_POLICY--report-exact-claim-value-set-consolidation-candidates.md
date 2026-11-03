---
subjects:
  active: Atom.Content
  passive:
  - Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - Entity/Object/Continuant/Governing Objects/Atom.Subjects.Governs
  - Term//Property
  - CFEL<+Operator//AllowedValue
version: 36
updated_at: 2026-11-02 08:06:47 +0400
relations:
  evaluation_for:
  - CA-R-1358
  - CA-R-1359
atom_id: CA-E-403
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Evaluation
form: Eval Policy
---
## Summary

Report Exact Claim Value-Set Consolidation Candidates

## Claim scope

Claim Value Set consolidation candidates.

## Claim

the Evaluation **must** report **`=1`** Claim Value Set consolidation candidate **only** **if** **every** contributing active Atom has the same Atom Scope, Atom Governed Subject, Claim Target Scope Unit, textual Claim Scope, Property, **and** exact qualifiers, has **`=1`** mechanically parseable single-value Claim, **and** differs **only** by **`=1`** unique value proven as allowed by the `:` qualification for that Property; it **must not** mutate, merge, archive, replace, compile, **or** change a Source Atom by another operation, use semantic **or** LLM inference, **or** cause Applicable Methodology compilation **to** fail.
