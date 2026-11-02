---
atom_id: CA-E-612@12
content_role: Evaluation
type: Eval Case
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Release Version/Source Binding
  depends_on:
  - Subject/Documentation/README
  - Subject/Engineering/Pull Request
  - Subject/Engineering/Release/Version History
version: 12
updated_at: 2026-10-24 20:11:44 +0400
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
