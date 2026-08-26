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
version: 2
updated_at: 2026-08-23 16:07:56
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

## Task Scope Resolution

- Resolved at: `2026-08-23 15:26:12 +04:00`.
- Project revision: Git revision `a3d2bcb4e37012bb8309a63741919ba8217b74e9` plus the governed working-tree carrier revisions in the CA-P-078 version 2 manifest.
- Final Validation Set: the exact 535-row Task Scope Resolution recorded by CA-P-078 version 2.
- Validation-set digest: `c26edf0200ddf5a11bdc24cc6752d6ea21a670bfda5058af8e721ee1547e308c`.

## Validation Result

PASS.

- 535 Atoms were validated.
- 472 Atoms have exactly one DECLARED Subject.
- 63 Atoms have exactly two DECLARED Subjects.
- Zero Atoms have zero DECLARED Subjects.
- 473 DECLARED Subjects are CONTINUANT.
- 125 DECLARED Subjects are OCCURRENT.
- Zero validation errors were found.
- The final validation digest is `c26edf0200ddf5a11bdc24cc6752d6ea21a670bfda5058af8e721ee1547e308c`.
