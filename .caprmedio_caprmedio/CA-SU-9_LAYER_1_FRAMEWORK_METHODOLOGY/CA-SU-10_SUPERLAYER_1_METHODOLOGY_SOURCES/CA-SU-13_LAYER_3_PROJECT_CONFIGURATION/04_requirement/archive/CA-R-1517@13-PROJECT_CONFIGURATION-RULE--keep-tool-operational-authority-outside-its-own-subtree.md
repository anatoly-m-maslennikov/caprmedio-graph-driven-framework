---
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Tool
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
  - Subject/Graph Node/Domain/Continuant/Selection//Methodology Sources
version: 13
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
atom_id: CA-R-1517@13
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Keep Tool operational authority outside its own subtree

## Scope

Tools' implementation references to methodology Action and Workflow definitions in the caprmedio Project.

## Claim

**in** the caprmedio Project, a Tool's implementation reference **to** a methodology Action **or** Workflow definition **must not** target an O Atom owned by the Tool's Scope Unit **or** **any** descendant of that Scope Unit.

## Details

- the restriction concerns the owner of the operational definition, **not** the location of the Tool's code, prompts, **or** runtime results.
- methodology Evaluations of their own Action **and** Workflow definitions under CA-R-1518 are **not** Tool implementation references **and** are **not** prohibited by this rule.

this restriction prevents self-reference through the Tool's own subtree; it does **not** establish that **all** indirect dependency cycles are absent.
