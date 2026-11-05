---
atom_id: CA-A-1272
ref_id: CA-A-1272
role: Analysis & Advisory
form: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
topics:
  main_subject: Model
version: 3
updated_at: 2026-11-02 15:49:28 +0400
tier: 3
container:
  scope_unit: CA-SU-00
---
# Summary

Rename Test Package to Eval Package

## Decision

Use Eval Package instead of Test Package. An Eval Package is a Package for evaluation implementation and can contain executable Modules, executable Prompts, and their required Assets. Tests implemented as Modules are one evaluation mechanism, not the boundary of this Package kind. Prompt-based evaluations are included.

Runtime Package and Project Implementation remain unchanged. Eval Package keeps the common Package structure and can contain nested Packages and Documentation where applicable. This introduces no new Module, Prompt or Asset kind and no mandatory usage field. Files remain Carriers.

## State

The new Eval Package Definition is the promotion candidate. The old Test Package Draft remains explicitly superseded for historical links. Active prepared definitions and the proposal are aligned; Current methodology and runtime are unchanged.
