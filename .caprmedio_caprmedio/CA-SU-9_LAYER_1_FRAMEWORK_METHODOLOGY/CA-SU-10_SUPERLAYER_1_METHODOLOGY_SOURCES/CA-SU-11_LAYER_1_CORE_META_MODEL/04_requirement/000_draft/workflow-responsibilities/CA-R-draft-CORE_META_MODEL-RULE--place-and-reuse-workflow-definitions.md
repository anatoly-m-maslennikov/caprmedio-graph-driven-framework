---
atom_id: CA-R-draft
role: Requirement
form: Rule
status: Draft
tier: 2
version: 1
updated_at: 2026-10-29 19:51:23 +0400
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Workflow
relations: {}
---
## Summary

Place and Reuse Workflow Definitions

## Claim scope

Responsibility for Workflow definitions and Project Workflow composition across Scope Units.

## Claim

Place each Workflow definition in the Scope Unit responsible for its meaning. Runtime Workflow and Project Workflow follow the same ownership rule; Purpose does not select the owner. Reusable business meaning, including general implementation work, belongs to Core Meta-model. Engine Scope Units own technical Workflow definitions and their runtime implementation. Project-specific orchestration, including Local Release and Public Release for this Project, belongs to the Project itself.

A Workflow with either Purpose may use a Step to call a Workflow owned by Methodology, an Engine Scope Unit or the Project with its parameters. Such a call reuses the callee's definition without copying it or changing its owner. The caller's Scope Unit does not require every called Workflow to be locally defined.

## Semantics

Runtime Workflows provide behavior through the delivered result. Project Workflows develop, validate, maintain or release that result. A general implementation procedure can therefore be a reusable Project Workflow owned by Core. The exact Local/Public Release procedures for this repository are Project-specific even though they compose reusable definitions. Both kinds share the same Steps, Substeps and Actions.

## Details

Core, Engine and Project remain different responsibility boundaries. Composition reuses definitions across those boundaries. A Step may call an Action or Workflow; a Substep calls an Action only. Runtime mechanics and reference encoding remain under their existing authority.
