---
atom_id: CA-A-1227
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 2
updated_at: 2026-10-27 22:47:33 +0400
relations: {}
tier: 3
---
# Summary

Distinguish Prompts and Documentation by purpose

## Question

What distinguishes Prompts from Documentation when both may be read by LLMs?

## Operator decision

“prompts are runbook, how-to, instruction, mostly for LLM”

“documentation is other docs for users and LLMs about the project and the framework”

## Proposal

Prompts guide work through runbooks, how-tos and instructions, primarily for LLMs. Documentation supplies the other descriptive, explanatory and reference information about the project and framework, for users and LLMs. Purpose is the distinction; audience alone does not select the category.

## Review disposition

This resolves C10-I05 by clarifying the existing definitions. It does not require a new entity, a new Content Role, a particular filename or a separate copy of the same content. Carrier structure and classification of individual mixed-content files remain outside this decision.

## Adoption result

Current R2179@3 and R2180@3 carry the accepted purpose-based definitions. Their predecessors are archived; no category was selected merely from the reader being an LLM.

[Rebuilt main Subject view](../_projection/CA-PROJ-009-CAPRMEDIO--Subject-Graph--Current-RMEDO.md).
