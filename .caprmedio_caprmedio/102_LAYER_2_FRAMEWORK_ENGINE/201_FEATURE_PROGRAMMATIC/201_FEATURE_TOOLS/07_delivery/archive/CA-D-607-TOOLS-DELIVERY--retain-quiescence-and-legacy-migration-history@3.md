---
atom_id: CA-D-607
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-10 09:25:37 +0400"
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

### Predecessor evidence kinds

The publisher internally derives one predecessor binding while holding the installation lock and, for a bootstrap predecessor, the existing Framework selector lock. Its closed kind is `native_target_context` or `legacy_bootstrap_source_proof`:

- `native_target_context` binds the actual prior CA-D-600 Target Project Context and exact raw native execution selector. Existing native context fields retain their meaning.
- `legacy_bootstrap_source_proof` binds the exact raw Framework and Tool selectors, original package manifest SHA-256, original SourceContext SHA-256, immutable image digest, canonical bootstrap proof key and raw proof-receipt SHA-256. The existing retained-bootstrap reader physically verifies the original package, context, command and canary evidence. This kind admits only that reader's supported original bootstrap package shape, not arbitrary legacy packages.

SourceContext is not Target Project Context. Bootstrap coverage omits the unavailable prior native context field instead of filling it with SourceContext or a prospective context. Keep the explicit predecessor kind and actual proof bindings inside the existing canonical `evidence_json` and, where a process is observed, `observations_json`; do not introduce a second Journal or a standalone provenance registry.

The three provider queries bind that predecessor evidence, the actual Project root and instance, the prospective target context and exact prior execution selector. They hold their existing provider-owned fences through replacement. Reopen the same predecessor selectors and immutable proof before effects; edits to current development sources do not rewrite the retained predecessor's source identity. An observed bootstrap process still requires its own actual command, start, generation and acknowledged shutdown evidence. Unknown candidates, changed bindings or an unavailable query block before copy or removal; authentic bootstrap evidence alone never proves process absence.
