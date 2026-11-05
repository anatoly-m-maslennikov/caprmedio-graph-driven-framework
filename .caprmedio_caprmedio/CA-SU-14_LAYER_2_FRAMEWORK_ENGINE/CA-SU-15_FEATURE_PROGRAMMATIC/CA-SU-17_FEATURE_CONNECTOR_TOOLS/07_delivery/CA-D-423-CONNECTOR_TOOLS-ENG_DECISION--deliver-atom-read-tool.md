---
atom_id: CA-D-423
ref_id: CA-D-423
container:
  scope_unit: CA-SU-17
role: Delivery
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool//ATOM_READ
tier: 4
relations:
  delivery_for:
  - CA-R-864
status: Active
version: 21
updated_at: 2026-11-02 19:46:47 +0400
claim_target_scope_unit: CONNECTOR_TOOLS
current_scope_unit: CONNECTOR_TOOLS
cce_version: cce_1
cce_form: delivery
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
---
# Deliver ATOM_READ Tool

the `ATOM_READ` Tool **must** deliver its canonical executable Carrier at `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/ATOM_READ/atom_read.py`; that Carrier realizes `CA-R-864` through the Action `CA-O-047`.

## Required logical Read contract

Under CA-D-625, Read accepts one explicit full Atom ID in the source view fixed by target/context and returns the complete logical Atom state with its actual exact Version and bound source-state evidence. A pre-known Version is not required. If a Version or expected state is supplied for pinned or historical Read, verify it exactly rather than substituting another state. Missing, ambiguous, unavailable or stale bound state fails explicitly; no path or filename alias replaces logical identity. Read invokes neither Find nor Modify.

The existing executable location is the current file adapter binding. This required logical contract is not a claim of implementation, installation or an admitted MCP route; a replaceable backend preserves the same logical request/result boundary.

## Responsibility boundary

This primitive uses CA-D-625's coherent logical connector interface. The bound caller context supplies the requested scope, source view, permission and applicable validation authority; the connector checks them mechanically. It does not choose Atom identity, Version changes, lifecycle, defaults or a configuration schema.
