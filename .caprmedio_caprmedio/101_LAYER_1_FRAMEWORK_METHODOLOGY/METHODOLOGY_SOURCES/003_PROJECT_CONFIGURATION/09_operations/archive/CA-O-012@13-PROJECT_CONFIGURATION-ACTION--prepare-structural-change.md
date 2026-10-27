---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action//Prepare Structural Change'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Domain/Node/Continuant/Scope Unit
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement/Type: Goal'
  - Subject/Engineering/Carrier
version: 13
updated_at: 2026-10-24 06:13:45 +0400
relations:
  relates_to:
  - CA-M-291
  - CA-R-926
atom_id: CA-O-012@13
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
type: Action
tier: 3
---
# Summary

Prepare structural change

## Operation

Prepare Structural Change **means** the Action that produces one bounded change proposal against the exact current Project Structure state. the proposal identifies the requested creation, rename, reparenting, reorder, path rebinding, removal, **or** reconciliation; its expected declarations; affected references, Goals, descendants **and** Carriers; required source changes; validation conditions; **and** a recoverable cutover boundary. a rename **or** reparenting **must** account for incoming references **and** parent-owned Goals, rather than leaving them attached **to** a different unit. declaration removal **must not** imply Carrier deletion. an undeclared folder, missing folder, **or** missing Active Goal is an observation requiring an explicit disposition, **not** permission **to** invent, erase, **or** accept authority.

## Details
