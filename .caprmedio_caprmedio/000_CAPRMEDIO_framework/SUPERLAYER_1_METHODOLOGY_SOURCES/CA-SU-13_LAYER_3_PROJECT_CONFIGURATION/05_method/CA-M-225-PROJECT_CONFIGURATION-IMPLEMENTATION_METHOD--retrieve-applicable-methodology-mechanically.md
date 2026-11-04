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
---
## Summary

Retrieve Applicable Methodology Mechanically

## Claim

### Prose Claim


Applicable Methodology retrieval for one Subject **or** Workflow query.


**to** retrieve Applicable Methodology for one Subject **or** Workflow query, the Retriever **must** derive GOVERNS **and** DEPENDS_ON indexes on demand from projected Atom Subjects, select matching GOVERNS paths, add DEPENDS_ON authority **only** through transitive prerequisite closure, retain Applicable Methodology membership order, make no inference, **and** return no Atom **if** no matching GOVERNS path exists.
