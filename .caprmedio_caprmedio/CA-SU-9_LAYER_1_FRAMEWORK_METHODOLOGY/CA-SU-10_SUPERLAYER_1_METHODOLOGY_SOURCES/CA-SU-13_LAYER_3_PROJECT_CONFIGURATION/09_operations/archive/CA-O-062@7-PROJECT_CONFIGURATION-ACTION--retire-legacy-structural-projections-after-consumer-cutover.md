---
subjects:
  governs: Retire Legacy Structural Projections
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/Project.Structure
  - Project Scope Unit Graph Projection
  - Subject/Engineering/Carrier
version: 7
updated_at: 2026-10-23 03:14:50 +0400
relations:
  relates_to:
  - CA-D-453
  - CA-D-454
  - CA-R-1483
atom_id: CA-O-062@7
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
status: Archived
author: Anatoly Maslennikov
type: Action
global_tier: 11
---
# Retire legacy structural Projections after consumer cutover

Retire Legacy Structural Projections **means** the Action that retires the obsolete Project Scope Unit Graph Sources Projection **or** Project Scope Unit Graph Projection **after** validated direct-consumer cutover.

- the selected target is a legacy Projection retained under CA-D-453 **or** CA-D-454, **not** authoritative Project Structure.
- retire that target **only** **after** its direct-consumer cutover is validated; an unresolved cutover does **not** satisfy this condition.
- preserve its recorded migration disposition **and** return the actual retirement result. this Action does **not** require rebuilding **or** refreshing the obsolete Projection **or** reintroducing consumer dependence.

this Action governs the retirement job **only**; it does **not** grant new mutation authority **or** prescribe the Tool implementation that performs it.
