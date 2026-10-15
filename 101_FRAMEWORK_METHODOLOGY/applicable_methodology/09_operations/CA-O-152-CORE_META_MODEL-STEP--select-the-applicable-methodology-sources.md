---
atom_id: CA-O-152
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-14 13:44:47 +0400"
subjects:
  governs: "Applicable Methodology Compilation/Step: select"
  depends_on:
    - "Workflow"
    - "Step"
    - "Action"
    - "Workflow Run"
    - "Applicable Methodology"
    - "Select Reconciliation Sources"
    - "Methodology Source"
    - "Scope Unit"
    - "Framework Instance Settings"
    - "Extension"
    - "Project Configuration"
    - "Atom/Revision"
relations:
  relates_to: [CA-O-011, CA-O-004]
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-011-CORE_META_MODEL-WORKFLOW--bind-source-reconciliation-to-applicable-methodology/CA-O-152-CORE_META_MODEL-STEP--select-the-applicable-methodology-sources.md
  source_atom_id: CA-O-152
  source_atom_revision: 3
  source_sha256: 1d9f1192496a2c42692ffe9d9628ac2b6b1ef4e362bde2eb2d7832694ac0f850
  original_relations_sha256: 311198b9d39fd208f3cb18f1176254443ffa87a8577be8789b9988599e51e0f9
---
# Summary

Select the Applicable Methodology sources

## Operation

this Step is the select node **of** CA-O-011, Applicable Methodology Compilation, invoking **`=1`** Action, CA-O-004, Select Reconciliation Sources.

### Inputs and parameters

bind the Workflow Run's requested Applicable Methodology construction, registered Methodology Source Scope Units, current Framework Instance Settings, and applicable source authority.

resolve the complete current source set under CA-R-1228 from registered Methodology Source Scope Units, using Framework Instance Settings for current Extension activation **and** selected Extension Revisions. include CORE_META_MODEL, PROJECT_CONFIGURATION, **and** **every** applicable installed Extension Revision. discover registered source Carriers **without** requiring particular Extension names **or** Project-specific Project Configuration Claims; an empty Extension contribution requires no empty collection Carrier. collect **`=1`** current active Revision of **every** eligible source Atom under CA-R-1315 **without** omitting previously unknown conforming contents.

### Agentic invocation binding

for an invocation whose actual bound Action is Agentic, bind **`=1`** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. retain the selected context with the Step Run. a Programmatic invocation does **not** acquire an Agent context **or** require this parameter. this binding grants no additional authority **and** does **not** change the Action's identity **or** behavior.

## Details
