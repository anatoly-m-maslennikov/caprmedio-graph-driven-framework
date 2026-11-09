---
atom_id: CA-M-327
ref_id: CA-M-327
container:
  scope_unit: CA-SU-14
role: Method
form: Direct Policy
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Test
    Design
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Prompt Authoring
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Test Design
tier: 3
status: Active
version: 14
updated_at: 2026-11-09 17:00:18 +0400
carrier_destination:
  file:
    name: CA-M-327-FRAMEWORK_ENGINE-DIRECT_POLICY--stage-golden-e2e-tests-before-implementation-work.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/05_method
current_scope_unit: FRAMEWORK_ENGINE
claim_target_scope_unit: FRAMEWORK_ENGINE
author: Anatoly Maslennikov
---

## Summary

Stage golden E2E tests before implementation work

## Claim

### Prose Claim

**to** prepare implementation, first specify executable golden E2E cases from E authority and runnable baselines, then implement only the admitted R/D behavior and run the selected checks.

## Details

### Scope

the tests-first portion of a selected bounded implementation packet.

Mock external boundaries rather than the behavior under test. A baseline or expected initial failure is evidence for preparation, not a completed test or behavior pass.
