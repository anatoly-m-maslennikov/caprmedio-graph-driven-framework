---
atom_id: CA-E-562@6
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 02:14:24 +0400
subjects:
  governs: Tool/WORKFLOW_OPERATIONS/APPLICABLE_METHODOLOGY
  depends_on:
  - Tool
  - Methodology Source
  - Carrier
  - Projection
  - Journal
  - Workflow Run
relations:
  evaluation_for:
  - CA-R-1839
  - CA-R-1842
  - CA-M-226
tier: 5
---
# Summary

Plan functional proof that incomplete inputs and publication recovery preserve prior output without replaying authority edits.

## Scope

Functional incomplete-frontier, injected publication-failure, and recovery cases.

## Claim

An implementation **must** prove that incomplete input and failed or uncertain publication preserve the prior projection and never replay a source correction or claim a completed publication without independently verified output/effect evidence. A failed Journal append after successful publication remains a recording diagnostic and does not require rollback.

## Details

Given a known prior output, exercise missing source, malformed carrier, inaccessible activated Extension, changed source during staging, newly added source during currentness validation, and incomplete conflict assessment. Every case must block before output mutation and return the exact finding. Inject a failure during multi-role publication and assert byte-for-byte restoration of the prior complete projection, no partial role tree, and no success receipt. Separately inject a Journal append failure after a successful atomic publication and assert that the published output and independently observed effects remain available with a `recording_error` diagnostic and no rollback. Repeat the explicit Journal append and assert that it remains a plain business record operation with no identity or authorization gate.

For recovery, provide the failed publication evidence and unchanged current inputs: the Tool may retry staging/publication only, retaining the same source and decision provenance and shared Run references. If any input or provenance changes, recovery must return to selection and assessment; it must not replay an external source correction. Record no completed publication until the atomic output and independently verified publication/effect evidence exist. A missing or failed Journal append yields a recording diagnostic and does not by itself invalidate or roll back a successful publication. This carrier records planned functional proof, not a runtime pass.

### Sources

- CA-R-1839; CA-R-1842; CA-M-226 v7; CA-O-157 v2; CA-O-009 v5.
