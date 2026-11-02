---
atom_id: CA-C-587
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: high
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-M-410]
  relates_to: [CA-P-2613, CA-P-2633, CA-P-2634, CA-C-576]
version: 1
updated_at: "2026-10-23T13:18:33+0400"
---
# Summary

Cold-start test budget does not match Gateway readiness budget

## Concern

The canonical legacy stdio test harness gives its fixture client and MCP
discovery only 30 seconds, while the Gateway's production generation-ready
budget is 90 seconds. The bounded repros passed in 24.95 seconds, failed
during client initialization at the 30-second budget, and passed in 82.1
seconds when allowed to complete. A quiescent direct run measured generation
at 30.303 seconds, initial fingerprint work at 2.965 seconds and fingerprint
verification at 5.018 seconds. This is a test-harness readiness mismatch, not
evidence of a production outage. A separate sanitized ValueError/source-drift
hypothesis remains unproven and is intentionally outside this Problem.

## Required disposition

Refactor the canonical 304-line
102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests/test_rmed_workflow_mcp.py
into cohesive helper/fixture boundaries first, without changing timeout
semantics or production code. Then align the bounded test startup/readiness
budget with the existing 120-second disposable harness boundary, including
tests/naked_mcp_smoke.py and its support helpers, while leaving the
production Gateway's 90-second readiness budget unchanged. Run only the
focused cold-start and related checks after the refactor; do not rerun the
full suite, use the live MCP, release or deploy.

## Evidence boundary

CA-M-410 requires bounded resource use and explicit limits, but it does not
authorize silently changing a production readiness budget. The current
diagnosis was made against the canonical source and the existing bounded
test harness; no production binding, runtime image or Project authority was
changed. This Problem remains Active until the refactor and focused retest
provide a source-bound result.

## Next gate

Execute CA-P-2633 before CA-P-2634. Preserve the 90-second production Gateway
budget and report the separate sanitized ValueError hypothesis independently
if a focused retest reproduces it.
