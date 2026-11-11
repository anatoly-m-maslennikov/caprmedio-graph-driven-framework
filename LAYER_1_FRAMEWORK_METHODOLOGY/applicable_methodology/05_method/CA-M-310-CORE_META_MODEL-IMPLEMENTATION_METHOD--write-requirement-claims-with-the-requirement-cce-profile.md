---
atom_id: CA-M-310
ref_id: CA-M-310
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement).Content.Claim'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Controlled English"
  - CAPRMEDIO_MODEL <+ Atom.Content
tier: 6
relations:
  child_of:
  - CA-M-307
status: Active
version: 25
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-M-310-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-requirement-claims-with-the-requirement-cce-profile.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-310-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-requirement-claims-with-the-requirement-cce-profile.md
  source_atom_id: CA-M-310
  source_atom_revision: 25
  source_sha256: 242abdc59b3c9aca322792174a61f0fbbcb18327ac631f7a28ae1935e774ab76
  original_relations_sha256: 1037ec3e9bee824bbe0013d533c233bc31238f593358d3400af78e5150b7d7f4
---
## Summary

Write Requirement Claims with the Requirement CCE Profile

## Claim

### Prose Claim


Requirement Claims with the Requirement CCE Role Profile.


**to** write a Requirement Claim with the Requirement CCE Role Profile, the Author **must** perform **all** of:

1. state the primary contribution as one Entity model **or** required result by its meaning **and** value under CA-R-2512. express required properties **and** observable boundaries within that model **or** result; an obligation, permission, **or** prohibition alone does **not** select Requirement.
2. use **must**, **must not**, **may**, **only**, quantification, predicates, comparisons, **and** explicit conditions as applicable **to** state what is required, permitted, prohibited, **or** bounded.
3. use **means** **only** **when** the Claim defines the governed Requirement subject rather than merely describing it.
4. express temporal Operators **only** as observable timing boundaries **or** conditions on the required result.
5. keep procedural selection, ordered execution steps, implementation instructions, **and** reusable operational behavior outside the primary contribution. reference applicable Method **or** Operations authority rather than reproducing it.

## Details

the Requirement profile governs the required model **or** result. an observed test result remains execution evidence; it is **not** the required-result specification.
