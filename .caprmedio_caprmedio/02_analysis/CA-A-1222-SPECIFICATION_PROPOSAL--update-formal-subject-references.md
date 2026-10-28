---
atom_id: CA-A-1222
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 1
updated_at: 2026-10-27 19:45:11 +0400
relations: {}
tier: 3
---
# Summary

Update formal Subject references during migration

## Question

May the Subject migration update literal Subject references inside two formal Graph Rules?

## Proposal

Update only the literal Subject paths in CA-R-2003 claim.applies_to.node and claim.condition.other_endpoint[0], and CA-R-2149 claim.applies_to.relation_selection. Resolve them through the same accepted Subject mapping used for Subjects.

Keep the rules' conditions, allowed values and other operative data unchanged. This is not permission for a general content rewrite.

## Decision

Operator: “Yes—update those formal Subject references too.”

## Adoption

Apply these literal changes to the same next-version Drafts as their Governs and Depends On changes. Current sources remain unchanged until the batch review and adoption task.

## References

- [Candidate #10](CA-A-1218-SPECIFICATION_PROPOSAL--subject-model-candidate-10.md).
