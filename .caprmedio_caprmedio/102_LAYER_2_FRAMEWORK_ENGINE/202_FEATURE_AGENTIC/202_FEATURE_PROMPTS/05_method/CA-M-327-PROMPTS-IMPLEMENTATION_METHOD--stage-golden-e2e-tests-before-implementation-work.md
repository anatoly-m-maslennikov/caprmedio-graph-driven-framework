---
atom_id: CA-M-327
content_role: Method
type: Implementation Method
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-27 19:59:42 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Test Design
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Prompt Authoring
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Test Design
relations: {}
tier: 3
---
# Summary

Stage golden E2E tests before implementation work

## Scope

the tests-first portion of a selected bounded implementation packet.

## Claim

**to** prepare implementation, first specify executable golden E2E cases from E authority and runnable baselines, then implement only the admitted R/D behavior and run the selected checks.

## Details

Mock external boundaries rather than the behavior under test. A baseline or expected initial failure is evidence for preparation, not a completed test or behavior pass.
