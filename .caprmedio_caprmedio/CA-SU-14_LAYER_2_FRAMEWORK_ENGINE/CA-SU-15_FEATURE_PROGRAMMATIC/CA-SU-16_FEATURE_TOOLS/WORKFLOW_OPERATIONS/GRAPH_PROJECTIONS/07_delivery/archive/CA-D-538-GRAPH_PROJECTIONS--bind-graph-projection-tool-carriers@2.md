---
atom_id: CA-D-538
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 19:23:34 +0400"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/Carrier"
  depends_on: [Tool, Projection, Artifact]
relations:
  delivery_for: [CA-R-1835, CA-R-1836, CA-R-1837]
---
# Summary

Bind graph projection Tool carriers

## Scope

The declared existing Tool entrypoint and RMED packet for the two graph builders.

## Claim

The bounded packet **must** keep `GENERATE_ENTITY_GRAPH` as the single declared Tool carrier while exposing separate Entities and Terms graph namespaces.

## Details

```toml
[tool_binding]
name = "GENERATE_ENTITY_GRAPH"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/generate_entity_graph.py"
mcp_name = "generate_entity_graph"
graph_kinds = ["entities", "terms"]
```

The `mcp_name` above is a declared Tool binding, not evidence that that name is registered, exposed or admitted by a connected server. The existing selected Workflow entrypoints are `build_entities_graph` for CA-O-133/CA-O-135/CA-O-134 and `build_terms_graph` for CA-O-136/CA-O-138/CA-O-137. Their executable request schemas and exact source bindings come from current admitted discovery/context and the canonical selected manifest. A declared carrier, available source file or listed public route name alone does not establish executable admission; an unavailable binding remains unavailable rather than inviting a guessed call or another graph engine.

Both Workflows reuse this single Tool implementation and the CA-D-539 boundary; this carrier does not register a duplicate MCP gateway or prescribe new request/context grammar. Any admitted derived fact context remains source-bound input, not a new source authority. Implementation remains gated on independent corrected RMED review under CA-D-540.
