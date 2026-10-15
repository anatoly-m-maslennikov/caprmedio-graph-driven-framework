---
atom_id: CA-O-088
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Check Atoms Step"
  depends_on:
    - "Step"
    - "Action"
    - "Check Atoms"
    - "Workflow Run"
version: 4
updated_at: "2026-10-14 13:43:13 +0400"
relations:
  relates_to:
    - CA-O-087
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-080-CORE_META_MODEL-WORKFLOW--validate-atom-carriers/CA-O-088-CORE_META_MODEL-STEP--check-selected-atoms.md
  source_atom_id: CA-O-088
  source_atom_revision: 4
  source_sha256: 174df929fbdb60ff1e802b75a69fc13b8ac77ef64db37d5b7ab5aaac3140050b
  original_relations_sha256: 94ed4306247b86e5e0ce0e5e32ec1a0ecc5092eeb2b491198ee7160e2f32e98a
---
# Summary

Check selected Atoms

## Operation

Check Atoms Step **means** the Workflow node that invokes **=1** Action, CA-O-087, with the admitted Workflow Run's source inventory, selector, applicable methodology, reference context, read boundaries, **and** execution limits.

- pass these inputs **without** independent reselection **or** inference from the Step's location.
- expose the Action's unchanged result tag **and** report payload **to** the Workflow.

## Details
