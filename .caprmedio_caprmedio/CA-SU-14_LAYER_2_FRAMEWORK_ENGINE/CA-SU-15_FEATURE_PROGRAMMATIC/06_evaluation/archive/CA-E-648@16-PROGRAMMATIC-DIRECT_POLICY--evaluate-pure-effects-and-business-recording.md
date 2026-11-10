---
identity:
  atom_id: CA-E-648
  ref_id: CA-E-648@16
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component
      Structure
    dependencies:
    - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  tier: 6
relations:
  evaluation_for:
  - CA-M-399
  - CA-M-425
state:
  status: Archived
  version: 16
  updated_at: 2026-11-09 14:19:14 +0400
destination:
  file:
    name: CA-E-648@16-PROGRAMMATIC-DIRECT_POLICY--evaluate-pure-effects-and-business-recording.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Evaluate pure effects and business recording

## Claim

### Prose Claim

Accept the boundary only when pure computations have no hidden I/O or event emission. Explicit external effects belong to effect owners and cannot become pure merely through a name or wrapper. Technical diagnostics stay on stdout/stderr, business lifecycle records are written to the Journal, preflight does not invent a business Run, and failure to record a business event is reported independently without invalidating an already applied effect.

## Details

### Scope

PROGRAMMATIC functions, methods, Tools, workflows and lifecycle paths that compute decisions, apply effects or record technical and business history.

- Invoke pure transformations with controlled inputs and observe no file, network, time, process, database, Journal or log effects.
- Verify any operation that needs such an effect is owned by an explicit effect boundary rather than labeled as pure.
- Observe effect owners separately and verify each effect has a target, precondition and completion fact.
- Trigger technical warnings and runtime failures and verify they are not fabricated business records.
- Trigger workflow lifecycle events and verify Journal records contain only business events with the correct initiative and run identity.
- Simulate a Journal or diagnostic sink failure after a valid effect and verify the effect result remains truthful while record failure uses its own channel.
