---
atom_id: CA-A-1254
content_role: Analysis & Advisory
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Formal Model
version: 2
updated_at: 2026-11-02 15:49:28 +0400
relations: {}
tier: 3
---
# Summary

Replace the Code wrapper with a root Package

## Decision

Use Implementation > Package >@(Package), Implementation > Package > Module, and Implementation > Package > Asset. Remove Code as a kind from this Draft model. Implementation contains the root Package; nested Packages have a Package parent. Every Module and Asset belongs to a Package. Code Unit remains inside Module, specialized as Class and Function. This removes the earlier direct Code-versus-Package Module alternatives. The existing Code Definition is a retirement candidate, not a Draft to promote. Documentation and Resources retain their last agreed placements until separately refined.

## State

Updates review Drafts only. Current sources, code and runtime remain unchanged.
