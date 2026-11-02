---
subjects:
  governs: Subject/Graph Rule/CCE Role Profile
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement'
  - Subject/Graph Node/Engineering/CCE Operator
  - Subject/Graph Node/Domain/Continuant/Atom.Content
version: 18
updated_at: 2026-10-26 05:59:45 +0400
relations:
  child_of:
  - CA-M-307
atom_id: CA-M-310@18
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 6
type: Implementation Method
---
# Summary

Write Requirement Claims with the Requirement CCE Profile

## Scope

Requirement Claims with the Requirement CCE Role Profile.

## Claim

**to** write a Requirement Claim with the Requirement CCE Role Profile, the Author **must** perform **all** of:

1. state the primary contribution as one Entity model **or** required result by its meaning **and** value under CA-R-1339. express required properties **and** observable boundaries within that model **or** result; an obligation, permission, **or** prohibition alone does **not** select Requirement.
2. use **must**, **must not**, **may**, **only**, quantification, predicates, comparisons, **and** explicit conditions as applicable **to** state what is required, permitted, prohibited, **or** bounded.
3. use **means** **only** **when** the Claim defines the governed Requirement subject rather than merely describing it.
4. express temporal Operators **only** as observable timing boundaries **or** conditions on the required result.
5. keep procedural selection, ordered execution steps, implementation instructions, **and** reusable operational behavior outside the primary contribution. reference applicable Method **or** Operations authority rather than reproducing it.

## Details

the Requirement profile governs the required model **or** result. an observed test result remains execution evidence; it is **not** the required-result specification.
