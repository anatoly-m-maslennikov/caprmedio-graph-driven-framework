---
atom_id: CA-O-222@1
content_role: Operations
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
type: Action
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-14 18:37:38 +0400"
subjects:
  governs: "Append Change Records"
  depends_on: [Journal, Journal/Record, Operator]
relations: {}
---
# Summary

Append Journal change records

## Scope

An authorized Project-local APPEND_CHANGE_RECORDS request containing supplied actual Journal observations.

## Claim

Append Change Records **means** the reusable Action that appends supplied actual observations through the shared Project Journal library, **without** performing the recorded source/lifecycle operation **or** a Git effect.

## Action

1. Bind the actual authorized Project caller **and** existing Journal location inputs. Treat supplied record values as observations, **not** permission **or** proof; do **not** invent an Actor, session, time, prior event, baseline, result **or** replacement reference.
2. Dry run changes nothing. Authorized apply appends the supplied data through the existing shared library. Each explicit append is an append, including repeated data; no prior-history, chain, schema/digest validation, canonical receipt, deduplication, retry **or** recovery prerequisite applies.
3. Preserve existing entries as recorded **and** retain truthful I/O failure **and** any observed partial append. Do **not** automatically retry, replay a source effect, acquire a Git-effect lease, alter the index **or** create a Commit.

## Details

CA-R-812 **and** CA-R-1491 govern plain append/read; CA-D-009, CA-D-340 **and** CA-D-435 serialize supplied observations. Existing Journal readers return stored data **without** migration, repair **or** historical replay. The supplied source-authoring action identity is payload data, **not** silently replaced by this Action definition's ID. The appender creates no additional Workflow Run, Session **or** approval record. Source mutation, replacement correctness, permissions **and** Git effects retain their independent governing rules.
