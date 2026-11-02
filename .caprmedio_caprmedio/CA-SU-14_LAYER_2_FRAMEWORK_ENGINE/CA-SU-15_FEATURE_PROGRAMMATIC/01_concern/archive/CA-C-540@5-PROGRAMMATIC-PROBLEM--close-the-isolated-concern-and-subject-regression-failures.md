---
atom_id: CA-C-540@5
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
priority: high
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2439, CA-P-2437]
version: 5
updated_at: "2026-10-20T14:09:53.000Z"
---
# Summary

Close isolated Concern and Subject regression failures

## Concern

The selected isolated Docker/MCP gate failed two new regression cases. The 29 supported Role/Status creation pairs passed, but Concern relation creation interrupted and the approved double-slash Subject case errored. Fixture/call defects have not yet been distinguished from implementation defects; this is not a claim of two reproduced production failures.

## Evidences

Final candidate image sha256:4adc89a63bcd79c56bd3ef6eda2a118e852eee89ebadd5d0b31b6eae34fc5b10, fingerprint942d1eb4b1618ccaf6d4960790f48d052a1c465a8151c666ef67392b8073f93e. First isolated receipt .caprmedio_tmp/mcp-audit-20261020/isolation/execute/p2439-_e0nsgim/receipt.json records3tests,1failure,1error,0skips and exact production snapshot equality. The Concern run stopped at nested CA-O-032 with interrupted_pending. A fresh diagnostic-only fixture run retains full traces and fake-project records; no historical production request was replayed.

### Diagnostic checkpoint

The bounded read-only diagnosis separates two fixture/client causes from any production claim: the disposable Subject-test client initialization surfaced `AttributeError`, and the retained isolated Concern fixture is missing D378 required for the frozen identity-authority check. The admission receipt records the interruption without a chained cause. Runtime verification remains pending in P2439; this update does not accept a runtime pass, reproduce a production failure, or close the release gate.

### Follow-up diagnostic checkpoint

The fresh read-only disposable receipt `.caprmedio_tmp/mcp-audit-20261020/isolation/execute/p2439-2_q41z2v/receipt.json` records 3 tests, 2 failures, 0 errors, 0 skips, and all 29 matrix cases passing, with `production_equal: true`. Frozen D378 was supplied, so the earlier D378-only diagnosis is insufficient: the Concern remains the first Active target and fails with `LifecycleError`. The Subject reaches preview and then reports `subject-grammar-pin-stale` because the exact grammar source cannot be read at the selected location. This narrows the next preflight work but does not claim a product cause, validation weakening, runtime acceptance, or release closure.

### Confirmed diagnostic chain

Read-only `prepare_create_atom_revision` on retained fixture `tmpn5hzd7v1` reproduces `_validate_complete_carrier->validate_proposed_carrier:459->_frontier_status_folders:246->_source:148`; the first missing frontier source is D434. `ToolError complete-carrier-invalid` wraps `ProposedCarrierError requiredsourceunreadablechangedorinactive`. D378 is present exactly; other missing frontier sources are D467, R1608, R1875, R1309, R1397, R1398, R1399, and R1874. This confirmed chain supersedes the incomplete D378-only diagnosis but remains diagnostic evidence, not a product cause or runtime acceptance. The final full-pass resolution below supersedes this earlier Active-state boundary.

### Resolution checkpoint

Final receipt `.caprmedio_tmp/mcp-audit-20261020/isolation/execute/p2439-1q3i92q7/receipt.json` records 3 tests, 0 failures, 0 errors, 0 skips, `production_equal: true`, all 29 matrix pairs passing, Current Concern Active/Done/Canceled coverage, and `//subjects` preview with stage canonical bytes unchanged. Image `2c2c218b561ff9868d2e6648c32b6ac0c6bb7df587d340cf6134e54bee03c427`, fingerprint `d08ba9be7c5d275a5c72e77c24e8a3994cf63ab194f88ff71a4b2426ee0591e6`, and admission `p2410-20261020T140246Z-202e3399` are retained. The earlier failures are resolved by fixture-only causal corrections; no product bugfix or deployment claim is made. C540 is Resolved as a planning concern after this bounded isolated pass, not as public-release approval.

## Blast radius

The conditional release gate was held until the causes were explained, selected public cases passed, and production isolation was reverified. The final pass resolves this planning concern; deployment and public release remain separate, and validation must not be weakened.
