---
atom_id: CA-D-621
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-11 01:39:05 +0400"
subjects:
  governs: "TOOLS/uniform self-description Carrier"
  depends_on: [Tool, Model, Implementation, Action, Admission, Carrier]
relations:
  delivery_for: [CA-R-1930]
---
# Summary

Encode uniform Tool self-description

## Scope

The dictionary returned by `describe_tool()` for one Tool.

## Claim

The delivered Tool self-description **must** be one JSON dictionary with exactly `schema_version`, `identity`, `binding`, `models`, `callable`, `effect_hints`, `permissions`, `source_pins`, `admission`, `diagnostics`, and `failure_contract`.

## Details

- `schema_version` is integer `1`.
- `identity` contains `name`, `tool_version`, `title`, `description`, and `purpose`.
- `binding` contains `delivery_atom_id`, `action_ids`, and `implementation_entrypoint`.
- `models` contains `input` and `output`, each with `module` and `symbol`. `module` is a stable, installed Engine-relative source-file locator, not a temporary loader namespace. Consumers resolve the sealed source through the trusted installed-code loader and derive schemas solely from these canonical model symbols.
- `callable` contains `module` and `symbol`. Its factory creates a root-bound Tool invoker exposing `.invoke(request)` with the canonical models. This invoker carries no MCP request or response envelope. MCP names and protocol wrappers belong to the MCP projection.
- `effect_hints` contains `read_only_hint`, `destructive_hint`, `idempotent_hint`, and `open_world_hint`.
- `permissions` contains `execution`, `enforcement`, and `metadata_grants_permission`. Declared permission requirements and effect hints describe the canonical invocation boundary; they do not grant permission.
- `source_pins` identify the Delivery and bound Actions. Consumers match them to the admitted source records and retain the observed source locators and digests in the generated projection.
- `admission` contains the validator's stable `module` locator, `symbol`, and Boolean `refresh_after_success` flag.
- `diagnostics` and `failure_contract` preserve canonical model-readable outcomes.

Missing, unknown, stale, conflicting, untrusted, or noncanonical fields make only that Tool descriptor unavailable with an attributable diagnostic. Description, import, schema derivation, validation, and projection never invoke the Tool or cause an effect.
