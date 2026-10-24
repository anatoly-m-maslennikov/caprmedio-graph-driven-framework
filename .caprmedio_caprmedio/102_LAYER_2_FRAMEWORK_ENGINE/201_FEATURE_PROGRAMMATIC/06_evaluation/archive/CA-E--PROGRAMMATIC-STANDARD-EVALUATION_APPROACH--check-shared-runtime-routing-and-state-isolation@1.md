---
content_role: Evaluation
type: Evaluation Approach
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Draft
subjects:
  governs: PROGRAMMATIC
  depends_on: []
version: 1
updated_at: "2026-10-20 02:55:30 +0400"
relations: {}
---
# Summary

Check shared-runtime routing and state isolation

## Scope

Evaluation design for one shared container/MCP endpoint and the chosen Project-binding mechanism.

## Claim

Use two valid Projects with their authoritative prefixes, roots/control roots, distinct configurations and model generations. Show that explicit caller context selects the correct Project and that concurrent/interleaved operations, asynchronous continuation and reload cannot substitute another Project's configuration, applicable sources, caches, locks, Run state, receipts, Journal entries, outputs or results. Shared immutable source bytes shall still resolve under each Project's correct frontier. A receipt/effect frontier for one Project shall not satisfy another Project's lifecycle admission merely because local IDs or prefix strings resemble each other.

## Details

Exercise unknown/outside-root selectors, mismatched prefix/root, ambiguous aliases or overlapping roots, stale session binding, a current-directory switch, a conflicting request context on a bound session, and the selected duplicate-prefix policy. Use identical local Run/receipt/result IDs in the two Projects and verify qualified lookup/refusal. Check that failures cause no cross-Project fallback or effects. Interleave Project removal/remapping with asynchronous continuation and path resolution; verify the retained mapping/freshness policy and no symlink or alias escape. Check model-refresh overlap, Project removal and the declared mount-change procedure. Demonstrate one container and endpoint serving both Projects under the supported lifecycle; separate per-Project containers do not establish this claim. Preserve existing admission/recovery checks. Record the one-process/shared-host limits and untested failure cases; this Draft does not claim OS-level isolation between mutually hostile workloads or an implemented service.
