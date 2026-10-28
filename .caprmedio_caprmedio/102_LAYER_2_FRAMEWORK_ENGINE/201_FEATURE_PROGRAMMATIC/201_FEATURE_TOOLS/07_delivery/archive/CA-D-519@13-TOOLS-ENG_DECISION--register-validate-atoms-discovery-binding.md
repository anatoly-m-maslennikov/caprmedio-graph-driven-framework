---
atom_id: CA-D-519@13
content_role: Delivery
current_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Architecture/Communication
  depends_on:
  - Subject/Graph Node/Engineering/Data Handling/Serialization
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations: {}
type: Eng Decision
tier: 3
---
# Summary

Register VALIDATE_ATOMS discovery binding

## Scope

the TOOLS capability for Tool/VALIDATE_ATOMS/Carrier.

## Claim

the VALIDATE_ATOMS discovery binding **must** be carried **in** the following TOML table **in** this Atom's Details.

## Details

```toml
[tool_binding]
name = "VALIDATE_ATOMS"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/validate_atoms.py"
action_ids = ["CA-O-087"]
workflow_ids = []
mcp_name = ""
```

the binding registers the existing Implementation; it does **not** claim an independent Action **or** Workflow Run engine. unavailable paths **or** bindings are explicit discovery findings.
