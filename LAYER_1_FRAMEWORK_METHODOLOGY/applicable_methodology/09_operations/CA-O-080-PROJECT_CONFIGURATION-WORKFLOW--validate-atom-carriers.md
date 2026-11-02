---
atom_id: CA-O-080
content_role: Operations
type: Workflow
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Atom Carrier Validation"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Relation/Type: On Result", "Check Atoms Step"]
version: 9
updated_at: "2026-10-19 15:56:49 +0400"
relations:
  relates_to:
    - CA-O-088
    - CA-R-1513
    - CA-R-1519
    - CA-R-1570
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-080-PROJECT_CONFIGURATION-WORKFLOW--validate-atom-carriers.md
  source_atom_id: CA-O-080
  source_atom_revision: 9
  source_sha256: ee021e8e71041496fdbc69309092d038a03c216a7b02e51aa88951d0160d05a3
  original_relations_sha256: f59b0957a2d6f670bd211e54ae86aee3b30520244c95f04e6fd1545abae07fe7
---
# Summary

Validate Atom Carriers

## Operation

Atom Carrier Validation **means** the reusable Workflow with the following graph; the referenced Step owns its invocation binding.

- entry **and** sole node: CA-O-088.
- terminal results end the Workflow Run **and** are **not** Steps.

| From Step | Result condition | Terminal result |
|---|---|---|
| CA-O-088 | valid | valid |
| CA-O-088 | invalid | invalid |
| CA-O-088 | incomplete | incomplete |
| CA-O-088 | error | error |

an undeclared result **or** failed Step invocation ends the Run as `error` with available partial evidence. the graph has no back edge, automatic retry, repair, **or** successor-Workflow invocation.

## Details
