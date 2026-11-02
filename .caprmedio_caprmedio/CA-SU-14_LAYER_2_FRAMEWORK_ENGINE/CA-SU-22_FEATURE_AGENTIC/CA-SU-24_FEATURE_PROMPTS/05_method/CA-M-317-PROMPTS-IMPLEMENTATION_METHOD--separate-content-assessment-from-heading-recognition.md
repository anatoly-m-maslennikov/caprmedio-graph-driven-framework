---
atom_id: CA-M-317
content_role: Method
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Active
author: Anatoly Maslennikov
version: 16
updated_at: 2026-10-27 19:59:42 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Prompt Authoring
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content.Scope
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Details
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
relations: {}
tier: 3
type: Implementation Method
---
# Summary

Separate content assessment from heading recognition

## Scope

authoring the content-review instructions of the RMED review prompts.

## Claim

**to** implement local content assessment, use semantic reading of the complete carried text for content judgments **and** structural parsing for Property conformance, keeping the two judgments separate.

## Details

- instructions request actual quoted passages **and** an explanation of their semantic function, including applicability, contribution, supporting detail, **or** Summary.
- a missing heading is evidence of a Carrier defect; it is **not** evidence that readable content cannot be assessed. a semantic interpretation does **not** declare a missing Property section present.
- instructions distinguish independently replaceable Claims from clauses, examples, **or** conditions of the same Claim. they preserve useful content **when** proposing a correction.
- unresolved meaning **or** genuinely unavailable evidence is stated precisely for the affected check. a generic layout failure is insufficient justification for skipping readable content.
