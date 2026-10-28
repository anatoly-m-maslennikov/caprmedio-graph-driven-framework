---
atom_id: CA-E-612
content_role: Evaluation
type: Eval Case
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Documentation
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History
version: 17
updated_at: 2026-10-27 19:59:38 +0400
relations:
  evaluation_for:
  - CA-M-366
tier: 5
---
# Summary

Validate public material source binding

## Scope

one selected public documentation closure.

## Claim

**the Operator** **must** verify that README, full PR body, Version History carrier and selected Version remain the exact prepared public material bindings and reject substituted carrier, Version, document bytes or PR identity.

## Details

The golden successful case contains distinct What's new and What's fixed PR sections. Adding only the actual matching PR URL to the already-generated concise Version History summary may change those metadata bytes while preserving the selected Version and all non-metadata source/material bindings. A substituted raw document byte, substantive summary rewrite, guessed or unrelated PR identity, or changed non-metadata binding is refused. This tests actual prepared material binding, not a retired CA-D-566 snapshot or a newly invented Source Proof serialization.
