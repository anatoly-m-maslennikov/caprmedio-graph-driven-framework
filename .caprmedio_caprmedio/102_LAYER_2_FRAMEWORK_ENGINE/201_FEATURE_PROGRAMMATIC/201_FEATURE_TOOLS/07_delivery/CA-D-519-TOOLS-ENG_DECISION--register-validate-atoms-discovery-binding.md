---
atom_id: CA-D-519
content_role: Delivery
current_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 14
updated_at: 2026-10-27 19:59:26 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
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
