---
atom_id: CA-O-108
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 10
updated_at: "2026-10-19 13:28:30 +0400"
subjects:
  governs: "RMED Review Selection Step"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Agentic Step Execution Context", "Entity/Occurrent/Execution/Workflow Run", "Entity/Occurrent/Execution/Step Run", "Entity/Continuant/History/Journal", "Evaluation Report"]
relations: {"relates_to":["CA-O-105"]}
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-104-PROJECT_CONFIGURATION-WORKFLOW--review-and-repair-a-bounded-rmed-atom-batch/CA-O-108-PROJECT_CONFIGURATION-STEP--select-the-rmed-review-batch.md
  source_atom_id: CA-O-108
  source_atom_revision: 10
  source_sha256: 42f6271f3e36bfb8f053e1e0e7047cb122164ee5aec4577124f18556477f6408
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
