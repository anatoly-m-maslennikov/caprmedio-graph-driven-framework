---
atom_id: CA-A-1220@2
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 2
updated_at: 2026-10-27 18:12:00 +0400
relations: {}
tier: 3
---
# Summary

Define Project as a whole entity

## Question

What does Project name in the primary Subject structure?

## Proposal

Project means the whole project as one entity, distinct from any particular part such as an Atom or Implementation.

This Subject supports claims about the project as a whole. Its parts retain their own Subjects. Project Model groups the vocabulary for Project and its parts; it does not replace the Project entity.

## Decision

Operator: “Project is an entity. We have something about the whole project, not it's parts (atoms, implementation, etc)”.

This resolves C10-I02 through the Operator's own definition. The review's C10-F02 suggestion to define Project primarily as an undertaking is superseded, not adopted as written. The alternative aggregate-of-work-and-material wording is also not the accepted definition.

## Content Scope

Project as a primary Subject in Candidate #10. No instances, property inventory, work lifecycle, graph machinery, source promotion or migration.

## Proposed specification changes

R2220@1-draft defines Project as the whole project entity. Candidate #10 reflects that proposed definition. R2220 remains Draft; no Current RMED is promoted.

## References

- [Candidate #10](CA-A-1218-SPECIFICATION_PROPOSAL--subject-model-candidate-10.md).
- [Resolve review findings](../03_plan/done/CA-P-2673-EPIC--subject-refinement-stage-3/done/04-CA-P-2677-TASK--resolve-candidate-10-review-findings.md).
- [FPF review](../../fpf-reports/20261027T134959Z-fpf-design-challenge-subject-model-candidate-10-review.md).
