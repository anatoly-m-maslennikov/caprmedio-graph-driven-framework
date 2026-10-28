---
atom_id: CA-A-1221
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 1
updated_at: 2026-10-27 19:24:33 +0400
relations: {}
tier: 3
---
# Summary

Retain Continuant and Occurrent Subjects

## Question

Should Continuant and Occurrent remain Subjects in the Candidate #10 Project Model?

## Proposal

Retain both as classification Subjects directly under Project Model:

- Subject/CAPRMEDIO/Graph/Node/Project Model/Continuant, defined by CA-R-1967.
- Subject/CAPRMEDIO/Graph/Node/Project Model/Occurrent, defined by CA-R-1972.

Continuants are persistent identifiable things, including artifacts. Occurrents are actual happenings, including live Workflow Runs. Their existing meanings are settled; this decision places the Subjects without redefining them. The distinction between actual occurrences and their records remains.

These are not compulsory intermediate layers for every concrete kind. The agreed direct Project Model paths for Atom, Actor, Event, Execution, Runtime and other kinds remain.

## Decision

Operator selected “Retain Continuant and Occurrent as Subjects under Project Model.” The subsequent terminology answer was “yes, and we already have it settled.” This confirms the existing distinction rather than creating another category or retiring either definition.

## Scope

Two Subject placements and their references, with source meaning preserved. No instance redesign or general content migration.

## References

- [Candidate #10](CA-A-1218-SPECIFICATION_PROPOSAL--subject-model-candidate-10.md).
- [Governs mapping Task](../03_plan/CA-P-2673-EPIC--subject-refinement-stage-3/05-CA-P-2678-TASK--map-candidate-10-governs-subjects.md).
