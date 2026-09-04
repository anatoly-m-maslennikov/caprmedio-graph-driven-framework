---
atom_id: CA-P-079
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    occurrent:
      - bseed-subject-validation
  prerequisite:
    continuant:
      - CA-P-078
version: 1
updated_at: 2026-08-23 15:30:15
autonomous_confidence_threshold: 98
---
# Validate Subject normalization after CA-P-078

WHEN CA-P-078 is Done, THE Assignee MUST validate every Atom in Task Scope against the current Subject authority.

## Scope

`(ALL Atoms WHERE (Current Scope IN (META_METHODOLOGY, METAMODEL, SEMANTICS, GOVERNANCE) AND Lifecycle State IN (active, draft)))`

## Definition of Done

THE Task is NOT DONE IF (CA-P-078 is not Done OR the final Validation Set does not equal the resolved Task Scope OR ANY Atom in the Validation Set violates its required Subject encoding, classification, cardinality, reference, or Scope-separation rule OR the counts of Atoms with one and two DECLARED Subjects do not sum to the Validation Set count OR the validation digest and result are not recorded).

## Details

Validate the complete set rather than only changed Atoms. Count declared Subjects independently from prerequisite Subjects. Treat an Atom with one DECLARED CONTINUANT Subject and one DECLARED OCCURRENT Subject as valid.

## Task Scope Resolution

THE final Validation Set contains exactly 535 active or draft BSEED Atoms across META_METHODOLOGY, METAMODEL, SEMANTICS, and GOVERNANCE.

## Validation Result

PASS.

- 472 Atoms have exactly one DECLARED Subject.
- 63 Atoms have exactly two DECLARED Subjects.
- Zero Atoms have zero DECLARED Subjects.
- 473 DECLARED Subjects are CONTINUANT.
- 125 DECLARED Subjects are OCCURRENT.
- The final validation digest is `c26edf0200ddf5a11bdc24cc6752d6ea21a670bfda5058af8e721ee1547e308c`.
