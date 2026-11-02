---
atom_id: CA-P-2513
content_role: Plan
type: Plan
label: Task
work_sequence_number: 73
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2401]
version: 5
updated_at: "2026-10-21T01:18:09Z"
---
# Summary

Run local release and verify the installed MCP health page

## Objective

Execute the expressly authorized normal local release and verify actual installed MCP adoption.

## Details

At most 15 minutes own work; split before extending. Depends on reviewed P2512 and the normal full release gates. At most 15 minutes own coordination work; automated gate elapsed time may be longer. Run the existing host command without push/public release/merge. Preserve pending/uncertain Runs and never replay held batches. Verify the new image/endpoint and browser health page plus its machine readiness and a safe real read-only MCP invocation after startup; no mutation test traffic on production. Record actual release receipt, installed version/fingerprint, remaining Problems and unfinished cleanup. Acceptance: successful normal release plus actual endpoint evidence, or truthful failed/blocked status; no false completion.

### Verified checkpoint and dependent review

Dependency review: P2512 preflight is Done following frozen implementation/fixture acceptance and both independent reviews. Execute the normal host local release with run ID local-20261021-mcp-health-0434 using the locked launcher virtualenv, managed Python3.14, no-sync/no-env-file and -B. Normal flow commits all eligible current changes and runs the complete suite before image/install/startup. Stop honestly on any failed gate; never waive tests or replay held work. After success inspect the actual installed image/version, same-port JSON/HTML health and fresh read-only MCP observations. Release has not started at this activation; no completion/deployment claim.

### Environment preparation correction and fresh release review

The first local release local-20261021-mcp-health-0434 committed eligible changes at01ec043df, validated inputs, then exposed missing launcher dependencies (mcp/anyio) at tests. Root interrupted only that verified release; exit130/report/log are retained, owned suite parents exited, and no install/startup or production replacement occurred. The earlier Python-version-only preflight was insufficient; focused health tests used the separate populated .venv. CA-C-556 records this environment defect and its bounded repair.

The actual selected launcher virtualenv is now synchronized with unchanged uv.lock/all groups. The exact no-sync launcher invocation imports all required runtime/test libraries successfully. UV_CACHE_DIR is explicitly the project-local .caprmedio_tmp/cache/uv because the inherited shared cache had a missing wheel entry; no shared cache was deleted. P2512 preparation is corrected and Done. P2513 remains Active for fresh run local-20261021-mcp-health-verified-env, rerunning every full gate from the beginning. This is a newly authorized local-release attempt, not replay of an uncertain MCP call or held Workflow. Production remains the original healthy container; no gate bypass or release-completion claim.

### Failed full gate retained and repaired dependencies reviewed

The environment-verified attempt ended failed at tests:424 modules,3796 tests,zero skips,six failed modules; launcher integration passed. Its complete report/log and candidate commit5420b2df6 are preserved. No copy/install/startup phase ran. P2514 and P2515 are Done after release-env focused tests and independent final reviews; C557 fixture-only closure is accepted. C558/P2516 canonical Draft predecessor lookup and C559/P2517 masked Plan preview remain pending source/regression acceptance. Do not restart this Task's release execution until both are reviewed, final frozen integrated checks pass and a fresh run ID is recorded. Production remains unchanged; no failed gate is waived or held/uncertain operation replayed.

### Canonical Draft lookup dependency accepted

P2516 is Done and C558 Resolved after independent source/nested-test review, bounded9 positive checks and root broader20/20 lifecycle checks. The candidate still requires C559/P2517 frozen fixture closure and remaining Plan transition diagnosis, final bound integrated tests and a fresh complete normal local release. No failed/full prior report is reused as acceptance, and no new release has started.
