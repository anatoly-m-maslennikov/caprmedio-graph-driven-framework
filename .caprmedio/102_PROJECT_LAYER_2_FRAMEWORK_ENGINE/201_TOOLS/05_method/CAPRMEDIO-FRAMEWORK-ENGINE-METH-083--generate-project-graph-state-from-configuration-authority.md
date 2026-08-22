---
subject_scopes:
  - project-settings
tier: core
version: 4
updated_at: 2026-08-22 04:20:12
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  method_for:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-674--derive-project-graph-state-and-map-from-configuration-authority
---
# Generate Project Graph State from Configuration Authority

Resolve exactly one Project Configuration Atom through its governed external
binding and treat it as the sole owner of current operator-selected settings.
Enumerate only applicable active Atom contributions admitted under the
top-level `project_graph_state` map; use them for registered facts, allowed
values, defaults, structural context, and other non-configurational Graph State
inputs. Reject every `project_settings` contribution outside the Configuration
Atom.

Generate Project Graph State and its Source Map from the exact Configuration
revision and exact admitted contribution and Journal revisions. Preserve
per-value source bindings, canonical source order where a registered output
permits multiple sources, and deterministic bytes. Never read a prior Graph
State or Source Map Projection as semantic input. Fail before writing either
Projection when the Configuration binding or an admitted source is missing,
malformed, unresolved, ambiguous, stale, contradictory, or incompletely
mapped.
