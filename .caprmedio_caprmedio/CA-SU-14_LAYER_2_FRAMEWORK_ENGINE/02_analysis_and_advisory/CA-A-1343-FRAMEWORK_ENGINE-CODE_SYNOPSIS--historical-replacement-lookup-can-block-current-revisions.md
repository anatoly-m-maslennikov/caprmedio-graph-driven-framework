---
identity:
  atom_id: CA-A-1343
  ref_id: CA-A-1343
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
  updated_at: '2026-11-12T12:43:43.918340+00:00'
destination:
  file:
    name: CA-A-1343-FRAMEWORK_ENGINE-CODE_SYNOPSIS--historical-replacement-lookup-can-block-current-revisions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Historical replacement lookup can block current revisions

## Claim

### Prose Claim

In the CAPRMEDIO working tree based on commit `c0b983cb27`, `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/ATOM_LIFECYCLE/publish.py`, `update_atom` and `resolve_replacement`, reselect historical targets of retained replacement links before archiving a Current revision. `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/service.py`, `lifecycle_archive_candidates`, selects indexed or admitted Archive locations.

The local MCP refused content-only revisions of CA-M-509@6, CA-R-1114@24 and CA-R-1901@19 with `Replacement target cannot be resolved safely`, before any write. CA-D-705 and CA-M-176 had no query-visible Archive row after loading their declared Scope and Role. CA-R-1901 also retains CA-D-594 under a retired Scope. CA-R-1105@31 defines an exact Current-to-Draft Update and CA-M-1006@7 requires explicit selection errors. The retained lineage prevented promotion and the response did not identify which source failed.
