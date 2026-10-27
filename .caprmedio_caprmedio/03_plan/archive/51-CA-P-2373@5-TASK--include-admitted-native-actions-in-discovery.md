---
atom_id: CA-P-2373@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 51
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 5
updated_at: 2026-10-24 06:12:26 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
tier: 3
---
# Summary

Include admitted native Actions in discovery

## Objective

Discovery and execution context associate an admitted native Action with its existing exposed selected route.

## Details

Reuse CA-D-547's exact native_action_calls binding alongside ordered_actions in the shared capability catalog under CA-R-1810, CA-R-1805 and CA-R-1806. CA-O-030 belongs to update_atom even when it is not an ordered Action. Preserve selected-manifest admission, source freshness and actual exposed-server-frontier checks. Do not create a standalone native Action endpoint, invent a schema, refresh source pins, publish a manifest or claim installed readiness.

Bound implementation to capability_discovery/service.py and focused discovery tests. Keep unrelated dirty work unchanged. Root owns integration and Git. Estimated own work: up to 15 minutes; split before exceeding it.

### Definition of Done

A regression test fails before the correction and passes after it. Through the shared discovery/context paths, an admitted and exposed update_atom includes CA-O-030 exactly once. Unexposed routes, invalid or stale manifests and unrelated native Actions do not gain availability. Existing discovery checks pass. A different reviewer accepts the actual change and its bounded evidence; live MCP activation remains separate.

### Verified implementation checkpoint

The shared catalog now includes source-admitted native_action_calls in the existing route's action_ids with stable deduplication. CA-O-030 is associated with update_atom, not a new standalone endpoint. Current manifest admission, exposed-server checks and route-bound context schema remain unchanged. Independent connected-code review passed.

The regression failed before the correction (CA-O-030 had zero MCP matches) and all four focused tests pass afterward. They check shared discovery/context, native/ordered overlap, unexposed routes, stale/invalid/unavailable loader evidence, source-only Actions and empty native calls. Service SHA-256: `55e24c1d405b62836f5679ad264b661a6eebc89d7fdd99ed096716f071e7ddaf`; test SHA-256: `4d548840a4e0c8efab54209ece99820c0ef0f37e6ee9010f5bbb592a633f2712`.

The nearby existing service suite ran 39 checks: 31 passed, three failed and five errored. Two MCP discovery suites ran seven checks: five passed, one failed and one errored. All ten failing/error cases reproduce with the pre-change method substituted in memory: direct-release expectation drift and missing legacy O199 fixture paths are unrelated to the native association correction. They are not waived or called passing. This Task remains Active because its existing-suite acceptance condition is not yet satisfied; do not broaden Subject migration into unrelated release or legacy changes without a demonstrated need.

No production manifest, installed MCP, source authority, Session, Journal, staged candidate or live Atom was changed by this correction.


### Final acceptance — 2026-10-14

The existing-suite condition now passes after test-only fixture correction. Selected-route admission/frontier cases use create_atom/O127/O128, preserving positive, stale, absent and unexposed assertions; direct release has its own checks. Retired O199 fixture bytes come from its exact archive. Previously no-op malformed-binding cases now accurately test internal-only non-exposure; actual malformed/ambiguous O200 coverage remains intact. Production discovery code, release behavior, authorities and manifests were not changed by this fixture repair.

Author verification passed 68 checks: 39 service, 12 implementation server, four native association, seven MCP discovery and six direct-release fixture checks. Root independently reviewed all three test diffs and reran 63 affected checks successfully. The original regression and independent native-association code review remain valid. Only this bounded Task is Done; installed MCP activation and migration remain separate.
