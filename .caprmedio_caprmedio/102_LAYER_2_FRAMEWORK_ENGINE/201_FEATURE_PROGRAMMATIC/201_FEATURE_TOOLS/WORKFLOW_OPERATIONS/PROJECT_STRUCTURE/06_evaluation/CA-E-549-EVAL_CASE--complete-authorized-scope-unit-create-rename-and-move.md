---
atom_id: CA-E-549
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-27 19:59:37 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
relations: {}
tier: 3
---
# Summary

Complete authorized Scope Unit Create, Rename, and Move

## Scope

Golden functional cases against a disposable project with declared TOML authority and independently observed implementation paths, entered only through CA-D-527's shared service interface.

## Claim

The Evaluation **must** prove an authorized Create, Rename, and Move produce the expected tree and repaired reference sets through the real workflow boundary without constructing a second route envelope.

## Details

- Submit one complete CA-D-527 request with PROJECT_STRUCTURE route-specific `parameters` and omitted `mode`; assert the default service `preview`, a sealed preview receipt/proposal, no Run or Event identity, and no TOML, reference, or Carrier effect. The payload declares a valid Ordered Create with unique sibling `local_order`, nonempty label, correct structural level, nonnegative navigation number, separate paths, and an explicit direct-parent Goal-coverage disposition.
- Submit the authorized explicit `execute` through that same interface, using D527's current/pinned bindings and preview authorization. Create the unit, Rename it, and Move it under a valid parent; assert the service result and Run evidence separately from a `structural_result.state = completed`.
- Assert authoritative TOML changes, distinct authority/delivery paths, cycle-free declarations, correct explicit or inherited effective authority mode, repaired incoming references/parent-owned attachments, reported Carrier observations, and exact result revisions. Assert no unrelated Carrier is deleted and inspect shared Journal evidence only through its existing contract.
