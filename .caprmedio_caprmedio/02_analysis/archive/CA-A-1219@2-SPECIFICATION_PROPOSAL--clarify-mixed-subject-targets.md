---
atom_id: CA-A-1219@2
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

Clarify mixed Subject targets

## Question

Can the Subject graph intentionally mix actual things, descriptions and abstract topics without treating them as one uniform entity kind?

## Proposal

Yes. The mix is intended: a Subject names the thing or topic an Atom governs or depends on.

A Node identifies a thing or topic addressed by the graph. Its description and Carrier are separate. A description can itself be another Subject. Carrying a record of an occurrence does not carry the actual occurrence.

## Decision

Accepted by the Operator: “The mix is intended, and your recommendation is good.” Then: “This is why it's subject.”

This resolves C10-I01 and accepts clarification C10-F01 from the Candidate #10 FPF review. It does not introduce a new entity, force a uniform category, or approve source promotion or migration.

## Content Scope

The meaning of Node and Project Model in the primary Subject structure. No instances, property inventory, runtime implementation or additional graph machinery.

## Proposed specification changes

- R1994@11-draft clarifies Node and distinguishes a thing, its description and its Carrier.
- R2209@1-draft identifies Project Model as a vocabulary grouping rather than another copy of the represented things.
- A1218 reflects these proposed definitions. Current RMED remains unchanged; the two defining Atoms are still Drafts.

## References

- [Candidate #10](CA-A-1218-SPECIFICATION_PROPOSAL--subject-model-candidate-10.md).
- [Resolve review findings](../03_plan/done/CA-P-2673-EPIC--subject-refinement-stage-3/done/04-CA-P-2677-TASK--resolve-candidate-10-review-findings.md).
- [FPF review](../../fpf-reports/20261027T134959Z-fpf-design-challenge-subject-model-candidate-10-review.md).
