---
atom_id: CA-C-567
content_role: Concern
type: Question
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: medium
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-P-2537, CA-P-2536, CA-O-164]
version: 1
updated_at: "2026-10-21T12:06:05Z"
---
# Summary

Verify failed launch and interrupted test network disposal

## Concern

Can Project-launcher startup failure before any labelled container, or forced interruption before fixture finally completes, leave owned Docker networks behind? Reproduce each boundary before deciding a minimal repair. This is an unproven recurring-risk question, not attribution of the 25 historical unknown-owner networks.

## Evidences

P2539 source review: test_project_launcher_docker_e2e._cleanup skips Compose down when backend.inspect finds no labelled container; Compose up could create a network first. Existing Runtime.stop intentionally retains production state. local_release_test_process eventually kills the owned process group after its grace period, potentially bypassing fixture finally. Ordinary, selected and first-cut fixtures already perform scoped down on normal and partial-failure paths. The failed release's attempted anonymousHTTP networks never materialized; inventory cannot link the old empty networks to these paths.

## Blast radius

Future test-resource lifetime and release reliability. Separate reproduction/functional coverage must preserve live/readiness-failed production runtimes, other Projects, unknown ownership, volumes and no-prune/no-force guards. Do not add automatic production rollback or broader cleanup based only on this hypothesis. Current recovery/full-release acceptance remains separate.
