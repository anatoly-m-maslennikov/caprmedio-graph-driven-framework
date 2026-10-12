---
atom_id: CA-D-607
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 4
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

### Native quiescence without a legacy inventory

A native installation with none of the three legacy state directories retains its genuine provider coverage without a D605 inventory. Its carrier is `.caprmedio_runtime/installation/quiescence/<installation_lock_generation>/<quiescence_sha256>/quiescence.toml`, mode 0600. Existing legacy inventory-bound quiescence carriers keep their current schema.

The closed native carrier has `schema_version = 2`, `kind = native_process_coverage`, `target_context_sha256`, `prior_target_context_sha256`, `prior_selector_sha256`, `installation_lock_generation`, `safe`, `revalidation_error_code`, `quiescence_sha256`, `provider_coverage` and `processes`. The proof digest is the canonical JSON digest of these fields except `quiescence_sha256`. Provider rows reuse the existing ordered namespaces and canonical `evidence_json`/`observations_json`; process rows reuse the existing identity, status and reason encoding. This branch contains no migration ID, inventory digest, synthetic source-root rows or copied legacy state.

The native predecessor proof supplies the prior context and execution-selector digest; the concrete current installation lock supplies the target context and lock generation. The retained rows come from the still-open provider coverage, not a caller list. `safe` is derived from complete provider evidence and the existing process-quiescence checks. Stable absence is sufficient. An observed process needs its existing matching shutdown proof; unknown coverage or failed physical revalidation gives `safe = false`. `revalidation_error_code` is empty after successful reopening or the actual coverage error code after failure; frozen query rows are preserved as frozen observations, not asserted to be fresh after a failed revalidation.

Retain the exact observed proof before accepting or refusing the attempt. A differing observation has its own digest-named carrier; existing attempt evidence is never overwritten. Physically reopen the carrier's exact closed fields, digest, bindings, ordered rows and process decisions, together with the same held provider fences, before live Methodology publication and before package deletion or selector switch. A failed reopen retains the observed failure and blocks effects. These carriers are installation evidence, not another Journal or an authority registry.
