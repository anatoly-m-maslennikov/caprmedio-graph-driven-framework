---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    occurrent:
      - bseed-subject-normalization
  prerequisite:
    continuant:
      - CA-P-077
version: 3
updated_at: 2026-08-23 16:16:51
autonomous_confidence_threshold: 98
---
# Normalize current BSEED Subjects after CA-P-077

WHEN CA-P-077 is Done, THE Assignee MUST make every Atom in Task Scope comply with the current Subject authority.

## Scope

`(ALL Atoms WHERE (Current Scope IN (META_METHODOLOGY, METAMODEL, SEMANTICS, GOVERNANCE) AND Lifecycle State IN (active, draft)))`

## Definition of Done

THE Task is NOT DONE IF (CA-P-077 is not Done OR the exact Task Scope and Project revision are not recorded OR ANY Atom in Task Scope has zero DECLARED Subjects OR ANY Atom has more than one DECLARED CONTINUANT Subject OR ANY Atom has more than one DECLARED OCCURRENT Subject OR ANY DECLARED Subject lacks a CONTINUANT or OCCURRENT Temporal Form OR ANY changed Atom lacks its exact archived predecessor Revision OR ANY changed Atom fails to advance `version` and `updated_at`).

## Details

Normalize only Subject classifications and the changes required by declared-Subject cardinality. Preserve every governed Claim, Current Scope, Claim Scope, identity, Content Role, Type, Tier, relation, and CCE form unless the Subject authority requires an Atom split.
