---
subjects:
  governs: Apply Structural Change
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Project.Structure
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Engineering/Carrier
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement/Type: Goal'
  - Subject/Domain/Node/Continuant/History/Journal
version: 10
updated_at: 2026-10-23 03:14:50 +0400
relations: {}
atom_id: CA-O-014@10
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
status: Archived
author: Anatoly Maslennikov
type: Action
global_tier: 11
---
# Summary

Apply structural change

## Operation

Apply Structural Change **means** the Action that rechecks the authorized proposal against the unchanged selected source state **and** applies its accepted declarations, reference repairs, **and** explicitly included Carrier changes through one recoverable cutover. **if** the source state differs, required validation fails, **or** permission no longer covers the effects, it **must** stop **before** mutation. **if** a partial failure occurs, it **must** report the actual effects **and** use **only** the authorized recovery boundary; it **must not** delete unapproved contents, overwrite concurrent edits, reset the retry budget, **or** claim a completed migration. event evidence follows the applicable Journal model, **not** a second structural authority.

## Details
