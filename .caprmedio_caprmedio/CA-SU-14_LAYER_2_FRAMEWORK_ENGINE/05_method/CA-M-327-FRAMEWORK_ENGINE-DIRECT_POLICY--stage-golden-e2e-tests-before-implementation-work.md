---
atom_id: CA-M-327
ref_id: CA-M-327
container:
  scope_unit: CA-SU-14
role: Method
form: Direct Policy
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
    <+ Verification <+ Test Design
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring
    <+ Prompt Authoring
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Evaluation)
tier: 3
status: Active
version: 15
updated_at: 2026-11-10 20:47:54 +0400
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

**to** prepare implementation, specify executable golden E2E cases from E authority and runnable baselines before implementing admitted R/D behavior and running selected checks.

## Details

### Scope

the tests-first portion of a selected bounded implementation packet.

Mock external boundaries, not the behavior under test. A baseline or expected initial failure is evidence for preparation, not a completed test or behavior pass.
