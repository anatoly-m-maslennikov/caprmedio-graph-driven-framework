---
identity:
  atom_id: CA-A-1372
  ref_id: CA-A-1372
context:
  role: analysis_and_advisory
  form: code_synopsis
  tier: 4
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Atom
  container:
    scope_unit: FRAMEWORK_ENGINE
state:
  version: 1
  status: active
  updated_at: '2026-11-12T12:59:01.708450+00:00'
destination:
  file:
    name: CA-A-1372-FRAMEWORK_ENGINE-CODE_SYNOPSIS--graph-output-uses-a-different-metadata-shape.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Graph output uses a different metadata shape

## Claim

### Prose Claim

CA-D-634@23 requires a Markdown Graph Projection with `type: Entities Graph`, `named_selection`, `source_of_truth` and `sources`. `FEATURE_TOOLS/GENERATE_ENTITY_GRAPH/readable_entity_tree.py` emits a Map or Catalog with a nested `source` mapping. CA-D-653@16 calls for persistent focused Subject Graph carriers. The inspected `render_subject_projections.py` path writes the focused body to stdout. No caller-side publishing was tested.
