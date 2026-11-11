---
atom_id: CA-A-1295@2
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Model::CAPRMEDIO::Graph Syntax
version: 2
relations: {}
tier: 3
updated_at: 2026-10-29 21:51:04 +0400
---
# Summary

Introduce functions only for reusable patterns that reduce complexity

## Decision

Use prose when a case does not justify additional formal machinery. Introduce a function only after real recurring patterns establish a reusable operation and its reuse reduces overall complexity.

Do not introduce a new function or helper for each case or instance. More formal spelling alone is not a reason to add an API, lookup operation, parameter set or evaluation rule. Existing speculative function examples remain separate proposals; their appearance in a discussion does not admit them into the current Model syntax.

The Tier case in A1294 therefore uses a simple integer lower bound and prose. This does not remove the already chosen bracketed value-constraint context or ordinary graph links; it adds no runtime function.

## State

This authoring decision is recorded and reflected in the prepared syntax-authoring Method. Existing function proposals remain deferred. No Core source promotion, implementation or runtime change occurs.
