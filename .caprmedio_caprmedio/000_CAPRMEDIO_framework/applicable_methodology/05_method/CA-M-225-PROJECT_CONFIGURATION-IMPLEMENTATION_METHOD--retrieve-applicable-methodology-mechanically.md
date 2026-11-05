---
atom_id: CA-M-225
ref_id: CA-M-225
container:
  scope_unit: CA-SU-13
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection/(.Form:=Applicable Methodology)
  dependencies:
  - CAPRMEDIO_MODEL <+ Projection/(.Form:=Applicable Methodology)
  - CAPRMEDIO_MODEL <+ Atom.Header.Topics
tier: 3
status: Active
version: 33
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-M-225-PROJECT_CONFIGURATION-IMPLEMENTATION_METHOD--retrieve-applicable-methodology-mechanically.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/05_method
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/05_method/CA-M-225-PROJECT_CONFIGURATION-IMPLEMENTATION_METHOD--retrieve-applicable-methodology-mechanically.md
  source_atom_id: CA-M-225
  source_atom_revision: 33
  source_sha256: 62fe957b5c028f1d03c337db68c1b234d8236c1abd2104ac6c7fc11971e9d4a0
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Retrieve Applicable Methodology Mechanically

## Claim

### Prose Claim


Applicable Methodology retrieval for one Subject **or** Workflow query.


**to** retrieve Applicable Methodology for one Subject **or** Workflow query, the Retriever **must** derive GOVERNS **and** DEPENDS_ON indexes on demand from projected Atom Subjects, select matching GOVERNS paths, add DEPENDS_ON authority **only** through transitive prerequisite closure, retain Applicable Methodology membership order, make no inference, **and** return no Atom **if** no matching GOVERNS path exists.
