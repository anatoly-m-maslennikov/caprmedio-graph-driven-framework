---
identity:
  atom_id: CA-M-404
  ref_id: CA-M-404@11
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
      Control/Effect Authorization
    dependencies: []
  tier: 1
state:
  status: Archived
  version: 11
  updated_at: 2026-11-09 07:45:14 +0400
destination:
  file:
    name: CA-M-404@11-PROGRAMMATIC-DIRECT_POLICY--limit-effects-to-the-authorized-target-and-delta.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method/archive
current_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Limit effects to the authorized target and delta

## Claim

### Prose Claim

**To** change state, bind the admitted target, explicit delta and required expected state, then apply **only** that authorized change.

## Details

### Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and tests.

Candidate source: [CA-M-388@2](archive/CA-M-388-PROGRAMMATIC-CORE--limit-effects-to-the-authorized-target-and-delta@2.md)

- Do not substitute targets, broaden the affected frontier or add semantic operations.
- Observing additional files or state does not grant permission to change them.
- An unresolved, ambiguous, stale or unsupported binding stops the affected change; it does not authorize a fallback target or broader effect.

Source basis: CA-M-376, CA-M-381.
