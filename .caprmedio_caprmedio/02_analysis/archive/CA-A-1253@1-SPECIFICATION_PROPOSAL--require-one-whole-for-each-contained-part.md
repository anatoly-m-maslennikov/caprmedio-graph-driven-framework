---
atom_id: CA-A-1253@1
content_role: Analysis
type: Specification Proposal
status: Archived
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
subjects:
  governs: Formal Model
version: 1
updated_at: 2026-10-28 20:51:13 +0400
relations: {}
tier: 3
---
# Summary

Require one whole for each contained part

## Decision

The Operator states: X > Y also means an instance of Y is part of exactly one X instance. This constrains the part-to-whole direction. It does not impose a minimum or maximum number of Y parts per X. The reference marker @ does not weaken containment.

## Open interaction

Code > Module and Package >@(Module) currently provide two permitted container kinds. One question is pending: one immediate container selected from those alternatives, or one instance of each kind. Do not invent the answer or promote conflicting containment rules.

## State

Latest cardinality decision supersedes the earlier absence of an exact upper bound. Current sources remain unchanged.
