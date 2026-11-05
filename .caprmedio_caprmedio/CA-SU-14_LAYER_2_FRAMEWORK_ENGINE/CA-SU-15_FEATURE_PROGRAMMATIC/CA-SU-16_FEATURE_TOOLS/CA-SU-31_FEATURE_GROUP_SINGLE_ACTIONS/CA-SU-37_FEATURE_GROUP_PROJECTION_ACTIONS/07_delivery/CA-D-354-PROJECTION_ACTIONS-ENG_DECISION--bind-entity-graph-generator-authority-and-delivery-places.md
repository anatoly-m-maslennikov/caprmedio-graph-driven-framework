---
atom_id: CA-D-354
ref_id: CA-D-354
container:
  scope_unit: CA-SU-37
role: Delivery
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
tier: 4
relations:
  delivery_for:
  - CA-R-1387
  - CA-M-259
status: Active
version: 18
updated_at: 2026-11-02 19:46:47 +0400
carrier_destination:
  file:
    name: CA-D-354-PROJECTION_ACTIONS-ENG_DECISION--bind-entity-graph-generator-authority-and-delivery-places.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-31_FEATURE_GROUP_SINGLE_ACTIONS/CA-SU-37_FEATURE_GROUP_PROJECTION_ACTIONS/07_delivery
cce_version: cce_1
cce_form: delivery
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROJECTION_ACTIONS
claim_target_scope_unit: PROJECTION_ACTIONS
author: Anatoly Maslennikov
---
# Summary

Bind Entity graph generator authority and delivery places

## Scope

PROJECTION_ACTIONS owns generation and optional persistence of non-authoritative graph Projections from selected source frontiers.

## Claim

The Delivery Atom is governed under `.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-31_FEATURE_GROUP_SINGLE_ACTIONS/CA-SU-37_FEATURE_GROUP_PROJECTION_ACTIONS/`. The canonical executable Carrier remains at `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/GENERATE_ENTITY_GRAPH/generate_entity_graph.py`. Installed copies **and** mutable execution state remain respectively under `.caprmedio_runtime/tools` **and** `.caprmedio_runtime`; persisted non-authoritative view Projection destinations resolve from an explicit caller path or registered Project setting and must remain beneath `.caprmedio_caprmedio/_projection/`; reject a persistent destination outside that registered root. Native executable Implementation remains at its governed delivery place and can supply actual-state facts without moving into _projection. Runtime technical and business Journals use their configured governed sinks and are preserved during disposable-state cleanup.
