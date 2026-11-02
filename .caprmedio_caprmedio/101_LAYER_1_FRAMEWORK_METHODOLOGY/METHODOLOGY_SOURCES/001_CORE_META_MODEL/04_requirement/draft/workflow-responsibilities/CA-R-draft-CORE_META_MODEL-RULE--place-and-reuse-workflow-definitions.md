---
atom_id: CA-R-draft
content_role: Requirement
type: Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
tier: 2
version: 1
updated_at: 2026-10-29 19:51:23 +0400
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
relations: {}
---
## Summary

Place and Reuse Workflow Definitions

## Claim scope

Responsibility for Workflow definitions and Project Workflow composition across Scope Units.

## Claim

Place each Workflow definition in the Scope Unit responsible for its meaning. Reusable business Workflows that define what happens to Atoms, Projections, Journal and other governed Objects, including general implementation work, belong to Core Meta-model. Engine Scope Units own the technical Workflows and runtime implementation that realize those business Workflows. Project-specific orchestration, including Local Release and Public Release for this Project, belongs to the Project itself.

A Project Workflow may use a Step to call a Workflow owned by Methodology or an Engine Scope Unit with its parameters. Such a call reuses the callee's definition without copying it or changing its owner. The caller's Scope Unit does not require every called Workflow to be locally defined.

## Semantics

Business meaning is what happens to governed Objects and why an operation is complete; technical implementation is how the runtime executes it. A Workflow concerned with implementing requirements can still have reusable business meaning in Core. A concrete Workflow name alone does not make it project-specific. The exact Local/Public Release procedures for this repository are Project-specific even though they can compose reusable Methodology and Engine Workflows.

## Details

The latest Operator decision supersedes the earlier blanket proposal putting all named O definitions into Project Configuration. Core, Engine and Project are different responsibility boundaries. Their composition does not merge those boundaries or duplicate the callee's rules.

Preserve the established call distinction: a Step may call an Action or Workflow; a Sub-step calls an Action only. This rule introduces no new carrier field, Relation Type, delegation approval, or generic exemption to RMED governing-relation constraints. Runtime mechanics and reference encoding remain under their existing authority. Existing Current O/RMED sources are not moved by this Draft.
