---
atom_id: CA-R-1923
ref_id: CA-R-1923
container:
  scope_unit: CA-SU-27
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Release.ID
tier: 3
status: Active
version: 13
updated_at: 2026-11-09 15:54:30 +0400
carrier_destination:
  file:
    name: CA-R-1923-FRAMEWORK_DELIVERY-RULE--require-an-actual-pr-link-in-version-history.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/04_requirement
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
relations: {}
---

# Summary

Require an actual PR link in Version History

## Scope

one Version History entry for one public release.

## Claim

**the Operator** **must** record only a concise selected-Version summary and the actual matching public PR hyperlink in that Version History entry.

## Details

A guessed URL, placeholder, prose-only reference, or unrelated PR does not satisfy the Claim. When the actual URL becomes known after the initial push, CA-O-198 owns mechanical finalization and same-PR refresh without another suite or prompt.
