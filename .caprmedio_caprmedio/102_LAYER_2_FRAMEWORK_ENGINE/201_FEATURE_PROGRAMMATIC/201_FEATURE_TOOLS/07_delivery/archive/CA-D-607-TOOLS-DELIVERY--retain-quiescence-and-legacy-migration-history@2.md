---
atom_id: CA-D-607
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-10 05:42:00 +0400"
subjects:
  governs: "Framework Installation contribution/Migration quiescence and retention"
  depends_on: [Tool, Runtime, Process, Journal, Project]
relations:
  delivery_for: [CA-R-1915, CA-R-1916, CA-M-363]
---
# Summary

Retain quiescence and legacy migration history

## Scope

The evidence that migration stopped only owned processes safely and preserved old N/history.

## Claim

the INSTALL_TOOLS facade **must** quiesce **only** an exactly identified owned process before migration switch and **must** retain old state and N/history when quiescence is unsafe, blocked or incomplete.

## Details

`quiescence.toml` records each proposed process's owned subtree, package/context/generation proof, command digest, start token, requested shutdown, observed response and deadline. A PID absent its matching command and generation proof is not owned. Unknown, changed, externally owned, ambiguous or non-responsive processes block migration without signaling, killing or replacing them.

`history.toml` retains prior selector bytes, N/history references, inventory digest and terminal migration outcome. It is append-only for migration attempts and does not authorize deletion. The canonical Journal records actual start and terminal evidence separately; this carrier is not another Journal.

### Process coverage

These process-coverage requirements apply to the full-package publisher defined by `CA-D-562-TOOLS-DELIVERY--bind-full-framework-runtime-installation-boundary` when replacing either an exact legacy predecessor or an exact native predecessor. Inventory and copy mapping defined by `CA-D-605-TOOLS-DELIVERY--inventory-owned-legacy-installation-subtrees` and `CA-D-606-TOOLS-DELIVERY--map-legacy-state-copy-verification-and-switch` remains limited to the three owned legacy state subtrees.

1. Quiescence evidence contains exactly one ordered provider row for each owned namespace: `project_mcp`, `mcp_hot_reload`, `workflow_orchestrator`. Bind every row to the target context, prior execution selector, exact provider namespace and its queried ownership records. Provider-owned collection holds its admission fence through the copy/switch boundary and revalidates the same coverage before replacement effects.
2. A provider row is `absent`, `observed` or `unknown`. `absent` requires a successful bounded query of that exact owned namespace with no matching live process; an empty caller list or a missing state file alone proves nothing. `observed` requires the matching identity and shutdown evidence described above for every matched process. Query failure, incomplete coverage, identity ambiguity or a changed live process yields `unknown` and blocks replacement without process action.
3. A dormant predecessor with complete provider-verified absence is valid: the installer does not require a process to exist. A typed coverage value is admitted only by physically reopening its provider evidence; the type, caller mapping or checksum alone never proves observation. Persist the exact coverage and query outcome in the retained quiescence evidence, including blocked attempts.
