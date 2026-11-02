---
atom_id: CA-E-650@7
content_role: Evaluation
type: Policy
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-24 02:14:24 +0400
subjects:
  governs: Subject/Engineering/Callable Frontier Publication
  depends_on: []
relations:
  evaluation_for:
  - CA-M-193
tier: 5
---
# Summary

Verify active native Tool frontier

## Scope

The source-bound active declared callable CAPRMEDIO Tool and Workflow frontier governed by CA-M-193 for a bound Project and shared runtime. Internal CONNECTORS/adapters and PROJECT_TOOLS are excluded.

## Claim

The frontier passes only when every active native Tool is represented with a canonical structural request/result schema and the same decoded payload meaning, while inactive or blocked Tools are excluded. Transport serialization differences are allowed, except for any declared outer Project field such as project_root; no other transport-shape drift is silently introduced. Direct reads remain owned by their canonical Tool without forced workflow routing. Identical structural schemas may be unioned. A partially invalid Project Tool is quarantined and diagnosed without removing healthy Tools, and a failed replacement retains the prior valid frontier explicitly as prior, never as the current frontier.

## Details

- Inventory declared callable Tools and Workflows separately. Verify valid Workflow machine-invocation contracts and declared providers are exposed and delegated unchanged, with no invented workflow endpoint or hidden composition. A source definition alone does not establish executability; an unavailable required binding remains an explicit coverage/publication gap.
- Verify internal CONNECTORS/adapters and PROJECT_TOOLS never enter this frontier merely because their code or files exist. Preserve direct Tool reads without a mandatory Workflow wrapper.

- Build the frontier from a frozen admitted native inventory and compare names, descriptions and canonical structural schemas, including definitions and required fields; compare decoded request/result meaning rather than transport bytes.
- Verify a direct read Tool reaches its canonical owner and preserves the native request/result meaning, with only the declared outer Project field added.
- Present identical same-name schemas and verify one endpoint is possible; present conflicts or a partially invalid Project Tool and verify quarantine and attribution for that Tool while healthy frontier entries remain available.
- Verify inactive, disabled or blocked Tools do not enter the frontier or become callable through stale publication.
- If a replacement frontier is invalid, retain the previous valid frontier with an explicit prior status and do not label it current; mark construction unresolved when native source, Project binding or schema comparison is unavailable.
