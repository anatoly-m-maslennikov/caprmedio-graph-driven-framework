---
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation).Content.Claim'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Controlled English
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
version: 24
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-M-307
  depends_on:
  - CA-M-264
atom_id: CA-M-312
ref_id: CA-M-312
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 6
role: Method
form: Eng Decision
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-M-312-CORE_META_MODEL-ENG_DECISION--write-evaluation-claims-with-the-evaluation-cce-profile.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
---
## Summary

Write Evaluation Claims with the Evaluation CCE Profile

## Claim

### Prose Claim


Evaluation Claims with the Evaluation CCE Role Profile.


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
