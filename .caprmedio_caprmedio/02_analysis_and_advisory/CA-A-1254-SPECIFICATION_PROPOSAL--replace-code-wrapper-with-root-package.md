---
atom_id: CA-A-1254
ref_id: CA-A-1254
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Formal Model
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 15:49:28 +0400
carrier_destination:
  file:
    name: CA-A-1254-CAPRMEDIO-SPECIFICATION_PROPOSAL--replace-the-code-wrapper-with-a-root-package.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Replace the Code wrapper with a root Package

## Decision

Use Implementation > Package >@(Package), Implementation > Package > Module, and Implementation > Package > Asset. Remove Code as a kind from this Draft model. Implementation contains the root Package; nested Packages have a Package parent. Every Module and Asset belongs to a Package. Code Unit remains inside Module, specialized as Class and Function. This removes the earlier direct Code-versus-Package Module alternatives. The existing Code Definition is a retirement candidate, not a Draft to promote. Documentation and Resources retain their last agreed placements until separately refined.

## State

Updates review Drafts only. Current sources, code and runtime remain unchanged.
