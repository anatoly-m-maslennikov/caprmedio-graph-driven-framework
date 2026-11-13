---
atom_id: CA-D-704
ref_id: CA-D-704
container:
  scope_unit: CA-SU-21
role: Delivery
form: Solution
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication
tier: 3
relations:
  delivery_for:
  - CA-R-3013
  - CA-M-506
  - CA-R-1116
  - CA-R-1117
  - CA-R-1119
status: active
version: 6
updated_at: '2026-11-12T12:32:31.781804+00:00'
carrier_destination:
  file:
    name: CA-D-704-MCP-SOLUTION--carry-code-owned-mcp-registration-in-the-installed-package.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/07_delivery
current_scope_unit: MCP
author: Anatoly Maslennikov
---
## Summary

Carry code-owned MCP registration in the installed package

## Claim

### Prose Claim

The MCP package carries tool_providers.json as its code-owned provider inventory, generate_tool_registry.py as generator, and tool_registry.json as generated runtime registration asset in FEATURE_MCP. The generator accepts --package-root, reads inventory and installed provider code, and never reads Project Atom carriers or executes a capability; equivalent installed inputs produce equivalent bytes using canonical descriptors, models, and adapters.

In refresh mode, generate the asset in the staged package before final inventory verification and image build. In existing mode, copy the checkout asset unchanged. Include its bytes in the package and image identities. A missing asset or failed refresh stops delivery before startup. Direct source development uses the same asset/generator. Do not add a daemon, watcher, Workflow scheduler, or Atom fallback.

Inventory carries provider keys, implementation/factory symbols, descriptor factories, and explicit global mcp_blacklist; generated data carries resolved provider/Tool registration and exclusions. Keep these as configuration files, not a fixed Python Tool-name list. The installed adapter distribution keeps its version-bound interface declaration at the existing MCP Delivery location; use canonical descriptor/model symbols, preserve protocol revision/capability/result meanings, and keep declarations, schemas, and examples credential-free. Registration/schema generation grants no effect permission.

The version-bound interface declaration carries the supported protocol revision and capabilities, admitted progress/cancellation/correlation/resource-bound fields, and existing result meanings. Derive its descriptor schema only from installed canonical model symbols; accept no caller-supplied descriptor schema. Registration, schema derivation, projection and refresh never invoke a capability, start a Workflow or infer approval. Keep declarations, schemas and examples credential-free.
