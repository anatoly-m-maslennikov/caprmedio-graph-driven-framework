---
atom_id: CA-O-156
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 7
updated_at: "2026-10-19 15:56:35 +0400"
subjects:
  governs: "Applicable Methodology Compilation Correct Step"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Occurrent/Execution/Workflow Run", "Entity/Node/Continuant/Projection/Type: Applicable Methodology", "Apply Approved Source Corrections", "Entity/Node/Continuant/Actor/Type: Operator", "Entity/Node/Continuant/History/Journal.Record", "Methodology Source", "Entity/Node/Continuant/Atom.Substance"]
relations:
  relates_to: [CA-O-011, CA-O-008]
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-011-PROJECT_CONFIGURATION-WORKFLOW--bind-source-reconciliation-to-applicable-methodology/CA-O-156-PROJECT_CONFIGURATION-STEP--apply-approved-applicable-methodology-source-corrections.md
  source_atom_id: CA-O-156
  source_atom_revision: 7
  source_sha256: c4c8701c4b98651ef3d41b510878b8b8d709de472760158cdb61fc71de937b95
  original_relations_sha256: 096b0599580a28c8c6f7e0bdc2d9f2defb1fb2b6089cf791e3f3adfc1be1f947
---
# Summary

Apply approved Applicable Methodology source corrections

## Operation

this Step is the correct node **of** CA-O-011, Applicable Methodology Compilation, invoking **`=1`** Action, CA-O-008, Apply Approved Source Corrections.

### Inputs and parameters

bind the exact approved correction and recorded decision from CA-O-155, their selected frontier, and the Workflow Run's current source state and separately authorized owning-source change workflow.

require the separately authorized source change workflow; corrections are **not** compiler side effects **or** edits **to** projected Claims. **if** **any** source changes, the Workflow Run returns **to** select **and** repeats assessment against the new frontier. failure **or** partial effects never justify publishing from the earlier assessment.

### Agentic invocation binding

for an invocation whose actual bound Action is Agentic, bind **`=1`** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. retain the selected context with the Step Run. a Programmatic invocation does **not** acquire an Agent context **or** require this parameter. this binding grants no additional authority **and** does **not** change the Action's identity **or** behavior.

## Details
