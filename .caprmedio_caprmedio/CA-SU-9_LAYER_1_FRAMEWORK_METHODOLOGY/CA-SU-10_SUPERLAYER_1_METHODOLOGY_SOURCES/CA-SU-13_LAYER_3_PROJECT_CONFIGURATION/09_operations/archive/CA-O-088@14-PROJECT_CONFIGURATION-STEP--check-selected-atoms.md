---
atom_id: CA-O-088@14
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step//Check Atoms Step'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action//Check Atoms'
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
version: 14
updated_at: 2026-10-25 17:32:27 +0400
relations:
  relates_to:
  - CA-O-087
tier: 3
---
# Summary

Check selected Atoms

## Operation

Check Atoms Step **means** the Workflow node that invokes **=1** Action, CA-O-087, with the admitted Workflow Run's source inventory, selector, applicable methodology, reference context, read boundaries, **and** execution limits.

- pass these inputs **without** independent reselection **or** inference from the Step's location.
- expose the Action's unchanged result tag **and** report payload **to** the Workflow.

## Details
