---
identity:
  atom_id: CA-A-1370
  ref_id: CA-A-1370
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
  updated_at: '2026-11-12T12:58:55.273920+00:00'
destination:
  file:
    name: CA-A-1370-FRAMEWORK_ENGINE-CODE_SYNOPSIS--duplicate-carrier-selection-can-open-several-files-per-target.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Duplicate carrier selection can open several files per target

## Claim

### Prose Claim

CA-M-1006@7 allows one exact file read per selected target. `FEATURE_TOOLS/ATOM_LIFECYCLE/source.py` opens candidate files until `_unique_candidate` finds a valid version, identity and status. A stale or malformed duplicate can cause a second physical read for the same target. `publish.py` also stops indexed Archive replacement lookup on an invalid first match, even if a later result may be valid.
