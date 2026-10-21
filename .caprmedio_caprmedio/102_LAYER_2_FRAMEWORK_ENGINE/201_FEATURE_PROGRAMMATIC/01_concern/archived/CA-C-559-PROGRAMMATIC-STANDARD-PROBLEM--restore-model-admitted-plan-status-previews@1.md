---
atom_id: CA-C-559
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
  concern_about: [CA-P-2513, CA-P-2517]
version: 1
updated_at: "2026-10-21 05:09:34 +0400"
---
# Summary

Restore model-admitted Plan status previews

## Concern

The Plan lane in the complete W04 status matrix is blocked before execution under the new containment observation path; its actual inner exception is hidden by the existing broad observer catch.

## Evidences

The completed full gate reports test_selected_w04_status_matrix.py Plan Draft preview blocked and aggregate23/7/7 rather than29/8/8. selected_routes.observe catches manifest/preflight/containment exceptions and resets selected/current false. The receipt echoes route versus outer manifest digests; comparing those does not establish source drift. Exact inner cause remains unknown. Current E545/D531 require all model-admitted statuses; no count or guard relaxation is accepted.

## Blast radius

CA-P-2517 owns bounded diagnosis/repair with a focused regression and independent review. Reuse canonical owners, preserve non-Plan and contained-history behavior, source-currentness/refusal and exact predecessor/recovery claims. No manually added legacy archive path, weakened matrix or swallowed exception may conceal the issue. Production MCP remains unchanged; all reproductions use disposable fixtures and no held or uncertain Run is replayed. A fresh complete normal local-release gate is required before installed acceptance.
