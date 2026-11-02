---
atom_id: CA-E-557@9
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-24 02:14:24 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Projection
  depends_on:
  - Subject/Engineering/Graph Projection
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/Term//Artifact
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  evaluation_for:
  - CA-R-1835
  - CA-R-1836
  - CA-R-1837
tier: 4
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

For both graph kinds, exercise the public descriptor and direct native boundary with `subject_profile` null, Boolean, number, object, array, empty string and unknown name; each is rejected without output effects or fallback. An approved request rejects absent, unreadable, changed and symlinked grammar pins, including a symlinked parent directory, with stable diagnostics and preserved prior output. Reject malformed approved expressions and unsupported `@` without switching to legacy. The reviewed selector and `/`, `.`, `:` fixtures retain only syntax/incidence evidence: no spelling/path/selector-derived native node or Relation, including `NARROWER_THAN`, `IS_BORNE_BY`, `IS_ALLOWED_VALUE_OF` or `BEARS`, is admitted by this profile selection. Compare the independently bound fact context and admitted facts for identical ordinary sources under default/explicit legacy and approved requests; changing only the syntax profile cannot create or alter a native admission decision. Unsupported required native families remain unresolved rather than complete/empty.
