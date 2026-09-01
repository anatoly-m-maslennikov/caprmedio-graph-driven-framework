---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - feature-boundary
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-1102
  derived_from:
    - CA-A-058
---
# Register the CODEX_PLUGIN unit

## Applicable when

Use this Method when adding the Codex-specific plugin boundary under AGENT_HOST_PLUGINS.

## Procedure

1. Register CODEX_PLUGIN as one immediate child Scope Unit of AGENT_HOST_PLUGINS with its stable address, scope token, source path, and structural level.
2. Place only Codex package metadata, supported host wiring, and Codex-specific adapters inside the unit.
3. Reference GRAPH_APP, Skills, and provider-neutral MCP behavior from their owning Scope Units instead of copying them.
4. Rebuild the Project Scope Unit Graph and verify the immediate typed ownership edge from AGENT_HOST_PLUGINS to CODEX_PLUGIN.

## Outcome

The Codex integration has one explicit host-specific structural owner without duplicated provider-neutral behavior.

## Failure or stop

Stop on a duplicate CODEX_PLUGIN unit, an invalid address or source path, a non-immediate parent, or copied authority from another Scope Unit.
