---
atom_id: CA-D-005
ref_id: CA-D-005@20-draft
role: Delivery
form: Solution
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation
  dependencies:
  - CAPRMEDIO_MODEL <+ Projection
tier: 2
relations:
  delivery_for:
  - CA-R-1076
  - CA-M-153
status: Draft
version: 20
updated_at: 2026-11-10 08:25:53 +0400
subject_scopes:
- projection-pipeline
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: GRAPH_UI
carrier_destination:
  file:
    name: CA-D-005@20-draft-GRAPH_UI-SOLUTION--deliver-the-requirement-projection-browser-locally.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-44_APP_GRAPH_UI/07_delivery/draft
container:
  scope_unit: CA-SU-44
---

## Summary

Deliver the Requirement Projection browser locally

## Claim

### Prose Claim

Deliver the optional GRAPH_UI Requirement Projection browser as exactly one project-local, non-authoritative `_projection/mrt_atoms.html` under the selected Project’s declared authority root file with embedded JavaScript and presentation assets. Serve this generated asset through the selected Workbench listener, on the same origin as its query API. Back its live reads with the declared Workbench query contract and current indexed Atom Content, without a separate server, file-origin API access or a general source-file HTTP service.

Create no sibling web assets. This delivery is not required for headless Workbench, Tool or MCP operation and does not publish, host or distribute the MRT outside the Project. Deleting the generated file changes no governed Atom, Journal or other Projection.
