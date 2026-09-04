---
atom_id: CA-P-077
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    occurrent:
      - subject-authority-establishment
version: 1
updated_at: 2026-08-23 15:30:15
autonomous_confidence_threshold: 98
---
# Establish two-axis Subject authority

THE Assignee MUST establish the two-axis Subject authority for every Atom in Task Scope.

## Scope

`(Atoms with Atom IDs in (CA-R-1012, CA-R-1013, CA-R-1014, CA-R-1015, CA-R-1084, CA-R-1085, CA-R-1086, CA-R-1087, CA-R-1088, CA-R-1089, CA-R-1090, CA-R-1091, CA-R-1092, CA-M-125, CA-M-126, CA-E-246))`

## Definition of Done

THE Task is NOT DONE IF (ANY Atom in Task Scope is absent OR ANY Subject lacks exactly one Claim Role and one Claim Participant Temporal Form OR the Claim Role values are not exactly DECLARED and PREREQUISITE OR the Claim Participant Temporal Form values are not exactly CONTINUANT and OCCURRENT OR an active or draft Atom may have zero DECLARED Subjects OR an Atom may have more than one DECLARED CONTINUANT Subject OR an Atom may have more than one DECLARED OCCURRENT Subject OR independently replaceable DECLARED Subjects of the same Temporal Form are not split across Atoms OR the governed Subject frontmatter encoding and validation case are incomplete).

## Details

The established authority permits one DECLARED CONTINUANT Subject and one DECLARED OCCURRENT Subject in the same Atom. It permits any number of PREREQUISITE Subjects in either Temporal Form. A Task dependency may therefore be a PREREQUISITE CONTINUANT Subject.

## Task Scope Resolution

THE resolved Task Scope contains exactly the 16 Atom identities listed by the Scope expression.

## Execution Result

PASS. The current BSEED authority defines both Subject axes, all four classifications, declared-Subject cardinality, same-form split behavior, frontmatter encoding, assignment and projection Methods, and the Subject Evaluation case.
