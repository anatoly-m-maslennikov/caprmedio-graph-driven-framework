---
atom_id: CA-P-2440@9
content_role: Plan
type: Plan
label: Task
work_sequence_number: 29
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on:
  - CA-P-2459
relations:
  is_decomposition_of:
  - CA-P-2401
version: 9
updated_at: 2026-10-24 08:06:50 +0400
tier: 3
---
# Summary

Replace the approved MCP image after isolated proof

## Objective

Complete one bounded Epic CA-P-2401 responsibility with truthful source, fixture and runtime evidence.

## Details

Human explicitly approved replacing running MCP only after isolated tests pass. Use canonical deployment with exact reviewed digest, production Project binding and preserved state, inspect readiness and immutable parser provenance; keep a rollback target. Coordinate Methodology safe handoff and never replay/reset the stopped batch. No broad release/auto-commit authorization inferred.

Use the PROGRAMMATIC M projection. At most15minutes own work; split dependent Tasks before extending. Preserve concurrent edits, exact predecessors and selected uv-managed environment. Review/update dependent Task before execution.

### Definition of Done

Bounded deliverable and reproducible checks are recorded, with runtime effects and limitations explicit.

### Explicit release authorization

The Operator answered Yes—use the full local release to the separate question naming automatic commits of all current changes including otherchat changes. This authorizes the normal localrelease flow only after isolatedtests pass; coordinate source/Git freeze, preserve stoppedbatchstate and record actualphase results/readiness. No publicrelease/push/merge authorization is inferred.

### Latest review gate

The final isolated receipt `.caprmedio_tmp/mcp-audit-20261020/isolation/execute/p2439-1q3i92q7/receipt.json` records 3 tests, 0 failures, 0 errors, 0 skips, `production_equal: true`, all 29 matrix pairs passing, Current Concern Active/Done/Canceled coverage, and `//subjects` preview with stage canonical bytes unchanged. The human explicitly approved the full local release flow including all current changes, with source freeze and the full-release approval gate recorded. This Task remains unexecuted: no MCP replacement, deployment, public release, or Git action is claimed here.

### First-attempt checkpoint

The first full local release attempt after the isolated gate failed in tests and was intentionally interrupted with exit 130 (`KeyboardInterrupt`). Root recorded Git checkpoint `c1df`, and the old production state was verified unchanged. The actual retry is delegated to CA-P-2454 after the new CA-P-2453 isolated gate passes; no historical replay or release success is claimed here.

### Successor dependency checkpoint

The second full local release terminal also failed; its bounded runner and frozen-fixture repairs are CA-P-2455 and CA-P-2456, followed by fresh build CA-P-2457, isolated gate CA-P-2458 and release retry CA-P-2459. This replacement Task now depends on CA-P-2459 and remains Active/unexecuted. No MCP replacement, deployment, readiness proof or installed-runtime resolution is claimed.

### Verified replacement and release checkpoint

The approved full local release completed successfully. Proof `.caprmedio_tmp/mcp-audit-20261020/continuation/local-release-verified-20261020.json` and canonical receipt `.caprmedio_runtime/simple_local_release/reports/local-20261020-current-target-parser-repair-1521.md` record version `0.4.4.8`, 410 modules, 3680 tests, zero skips/failures and a passing final isolated launcher. The released image is `sha256:a26b88751f9e8eb57132f648e114f0af4d0c25ff5acf66a6f891f7d05fb4fab3` with source fingerprint `b95525f5be4b87c9b342f52199cd8f9260ff4206c2f130090cf63f4cc3e38f76`; healthy container `b1676bbd01e451f6bf5b32237bdc0d44147dbcc7f9da43638ca8de724a939d44` serves port `56317`, the old container is absent and the old image was removed by the approved release. Parser `6b377172306c9a6aa662f8436885aeee51922e9980606d08d70b0dc2273c0329` was verified in both the released package and the container. This closes the separately authorized replacement responsibility; it does not claim public release, merge, historical batch replay or completion of the broader Epic.
