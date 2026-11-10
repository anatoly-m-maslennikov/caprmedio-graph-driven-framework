---
atom_id: CA-E-525@6
content_role: Evaluation
type: Eval Case
current_scope_unit: DISCOVER_TOOLS
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Verification/Dynamic Testing
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Occurrent/Execution
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations:
  relates_to:
  - CA-R-1804
  - CA-D-512
tier: 3
---
# Summary

Verify DISCOVER_TOOLS

## Scope

the DISCOVER_TOOLS capability for Tool/DISCOVER_TOOLS.

## Claim

the Evaluation **must** check the DISCOVER_TOOLS Tool against its declared result **and** Carrier contract using an end-to-end mock Project.

## Details

- exercise search, pagination, missing implementations, disabled or inactive authority, duplicate identities, malformed YAML, protected paths, and current-source refresh.
- compare complete expected results with actual results; successful counts alone do **not** establish correctness.
- invoke the real MCP transport for the exposed schema **and** result boundary.
- retain existing RMED Atoms Base Revise behavior, including its initial evidence **and** absence of a saved-output recheck.
