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
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Topics
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
---
## Summary

Retrieve Applicable Methodology Mechanically

## Claim

### Prose Claim


Applicable Methodology retrieval for one Subject **or** Workflow query.


**to** retrieve Applicable Methodology for one Subject **or** Workflow query, the Retriever **must** derive GOVERNS **and** DEPENDS_ON indexes on demand from projected Atom Subjects, select matching GOVERNS paths, add DEPENDS_ON authority **only** through transitive prerequisite closure, retain Applicable Methodology membership order, make no inference, **and** return no Atom **if** no matching GOVERNS path exists.
