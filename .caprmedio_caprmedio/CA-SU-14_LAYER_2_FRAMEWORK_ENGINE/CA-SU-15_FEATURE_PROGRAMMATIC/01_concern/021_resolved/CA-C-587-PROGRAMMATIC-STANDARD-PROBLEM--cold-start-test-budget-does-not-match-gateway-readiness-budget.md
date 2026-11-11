---
atom_id: CA-C-587
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Resolved
priority: high
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-M-410]
  relates_to: [CA-P-2613, CA-P-2633, CA-P-2634, CA-C-576]
version: 2
updated_at: "2026-10-23T13:38:38+0400"
---
# Summary

Cold-start test budget does not match Gateway readiness budget

## Concern

The canonical legacy stdio test harness gave its fixture client and MCP
discovery only 30 seconds, while the Gateway's production generation-ready
budget is 90 seconds. The bounded repros passed in 24.95 seconds, failed
during client initialization at the 30-second budget, and passed in 82.1
seconds when allowed to complete. A quiescent direct run measured generation
at 30.303 seconds, initial fingerprint work at 2.965 seconds and fingerprint
verification at 5.018 seconds. This was a test-harness readiness mismatch,
not evidence of a production outage. A separate sanitized ValueError/source-
drift hypothesis remains unproven and is outside this resolution.

## Resolution

CA-P-2633 completed the bounded refactor: the observed 305 source lines were
reduced to 200 and a 199-line support helper was added. CA-P-2634 then aligned
the disposable test startup/readiness boundary to 120 seconds while leaving
the production Gateway's 90-second readiness budget unchanged. Twelve focused
stdio/telemetry checks passed in 117.937 seconds and five focused hot-reload
readiness/telemetry checks passed in 20.556 seconds. Ruff, strict Mypy, AST
diff verification and independent review passed after the RMED ownership
header correction. The finite test-harness readiness mismatch is resolved.

## Evidence boundary

CA-M-410's bounded-resource policy is satisfied for this disposable test
boundary. The resolution does not change the production Gateway budget,
Project binding, runtime image, live MCP, release or deployment state. The
unproven sanitized ValueError/source-drift hypothesis is not resolved by this
Problem and remains separately tracked if reproduced.

## Residual boundary

CA-C-586 remains an open Operator question about O011 interactive decision
acquisition, and compiler behavior is unchanged. No full-suite result or
production-readiness claim follows from this resolved Problem.
