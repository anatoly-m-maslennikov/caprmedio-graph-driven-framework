---
atom_id: CA-A-1255
ref_id: CA-A-1255
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Formal Model
tier: 3
status: Done
version: 3
updated_at: 2026-11-02 15:49:28 +0400
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Distinguish Prompt and Module execution

## Decision

Implementation > Package > Prompt. A Prompt is executable instructions for an LLM AI Agent engine. A Module is executable by its language engine, through compilation or interpretation as applicable. Prompt and Module are logical Implementation parts; their File or other Carriers are representations, not execution engines. Asset covers non-executable Implementation content; Prompt is not classified as Asset merely because its stored text file is not executable by the operating system. This refines the previous instructional-purpose definition without introducing another Runtime kind or Relation Type.

## State

Updates review Drafts only. Current sources, code and runtime remain unchanged.
