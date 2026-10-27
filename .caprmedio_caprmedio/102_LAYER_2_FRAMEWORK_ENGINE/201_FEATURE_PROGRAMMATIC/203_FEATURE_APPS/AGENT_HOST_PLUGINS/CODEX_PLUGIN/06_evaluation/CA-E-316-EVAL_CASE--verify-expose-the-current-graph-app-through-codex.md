---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph Node/Engineering/Architecture/Communication
  depends_on: []
version: 19
updated_at: 2026-10-27 06:04:45 +0400
relations:
  evaluation_for:
  - CA-M-198
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-316
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Eval Case
tier: 3
---
# Verify expose the current graph_app through codex

## Claim checked

CA-M-198 exposes current GRAPH_UI state through Codex as an attributable read-only view with explicit stale **and** unavailable states.

## Applicable when

Apply **before** accepting **any** Codex plugin release that exposes Project Graph browsing.

## Test case

Compare the Codex viewing response for one governed-filtered node under three bounded GRAPH_UI states: a current source frontier, the same source carrier changed **after** the graph state was derived, **and** an unavailable source frontier. Retain the relevant source, graph-state, **and** repository digests **before** **and** **after** each view.

## Acceptance criteria

the current view returns navigation, the applied governed filter, node content, exact source path, digest, **and** provenance; the changed-source view reports stale state rather than presenting old content as current; the unavailable view reports its unavailable state; **and** viewing changes no Atom, Journal, Projection, graph source, **or** derived GRAPH_UI state.

## Failure disposition

Reject the Codex exposure **and** preserve the three GRAPH_UI states, selected-node responses, filter evidence, stale **and** unavailable handling, **and** before-and-after mutation evidence.
