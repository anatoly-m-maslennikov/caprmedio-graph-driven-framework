---
atom_id: CA-D-621@6
content_role: Delivery
current_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 00:51:05 +0400
subjects:
  governs: Subject/Engineering/Carrier
  depends_on:
  - Subject/Engineering/Tool.Self Description
  - Model
  - Subject/Engineering/Tool Discovery Binding
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Admission
  - Subject/Engineering/Carrier
relations:
  delivery_for:
  - CA-R-1930
type: Eng Decision
tier: 3
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
- `source_pins` contains `delivery_atom_id` and `action_ids`, matching the admitted binding exactly. Consumers retain the observed Delivery source locator and digest in the generated projection. The canonical Tool invocation enforces its Action revision pins; the self-description does not repeat unverified revision metadata.
- `admission` contains the validator's stable `module` locator, `symbol`, and Boolean `refresh_after_success` flag.
- `diagnostics` and `failure_contract` preserve canonical model-readable outcomes.

Missing, unknown, stale, conflicting, untrusted, or noncanonical fields make only that Tool descriptor unavailable with an attributable diagnostic. Description, import, schema derivation, validation, and projection never invoke the Tool or cause an effect.
