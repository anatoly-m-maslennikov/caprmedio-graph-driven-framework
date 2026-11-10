---
atom_id: CA-O-183
ref_id: CA-O-183
container:
  scope_unit: CA-SU-27
role: Operations
form: Action
topics:
  main_subject: Subject/caprmedio/Action//Aggregate the full Release Gate
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification
  - Subject/CAPRMEDIO/Carrier/Docker Image
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
status: Active
version: 15
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-O-183-FRAMEWORK_DELIVERY-ACTION--aggregate-the-full-release-gate.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/09_operations
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
relations: {}
---

# Summary

Aggregate the full Release Gate

## Action

Aggregate the full Release Gate **means** the read-only decision over the exact closed-unit, image-canary and host Candidate E2E receipts for one frozen N/N+1 candidate.

## Details

Every receipt must name the same candidate manifest, source frontier, compiled output, package, immutable image and parent lineage. The Unit receipt must cover every declared testcase outside the current `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/tests/` host-capable runtime-test set; the E2E receipt must cover every testcase in that set. Every declared testcase must terminal-pass: skipped, excluded, missing or zero-coverage testcase is non-pass. Missing, stale, mixed-candidate, partial or unjournalable evidence is non-pass. This Action creates no runtime/Skill selection, image removal, retry, Docker effect or new authority.
