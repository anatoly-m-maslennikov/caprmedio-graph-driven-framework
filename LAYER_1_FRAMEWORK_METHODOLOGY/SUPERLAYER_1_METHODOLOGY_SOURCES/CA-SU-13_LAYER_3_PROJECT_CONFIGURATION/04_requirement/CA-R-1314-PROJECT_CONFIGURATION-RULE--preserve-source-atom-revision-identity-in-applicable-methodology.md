---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Projection/(.Form := Applicable Methodology)
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation//DERIVED_FROM
version: 34
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1314
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Preserve Source Atom Revision Identity in Applicable Methodology

## Claim scope

The direct source relation of each projected Applicable Methodology member.

## Claim

Applicable Methodology **must** retain each member’s **`=1`** direct DERIVED_FROM relation **to** that member’s exact source Atom Revision.
