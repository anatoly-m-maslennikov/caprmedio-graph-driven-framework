---
atom_id: "CA-E-612"
content_role: "Evaluation"
type: "QA Case"
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release material source proof"
  depends_on: [README, Pull Request, Version History, Source Proof]
version: 2
updated_at: "2026-10-10 19:05:35 +0400"
relations:
  evaluation_for: [CA-R-1922, CA-M-366]
---
# Summary

Validate public material source binding

## Scope

one selected public documentation closure.

## Claim

**the Operator** **must** verify that README, full PR body, Version History carrier, selected Version, D566 candidate snapshot, and canonical public-document closure remain the exact submitted source proof and reject substituted carrier, closure, or snapshot results.

## Details

The golden successful case contains distinct What’s new and What’s fixed PR sections. It proves that adding an actual Version History PR link changes the public-document-closure digest while retaining the same candidate snapshot, Version, and `version.toml` digest; a substituted raw document byte, summary, PR identity, or closure digest is refused.
