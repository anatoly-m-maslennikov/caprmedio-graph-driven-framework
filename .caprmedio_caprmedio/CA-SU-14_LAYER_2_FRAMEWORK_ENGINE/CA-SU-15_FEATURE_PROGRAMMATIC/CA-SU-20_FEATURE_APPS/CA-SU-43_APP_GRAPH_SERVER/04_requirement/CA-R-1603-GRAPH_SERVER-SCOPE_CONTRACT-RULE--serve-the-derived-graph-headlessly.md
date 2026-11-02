---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component
    Structure
version: 14
updated_at: 2026-11-02 19:44:26 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1603
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: GRAPH_SERVER
type: Rule
tier: 0
claim_target_scope_unit: GRAPH_SERVER
---
## Summary

Serve the Derived Graph Headlessly

## Claim

GRAPH_SERVER **must** own the rebuildable non-authoritative graph read model **and** read-only service used by Tools, MCP, **and** optional interfaces without requiring GRAPH_UI.
