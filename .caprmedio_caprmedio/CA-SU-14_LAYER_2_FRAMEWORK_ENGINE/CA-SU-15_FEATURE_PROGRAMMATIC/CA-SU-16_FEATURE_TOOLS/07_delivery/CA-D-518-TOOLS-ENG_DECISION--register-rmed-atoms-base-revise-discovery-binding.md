---
atom_id: CA-D-518
ref_id: CA-D-518
role: Delivery
current_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 16
updated_at: 2026-11-02 19:46:47 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
form: Eng Decision
tier: 3
container:
  scope_unit: CA-SU-16
carrier_destination:
  file:
    name: CA-D-518-TOOLS-ENG_DECISION--register-rmed-atoms-base-revise-discovery-binding.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/07_delivery
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
entrypoint = "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/RMED_ATOMS_BASE_REVISE/rmed_atoms_base_revise.py"
action_ids = ["CA-O-105", "CA-O-106", "CA-O-111"]
workflow_ids = ["CA-O-104"]
mcp_name = "rmed_atoms_base_revise"
```

the binding registers the existing Implementation; `action_ids` identify the bounded selection, evaluation, and repair Actions that it carries. `workflow_ids` retains CA-O-104 only as workflow context, not as an Action mapping or an independent Workflow Run engine. unavailable paths **or** bindings are explicit discovery findings.
