---
atom_id: CA-O-108
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
version: 20
updated_at: 2026-10-27 19:59:46 +0400
subjects:
  governs: Subject/caprmedio/Step//RMED Review Selection Step
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run.Agentic Step Execution Context
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
relations: {}
tier: 3
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-104-PROJECT_CONFIGURATION-WORKFLOW--review-and-repair-a-bounded-rmed-atom-batch/CA-O-108-PROJECT_CONFIGURATION-STEP--select-the-rmed-review-batch.md
  source_atom_id: CA-O-108
  source_atom_revision: 20
  source_sha256: 5387795744409bca5d187804f55d31e00088218451badffb400a3fddd6c3c4a8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Select the RMED review batch

## Operation

RMED Review Selection Step **means** the Workflow node invoking **`=1`** Action, CA-O-105, **in** Integrated context.

- bind the active RMED request, carried source inventory, selection data, compact `atom_local` rule pack, **and** temporary output directory.
- carry the caller's Workflow name, Run ID, full report location, **and** shared Journal reference with the selected queue, including an empty **or** blocked result.
- record the original selected queue, source observations, **and** pending work **in** **`=1`** progress list.
- pass the full selection **and** shared rules **to** the caller for dispatch **in** the check phase; native file **and** session capabilities are sufficient.

## Details

the Step selects work **without** modifying source Atoms. it does **not** load global Entity **or** relation graphs for evaluation.
