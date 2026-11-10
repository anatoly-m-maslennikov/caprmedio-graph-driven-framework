---
atom_id: CA-M-153
ref_id: CA-M-153@29-draft
container:
  scope_unit: CA-SU-44
role: Method
form: Solution
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation
tier: 3
relations:
  method_for:
  - CA-R-1076
  SPECIALIZES:
  - CA-M-222
  DERIVED_FROM:
  - CA-A-057
status: Draft
version: 29
updated_at: 2026-11-10 11:53:32 +0400
carrier_destination:
  file:
    name: CA-M-153@29-draft-GRAPH_UI-SOLUTION--render-and-navigate-active-graph-html.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-44_APP_GRAPH_UI/05_method/draft
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: GRAPH_UI
claim_target_scope_unit: GRAPH_UI
author: Anatoly Maslennikov
---

## Summary

Render and navigate active graph HTML

## Claim

### Prose Claim

Bind this GRAPH_UI interface to the declared Workbench query contract. Preserve the request, result, cancellation, stale and error states that contract actually supplies, without adding commands or assuming effect ownership.

Render the optional GRAPH_UI from the current Workbench query Projection:

1. Resolve the selected Project, Scope Units and current query schema through the declared Workbench service contract. Use its current source tables, indexed Atom Content and direct/derived Relations. Do not require registered legacy STG files or a raw-source-file HTTP endpoint.
2. Query the required node, link, Subject and lineage data through that contract. Keep SQL selection and complete-graph orphan/cycle classification in the backend; fetch bounded pages and requested node Content instead of treating an embedded source copy as current authority. Missing schema, source rows or required state remains explicit.
3. Materialize exactly one project-local `_projection/mrt_atoms.html` under the selected Project’s declared authority root file with embedded JavaScript and presentation assets. Serve this generated asset through the selected Workbench listener on the same origin as its query API. Do not require a separate server, file-origin API access or a general source-file endpoint. Create no sibling script, stylesheet, data, index, view or per-Atom HTML files. Owned disposable service state remains under `.caprmedio_runtime`.
4. Record the selected query/source bindings and each consumed Atom reference, Version, relative carrier location and public row hash in a source-lineage manifest. Use the current Workbench contract for subsequent reads. A public row hash identifies projected state; do not present it as the raw carrier-byte digest or present indexed Content as complete raw Markdown bytes.
5. Derive the Scope Unit filter tree from current Scope Unit rows. Provide Tier, Scope Unit, Content Role and Form filters, orphan/cycle visibility and unknown-region diagnostics. Hiding a neighbour does not make its node an orphan in the complete selected graph.
6. In short mode, show `<Atom ID> <Summary>` using the authored Summary. The first click shows current indexed Content above the node; the second also shows the available indexed Header. In detailed mode, show the Content initially and the Header on click. Display untrusted values as data; no content executes or gains authority.
7. Compare manifest bindings with current returned rows and available synchronization state. Distinguish a stale rendered view, changed indexed Atom and unavailable data without inventing a freshness proof from absent metadata. Preserve filters and focused node in the URL, and link each identity to its canonical relative carrier location.

This graph interface consumes the shared service; it does not become an authority, effect owner, scheduler or source-file reader. It does not construct or review the deferred Terms Graph. An existing admitted Terms Projection may be consumed only through its declared input contract, without making it a prerequisite for the ordinary graph view.
