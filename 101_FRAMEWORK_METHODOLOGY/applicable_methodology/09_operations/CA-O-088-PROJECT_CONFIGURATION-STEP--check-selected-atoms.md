---
atom_id: CA-O-088
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Check Atoms Step"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Check Atoms", "Entity/Node/Occurrent/Execution/Workflow Run"]
version: 8
updated_at: "2026-10-19 15:56:49 +0400"
relations:
  relates_to:
    - CA-O-087
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-080-PROJECT_CONFIGURATION-WORKFLOW--validate-atom-carriers/CA-O-088-PROJECT_CONFIGURATION-STEP--check-selected-atoms.md
  source_atom_id: CA-O-088
  source_atom_revision: 8
  source_sha256: 82c5e1fa18703ab1428d5b58b086cf6b067b18b106db1120317d2b6f37ebd82f
  original_relations_sha256: 94ed4306247b86e5e0ce0e5e32ec1a0ecc5092eeb2b491198ee7160e2f32e98a
---
# Summary

Check selected Atoms

## Operation

Check Atoms Step **means** the Workflow node that invokes **=1** Action, CA-O-087, with the admitted Workflow Run's source inventory, selector, applicable methodology, reference context, read boundaries, **and** execution limits.

- pass these inputs **without** independent reselection **or** inference from the Step's location.
- expose the Action's unchanged result tag **and** report payload **to** the Workflow.

## Details
