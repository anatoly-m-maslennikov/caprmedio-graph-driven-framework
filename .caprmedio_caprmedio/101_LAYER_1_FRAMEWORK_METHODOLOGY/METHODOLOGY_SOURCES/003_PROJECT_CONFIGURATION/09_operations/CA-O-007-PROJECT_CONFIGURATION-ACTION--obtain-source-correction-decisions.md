---
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit//PROJECT_CONFIGURATION
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - Subject/Domain/Node/Continuant/Term//Artifact
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Continuant/History/Journal.Record
version: 17
updated_at: 2026-10-24 01:18:03 +0400
relations: {}
atom_id: CA-O-007
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
type: Action
tier: 3
---
# Summary

Obtain source correction decisions

## Operation

Obtain Source Correction Decision **means** the reusable Action that obtains the Operator's explicit decision about an exact conflict-resolution proposal.

1. present the proposal, the conflict it addresses, **and** the selected source frontier **to** the Operator.
2. request an explicit decision. distinguish approval, rejection, requested revision, **and** absence of a decision; confidence, inferred intent, **or** an LLM judgment is **not** approval.
3. retain the actual decision with its proposal, conflict, exact source-frontier binding, **and** provenance in admitted execution evidence. attempt the Journal append as a business-provenance record; an append failure yields a `recording_error` diagnostic and does not change the decision **or** block authorization. record a missing decision as missing, **not** as an approval **or** rejection.
4. return the actual decision and its independently verified execution evidence for the applicable authorization checks. a changed proposal **or** source frontier requires the decision's applicability **to** be checked again **before** reliance.

this Action **must not** apply the correction, record approval the Operator did **not** give, **or** create a duplicate approval Atom **in** Project Configuration. the Journal append is a business-provenance obligation; it does **not** independently redefine the governing source Claims **or** serve as proof, permission, completion, **or** recovery gate.

## Details
