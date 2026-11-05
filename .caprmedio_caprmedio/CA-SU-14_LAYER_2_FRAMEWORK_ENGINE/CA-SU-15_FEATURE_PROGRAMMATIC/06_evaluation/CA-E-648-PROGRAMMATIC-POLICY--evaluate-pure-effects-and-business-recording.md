---
atom_id: CA-E-648
ref_id: CA-E-648
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Policy
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 5
relations:
  evaluation_for:
  - CA-M-426
  - CA-M-399
status: Active
version: 13
updated_at: 2026-10-27 19:59:38 +0400
carrier_destination:
  file:
    name: CA-E-648-PROGRAMMATIC-POLICY--evaluate-pure-effects-and-business-recording.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Evaluate pure effects and business recording

## Scope

PROGRAMMATIC functions, methods, Tools, workflows and lifecycle paths that compute decisions, apply effects or record technical and business history.

## Claim

Accept the boundary only when pure computations have no hidden I/O or event emission. Explicit external effects belong to effect owners and cannot become pure merely through a name or wrapper. Technical diagnostics stay on stdout/stderr, business lifecycle records are written to the Journal, preflight does not invent a business Run, and failure to record a business event is reported independently without invalidating an already applied effect.

## Details

- Invoke pure transformations with controlled inputs and observe no file, network, time, process, database, Journal or log effects.
- Verify any operation that needs such an effect is owned by an explicit effect boundary rather than labeled as pure.
- Observe effect owners separately and verify each effect has a target, precondition and completion fact.
- Trigger technical warnings and runtime failures and verify they are not fabricated business records.
- Trigger workflow lifecycle events and verify Journal records contain only business events with the correct initiative and run identity.
- Simulate a Journal or diagnostic sink failure after a valid effect and verify the effect result remains truthful while record failure uses its own channel.
