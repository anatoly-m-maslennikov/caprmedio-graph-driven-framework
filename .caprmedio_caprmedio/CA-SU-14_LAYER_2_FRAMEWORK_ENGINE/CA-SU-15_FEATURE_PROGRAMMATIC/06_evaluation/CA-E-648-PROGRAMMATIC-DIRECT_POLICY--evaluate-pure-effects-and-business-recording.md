---
identity:
  atom_id: CA-E-648
  ref_id: CA-E-648
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Component Structure
    dependencies:
    - MODEL//CAPRMEDIO <+ Journal
  tier: 6
relations:
  evaluation_for:
  - CA-M-399
  - CA-M-425
state:
  status: Active
  version: 17
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-648-PROGRAMMATIC-DIRECT_POLICY--evaluate-pure-effects-and-business-recording.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
## Summary

Evaluate pure effects and business recording

## Claim

### Prose Claim

Pure computations have no hidden I/O/event emission; explicit effects belong to owners with target, precondition and completion fact. Technical diagnostics use stdout/stderr, business lifecycle records use Journal, preflight invents no Run, and record-sink failure is reported independently of applied effect.
