---
atom_id: CA-C-571
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
  concern_about: [CA-P-2536, CA-P-2550, CA-P-2551, CA-O-164]
version: 1
updated_at: "2026-10-21T17:01:24Z"
---
# Summary

Resolve incomplete image-ownership cleanup after focused Local adoption

## Concern

The focused Local release installed and adopted its candidate, but the release
reported `completed_with_cleanup_pending`. Some retained images remain unknown,
incomplete or foreign from the selected Project's ownership perspective. The
cleanup boundary must be resolved without treating retention as failure of the
installed runtime and without deleting resources whose ownership or references
are uncertain.

## Evidences

Run `local-20261021-focused-adoption-01` completed with
`completed_with_cleanup_pending`, CLI1 and `failed_step: null`. The approved
focused validation selected exactly 16 host modules and recorded 131 tests, zero
skips and zero failures. Version `0.4.4.10` was installed with candidate tag
`caprmedio-runtime:0.4.4.10-20261021T131557Z-0555ed0be341`; container
`649228a677661439d12d9771d606652525480ab4a2f5ef2131036b451a1cae7e` is
healthy, `/health` is ready, and connected MCP discovery returned O164 v20.
The launcher matched image/source fingerprint `80fc2b4` and the current
Project. Durable evidence is in
`.caprmedio_runtime/simple_local_release/reports/local-20261021-focused-adoption-01.md`.

The cleanup removed the prior Project container
`e81250f8ed4c39bf08007e05449c63b88d5c96b8f65f94f6fdec8622c6817d84` and
owned images
`00a99705a531c5673fa019b125ac3c473ec16934d36c2ac00cbec9578fe286a6`,
`08f26a9b8b14b6884fb6a8011264ea2e7c99a12f687377c355e50b34c2e4f929`, and
`c189bc1a31fc7da3513249e334b2498a8d4ad9d6ee3e32bb9c67d9b3884b3062`.
Unknown, incomplete and foreign resources were retained, including
`650023dd711fad2e48a3446b2780733d20881adbe088a8f63a09af48f938fd83`; no
force or broad prune was used.

The separate selected-workflow cleanup Run
`local-release-cleanup-problem-20261021-01` was observed ENQUEUED and was
then officially cancelled through the SDK as CANCELLED, with no child cascade
and no observed effect. The post-cancellation purpose-built observer reports
scheduler status CANCELLED while retaining a stale `outcome: queued` field;
the SDK cancellation and scheduler status establish that no pending execution
remains. This cancellation does not resolve the resource-ownership concern.

## Blast radius

Only selected-Project image/container cleanup and its evidence receipts are in
scope. Preserve the installed healthy runtime, foreign/unowned/incomplete
resources, references, volumes and host evidence. No force, prune, worker start,
queue drain, replay, release retry or whole-Epic closure is authorized.

## Next bounded action

CA-P-2551 is the Backlog follow-up under CA-P-2536. It must inspect exact image
and container ownership/reference evidence and remove only positively identified
eligible resources, or retain them with an explicit disposition. Keep this
Problem Active until that receipt exists.
