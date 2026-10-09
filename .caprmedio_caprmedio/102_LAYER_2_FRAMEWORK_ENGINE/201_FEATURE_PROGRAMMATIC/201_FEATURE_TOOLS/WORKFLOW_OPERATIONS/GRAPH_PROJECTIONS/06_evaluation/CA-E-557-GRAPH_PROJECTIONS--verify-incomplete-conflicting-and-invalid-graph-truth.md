---
atom_id: CA-E-557
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 19:23:34 +0400"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/Failure truth cases"
  depends_on: [Tool, Projection, Artifact, Journal]
relations:
  evaluation_for: [CA-R-1835, CA-R-1836, CA-R-1837]
---
# Summary

Verify incomplete, conflicting, and invalid graph truth

## Scope

Functional failure cases for incomplete source coverage, conflicts, cycles, malformed carriers, and self-references.

## Claim

Every invalid or incomplete fixture **must** preserve its source evidence and return a non-complete outcome; neither builder may repair authority or report `built`/`no_op`.

## Details

Exercise unreadable/malformed selected carriers, missing governing definition, stale existing output, unresolved endpoint, conflicting relation/definition evidence, Terms parent/dependency cycle, self-reference, and cardinality violation. Assert affected paths/identities/digests and diagnostics remain visible, only declared data is represented, validity/coverage/currentness dispositions fail or remain unresolved as appropriate, and the outcome is `incomplete`, `conflicting`, `stale`, `blocked`, or `failed`, never `built`/`no_op`. Assert no source edit, inferred Term/Entity/Property/Scope Unit, graph repair, retry, or fictitious Journal completion. This carrier specifies functional proof, not runtime evidence.

Also exercise negative cases for Atom/Carrier metadata leakage into governed Entity Properties; conversion of Subject incidence/provenance into a native Relation; an unsupported narrower display selector; and missing admitted source-fact coverage for requested Properties or native Relations. Assert an evidenced empty selection remains distinguishable from absent, malformed, or unreadable selection, with only the former eligible for its declared empty-result handling. For Terms, reject a path/spelling-derived qualified Term, `SUBKIND_OF` hierarchy alias, and any `NARROWER_THAN` lacking admitted kind, source-pinned evidence, or definition implication. Builder tests keep source and Journal bytes unchanged; shared-executor failure tests preserve prior Journal history and never invent actual Run completion.
