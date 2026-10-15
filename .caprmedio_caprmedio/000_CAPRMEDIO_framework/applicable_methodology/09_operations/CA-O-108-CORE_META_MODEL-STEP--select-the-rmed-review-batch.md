---
atom_id: CA-O-108
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 7
updated_at: "2026-10-14 13:44:47 +0400"
subjects:
  governs: "RMED Review Selection Step"
  depends_on:
    - "Step"
    - "Action"
    - "Step/Agentic Execution Context"
    - "Workflow Run"
    - "Step Run"
    - "Journal"
    - "Evaluation/Report"
relations: {"relates_to":["CA-O-105"]}
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-104-CORE_META_MODEL-WORKFLOW--review-and-repair-a-bounded-rmed-atom-batch/CA-O-108-CORE_META_MODEL-STEP--select-the-rmed-review-batch.md
  source_atom_id: CA-O-108
  source_atom_revision: 7
  source_sha256: 3831fb63b9b51bec003c1c16892fa31510e48654673d655a2c5adfea5a5189b2
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
