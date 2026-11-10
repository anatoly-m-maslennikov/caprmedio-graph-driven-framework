---
identity:
  atom_id: CA-D-711
  ref_id: CA-D-711
context:
  container:
    scope_unit: CA-SU-15
  role: Delivery
  form: Solution
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Storage
    dependencies:
    - MODEL//CAPRMEDIO <+ Carrier/Directory
    - MODEL//CAPRMEDIO <+ Package/Project Package
    - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage
      <+ Temporary State
  tier: 5
state:
  status: Active
  version: 1
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-D-711-PROGRAMMATIC-SOLUTION--PROGRAMMATIC-SOLUTION--separate-generated-outputs-from-hand-authored-software-sources.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/07_delivery
author: Anatoly Maslennikov
relations:
  delivery_for:
  - CA-M-419
cce_version: cce_1
cce_form: serialization
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
---
## Summary

Separate generated outputs from hand-authored software sources

## Claim

### Prose Claim

Hand-authored PROGRAMMATIC source distribution excludes generated Runtime/Delivery outputs. Generated outputs use CA-D-250 locations; temporary build/staging/cache uses CA-D-437 and does not overlap source. Separately declared installable generated outputs may be packaged.
