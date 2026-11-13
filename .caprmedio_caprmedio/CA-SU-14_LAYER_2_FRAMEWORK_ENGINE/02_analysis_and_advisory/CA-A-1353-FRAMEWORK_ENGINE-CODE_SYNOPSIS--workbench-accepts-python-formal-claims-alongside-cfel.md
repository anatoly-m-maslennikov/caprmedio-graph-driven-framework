---
identity:
  atom_id: CA-A-1353
  ref_id: CA-A-1353
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
  updated_at: '2026-11-12T12:49:24.671712+00:00'
destination:
  file:
    name: CA-A-1353-FRAMEWORK_ENGINE-CODE_SYNOPSIS--workbench-accepts-python-formal-claims-alongside-cfel.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Workbench accepts Python Formal Claims alongside CFEL

## Claim

### Prose Claim

In the CAPRMEDIO working tree based on `c0b983cb27`, `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/declaration_cfel.py` reads supported Python-labelled Formal Claim fences in addition to CFEL. CA-M-500@11 and CA-M-509@6 specify CFEL-only declaration facts for the current Workbench assets. The source currently permits both readers. Python migration is tracked separately in CA-P-3022. This observation concerns the checkout, with no claim that the mixed-language reader has been deployed.
