---
atom_id: CA-D-551@12
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Selection
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/Tool//FIND_AND_FETCH_ARTIFACTS
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Engineering/Journal Event Query
  - Subject/Graph Node/Engineering/Artifact Query
relations:
  delivery_for:
  - CA-R-1849
  - CA-R-1850
  - CA-M-330
  - CA-E-569
type: Eng Decision
tier: 5
---
# Summary

Place Artifact query Tool and golden test

## Scope

Delivery placement only; no implementation or registration is performed by
this Atom.

## Claim

FIND_AND_FETCH_ARTIFACTS **must** be delivered at
`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_ARTIFACTS/`
with its golden test at
`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_ARTIFACTS/tests/test_find_and_fetch_artifacts.py`,
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
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_ARTIFACTS/find_and_fetch_artifacts.py"
action_ids = ["CA-O-159"]
workflow_ids = ["CA-O-158"]
mcp_name = "find_and_fetch_artifacts"
```

This discovery binding identifies the existing read-only Tool and its existing
MCP route; it neither registers that route nor creates a Workflow, Action,
Run, or Journal.
