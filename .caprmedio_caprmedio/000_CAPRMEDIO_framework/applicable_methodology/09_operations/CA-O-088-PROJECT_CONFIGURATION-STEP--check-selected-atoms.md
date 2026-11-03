---
atom_id: CA-O-088
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/caprmedio/Step//Check Atoms Step
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/caprmedio/Action//Check Atoms
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
version: 16
updated_at: 2026-10-27 19:59:45 +0400
relations: {}
tier: 3
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-080-PROJECT_CONFIGURATION-WORKFLOW--validate-atom-carriers/CA-O-088-PROJECT_CONFIGURATION-STEP--check-selected-atoms.md
  source_atom_id: CA-O-088
  source_atom_revision: 16
  source_sha256: 95e4efba9838b0f75bc01578fbb09709dce69c15f363307dbf7e6f26912e5a89
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Check selected Atoms

## Operation

Check Atoms Step **means** the Workflow node that invokes **=1** Action, CA-O-087, with the admitted Workflow Run's source inventory, selector, applicable methodology, reference context, read boundaries, **and** execution limits.

- pass these inputs **without** independent reselection **or** inference from the Step's location.
- expose the Action's unchanged result tag **and** report payload **to** the Workflow.

## Details
