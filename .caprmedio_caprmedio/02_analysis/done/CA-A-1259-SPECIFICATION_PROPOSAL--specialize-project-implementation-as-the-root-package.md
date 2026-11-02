---
atom_id: CA-A-1259
content_role: Analysis & Advisory
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
subjects:
  governs: Formal Model
version: 3
updated_at: 2026-11-02 15:49:28 +0400
relations: {}
tier: 3
---
# Summary

Specialize Project Implementation as the root Package

## Decision

Implementation is a section heading, not a separate primary kind. Package/Project Implementation is specialization: Project Implementation is the root Package. Project Implementation >@(Package); Package >@(Package), >Module, >Asset and >Prompt. Module contains Code Unit, specialized as Class and Function. The root Package has no enclosing Package; each non-root Package has one immediate Package parent. The previous Implementation > Package wrapper is superseded. Existing Documentation and Resources kinds are retained separately as awaiting placement; no unapproved Package/Asset classification is inferred for them.

## State

Refine proposal and Definition Drafts only. Current source migration remains separate.
