---
atom_id: CA-O-152@10
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: Applicable Methodology Compilation Select Step
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - 'Subject/Domain/Node/Continuant/Projection/Type: Applicable Methodology'
  - Select Reconciliation Sources
  - Methodology Source
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Extension
  - Project Configuration
  - Subject/Domain/Node/Continuant/Atom
relations:
  relates_to:
  - CA-O-011
  - CA-O-004
tier: 3
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
