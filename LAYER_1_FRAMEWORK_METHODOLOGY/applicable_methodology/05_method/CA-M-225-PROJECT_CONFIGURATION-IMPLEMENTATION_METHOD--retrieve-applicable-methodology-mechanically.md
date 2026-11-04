---
subjects:
  active: CAPRMEDIO_MODEL <+ Projection/(.Form:=Applicable Methodology)
  passive:
  - CAPRMEDIO_MODEL <+ Projection/(.Form:=Applicable Methodology)
  - CAPRMEDIO_MODEL <+ Atom.Header.Subjects
version: 33
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-M-225
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/05_method/CA-M-225-PROJECT_CONFIGURATION-IMPLEMENTATION_METHOD--retrieve-applicable-methodology-mechanically.md
  source_atom_id: CA-M-225
  source_atom_revision: 33
  source_sha256: 160d876d0723711813a1856cd3c6867d0eba5b5f667e35ba772577d78c226957
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Retrieve Applicable Methodology Mechanically

## Claim

### Prose Claim


Applicable Methodology retrieval for one Subject **or** Workflow query.


**to** retrieve Applicable Methodology for one Subject **or** Workflow query, the Retriever **must** derive GOVERNS **and** DEPENDS_ON indexes on demand from projected Atom Subjects, select matching GOVERNS paths, add DEPENDS_ON authority **only** through transitive prerequisite closure, retain Applicable Methodology membership order, make no inference, **and** return no Atom **if** no matching GOVERNS path exists.
