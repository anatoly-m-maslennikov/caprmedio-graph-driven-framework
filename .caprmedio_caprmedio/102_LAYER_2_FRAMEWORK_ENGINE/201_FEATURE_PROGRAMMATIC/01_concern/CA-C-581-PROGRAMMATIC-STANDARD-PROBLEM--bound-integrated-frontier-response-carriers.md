---
atom_id: CA-C-581
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
  concern_about: [CA-P-2610, CA-P-2581, CA-O-016]
version: 2
updated_at: "2026-10-22T18:25:05Z"
---
# Summary

Bound Integrated frontier response carriers within the existing Run root

## Concern

A bounded full-source Interactive continuation reproduction cannot persist its
third completion receipt. The first two `Store.complete_receipt` calls succeed,
but the third raises `IntegratedFrontierError: state exceeds 512 KiB`. This is a
bounded response-carrier failure in the current Workflow continuation path, not
evidence that the Workflow completed or that the whole runtime is unavailable.

## Evidences

The frozen reproduction contains 40 Method rows and produces a 241,788-byte
response. In one root-controlled isolated Run, the first two completion-receipt
writes succeed and the third fails at the existing 512 KiB state boundary with
`IntegratedFrontierError`. The reproduction used no Docker, MCP endpoint or
production state. It establishes a persistent bounded full-source interactive
Run failure for the current `CA-O-016@18` Workflow/continuation behavior only.

This is an observed implementation/fixture result, not proof that any RMED
source authority is satisfied, nor proof of deployed runtime behavior. Preserve
the exact frozen inputs, response bytes, exception and existing Run-root paths;
do not convert the failure into a guessed schema, a new Workflow rule or a
successful receipt.

## Required disposition

Repair the response-carrier boundary under CA-P-2610 using the existing public
Store API and the same existing Run root. Keep carriers thin, immutable and
bounded; retain compact verified references to the actual response/evidence
instead of silently dropping, truncating or rewriting it. Preserve exact
duplicate behavior, reject conflicting receipts, and retain crash, tamper and
restart safety. Re-run focused functional checks against frozen inputs only.

No production MCP call, Docker action, full-suite run, release, deployment,
uncertain replay or RMED promotion is authorized by this Problem. Keep the
separate complete real-Manifest and runtime-admission gates visible.

## Blast radius

Integrated Workflow continuation, completion-receipt persistence, retained
partial results and reconnect/recovery behavior in the selected Run root. The
failure may block later continuation while leaving earlier verified receipts
intact; it does not authorize replaying completed Actions or changing the
business Journal boundary.

## Resolution

CA-P-2610 completed the bounded response-carrier repair. The combined integrated
portfolio passed 52/52 checks, including 20 frontier response, concurrency and
recovery checks. The frozen full-source continuation completed three
continuations successfully; exact duplicates, conflicting submissions, tamper
and restart behavior were handled without replaying completed Actions. The
third-receipt boundary is no longer reproduced in the accepted isolated path.

This Problem is Resolved for the observed bounded carrier failure. The final
public MCP privacy check and separate runtime-admission and manifest gates are
still independent; this resolution does not claim public deployment or RMED
promotion.
