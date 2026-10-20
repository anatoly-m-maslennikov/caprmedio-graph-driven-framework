---
atom_id: CA-C-529
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Resolved
priority: high
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2401, CA-R-1022]
version: 2
updated_at: "2026-10-20T15:21:00.000Z"
---
# Summary

Reconcile mechanical concern_about admission

## Concern

Complete-carrier authoring preflight for a Concern with concern_about relations reaches an unconditional unsupported-authority gap after identity, current source loading and endpoint resolution. The intended boundary between mechanically admitted governed-entity targets and semantic affectedness must be reconciled against the current Action; source relations must not be discarded merely to obtain a pass.

## Evidences

On 2026-10-20 the local read-only prepare_create_atom_revision preflight used the saved CA-C-528 carrier as a create-shaped candidate. No source was written, no native MCP execute was sent and the source hash was unchanged. It passed the earlier Concern identity and missing D305 locator gates, then refused with complete-carrier-invalid caused by relation or Plan decomposition admission failed or is unresolved.

The retained diagnostic contains no findings and one AUTHORITY_UNSUPPORTED gap on relations.concern_about, bound to current CA-D-268 v18 and CA-R-1022 v15: Affected governed-entity admission cannot be inferred from an Atom ID alone. check_graph_extended.py _other_rule adds this gap unconditionally for concern_about before the later target resolution. This is an observed source-level unsupported path, not a production reproduction or a claim that any Atom ID is sufficient target evidence.

Current CA-R-1022 defines a direct Concern-owned relation to one Observation or other directly affected governed entity. CA-O-087 v10 limits the Action to machine-checkable conformance and excludes semantic consistency; CA-R-1622 v4 forbids adding semantic-review behavior. Reconcile any machine-checkable target-class requirement and explicitly separate semantic affectedness. No new Journal or retained-review gate is implied by this Problem.

The fifteen catalog version/hash drifts found in CA-P-2426 are a separate consistency observation. authority._verified deliberately verifies observed source self-consistency rather than comparing the catalog entry's expected digest; those drifts alone do not prove an ordinary authoring refusal. The missing D305 locator was separately demonstrated and repaired in source.

## Blast radius

Concerns with this relation cannot pass the observed create-shaped full-carrier boundary. Empty-relation carriers, other tools and deployed impact are not established by this observation. Preserve owner/target/reference safeguards and source-bound tests; do not infer affectedness from identity alone or add semantic review inside the mechanical validator. Use isolated fixtures for functional acceptance, not production MCP or replay of historical requests.

### Resolution checkpoint

The approved release proof `.caprmedio_tmp/mcp-audit-20261020/continuation/local-release-verified-20261020.json` and canonical receipt `.caprmedio_runtime/simple_local_release/reports/local-20261020-current-target-parser-repair-1521.md` record the repaired mechanical Concern-admission path completing 410 modules and 3680 tests with zero skips/failures. The released candidate is image `a26b88751f9e8eb57132f648e114f0af4d0c25ff5acf66a6f891f7d05fb4fab3` with fingerprint `b95525f5be4b87c9b342f52199cd8f9260ff4206c2f130090cf63f4cc3e38f76`. This resolves the deployment-blocked mechanical admission repair; semantic affectedness remains outside the mechanical validator, and no historical batch replay or broad capability claim is made.
