---
global_tier: 11
local_tier: Standard
claim_target_scope_unit: CONNECTOR_TOOLS
current_scope_unit: CONNECTOR_TOOLS
content_role: Delivery
atom_id: CA-D-423@10
cce_version: cce_1
cce_form: delivery
subjects:
  governs: Tool/ATOM_READ/Carrier
  depends_on:
  - Tool/ATOM_READ
version: 10
status: Archived
updated_at: 2026-10-23 23:34:06 +0400
relations:
  delivery_for:
  - CA-R-864
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
type: Eng Decision
---
# Deliver ATOM_READ Tool

the `ATOM_READ` Tool **must** deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_READ/atom_read.py`; that Carrier realizes `CA-R-864` through the Action `CA-O-047`.

## Required logical Read contract

Under CA-D-625, Read accepts one explicit full Atom ID in the source view fixed by target/context and returns the complete logical Atom state with its actual exact Version and bound source-state evidence. A pre-known Version is not required. If a Version or expected state is supplied for pinned or historical Read, verify it exactly rather than substituting another state. Missing, ambiguous, unavailable or stale bound state fails explicitly; no path or filename alias replaces logical identity. Read invokes neither Find nor Modify.

The existing executable location is the current file adapter binding. This required logical contract is not a claim of implementation, installation or an admitted MCP route; a replaceable backend preserves the same logical request/result boundary.

## Responsibility boundary

This primitive uses CA-D-625's coherent logical connector interface. The bound caller context supplies the requested scope, source view, permission and applicable validation authority; the connector checks them mechanically. It does not choose Atom identity, Version changes, lifecycle, defaults or a configuration schema.
