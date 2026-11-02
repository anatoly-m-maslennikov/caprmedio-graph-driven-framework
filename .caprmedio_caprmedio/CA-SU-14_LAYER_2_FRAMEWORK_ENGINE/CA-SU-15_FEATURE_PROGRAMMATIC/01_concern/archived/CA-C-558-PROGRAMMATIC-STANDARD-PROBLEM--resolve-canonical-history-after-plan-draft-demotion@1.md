---
atom_id: CA-C-558
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
  concern_about: [CA-P-2513, CA-P-2516]
version: 1
updated_at: "2026-10-21 05:09:06 +0400"
---
# Summary

Resolve canonical history after Plan Draft demotion

## Concern

A Plan can be successfully demoted to Draft and then incorrectly reported failed because the caller reconstructs the superseded predecessor path.

## Evidences

The completed full gate failed test_selected_w04_fixture.py with not-markdown-atom at PARENT/03_plan/archive after native Draft publication. Static source comparison confirms lifecycle_intents._publish_status_change hardcodes local/archive, while atom_operations publisher retains Plan predecessors in the owning Scope Unit shared03_plan/archived. This is a production caller lookup defect, not a stale fixture to waive or migrate. The native demotion effect can already exist when the lookup fails.

## Blast radius

CA-P-2516 owns bounded diagnosis/repair with a focused regression and independent review. Reuse canonical owners, preserve non-Plan and contained-history behavior, source-currentness/refusal and exact predecessor/recovery claims. No manually added legacy archive path, weakened matrix or swallowed exception may conceal the issue. Production MCP remains unchanged; all reproductions use disposable fixtures and no held or uncertain Run is replayed. A fresh complete normal local-release gate is required before installed acceptance.
