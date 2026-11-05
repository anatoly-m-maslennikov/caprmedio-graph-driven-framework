---
atom_id: CA-E-525
content_role: Evaluation
type: Eval Case
current_scope_unit: DISCOVER_TOOLS
status: Active
author: Anatoly Maslennikov
version: 10
updated_at: 2026-11-05 13:04:02 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
relations:
  depends_on:
  - CA-D-678
tier: 3
carrier_destination:
  file:
    name: CA-E-525-DISCOVER_TOOLS-EVAL_CASE--verify-discover-tools.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-3_TOOL_DISCOVER_TOOLS/06_evaluation
---
# Summary

Verify DISCOVER_TOOLS

## Scope

the DISCOVER_TOOLS capability for Tool/DISCOVER_TOOLS.

## Claim

the Evaluation **must** check the DISCOVER_TOOLS Tool against its declared result **and** Carrier contract using an end-to-end mock Project.

## Details

- exercise search, pagination, missing implementations, disabled or inactive authority, duplicate identities, malformed YAML, protected paths, and current-source refresh.
- compare complete expected results with actual results; successful counts alone do **not** establish correctness.
- invoke the real MCP transport for the exposed schema **and** result boundary.
- retain existing RMED Atoms Base Revise behavior, including its initial evidence **and** absence of a saved-output recheck.

## Root MCP catalog

Verify the release script captures the actual MCP descriptors and that empty-request `discover_tools` returns the generated catalog. Add, remove and change descriptor inputs between generations and verify the next catalog reflects the change. Each tool appears once; the existing discovery name is at root, query/Worksheet/maintenance tools are grouped correctly, and unrelated tools remain at root. Respect the actual blacklist. Missing or corrupt generated data is an explicit error. Existing explicit selector search continues to use its source-binding contract. The release hook runs after replacement/readiness and its failure prevents successful completion. No tool or Workflow is invoked to generate this metadata.

Related contracts: CA-R-2785; CA-D-678.
