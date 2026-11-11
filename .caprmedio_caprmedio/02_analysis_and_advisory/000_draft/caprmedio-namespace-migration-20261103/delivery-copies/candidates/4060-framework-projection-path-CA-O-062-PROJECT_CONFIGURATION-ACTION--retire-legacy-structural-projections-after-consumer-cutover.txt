---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection//PROJECT_SCOPE_UNIT_GRAPH
  - Subject/CAPRMEDIO/Carrier
version: 14
updated_at: 2026-11-02 19:44:26 +0400
relations:
  depends_on:
  - CA-D-453
  - CA-D-454
atom_id: CA-O-062
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
type: Action
tier: 3
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-062-PROJECT_CONFIGURATION-ACTION--retire-legacy-structural-projections-after-consumer-cutover.md
  source_atom_id: CA-O-062
  source_atom_revision: 14
  source_sha256: 7b99b7f95b9a0b614b40cf7e92154fb846ec10bf4c31792eeef8cb6961067b74
  original_relations_sha256: acc4680717f4f8a037686b6fbd15a18e497fe033dae799974be421637af48a74
---
# Retire legacy structural Projections after consumer cutover

Retire Legacy Structural Projections **means** the Action that retires the obsolete Project Scope Unit Graph Sources Projection **or** Project Scope Unit Graph Projection **after** validated direct-consumer cutover.

- the selected target is a legacy Projection retained under CA-D-453 **or** CA-D-454, **not** authoritative Project Structure.
- retire that target **only** **after** its direct-consumer cutover is validated; an unresolved cutover does **not** satisfy this condition.
- preserve its recorded migration disposition **and** return the actual retirement result. this Action does **not** require rebuilding **or** refreshing the obsolete Projection **or** reintroducing consumer dependence.

this Action governs the retirement job **only**; it does **not** grant new mutation authority **or** prescribe the Tool implementation that performs it.
