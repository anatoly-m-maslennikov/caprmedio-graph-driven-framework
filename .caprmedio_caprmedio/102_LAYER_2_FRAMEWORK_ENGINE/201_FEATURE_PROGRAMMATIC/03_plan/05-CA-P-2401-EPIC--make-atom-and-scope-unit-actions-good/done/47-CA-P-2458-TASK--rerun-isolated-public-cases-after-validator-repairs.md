---
atom_id: CA-P-2458
content_role: Plan
type: Plan
label: Task
work_sequence_number: 47
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: [CA-P-2457]
relations:
  is_decomposition_of: [CA-P-2401]
version: 3
updated_at: "2026-10-20T15:18:47.000Z"
---
# Summary

Rerun the isolated public cases after validator repairs

## Objective

Run the three selected isolated public cases against the exact fresh candidate from CA-P-2457 and require protected production equality before any release retry.

## Details

Start only after CA-P-2457 supplies fresh immutable source/image identity and a passing production guard. Bind the isolated harness to that exact candidate and execute all three public cases, recording actual outcomes, canonical bytes and `production_equal: true`. Do not fall back to a prior candidate, replay either historical attempt, test production or treat host-only repair checks as this gate.

CA-P-2457 supplied image `sha256:a26b88751f9e8eb57132f648e114f0af4d0c25ff5acf66a6f891f7d05fb4fab3` with source fingerprint `b95525f5be4b87c9b342f52199cd8f9260ff4206c2f130090cf63f4cc3e38f76`; its prelaunch source/image/compose inputs were unchanged and production snapshot equality was `true`. The three-case runner label `p2439-tc7gaqat` was execution context only; the final receipt below is the authoritative outcome, and no historical wrapper completion is inferred.

At most15minutes ownwork, split before extending. Preserve project, port, state namespace, receipt and rollback identity. No deployment, public release or full-local-release action is authorized by this Task.

### Definition of Done

A fresh receipt records all three isolated public cases, exact candidate provenance, zero unexpected failures/errors/skips and protected production equality. Only that passing receipt unlocks CA-P-2459; no deployment or release completion is inferred.

### Completion checkpoint

Receipt `.caprmedio_tmp/mcp-audit-20261020/isolation/execute/p2439-tc7gaqat/receipt.json` records 3 tests, 0 failures, 0 errors, 0 skips, duration `215.658s`, protected production equality `true`, `production_endpoint_tested: false`, and `historical_replay: false`. It uses image `sha256:a26b88751f9e8eb57132f648e114f0af4d0c25ff5acf66a6f891f7d05fb4fab3` with source fingerprint `b95525f5be4b87c9b342f52199cd8f9260ff4206c2f130090cf63f4cc3e38f76`. This closes the isolated gate only; no full-suite, deployment, release or Epic completion is claimed.
