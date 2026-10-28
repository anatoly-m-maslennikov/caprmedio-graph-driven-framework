---
atom_id: CA-A-1227@1
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 1
updated_at: 2026-10-27 22:07:44 +0400
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

## Drafts

Prepare successors to CA-R-2179 and CA-R-2180. Current definitions and the derived Subject Graph remain unchanged pending promotion.
