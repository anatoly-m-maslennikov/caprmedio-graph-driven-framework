---
atom_id: CA-C-567
ref_id: CA-C-567@3
container:
  scope_unit: CA-SU-15
role: Concern
form: Question
topics:
  main_subject: Entity/Node/Continuant/Implementation
relations:
  concern_about:
  - CA-P-2537
  - CA-P-2536
  - CA-O-164
status: Archived
version: 3
updated_at: 2026-11-10 22:49:26 +0400
carrier_destination:
  file:
    name: CA-C-567@3-PROGRAMMATIC-STANDARD-QUESTION--verify-failed-launch-and-interrupted-test-network-disposal.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/01_concern/archive
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
priority: medium
---
# Summary

Verify failed launch and interrupted test network disposal

## Concern

Can Project-launcher startup failure before any labelled container, or forced interruption before fixture finally completes, leave owned Docker networks behind? Reproduce each boundary before deciding a minimal repair. This is an unproven recurring-risk question, not attribution of the 25 historical unknown-owner networks.

## Evidences

P2539 source review: test_project_launcher_docker_e2e._cleanup skips Compose down when backend.inspect finds no labelled container; Compose up could create a network first. Existing Runtime.stop intentionally retains production state. local_release_test_process eventually kills the owned process group after its grace period, potentially bypassing fixture finally. Ordinary, selected and first-cut fixtures already perform scoped down on normal and partial-failure paths. The failed release's attempted anonymousHTTP networks never materialized; inventory cannot link the old empty networks to these paths.

## Blast radius

Future test-resource lifetime and release reliability. Separate reproduction/functional coverage must preserve live/readiness-failed production runtimes, other Projects, unknown ownership, volumes and no-prune/no-force guards. Do not add automatic production rollback or broader cleanup based only on this hypothesis. Current recovery/full-release acceptance remains separate.

### New direct timeout evidence

The forced-termination branch now has direct evidence: selected_workflows_docker_e2e timed out at1800.064s in local-20261021-network-recovered-120901, and after the complete failed suite terminated two exact-attempt worker/agent containers plus network c55d28fd40e32fc1b60a5820d1a50444e7c36c9bf09ec06a7f8ec4168284f929 remained healthy/running. Root proved image c2805de9 and attempt ff9cb6b638a84a02a8325d6fc82679ce plus disposable fixture mount, then stopped/removed those exact containers, empty network and unused attempt image non-force. Five-network baseline and original healthy production restored; volumes/host evidence preserved, deleted container writable state/logs not backed up. This confirms one timeout-cleanup residual, not attribution of the historical25unknown networks. Failed-start-before-container branch remains unproven; no speculative production rollback was added.

## Current follow-up

This is an engineering investigation, not a pending Operator design choice. The historical project-launcher and selected-Workflow fixtures named above are absent from the current code. The shared local-release process timeout helper remains; historical leaked-resource evidence does not by itself prove a current defect in that retained path.

P2818 tracks checking the retained runner and current Docker fixtures, reproducing any applicable cleanup defect, and verifying the resulting correction under existing cleanup policies. Keep this Concern open until that evidence establishes the current outcome. No reproduction, resource removal or runtime repair was performed by this source update.
