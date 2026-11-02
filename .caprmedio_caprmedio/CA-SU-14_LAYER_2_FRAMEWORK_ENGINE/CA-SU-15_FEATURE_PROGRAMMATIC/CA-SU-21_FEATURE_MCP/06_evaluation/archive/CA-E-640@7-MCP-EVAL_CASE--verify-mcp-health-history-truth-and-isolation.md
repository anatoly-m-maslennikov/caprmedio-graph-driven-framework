---
atom_id: CA-E-640@7
content_role: Evaluation
type: Eval Case
current_scope_unit: MCP
claim_target_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-24 12:35:51 +0400
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  depends_on: []
relations:
  evaluation_for:
  - CA-R-2007
tier: 5
---
# Summary

Verify MCP health history truth and isolation

## Scope

The changed MCP health route, bounded Gateway observer and HTML representation under CA-R-2007.

## Claim

Accept the health increment only when isolated functional checks demonstrate preserved machine readiness, truthful bounded Tool/Workflow observations, escaped safe HTML and no diagnostic-GET execution effects. A green gateway check or scheduler success alone is not functional Tool/Workflow acceptance.

## Details

- Use disposable independent Project fixtures and an isolated ASGI app or distinct nonproduction listener/state. Do not test mutations on the production MCP port or use mutable live Atoms as a golden oracle.
- Verify default/JSON/* Accept returns the existing ready boolean shape and 200/503 semantics; explicit HTML returns the browser view with the same readiness status. Missing/dead generation is 503. Hostile Host/Origin requests retain 421/403 and cause no Tool/reload effects.
- Exercise real Gateway call routing for returned, rejected, failed, partial and uncertain observations. Preserve actual outcomes and no-replay behavior. Unknown/unobserved state is explicit; a returned RPC is not a fabricated terminal domain result.
- Verify known Workflow identities and separate scheduler_status from actual outcome/disposition, including scheduler SUCCESS with actual interrupted_pending or unknown. Health reads do not poll DBOS/Docker, invoke a provider, replay a call or change execution records.
- Overflow both histories and verify at most 32 observations each, deterministic eviction, bounded field sizes, concurrent-call isolation, since-start scope and restart reset. No cross-process completeness claim is made.
- Inject hostile names, diagnostics, credential-like arguments and path-bearing provider exception text. Verify HTML escaping and absence of raw arguments/results/secrets/paths/provider messages; only the admitted safe fields/error categories appear. Check healthy and failed representations against the same snapshot contract.
- Retain exact candidate/fixture bindings and actual outcomes. Focused passing tests do not replace the normal full local-release gates or prove installed adoption; verify the installed page separately after the authorized release.
