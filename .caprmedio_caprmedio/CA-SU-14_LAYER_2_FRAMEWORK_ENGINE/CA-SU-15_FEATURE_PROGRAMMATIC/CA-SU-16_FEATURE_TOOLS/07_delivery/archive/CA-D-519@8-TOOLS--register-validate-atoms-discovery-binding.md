---
atom_id: CA-D-519@8
content_role: Delivery
current_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-24 01:18:03 +0400
subjects:
  governs: Subject/Engineering/Tool Discovery Binding/Atom Validator
  depends_on:
  - Subject/Engineering/Tool Discovery Binding
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  relates_to:
  - CA-O-087
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
