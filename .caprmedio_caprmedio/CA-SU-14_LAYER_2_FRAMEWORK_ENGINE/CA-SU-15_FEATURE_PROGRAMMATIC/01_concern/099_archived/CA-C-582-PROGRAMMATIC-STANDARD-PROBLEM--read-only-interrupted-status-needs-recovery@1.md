---
atom_id: CA-C-582@1
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
  concern_about: [CA-P-2601, CA-P-2581, CA-O-016]
version: 1
updated_at: "2026-10-22T19:29:13Z"
---
# Summary

Read-only interrupted status requires recovery

## Concern

The strengthened isolated continuation run accepts a terminal submission with
the canonical terminal/interrupted_pending disposition and an
interrupted_pending graph result, but the final public status is blocked
with the message "selected checkpoint interruption requires explicit recovery".
The public read-only status therefore does not expose the accepted
interrupted state without a recovery action. This is a current status and
recovery-surface problem, not permission to replay a completed Action or to
change the business Journal.

## Evidences

The root-controlled isolated current-Workflow fixture reproduced the sequence
after the prior 4/4 journey result: terminal submission validation retained
the canonical terminal/interrupted_pending state and graph result, while the
public status path returned blocked and required explicit recovery. The
observation is bounded to the tested source-bound workflow and nonproduction
state; it does not establish current Project binding, runtime admission,
deployment or production MCP behavior.

## Required disposition

Add a bounded read-only status/recovery check under CA-P-2611. Preserve the
accepted terminal/interrupted_pending result, expose it consistently through
the public status read, and make recovery/replay behavior explicit. Verify
that a read-only status request does not mutate the Run, replay completed
Actions, or silently convert an interrupted result into a successful
completion. Keep the existing public API and business-only Journal boundary.

No production MCP call, Docker action, full-suite run, release, deployment,
uncertain replay or RMED promotion is authorized by this Problem.

## Blast radius

Public status, reconnect/recovery and retained partial-result visibility for
the selected Integrated Workflow Run. The issue may leave a valid interrupted
Run appearing blocked until recovery, while earlier accepted receipts remain
intact.
