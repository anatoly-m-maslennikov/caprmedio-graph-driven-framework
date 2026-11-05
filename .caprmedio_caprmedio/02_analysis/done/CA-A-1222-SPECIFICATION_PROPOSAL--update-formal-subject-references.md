---
atom_id: CA-A-1222
ref_id: CA-A-1222
role: Analysis & Advisory
form: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
topics:
  main_subject: Subject
version: 3
updated_at: 2026-11-02 15:49:28 +0400
tier: 3
container:
  scope_unit: CA-SU-00
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
