---
subject_scopes:
  - graph-app-access
tier: core
version: 2
updated_at: 2026-08-22 02:37:15
relations:
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-712--define-codex-plugin-unit
  relates_to:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-616--render-interconnected-html-graph-views
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-617--serve-live-graph-sources-read-only
---
# Expose the current GRAPH_APP through Codex

`CODEX_PLUGIN` must let a Codex operator open and navigate the current `GRAPH_APP`, apply its governed filters, select graph nodes, and inspect their current source content, paths, digests, and provenance without copying the graph read model into plugin authority. The plugin must consume the GRAPH_APP's read-only interface, preserve stale or unavailable-source states, and must not mutate an Atom, Journal, Projection, graph source, or derived GRAPH_APP state through the viewing path.
