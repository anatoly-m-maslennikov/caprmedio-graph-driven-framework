---
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - Subject/Domain/Node/Continuant/Selection//Methodology Sources
version: 9
updated_at: 2026-10-24 01:37:42 +0400
relations:
  relates_to:
  - CA-R-1515
  - CA-R-1516
  - CA-R-1518
atom_id: CA-R-1517
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
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
