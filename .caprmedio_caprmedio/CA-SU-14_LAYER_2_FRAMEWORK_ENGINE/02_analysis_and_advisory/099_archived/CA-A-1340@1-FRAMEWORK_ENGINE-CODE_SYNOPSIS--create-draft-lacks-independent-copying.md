---
identity:
  atom_id: CA-A-1340
  ref_id: CA-A-1340@1
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
  status: archived
  updated_at: '2026-11-12T12:43:32.994964+00:00'
destination:
  file:
    name: CA-A-1340@1-FRAMEWORK_ENGINE-CODE_SYNOPSIS--create-draft-lacks-independent-copying.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory/099_archived
---
## Summary

Create Draft lacks independent copying

## Claim

### Prose Claim

In the CAPRMEDIO working tree based on commit `c0b983cb27`, `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/ATOM_LIFECYCLE/draft.py` resolves a source in `_source`. In `prepare_draft`, an unchanged Role and Summary select the source Atom ID and the next Version. A fresh ID at Version 1 follows a new Atom request or a change in Role or Summary. The MCP Create Draft descriptor in `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/registry_lifecycle_provider.py` exposes no independent-copy choice.

CA-R-970308671@1 requires an independent copy from a selected Current, Archived or Draft source, with a new ID at Version 1 even when its content is copied as-is. CA-E-826@3 adds the corresponding functional check. The current request shape leaves the caller to reconstruct new Atom input or change identity-defining content.
