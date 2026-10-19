---
atom_id: "CA-O-088@draft"
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: "Draft"
subjects:
  governs: "Check Atoms Step"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Check Atoms", "Entity/Node/Occurrent/Execution/Workflow Run"]
version: 8
updated_at: "2026-10-19 11:49:24 +0000"
relations:
  relates_to:
    - CA-O-087
global_tier: 11
---
# Summary

Check selected Atoms

## Operation

Check Atoms Step **means** the Workflow node that invokes **=1** Action, CA-O-087, with the admitted Workflow Run's source inventory, selector, applicable methodology, reference context, read boundaries, **and** execution limits.

- pass these inputs **without** independent reselection **or** inference from the Step's location.
- expose the Action's unchanged result tag **and** report payload **to** the Workflow.

## Details
