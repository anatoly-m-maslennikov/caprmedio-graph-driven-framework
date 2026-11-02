---
atom_id: CA-D-041
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "scope-topology"
  depends_on: []
version: 11
updated_at: "2026-10-10 23:57:23 +0400"
relations:
  delivery_for:
    - CA-R-862
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Bind ATOM_UPDATE Delivery place

## Scope

This Delivery carrier binds the established `ATOM_UPDATE` authority and Delivery locations under the declared owner Scope Unit `TOOLS`. `ATOM_UPDATE` is an artifact collection below `TOOLS`, not an independently registered Scope Unit. The binding covers the existing wrapper location and its ordinary file-operation contract; it does not relocate sources, create a second Tool location, or establish an MCP capability.

## Claim

relative **to** parent Scope Unit `TOOLS`, `ATOM_UPDATE` uses authority-relative path `ATOM_UPDATE` **and** Delivery-relative path `ATOM_UPDATE`.

The `ATOM_UPDATE` Tool **must** remain bound to those authority-relative and Delivery-relative paths under `TOOLS`, with its canonical executable Carrier at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_UPDATE/atom_update.py`. The binding preserves the existing parent topology and filename identity. It does not make the `ATOM_UPDATE` folder a Scope Unit, replace the declared `TOOLS` owner, or authorize source repair, Subject migration, graph publication, or live execution.

## Details

- The authoritative carrier is the exact repository-relative file `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_UPDATE/atom_update.py`; its Delivery location remains `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_UPDATE/`.
- The carrier is delivered as part of `TOOLS`; no alternate install root, independent folder registration, or copied authority is admitted by this binding.
- CA-D-425 defines the delivered Update interface. This carrier only binds its location and preserves the existing `--repository` wrapper entrypoint and generic sealed-update boundary.
- A path, owner, or filename disagreement is a delivery finding and must stop consumption until the exact current source is re-pinned. No source bytes, Core Subjects, Projection, runtime, history, or Journal state are changed by this Delivery carrier.
