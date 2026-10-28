---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Projection
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Domain/Continuant/Projection//PROJECT_SCOPE_UNIT_GRAPH
  - Subject/Graph Node/Carrier
version: 12
updated_at: 2026-10-27 06:04:45 +0400
relations:
  depends_on:
  - CA-D-453
  - CA-D-454
atom_id: CA-O-062@12
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
type: Action
tier: 3
---
# Retire legacy structural Projections after consumer cutover

Retire Legacy Structural Projections **means** the Action that retires the obsolete Project Scope Unit Graph Sources Projection **or** Project Scope Unit Graph Projection **after** validated direct-consumer cutover.

- the selected target is a legacy Projection retained under CA-D-453 **or** CA-D-454, **not** authoritative Project Structure.
- retire that target **only** **after** its direct-consumer cutover is validated; an unresolved cutover does **not** satisfy this condition.
- preserve its recorded migration disposition **and** return the actual retirement result. this Action does **not** require rebuilding **or** refreshing the obsolete Projection **or** reintroducing consumer dependence.

this Action governs the retirement job **only**; it does **not** grant new mutation authority **or** prescribe the Tool implementation that performs it.
