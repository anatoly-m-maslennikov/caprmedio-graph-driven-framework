---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 6
updated_at: "2026-10-11 01:09:00 +0400"
relations:
  evaluation_for:
    - CA-M-169
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject one incomplete Tool invocation contract

## Claim checked

MCP exposes **only** a complete coherent canonical descriptor with `schema_version: 1`.

## Test case

Validate one Tool descriptor missing a required CA-D-621 field beside one complete Tool descriptor. Repeat with a handwritten duplicate input schema, an unresolved callable entrypoint, and a missing Action binding.

## Acceptance criteria

The defective Tool returns a field-level unavailable diagnostic and produces no eligible projection. The independent complete Tool remains eligible. The harness proves models are imported from canonical symbols and that validation never invokes or applies either Tool.

## Failure disposition

Stop exposure of the affected descriptor **until** its contract is complete, canonical-model-derived, **and** unambiguous.
