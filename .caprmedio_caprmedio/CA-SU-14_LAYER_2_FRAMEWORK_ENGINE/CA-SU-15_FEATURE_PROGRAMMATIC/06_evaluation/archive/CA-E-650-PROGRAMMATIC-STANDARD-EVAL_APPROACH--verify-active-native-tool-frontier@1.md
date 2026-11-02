---
atom_id: CA-E-650
content_role: Evaluation
type: Evaluation Approach
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-21T22:49:16Z"
subjects:
  governs: 'Entity/Node/Continuant/Atom/Content Role: Evaluation'
  depends_on:
  - Entity/Node/Continuant/Implementation
  - 'Entity/Node/Continuant/Atom/Content Role: Requirement'
  - 'Entity/Node/Continuant/Atom/Content Role: Method'
  - 'Entity/Node/Continuant/Atom/Content Role: Delivery'
  - Entity/Carrier
relations:
  evaluation_for:
    - CA-M-193
---
# Summary

Verify active native Tool frontier

## Scope

The MCP or equivalent provider frontier assembled from admitted active native Tool contracts for one bound Project and runtime.

## Claim

The frontier passes only when every active native Tool is represented with a canonical structural request/result schema and the same decoded payload meaning, while inactive or blocked Tools are excluded. Transport serialization differences are allowed, except for any declared outer Project field such as project_root; no other transport-shape drift is silently introduced. Direct reads remain owned by their canonical Tool without forced workflow routing. Identical structural schemas may be unioned. A partially invalid Project Tool is quarantined and diagnosed without removing healthy Tools, and a failed replacement retains the prior valid frontier explicitly as prior, never as the current frontier.

## Details

- Build the frontier from a frozen admitted native inventory and compare names, descriptions and canonical structural schemas, including definitions and required fields; compare decoded request/result meaning rather than transport bytes.
- Verify a direct read Tool reaches its canonical owner and preserves the native request/result meaning, with only the declared outer Project field added.
- Present identical same-name schemas and verify one endpoint is possible; present conflicts or a partially invalid Project Tool and verify quarantine and attribution for that Tool while healthy frontier entries remain available.
- Verify inactive, disabled or blocked Tools do not enter the frontier or become callable through stale publication.
- If a replacement frontier is invalid, retain the previous valid frontier with an explicit prior status and do not label it current; mark construction unresolved when native source, Project binding or schema comparison is unavailable.
