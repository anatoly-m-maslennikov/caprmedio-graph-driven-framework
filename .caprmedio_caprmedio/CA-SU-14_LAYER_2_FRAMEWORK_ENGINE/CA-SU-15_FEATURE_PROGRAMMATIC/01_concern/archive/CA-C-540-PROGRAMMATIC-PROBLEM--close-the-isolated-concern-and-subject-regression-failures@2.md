---
atom_id: CA-C-540
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
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2439, CA-P-2437]
version: 2
updated_at: "2026-10-20T13:49:01.000Z"
---
# Summary

Close isolated Concern and Subject regression failures

## Concern

The selected isolated Docker/MCP gate failed two new regression cases. The 29 supported Role/Status creation pairs passed, but Concern relation creation interrupted and the approved double-slash Subject case errored. Fixture/call defects have not yet been distinguished from implementation defects; this is not a claim of two reproduced production failures.

## Evidences

Final candidate image sha256:4adc89a63bcd79c56bd3ef6eda2a118e852eee89ebadd5d0b31b6eae34fc5b10, fingerprint942d1eb4b1618ccaf6d4960790f48d052a1c465a8151c666ef67392b8073f93e. First isolated receipt .caprmedio_tmp/mcp-audit-20261020/isolation/execute/p2439-_e0nsgim/receipt.json records3tests,1failure,1error,0skips and exact production snapshot equality. The Concern run stopped at nested CA-O-032 with interrupted_pending. A fresh diagnostic-only fixture run retains full traces and fake-project records; no historical production request was replayed.

### Diagnostic checkpoint

The bounded read-only diagnosis separates two fixture/client causes from any production claim: the disposable Subject-test client initialization surfaced `AttributeError`, and the retained isolated Concern fixture is missing D378 required for the frozen identity-authority check. The admission receipt records the interruption without a chained cause. Runtime verification remains pending in P2439; this update does not accept a runtime pass, reproduce a production failure, or close the release gate.

## Blast radius

The conditional release gate is closed until the causes are explained, legitimate fixes pass the selected public cases, and production isolation is reverified. Preserve diagnostic evidence; do not skip assertions, relabel incomplete Runs successful, weaken source validation or replace the running MCP before the tests pass.
