---
atom_id: "CA-E-618"
content_role: "Evaluation"
type: "QA Case"
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release Journal lineage"
  depends_on: [Journal, Workflow, Step, Action, Tool Call]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  evaluation_for: [CA-R-1928, CA-M-369]
---
# Summary

Validate public-release schema-v5 Run and Tool-call lineage

## Scope

the Journal output of one public-release fixture.

## Claim

**the Operator** **must** verify schema-v5 actual Workflow, Step, and Action Run parentage, started and terminal records, and Tool-call evidence references parented to their Step and Action without any Tool Run kind.

## Details

The check rejects source claims of success without durable Run evidence.
