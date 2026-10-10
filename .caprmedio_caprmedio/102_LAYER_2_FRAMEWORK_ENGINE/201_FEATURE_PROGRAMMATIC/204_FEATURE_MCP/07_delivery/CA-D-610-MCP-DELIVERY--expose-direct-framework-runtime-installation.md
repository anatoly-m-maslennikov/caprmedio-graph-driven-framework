---
atom_id: CA-D-610
content_role: Delivery
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-10 09:50:52 +0400"
subjects:
  governs: "MCP/Direct Framework runtime installation binding"
  depends_on: [MCP, Action, Operator, Framework Package, Runtime, Journal, Project]
relations:
  relates_to: [CA-O-200, CA-D-600, CA-D-601, CA-D-604, CA-D-607, CA-P-1855]
---
# Summary

Expose direct Framework runtime installation

## Scope

The direct Project MCP binding for CA-O-200, separate from selected Release promotion.

## Claim

the Project MCP **must** deliver direct Framework runtime installation through the closed, fixed-Project CA-O-200 binding below, delegating once to the reusable installer after physically reopening its existing package and Full Gate evidence.

## Details

### Binding

```toml
[tool_binding]
name = "INSTALL_FRAMEWORK_RUNTIME"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/framework_runtime_installation_mcp.py"
mcp_name = "install_framework_runtime"
action_ids = ["CA-O-200"]
```

Discovery and server registration use this exact source declaration. Missing, ambiguous or altered bindings remain unavailable; source availability alone is not executable admission.

### Input

The sole request variant has exactly `operation = "execute"`, `command_id`, `operator` and `native_packet`. The command ID and Operator use the existing direct-command validation. `native_packet` is a JSON value in the existing native Full Gate packet codec of `release_checkpoint.py`; it is documentary input, not a caller-created typed packet or a pass assertion. There is no additional authorization carrier, preview ritual or evidence grammar.

The server fixes the Project root and control child. Its current Project Settings, Project Structure and Operators Registry supply target identity and control carriers. The binding adopts that already declared Project with `mode = "adopt"`, including an empty first runtime or a quiesced replacement. Existing native context supplies its declared repository identity and root locator; without one, the established non-repository/root-name target facts apply. This binding does not create an undeclared Project.

No caller override supplies a root, identity, package, selector, generation, image, default member, raw Action ID or selected Workflow Run. A packet locator is reopened as a safe normalized Project-contained carrier, with alias and secret-path refusal before reading. The retained descriptor, package sidecar, complete package and exact constituent/aggregate receipts are physically reopened by the existing packet/package/gate readers. The original packet determines its package and aggregate receipt; it never selects the latest available evidence.

### Delegation and result

1. Resolve the fixed Project selection and the named Operator from its exact current registry.
2. Decode and physically verify the original packet using the existing closed codec and detached Full Gate verifier. Reopen package inventory/catalog and bind the target controls to that same package.
3. Construct the existing `PortableInstallationRequest` and call `install_framework_runtime` once with the explicit command ID and Operator. The installer reopens the command inputs, records the actual CA-O-200 start and owns lock, staging, quiescence, selector-last publication and terminal recording.
4. Return the actual effect outcome and its retained result/recording references. Pending terminal recording remains pending; missing bindings, stale evidence and uncertain effects never become a reported pass or automatic retry.

The admitted package supplies `defaults/runtime-config.toml`; configuration preservation and default admission remain governed by their existing contracts. This adapter neither launches a Workflow/container nor performs reload, source admission or selected CA-O-169 dispatch. Tests of adapter delegation do not assert that installation or the live release gate occurred.
