---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Isolated Python Execution
  depends_on:
  - Subject/Engineering/Python Environment Frontend
version: 12
updated_at: 2026-10-22 16:26:49 +0000
relations:
  evaluation_for:
  - CA-M-429
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-378@12
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Archived
author: Anatoly Maslennikov
---
# Run an installed Tool without uv

## Claim checked

one installed CAPRMEDIO Tool executes from `.caprmedio_runtime/tools` **without** uv, a
project virtual environment, **or** another dependency outside the selected
runtime release.

## Test case

invoke one installed Tool **in** a clean process **where** uv **and** the project virtual
environment are unavailable.

## Acceptance criteria

pass **only** **when** the Tool reaches its declared entry boundary using solely its
installed carrier **and** admitted host prerequisites.

## Failure disposition

reject the installed-runtime claim **until** the external workflow dependency is
removed.

## Sources

- [CA-M-429 — Use uv as the default Python workflow frontend](../05_method/CA-M-429-PROGRAMMATIC-STANDARD-IMPLEMENTATION_DECISION--use-uv-as-the-default-python-workflow-frontend.md)
