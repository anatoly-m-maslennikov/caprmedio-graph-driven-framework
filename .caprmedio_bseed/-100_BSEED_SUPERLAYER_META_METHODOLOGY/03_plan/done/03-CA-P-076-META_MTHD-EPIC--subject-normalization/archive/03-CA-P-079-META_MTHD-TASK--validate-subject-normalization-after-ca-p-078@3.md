---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    occurrent:
      - bseed-subject-validation
  prerequisite:
    continuant:
      - CA-P-078
version: 3
updated_at: 2026-08-23 16:16:51
autonomous_confidence_threshold: 98
---
# Validate Subject normalization after CA-P-078

WHEN CA-P-078 is Done, THE Assignee MUST validate every Atom in Task Scope against the current Subject authority.

## Scope

`(ALL Atoms WHERE (Current Scope IN (META_METHODOLOGY, METAMODEL, SEMANTICS, GOVERNANCE) AND Lifecycle State IN (active, draft)))`

## Definition of Done

THE Task is NOT DONE IF (CA-P-078 is not Done OR the final Validation Set does not equal the recorded Task Scope Resolution OR ANY Atom in the Validation Set has no nested DECLARED Subject mapping OR ANY DECLARED Temporal Form is not CONTINUANT or OCCURRENT OR ANY DECLARED Temporal Form does not contain exactly one Subject OR ANY Atom has fewer than one or more than two DECLARED Subjects OR the counts of Atoms with one and two DECLARED Subjects do not sum to the Validation Set count OR the validation digest and result are not recorded).

## Details

Validate the complete set rather than only changed Atoms. Count DECLARED Subjects independently from PREREQUISITE Subjects. Treat an Atom with one DECLARED CONTINUANT Subject and one DECLARED OCCURRENT Subject as valid.
