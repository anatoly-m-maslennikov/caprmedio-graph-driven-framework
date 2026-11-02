---
atom_id: CA-O-157@14
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
version: 14
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step//Applicable Methodology Compilation Publish Step'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Applicable Methodology'
  - Subject/Graph Node/Domain/Continuant/Scope Unit//PROJECT_CONFIGURATION
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Reconciled Projection'
relations:
  relates_to:
  - CA-O-011
  - CA-O-009
tier: 3
---
# Summary

Publish the Applicable Methodology

## Operation

this Step is the publish node **of** CA-O-011, Applicable Methodology Compilation, invoking **`=1`** Action, CA-O-009, Publish Reconciled Projection.

### Inputs and parameters

bind the final reassessed source frontier from CA-O-153, the corresponding selection from CA-O-152, required valid decisions from CA-O-155 when applicable, and the Workflow Run's selected Projection Delivery authority.

preserve **every** selected Atom ID, exact source Revision, authority owner, **and** Claim under CA-R-1314 **and** CA-R-1316; enforce CA-R-1461 **and** CA-D-305 **and** CA-D-306 source identity, exact source Carrier bytes **and** Carrier form. fail **without** changing Applicable Methodology membership **if** **any** conflict remains unresolved **or** **any** required approval is invalid. produce the same ordered Applicable Methodology membership from the same resolved source frontier.

### Agentic invocation binding

for an invocation whose actual bound Action is Agentic, bind **`=1`** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. retain the selected context with the Step Run. a Programmatic invocation does **not** acquire an Agent context **or** require this parameter. this binding grants no additional authority **and** does **not** change the Action's identity **or** behavior.

## Details
