---
atom_id: CA-D-551@8
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-24 00:51:05 +0400
subjects:
  governs: FIND_AND_FETCH_ARTIFACTS
  depends_on:
  - Subject/Engineering/Tool//FIND_AND_FETCH_ARTIFACTS
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Engineering/Journal Event Query
  - Subject/Engineering/Artifact Query
relations:
  delivery_for:
  - CA-R-1849
  - CA-R-1850
  - CA-M-330
  - CA-E-569
type: Eng Decision
tier: 3
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
