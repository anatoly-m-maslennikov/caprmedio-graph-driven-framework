---
atom_id: CA-M-397@10
content_role: Method
type: Eng Policy
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Execution Control
  depends_on: []
relations:
  child_of:
  - CA-M-396
tier: 2
---
# Summary

Contain invalid input and Project artifact failures

## Scope

New or changed PROGRAMMATIC implementation, including Tools, Apps, MCP adapters and their public operation boundaries.

## Claim

Handle invalid input and Project artifact problems as operation-local failures: report an attributable error in the Tool, MCP or other caller-visible output, emit a sanitized technical WARNING, and keep the runtime available.

## Details

1. Apply this classification to invalid requests and malformed, missing, stale, ambiguous or otherwise unusable Project artifacts and bindings. Technical ERROR severity is not permitted for these conditions, even when the affected operation cannot proceed.
2. Give the response a stable error code, a safe explanation and the affected logical target or safe Project-relative path when known. A warning in logs alone is not an error answer; do not rely on exception text or logs as the only output.
3. Reject unsafe or unauthorized effects at their applicable boundary. Continue only independently safe and authorized work; never select a substitute Project, repair input, bypass a guard or retry as an implicit error-handling policy.
4. Use the error/diagnostic structure of the applicable public result contract without discarding completed data. CA-M-398 governs partial-result presentation; result errors do not determine log severity.
5. Use the runtime-only blocking/ERROR distinction in CA-M-396. Return even an all-invalid result as an explicit failed or incomplete request outcome, not a crashed service or a false successful empty result.
