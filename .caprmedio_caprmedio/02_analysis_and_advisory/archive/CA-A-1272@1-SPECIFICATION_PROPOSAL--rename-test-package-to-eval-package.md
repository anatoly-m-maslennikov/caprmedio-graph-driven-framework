---
atom_id: CA-A-1272@1
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Model
version: 1
updated_at: 2026-10-29 00:21:40 +0400
relations: {}
tier: 3
---
# Summary

Rename Test Package to Eval Package

## Decision

Use Eval Package instead of Test Package. An Eval Package is a Package for evaluation implementation and can contain executable Modules, executable Prompts, and their required Assets. Tests implemented as Modules are one evaluation mechanism, not the boundary of this Package kind. Prompt-based evaluations are included.

Runtime Package and Project Implementation remain unchanged. Eval Package keeps the common Package structure and can contain nested Packages and Documentation where applicable. This introduces no new Module, Prompt or Asset kind and no mandatory usage field. Files remain Carriers.

## State

The new Eval Package Definition is the promotion candidate. The old Test Package Draft remains explicitly superseded for historical links. Active prepared definitions and the proposal are aligned; Current methodology and runtime are unchanged.
