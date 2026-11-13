---
identity:
  atom_id: CA-A-1373
  ref_id: CA-A-1373
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
  updated_at: '2026-11-12T12:59:04.618389+00:00'
destination:
  file:
    name: CA-A-1373-FRAMEWORK_ENGINE-CODE_SYNOPSIS--host-graph-generation-scans-atom-source-folders.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Host graph generation scans Atom source folders

## Claim

### Prose Claim

CA-M-1006@7 requires targeted Workbench queries for Atom reads and limits direct file reads to selected targets. `FEATURE_TOOLS/GENERATE_ENTITY_GRAPH/current_entity_sources.py` inventories folders and reads Atom files directly for the host graph commands. The review found no separate exception for those commands. Workbench indexing and offline image bootstrap have their own input boundaries.
