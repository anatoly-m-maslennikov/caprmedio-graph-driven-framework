---
atom_id: CA-R-2556
ref_id: CA-R-2556
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2556-CORE_META_MODEL-RULE--state-assertions-about-the-active-subject.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2556-CORE_META_MODEL-RULE--keep-assertions-about-the-active-subject.md
  source_atom_id: CA-R-2556
  source_atom_revision: 2
  source_sha256: fffe008309148c2def5857745c9d9bfb63c4f9f84deaedb9eeb1f05c88706e68
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

State assertions about the active Subject

## Claim

### Prose Claim


- For an Atom with an active Subject, all assertions and prescriptions concern that active Subject.
- References to other Subjects describe the active Subject's endpoints, inputs, outputs, conditions or dependencies.
- Independent assertions about another Subject belong in an Atom with that active Subject.
- For an Atom whose active Subject is a Node, each Relation count constrains that active Subject's own outgoing Relations.
