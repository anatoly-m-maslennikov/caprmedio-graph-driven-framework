---
atom_id: CA-M-327
content_role: Method
type: Implementation Method
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 01:50:12 +0400
subjects:
  governs: Subject/Engineering/Implementation prompt test-first sequencing
  depends_on:
  - Subject/Engineering/Prompt
  - Evaluation
  - Subject/Engineering/Evaluation Technique Selection
relations:
  relates_to:
  - CA-R-1844
  - CA-O-018
  - CA-O-019
  - CA-O-020
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
