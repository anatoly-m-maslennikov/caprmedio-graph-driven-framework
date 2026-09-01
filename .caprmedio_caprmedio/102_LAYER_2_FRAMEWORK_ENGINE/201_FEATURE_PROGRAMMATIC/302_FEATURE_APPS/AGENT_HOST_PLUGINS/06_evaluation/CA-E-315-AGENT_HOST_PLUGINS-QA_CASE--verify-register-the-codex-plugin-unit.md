---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - feature-boundary
    occurrent:
      - evaluation
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  evaluation_for:
    - CA-M-197
---
# Verify register the codex_plugin unit

## Claim checked

CA-M-197 registers one CODEX_PLUGIN child under AGENT_HOST_PLUGINS without duplicating provider-neutral authority.

## Applicable when

Apply whenever CODEX_PLUGIN structure, package boundary, or host wiring changes.

## Test case

Build the current Scope Unit Graph and inventory every authority and source carrier inside CODEX_PLUGIN, then compare them with GRAPH_APP, SKILLS, and MCP ownership.

## Acceptance criteria

Exactly one immediate typed ownership edge connects AGENT_HOST_PLUGINS to CODEX_PLUGIN; its address and path are valid; its owned content is Codex-specific; provider-neutral behavior appears only as references to external owners.

## Failure disposition

Reject the registration and preserve the structural graph, path evidence, and each duplicated or misowned authority carrier.
