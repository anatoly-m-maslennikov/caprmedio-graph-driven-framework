---
atom_id: CA-R-1801
content_role: Requirement
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Authoring/Prompt Authoring
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Term//Property
  - Scope
  - Subject/Graph Node/Domain/Continuant/Atom.Substance
  - Subject/Graph Node/Domain/Continuant/Atom.Details
  - Subject/Graph Node/Domain/Continuant/Atom.Summary
  - Subject/Graph Rule/CCE
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Engineering/Prompt Construction/Action Instructions
relations:
  relates_to:
  - CA-E-520
  - CA-O-104
  - CA-O-105
  - CA-O-106
  - CA-O-111
tier: 3
type: Goal
---
# Summary

Provide complete local RMED review capability

## Scope

the prompt Implementation of RMED Atoms Base Revise delivered by PROMPTS.

## Claim

the prompt Implementation **must** provide complete local RMED review capability under the admitted methodology checklist **and** Action definitions, including assessment of readable content whose Carrier layout is defective.

## Details

- the supported checklist is defined by CA-E-520-CORE_META_MODEL-POLICY--check-rmed-atom-coherence; the Implementation preserves its **`=6`** local check boundaries.
- malformed headings remain Properties defects. readable applicability, contribution, supporting text, **and** Summary remain assessable using their actual source passages.
- this is implementation authority for the capability, **not** another definition of the Workflow. CA-O-104-CORE_META_MODEL-WORKFLOW--review-and-repair-a-bounded-rmed-atom-batch owns the Workflow; its referenced Actions own selection, checking, **and** correction.
- the capability preserves the admitted local-review boundary. it does **not** require cross-Atom comparison **or** an Entity-graph audit.
