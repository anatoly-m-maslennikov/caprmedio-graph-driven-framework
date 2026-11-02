---
atom_id: CA-P-2610@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 12
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
version: 2
updated_at: '2026-10-22T18:25:05Z'
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2581
  depends_on:
  - CA-P-2596
  - CA-P-2597
  relates_to:
  - CA-C-581
  - CA-R-1527
  - CA-R-1843
  - CA-R-1845
  - CA-M-328
  - CA-D-544
  - CA-O-016
  - CA-O-018
---
# Summary

Repair bounded Integrated frontier response carriers

## Objective

Repair the observed third `Store.complete_receipt` failure in the current
Interactive continuation path without changing the Workflow contract or
replaying completed Actions. Keep the response carrier thin, immutable and
bounded while retaining compact verified references to the actual response and
evidence in the same existing Run root.

## Details

The bounded implementation is owned by the continuation-receipts worker and
must remain within 15 minutes of own work; split before expanding. Reuse the
existing public Store APIs and Run-root ownership. Preserve exact duplicate
receipt behavior, reject conflicting or tampered submissions, and make crash
and restart recovery leave already verified receipts intact without replaying
effects. Do not replace the frozen full-source reproduction with a reduced
fixture, discard the 241,788-byte response, or infer success from a projection.

Use frozen inputs and the root-controlled isolated harness only. Add at least
three response-focused functional tests covering successful bounded writes,
duplicate/conflict handling, and crash/tamper/restart recovery. Keep source
fixture integrity, implementation behavior, and runtime admission as separate
evidence. No Docker, live MCP, production state, full suite, release,
deployment, Journal rewrite or Git publication is authorized by this Task.

### Definition of Done

The existing Run root accepts the bounded response-carrier sequence through the
public Store API, with compact verified references and immutable retained
receipts; exact duplicates are safe, conflicts are refused, and crash/tamper/
restart checks preserve prior verified state without replay. At least three
focused response functional tests pass against the frozen reproduction, and the
report records exact paths, response/evidence references, remaining limits and
the separate complete real-Manifest/runtime-admission gate. Review the next
dependent Task after these checks; do not claim RMED or deployed-runtime
acceptance from this leaf alone.

### Accepted completion evidence

The bounded response-carrier repair passed the combined integrated portfolio:
52/52 checks, including 20 frontier response, concurrency and recovery checks.
The frozen full-source continuation completed three continuations successfully,
and exact-duplicate, conflict-refusal, tamper and restart behavior passed
without replaying completed Actions. This closes the response-carrier
implementation leaf only; the final public MCP privacy check and separate
runtime-admission and manifest gates remain outside this Task.
