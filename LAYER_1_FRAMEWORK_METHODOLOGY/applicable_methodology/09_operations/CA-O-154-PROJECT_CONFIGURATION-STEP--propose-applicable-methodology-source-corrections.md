---
atom_id: CA-O-154
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 7
updated_at: "2026-10-19 15:56:34 +0400"
subjects:
  governs: "Applicable Methodology Compilation Propose Step"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Occurrent/Execution/Workflow Run", "Entity/Node/Continuant/Projection/Type: Applicable Methodology", "Propose Source Corrections", "Methodology Source", "Entity/Node/Continuant/Atom.Substance", "Extension", "Project Configuration", "Core Meta-Model", "Methodology Source.Expansion Boundary"]
relations:
  relates_to: [CA-O-011, CA-O-006]
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-011-PROJECT_CONFIGURATION-WORKFLOW--bind-source-reconciliation-to-applicable-methodology/CA-O-154-PROJECT_CONFIGURATION-STEP--propose-applicable-methodology-source-corrections.md
  source_atom_id: CA-O-154
  source_atom_revision: 7
  source_sha256: 3e860d752751a5d965f47718b5d32dc339d4297de7d5fb0fc44cc1523b0e0b7c
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
