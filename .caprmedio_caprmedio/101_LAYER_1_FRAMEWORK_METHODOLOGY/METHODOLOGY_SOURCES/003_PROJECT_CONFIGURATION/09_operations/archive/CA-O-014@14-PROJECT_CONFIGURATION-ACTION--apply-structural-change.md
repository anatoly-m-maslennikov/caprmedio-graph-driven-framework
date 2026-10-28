---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action//Apply Structural Change'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Carrier
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement/Type: Goal'
  - Subject/Graph Node/Domain/Continuant/History/Journal
version: 14
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-O-014@14
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
type: Action
tier: 3
---
# Summary

Apply structural change

## Operation

Apply Structural Change **means** the Action that rechecks the authorized proposal against the unchanged selected source state **and** applies its accepted declarations, reference repairs, **and** explicitly included Carrier changes through one recoverable cutover. **if** the source state differs, required validation fails, **or** permission no longer covers the effects, it **must** stop **before** mutation. **if** a partial failure occurs, it **must** report the actual effects **and** use **only** the authorized recovery boundary; it **must not** delete unapproved contents, overwrite concurrent edits, reset the retry budget, **or** claim a completed migration. event evidence follows the applicable Journal model, **not** a second structural authority.

## Details
