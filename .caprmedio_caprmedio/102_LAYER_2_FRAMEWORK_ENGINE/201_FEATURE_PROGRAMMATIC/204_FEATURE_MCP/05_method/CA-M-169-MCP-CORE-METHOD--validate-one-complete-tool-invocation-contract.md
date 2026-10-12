---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 7
updated_at: 2026-10-11 01:09:00 +0400
relations:
  method_for:
    - CA-R-1107
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Validate one complete Tool invocation contract

## Applicable when

Apply **before** MCP exposes one Tool descriptor.

## Procedure

1. Call the Tool's canonical `describe_tool()` implementation and validate it against `CA-D-621-TOOLS-DELIVERY--encode-uniform-tool-self-description`.
2. Resolve model symbols and the provider adapter only from trusted installed Engine code; derive schemas from the canonical models and validate every descriptor field against the same Tool identity.
3. Reject a handwritten duplicate schema, missing field, conflicting field, ambiguous binding, or unresolved callable entrypoint; return field-level diagnostics without repairing, reinterpreting, importing untrusted code, or invoking the Tool.

## Outcome

One complete canonical descriptor is eligible for MCP projection, or that descriptor is quarantined as unavailable.

## Failure or stop

Stop exposure of **that** descriptor **when** **any** contract field is missing, conflicting, ambiguous, handwritten as a second schema, or unresolved.
