---
atom_id: CA-O-157
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
version: 17
updated_at: 2026-10-27 19:59:47 +0400
subjects:
  governs: Subject/caprmedio/Step//Applicable Methodology Compilation Publish Step
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Reconciled Projection'
relations: {}
tier: 3
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-011-PROJECT_CONFIGURATION-WORKFLOW--bind-source-reconciliation-to-applicable-methodology/CA-O-157-PROJECT_CONFIGURATION-STEP--publish-the-applicable-methodology.md
  source_atom_id: CA-O-157
  source_atom_revision: 17
  source_sha256: cad08f0f89f977e66f20026d070be68980374a16bd24333bd6a601527f914c3d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
