---
atom_id: CA-P-2453@3
content_role: Plan
type: Plan
label: Task
work_sequence_number: 42
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on:
  - CA-P-2452
relations:
  is_decomposition_of:
  - CA-P-2401
version: 3
updated_at: '2026-10-20T14:36:42.000Z'
---
# Summary

Rerun the isolated public cases on the fresh candidate

## Objective

Run the three selected isolated public cases against the exact new candidate from CA-P-2452 and record production equality without touching production.

## Details

Proceed only after CA-P-2452 supplies the fresh immutable candidate and exact source/image receipt. Bind the isolated harness to that candidate, execute the three public cases, and capture actual pass/failure/skip results, canonical output checks, and `production_equal` evidence. Stop on an isolation or provenance failure; do not fall back to the prior candidate, replay historical requests, or replace production.

The fresh candidate identity is image `febd5bcc189e3eda2b4926206beb23f26d26c7757092580b0ddf56705ac0aac9` with source fingerprint `b71c2770aef150235984df90e4e0984e17d2b7e8d7a8169ac8de15b3763a15b8`. Host proof currently records 128 affected checks: prior 66 plus base 48 plus stage 14. The scratch runtime label `p2439-e7s6sznn` is execution context only; its reused wrapper label is historical context and is not completion of CA-P-2439 or this Task.

At most15minutes ownwork, split before extending. Preserve the exact candidate, fixture, project, port, state namespace, and receipt. No production MCP/Docker replacement, Git mutation, public release, or full-local-release claim is made by this Task.

### Definition of Done

A fresh receipt identifies the exact candidate and records all three isolated public cases, their actual outcomes, canonical-output checks, and production equality. Only a passing receipt can unlock CA-P-2454; this Task does not claim deployment or full-release acceptance by plan alone.

### Required execution guard

The exact script guard must run all three isolated cases against this candidate and record `production_equal: true` with actual outcomes. Do not close this Task from host checks or the unknown scratch-runtime outcome alone.

### Completion checkpoint

Fresh receipt `.caprmedio_tmp/mcp-audit-20261020/isolation/execute/p2439-e7s6sznn/receipt.json` records 3 tests, 0 failures, 0 errors, 0 skips, duration `217.438s`, and `production_equal: true` for image `febd5bcc189e3eda2b4926206beb23f26d26c7757092580b0ddf56705ac0aac9` with source fingerprint `b71c2770aef150235984df90e4e0984e17d2b7e8d7a8169ac8de15b3763a15b8`. The affected host proof is 128 checks (`66 + 48 + 14`). This closes the isolated-case gate only; no full-suite, deployment, or release acceptance is claimed, and the reused P2439 wrapper label does not rewrite historical CA-P-2439.
