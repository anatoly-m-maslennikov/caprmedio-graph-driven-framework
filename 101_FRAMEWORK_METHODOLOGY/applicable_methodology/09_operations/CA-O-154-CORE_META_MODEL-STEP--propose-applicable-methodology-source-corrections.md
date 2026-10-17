---
atom_id: CA-O-154
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-15 18:53:51 +0000"
subjects:
  governs: "Applicable Methodology Compilation Propose Step"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Occurrent/Execution/Workflow Run", "Entity/Continuant/Projection/Type: Applicable Methodology", "Propose Source Corrections", "Methodology Source", "Entity/Continuant/Object/Atom.Substance", "Extension", "Project Configuration", "Core Meta-Model", "Methodology Source.Expansion Boundary"]
relations:
  relates_to: [CA-O-011, CA-O-006]
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-011-CORE_META_MODEL-WORKFLOW--bind-source-reconciliation-to-applicable-methodology/CA-O-154-CORE_META_MODEL-STEP--propose-applicable-methodology-source-corrections.md
  source_atom_id: CA-O-154
  source_atom_revision: 5
  source_sha256: 082cdd8c39fc9bc6bfb4d9cb6c0879ba4f6283ba4ac3b352a346047b3be277b2
  original_relations_sha256: e461ce9c32c592c86076b731943e0b9b8cd2bacf10bc9c4c9ba0b53088f9841c
---
# Summary

Propose Applicable Methodology source corrections

## Operation

this Step is the propose node **of** CA-O-011, Applicable Methodology Compilation, invoking **`=1`** Action, CA-O-006, Propose Source Corrections.

### Inputs and parameters

bind the assessment, conflicts and exact frontier returned by CA-O-153, together with the Workflow Run's authorized correction boundaries and owning source authority.

propose needed changes **only** through the separately authorized workflow of the owning source authority. source order, Claim synthesis, Claim merge, **and** LLM inference **must not** resolve a conflict. a prohibited Extension **or** Project Configuration override **must not** become conforming **without** an authorized change **to** its governing Core authority.

### Agentic invocation binding

for an invocation whose actual bound Action is Agentic, bind **`=1`** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. retain the selected context with the Step Run. a Programmatic invocation does **not** acquire an Agent context **or** require this parameter. this binding grants no additional authority **and** does **not** change the Action's identity **or** behavior.

## Details
