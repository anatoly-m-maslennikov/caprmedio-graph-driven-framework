---
atom_id: CA-A-1227
ref_id: CA-A-1227
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Subject
tier: 3
status: Done
version: 4
updated_at: 2026-11-02 15:49:28 +0400
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
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

[Rebuilt main Subject view](../../_projection/CA-PROJ-009-CAPRMEDIO--Subject-Graph--Current-RMEDO.md).
