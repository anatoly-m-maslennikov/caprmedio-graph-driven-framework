---
atom_id: CA-A-1253
ref_id: CA-A-1253
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Formal Model
tier: 3
status: Active
version: 3
updated_at: 2026-11-02 15:49:28 +0400
carrier_destination:
  file:
    name: CA-A-1253-CAPRMEDIO-SPECIFICATION_PROPOSAL--require-one-whole-for-each-contained-part.md
    path: .caprmedio_caprmedio/02_analysis
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Require one whole for each contained part

## Decision

The Operator states: X > Y also means an instance of Y is part of exactly one X instance. This constrains the part-to-whole direction. It does not impose a minimum or maximum number of Y parts per X. The reference marker @ does not weaken containment.

## Resolved example

CA-A-1254 removes the Code wrapper. Modules belong only to Package. The root Package belongs to Implementation; nested Packages belong to another Package. The earlier Module choice is therefore obsolete.

## State

Latest cardinality decision supersedes the earlier absence of an exact upper bound. Current sources remain unchanged.
