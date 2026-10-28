---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation.Content.Claim'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Controlled English
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Tier
version: 19
updated_at: 2026-10-27 19:59:41 +0400
relations:
  child_of:
  - CA-M-307
  depends_on:
  - CA-M-264
atom_id: CA-M-312
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 6
type: Eng Decision
---
# Summary

Write Evaluation Claims with the Evaluation CCE Profile

## Scope

Evaluation Claims with the Evaluation CCE Role Profile.

## Claim

**to** write an Evaluation Claim with the Evaluation CCE Role Profile, the Author **must** perform **all** of:

1. state the primary contribution as one falsifiable check, acceptance criterion, **or** disposition rule against identified checked authority **and** Scope.
2. state recoverable inputs, the evaluated subject, observable evidence, **and** the condition that yields each result necessary for reproducibility under CA-M-264-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-evaluations-with-reproducible-falsification.
3. use condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators with explicit scope over the checked evidence **and** result.
4. use modality **only** to constrain correct evaluation **or** disposition. an Evaluation **must not** create the Requirement that it checks.
5. specify the checked behavior, case inputs **or** fixture, expected observations, acceptance policy, **and** result disposition required by the check. include a checking procedure **only** as subordinate Evaluation content. reusable test-construction **or** selection conventions belong **in** Method authority; executable test code belongs **in** Implementation; a separately reusable test-running Action **or** Workflow belongs **in** Operations.
6. report unresolved, unavailable, **or** contradictory evidence as its governed result rather than silently converting it **to** pass **or** fail.

## Details

classification follows the primary contribution. quality-assurance policies **and**
test cases are Evaluation contributions; product outcome policy remains Requirement
authority, **and** tool **or** technique selection remains Method authority.
apply CA-M-438 for the Evaluation's numeric Tier; do not infer that Tier from semantic role, Type, or a named tier category.
