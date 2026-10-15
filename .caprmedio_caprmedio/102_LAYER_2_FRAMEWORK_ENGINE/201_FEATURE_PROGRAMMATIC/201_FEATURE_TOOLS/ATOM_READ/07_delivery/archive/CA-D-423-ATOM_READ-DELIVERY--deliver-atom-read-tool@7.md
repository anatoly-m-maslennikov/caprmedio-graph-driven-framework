---
cce_version: cce_1
cce_form: delivery
subjects:
  governs: "Tool/ATOM_READ/Carrier"
  depends_on:
    - "Tool/ATOM_READ"
version: 7
updated_at: "2026-10-12 23:13:13 +0400"
relations: {"delivery_for":["CA-R-864"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Deliver ATOM_READ Tool

the `ATOM_READ` Tool **must** deliver its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_READ/atom_read.py`; that Carrier realizes `CA-R-864` through the Action `CA-O-047`.

## Required logical Read contract

Under CA-D-622, Read accepts one full Atom ID and explicit Version and returns the complete logical Atom state with those same identity coordinates and bound source-state evidence. Missing, ambiguous, unavailable or stale state fails explicitly; no path or filename alias replaces the logical pair. Read is independent of Find and Modify.

The existing executable location is the current file adapter binding. This required logical contract is not a claim of implementation, installation or an admitted MCP route; a replaceable backend preserves the same logical request/result boundary.
