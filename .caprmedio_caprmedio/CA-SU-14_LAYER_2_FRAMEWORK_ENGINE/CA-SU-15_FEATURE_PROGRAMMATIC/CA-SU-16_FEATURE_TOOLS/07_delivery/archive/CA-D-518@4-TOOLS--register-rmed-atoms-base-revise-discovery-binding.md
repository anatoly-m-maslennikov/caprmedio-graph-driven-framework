---
atom_id: CA-D-518@4
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-23 03:06:32 +0400
subjects:
  governs: Subject/Engineering/Tool Discovery Binding/RMED Atoms Base Revise
  depends_on:
  - Subject/Engineering/Tool Discovery Binding
  - Action
  - Workflow
  - Subject/Domain/Node/Continuant/Atom
  - Scope Unit
  - Implementation
  - Workflow Run
  - Journal
relations:
  relates_to: [CA-O-104]
type: Engineering Decision
---
# Summary

Register RMED_ATOMS_BASE_REVISE discovery binding

## Scope

the TOOLS capability for Tool/RMED_ATOMS_BASE_REVISE/Carrier.

## Claim

the RMED_ATOMS_BASE_REVISE discovery binding **must** be carried **in** the following TOML table **in** this Atom's Details.

## Details

```toml
[tool_binding]
name = "RMED_ATOMS_BASE_REVISE"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/RMED_ATOMS_BASE_REVISE/rmed_atoms_base_revise.py"
action_ids = ["CA-O-105", "CA-O-106", "CA-O-111"]
workflow_ids = ["CA-O-104"]
mcp_name = "rmed_atoms_base_revise"
```

the binding registers the existing Implementation; `action_ids` identify the bounded selection, evaluation, and repair Actions that it carries. `workflow_ids` retains CA-O-104 only as workflow context, not as an Action mapping or an independent Workflow Run engine. unavailable paths **or** bindings are explicit discovery findings.
