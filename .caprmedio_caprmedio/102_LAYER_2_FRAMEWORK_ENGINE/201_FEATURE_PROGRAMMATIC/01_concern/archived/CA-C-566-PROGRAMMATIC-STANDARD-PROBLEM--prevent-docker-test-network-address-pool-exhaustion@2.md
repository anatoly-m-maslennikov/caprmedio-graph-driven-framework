---
atom_id: CA-C-566
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
  concern_about: [CA-P-2401, CA-P-2536, CA-P-2537, CA-O-164]
version: 2
updated_at: "2026-10-21T12:06:05Z"
---
# Summary

Prevent Docker test network address-pool exhaustion

## Concern

The actual Local-release suite cannot create required disposable Compose networks because Docker reports all predefined address pools fully subnetted. Determine positively attributable unused test resources and the canonical cleanup-lifetime gap before repairing or retrying. Do not infer permission to prune all networks or alter Docker daemon address-pool settings.

## Evidences

Run local-20261021-isolated-gate-114321 log .caprmedio_tmp/simple_local_release/local-20261021-isolated-gate-114321-tests-n4u1m0et.log records test_docker_e2e.py anonymousHTTPstartup RuntimeError during networks caprmedio-d7866cf7f7c2_http_publication/runtime creation. Module3tests/1error135.597s; crash-publication25tests passed397.444s. Root intentionally interrupted exactownedreleasePID96380 after failedgate; terminalreportfailed/tests/KeyboardInterrupt is not the underlying Docker failure. Prior release attempts also used disposable Compose Projects; stale-network ownership and exact origin remain unproven until inspection.

## Blast radius

Isolated test infrastructure and ability to complete the full Local-release gate. No evidence of production MCP failure; preserve working MCP, foreign/unknown/referenced networks, volumes and installedimage. Release remains uninstalled. Root owns exact validated cleanup only; no broadprune, force, inferredownership or unrelated daemon reconfiguration.

### Actual result and next boundary

The Operator explicitly approved deleting the exact 25 empty networks despite unrecoverable Project ownership. Root verified full ID/name/Compose labels, zero endpoints and absence of references from every container immediately before each non-force removal. All 25 IDs are absent; no other unknown network was selected. Separately, two exact failed-attempt containers, their one network and uniquely labelled unused test image were cleaned after release processes exited; volumes and host evidence retained. Production e812/08f/network6e489 remain healthy unchanged; five networks now remain. Existing ordinary test teardown already calls scoped down; no current normal-path leak is proven. C567 records unproven failed-start/forced-interruption edge cases. P2541 validates recovery before fresh full release.
