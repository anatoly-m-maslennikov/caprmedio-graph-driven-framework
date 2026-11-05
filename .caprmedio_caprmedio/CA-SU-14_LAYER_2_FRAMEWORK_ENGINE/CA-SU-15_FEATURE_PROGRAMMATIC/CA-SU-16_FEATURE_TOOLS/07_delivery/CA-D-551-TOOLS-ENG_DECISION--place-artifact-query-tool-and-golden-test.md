---
atom_id: CA-D-551
ref_id: CA-D-551
role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 15
updated_at: 2026-11-02 19:46:47 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval
relations:
  delivery_for:
  - CA-R-1849
  - CA-R-1850
  - CA-M-330
  - CA-E-569
form: Eng Decision
tier: 5
container:
  scope_unit: CA-SU-16
carrier_destination:
  file:
    name: CA-D-551-TOOLS-ENG_DECISION--place-artifact-query-tool-and-golden-test.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/07_delivery
---
# Summary

Place Artifact query Tool and golden test

## Scope

Delivery placement only; no implementation or registration is performed by
this Atom.

## Claim

FIND_AND_FETCH_ARTIFACTS **must** be delivered at
`LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/FIND_AND_FETCH_ARTIFACTS/`
with its golden test at
`LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/FIND_AND_FETCH_ARTIFACTS/tests/test_find_and_fetch_artifacts.py`,
and must not create route-local Run or Journal storage.

## Details

The delivery implements CA-O-158 through CA-O-160 and CA-R-1849, CA-R-1850,
CA-M-330, and CA-E-569. It remains read-only and has no source relocation,
Projection result carrier, credentials/secrets reader, or independent Journal.
The pure native Tool has no persistent Journal access. An actual admitted
selected Action/Workflow uses the configured canonical
`.caprmedio_<project name>/_journal/` root through CA-D-527 to CA-D-529; the
known physical carrier migration remains permission-blocked and this Delivery
does not bypass it.

```toml
[tool_binding]
name = "FIND_AND_FETCH_ARTIFACTS"
entrypoint = "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/FIND_AND_FETCH_ARTIFACTS/find_and_fetch_artifacts.py"
action_ids = ["CA-O-159"]
workflow_ids = ["CA-O-158"]
mcp_name = "find_and_fetch_artifacts"
```

This discovery binding identifies the existing read-only Tool and its existing
MCP route; it neither registers that route nor creates a Workflow, Action,
Run, or Journal.
