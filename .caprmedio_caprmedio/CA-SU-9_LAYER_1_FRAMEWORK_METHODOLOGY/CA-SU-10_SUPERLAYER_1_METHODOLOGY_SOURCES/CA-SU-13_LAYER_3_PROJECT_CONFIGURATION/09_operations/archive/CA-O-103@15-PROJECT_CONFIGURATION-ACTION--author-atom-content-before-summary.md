---
atom_id: CA-O-103@15
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action//Atom Content Authoring'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Domain/Continuant/Atom.Details
  - Subject/Graph Node/Domain/Continuant/Atom.Summary
  - Subject/Graph Node/Domain/Continuant/Atom/Content Role
relations:
  depends_on:
  - CA-D-479
  - CA-R-1464
version: 15
updated_at: 2026-10-26 05:59:45 +0400
tier: 3
---
# Summary

Author Atom content before Summary

## Operation

Atom Content Authoring **means** the Action that takes an authorized authoring request, the Atom's Content Role, applicable authority, **and** **any** existing Revision, then prepares a coherent candidate through this flow:

1. for RMED, write Scope describing applicability, **then** write **=1** Claim within that Scope. for other Content Roles, write their primary contribution: Question, Concern, Objective, **or** Operation.
2. write the remaining body sections under CA-D-479 **and** the applicable Method. keep Details within the primary contribution **and** its applicability; RMED Details support the Claim **without** changing Claim **or** Scope.
3. review the primary contribution **and** its applicability against the completed remaining content. for RMED, review Scope **and** Claim together. **if** either needs changing, revise it explicitly within the authorized request **and** recheck the affected sections; never let Details silently change the contribution **or** applicability.
4. derive Summary from the finalized primary contribution within its applicability **only after** that review. for RMED, summarize the Claim within Scope, **not** Scope alone. for an existing Atom identity, compare the needed Summary with its established value; **if** a change is needed, return replacement required under CA-R-1464 rather than mutating that identity.
5. return the candidate, its review findings, **and** ready, replacement required, **or** blocked outcome. unresolved inconsistency **or** unmet permission **or** confidence gates returns blocked, **not** a ready candidate.

## Details

this Action prepares content; it does **not** persist, promote, replace, **or** archive an Atom. Carrier display order remains Summary first even though Summary is authored last. an Analysis TLDR is part of the other Markdown written **before** the primary-contribution review; it does **not** become the Atom Summary source.
