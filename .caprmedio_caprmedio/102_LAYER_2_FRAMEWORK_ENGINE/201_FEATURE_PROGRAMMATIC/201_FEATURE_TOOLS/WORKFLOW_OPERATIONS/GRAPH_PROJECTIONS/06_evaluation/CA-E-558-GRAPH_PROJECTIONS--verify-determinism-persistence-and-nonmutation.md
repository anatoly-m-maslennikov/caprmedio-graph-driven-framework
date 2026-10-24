---
atom_id: CA-E-558
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-24 02:14:24 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Projection
  depends_on:
  - Subject/Engineering/Graph Projection
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/Term//Artifact
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Occurrent/Execution/Step Run
relations:
  evaluation_for:
  - CA-R-1837
  - CA-R-1838
tier: 4
---
# Summary

Verify determinism, persistence, and nonmutation

## Scope

Functional persistence, `no_op`, destination-rejection, and shared-recording boundary proof for both graph kinds.

## Claim

Only an exact current, complete and validated projection may persist or return final `no_op`; source authority and existing Journal history remain unchanged while shared support appends the actual required Run events.

## Details

Execute the following cases for both graph kinds against the admitted request/result contract and the actual implementation:

1. With neither an explicit output destination nor one current, unambiguously registered target, permitted description/generation has no Projection-file effect. A required unresolved Action target is blocked. A configured projection root or conventional output filename alone does not select a target. A current registered target permits only its admitted output effect; ambiguous registrations cannot authorize publication.
2. Persist to one authorized explicit derived destination and repeat through one current unambiguous registered destination. Assert atomic publication of only the admitted output, its actual identity/revision, and truthful `created`, `replaced` and unchanged effects. An existing destination with different bytes and no admitted current prior-output evidence is blocked and preserved. Whenever replacement is authorized, its effect is `replaced`, never `created`, regardless of how the exact prior-output evidence was obtained. Final `no_op` requires matching current selection/configuration/source evidence, all required checks and actual recording; it fabricates no Artifact mutation.
3. Reject authority/Journal destinations, traversal, symlink escape, ambiguous destination, authoritative-output requests, stale sources/context/settings or prior output, denied permission and incomplete-quality `no_op`. Preserve affected evidence and the prior accepted target rather than replacing it with an unapproved partial result.
4. Distinguish an explicitly evidenced empty selection from absent selection or unreadable coverage. Exercise the empty selection through the same source, quality, persistence and recording gates; do not convert missing evidence into an empty valid graph.
5. Inject publication failure before atomic replacement and failure after an actual replacement. Assert the observed prior/result bytes and truthful effects; an uncertain effect remains uncertain. Retain the real output and recovery boundary without blind replacement, rollback or construction replay.
6. Reject caller-authored recording substitutes and block construction on unresolved start recording. Inject terminal-recording failure after publication and assert the retained output revision/effects and exact shared pending reference, with no final completed Action/Workflow or `built`/`no_op` completion claim. Recover only the same event identity/payload through shared support; prove that the output and original construction are not replayed and the event is appended once.
7. Compare canonical semantic graph output byte-for-byte for identical admitted bytes/settings, keeping actual Run identities and receipts separate from semantic determinism. In the pure builder boundary, assert no source or Journal writes. In full Run execution, assert unchanged source authority and preserved Journal history plus only the actual append-only shared events, confirmed receipts and any truthful pending state. Confirm the read-only consumer boundary and retained non-authoritative status.

8. Exercise explicit `subject_profile: approved` through the public descriptor and existing Action/queue adapters for both graph kinds. Mixed `/`, `.`, `:` expressions and YAML-quoted initial `atom(...)` selectors retain their exact decoded Subject paths and distinct selected-owner literals in incidence. Assert the exact current grammar pins and `native_admission: not_performed` evidence are retained; no new native fact is accepted solely by the syntax profile. Default and explicit `legacy` requests remain byte-identical with the existing legacy evidence shape and behavior. Repeated approved requests with identical bound inputs produce identical canonical semantic bytes, and approved versus legacy profile selection remains distinguishable in persisted semantic identity. Exercise approved explicitly empty selection through the existing quality, permission, publication and recording gates. Inject approved grammar-pin drift after parsing and immediately before publication or unchanged-output confirmation; the request cannot publish, confirm `no_op`, silently rebind its pins or replace prior bytes. Retain truthful currentness diagnostics and unchanged source/Journal boundaries.

The cases specify functional proof, not a runtime pass. Mock source inputs may establish fixture expectations, but the implementation and required shared recording are exercised rather than replaced by mocks. Fixture success proves its fixture; live corpus delivery and the required exposed Tool/MCP and Docker evidence remain separate acceptance obligations under CA-D-540.
