---
atom_id: CA-P-1899
content_role: Plan
type: Plan
label: Task
work_sequence_number: 20
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Projection
  depends_on:
    - Requirement
    - Method
    - Evaluation
    - Delivery
    - Workflow
    - Action
    - Entity
    - Term
    - Plan
version: 1
updated_at: "2026-10-09 21:55:59 +0400"
relations:
  is_decomposition_of:
    - CA-P-1872
  blocks:
    - CA-P-1873
---
# Summary

Verify repaired graph RMED and Operations before implementation

## Objective

Independently verify and accept the repaired graph RMED+O packet before resuming implementation.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

Inputs: CA-P-1897's review, CA-P-1898's repairs and any required bounded fix children, exact current source bindings, revised tests and preliminary local code changes held for reconciliation.

Output: an independent accept/reject/unresolved disposition with current source pins and an explicit implementation gate. Check RMED+O agreement, functional cases CA-E-555–558, partial/complete result distinctions, applicable Method instructions and all known review findings.

Exclusive scope: read-only repaired graph authority and code/test evidence; write this Task's review evidence only. Do not grant runtime admission, alter release bindings or fabricate an MCP Run/Journal receipt.

Acceptance: the bounded graph packet is independently accepted under CA-D-540 and every preliminary edit is reconciled with it. Local implementation uses the Operator's without-MCP authorization and 90% question threshold. Live MCP generation, runtime activation and durable graph delivery remain separate gates. Unaccepted or unresolved source regions remain blockers, not passing checks.

### Source review evidence

Source-only disposition: ACCEPT. Independent semantic and operational reviewers accepted the repaired packet; the affected semantic review also accepted the unnamed inverse-navigation form, explicit candidate source_ref, derived BEARS binding and the Operator-approved Active declarations for the three primitive Relation Kinds.

Reviewed source bindings (repository-relative carrier paths are retained in the verified source inventory):

```text
CA-R-1260@13 ea7911f8d3bc88bcba954332193354c80df63005dbf94812960dda162615f54d
CA-R-1435@8 15fa6d3511be9f2d4ad76eea38373f13bcbb37522a2f7c5b985e0a4b836f54cb
CA-R-1436@8 a33bdc582beb140647e6012022730abf531f6311923edf80ed7d1fe1614dabad
CA-O-134@3 8a3dcb7cfdb3369ec268726cc54f3f0e0c1bfbc947841792deb87bb844245414
CA-O-137@3 8ea08ef172a82515db7f145bf642a3943ecc41fc6decf4a86a69bea78ce494fd
CA-M-259@8 a3bd97be0f83b8fbeb1bcfe69d38c7c20ad24262feb547d3de73ab7a938fc0a9
CA-R-1835@2 ac1bac759fc072bb10b725b3e63d0b072d56c688a5a52c70a74cffd89e212dbb
CA-R-1836@2 15575dc4ceea2f41507640ce9d82a27ce64d12e23ce964ef47a57e9dd8f40694
CA-R-1837@2 82bbdeb5af1f60cd53fa69b31560a877331df7de526f46016f434f912e97135a
CA-R-1838@2 587c33dba8a8fd196c05c38bf106624cdff9a24b38e94643863f2e3f3861e1c6
CA-E-555@2 1eac56c048d1e79eca9b82eeeba48456704bfcec9025583c33d37093185b856b
CA-E-556@2 6438415a2ea12165c1d963a7e4ab9acb087183e485e1d4c2a19ec3bf51e374ad
CA-E-557@2 7c11c7fb2146bcb7575897e7ef6ec9893aa99b0a352e65aa8ccd59d48e9bf5e8
CA-E-558@2 efaca2b118df0e0d49a837aaea9b8e290489aae0403679e5a3c507d63794087f
CA-D-538@2 3125c8e3b0c44336f452a853b3dba55d6b4dca2f2adfd9fead0a5f3154f79c36
CA-D-539@2 51c94e6877f28fe58fab931155d8d4ca4f65e1b2ea0bc65ef06f89e6d6a143de
CA-D-540@2 564280b33edcee8a6e656994cdd45106a9766f652d38d7930b61b65d84e6336a
```

Structural check: 50 unique Carriers, including 33 Plans and 17 changed source Carriers; required sections, identities, Status, Scope Unit references, revision distinction and acyclic Plan blocking/decomposition checked.

Applicable Method inventory: 237 unique Carriers; 118 confirmed Active Methods, 119 legacy/unverified candidates, zero duplicate identities, missing or unreadable inputs. Aggregate SHA-256: 2fec26f90e8563da693e17e5727033938ed6a5f0c4dff144d8bf292d225b94b9. This inventory does not make every inventoried Method applicable or every legacy candidate Active.

Preliminary code reconciliation: definition and hierarchy helpers recognize candidates only; Entity metadata and Subject incidence stay source-owned; the former main-builder metadata transfer, inferred native Relations, default publication and start-as-terminal behavior are being replaced, not accepted. The provider retains unknown coverage for unsupported nonempty selections. A checked partial implementation may proceed against the accepted source boundary; no provider profile or full-positive graph result is accepted by this source review.

This Task remains Active: final code reconciliation and independent implementation acceptance are separate evidence. CA-E-555/556 complete-positive cases, CA-E-557/558 exposed Tool/MCP and Docker proof, live delivery and recording-only recovery remain pending. No source-only review is an MCP Run, runtime receipt or completed graph Action. Existing frozen migration/manifest pins are stale where these sources changed and were not rebound.

### Preliminary implementation reconciliation

The corrected preliminary local pipeline passed independent bounded semantic and operational code review. It now has a factory-only immutable fact context; original-byte Claim/Operation evidence; candidate/native separation; checked source, authority, selection and loaded-profile bindings; explicit empty selection; exact prior-output replacement evidence; and closed, truthful effects/completion results. The executor helper supplies authorization only from its actual admitted session. Caller JSON, direct unminted contexts and nested caller capabilities cannot grant permission or terminal completion.

Verification: 101 graph tests, 8 isolated executor-authorization tests and 23 discovery tests passed. The broader selected-execution suite passed 18 of 20 tests; the two current-manifest positive tests correctly encounter Action bindings that are stale after the source repair. No frozen map or runtime admission was manually rebound to make those tests pass.

Reviewed implementation pins:

```text
generate_entity_graph.py ed9f6b5895bad44d077cec031b5d066e6d8abbf0f78f52f7516e88c831894584
strict_graph_request.py 69f1a83c9f25ad55a9ce3aa205ee616b3bb4d081962cf2867e2b8ad1dc1e3e60
graph_fact_context.py a021646fbb0ef8432ef70ae52cdddc5a33ef41912c91b74d5dc54ab0c55a3d70
definition_claims.py e21728f4fbfff61c4ae92c06e67c2d51e8a462eb56871cc787c8f90104a6baae
selected_execution.py cc148c105014029ac7e76a68831032d3c363e7d01ea13db772ecae7c3c0d928f
```

Remaining implementation boundaries: nonempty native fact admission still lacks a complete definition/property/registry evaluator portfolio. The Operator chose Core Meta-model by itself: Project Configuration overrides and enabled Extensions are not part of this graph's native meaning. This is a declared Core model, not project-effective applicability. A Term retains its exact Claim applicability Scope and needs uniqueness proof over the complete isolated Core authority frontier; ownership or matching prose cannot replace those checks. The isolated Core declaration/uniqueness profile is the next bounded evaluator work. The shared executor's terminal-finalization and recording-only recovery handoff remains separate work; the pure builder never reports built/no_op or writes a Journal.

These are partial-path receipts, not CA-E-555/556 full-positive acceptance or an Epic completion claim. The Task and Epic remain Active.

### Verified foundation integration

The revised foundation passed 107 graph tests. Independent review accepted exact source-owned Details evidence under D478/D479/R1624, the exact raw lifecycle boundary, and the two declared informational frontier exclusions. Concern's lowercase `active` remains pinned source evidence, not an invented universal lifecycle normalization or native admission. Unsupported lifecycle families retain an unresolved diagnostic. Scope evidence is permitted only inside a bounded RMED Claim-applicability evaluator with D478/D479/D495 support; it cannot become a separate native fact.

A read-only current Core check bound all 951 discovered carriers and selected 908 exact-Active Core-owned source Atoms. It recognized 135 preliminary candidates, admitted zero facts, and retained unknown definition/relation coverage. These counts describe this partial source snapshot, not the required final graph, lifecycle completeness, a publication, or a Run receipt.

Current independently reviewed foundation pins:

```text
graph_fact_context.py b4c33a8c3430b9b09f5f9f4afbd3915e5ca34a0c164e8fee839d24559075391f
strict_graph_request.py da4bbb9d8c81f658559008812997370b61f1e33d735f3b9b877da5bb261964f0
owned_scope_selection.py 174254059d5695c32b2beeff72fcc949b9f81a04baffc472bbcb9058c02ed64d
```

Native Core profiles and shared terminal reconciliation are separately owned in-progress changes and are not accepted by this foundation receipt. No MCP, runtime or source-manifest activation was performed.

### Shared recording integration

Independent bounded review: ACCEPT. Twenty-six fixtures passed: twelve graph completion/recovery cases, eight actual executor-authorization cases, and six existing public-status compatibility cases. Construction remains incomplete until a matching actual Action terminal receipt proves its recorded boundary. Pending recording retains the actual pending identity and observed output effects. Reconciliation uses saved construction/dispatch/Journal evidence and does not invoke a provider, reconstruct a graph, publish output or append a Journal event.

The existing status consumer uses read-only reconciliation even when the scheduler cached SUCCESS. That path does not write progress or dispatch work. Missing evidence retains a safe explicit blocker. Same-Run dispatch retries reconcile the exact frozen request only; changed requests cannot redispatch an accepted graph Run.

Reviewed implementation pins:

```text
graph_completion.py 62ff77386892030bd2a3bb3b0f0562135be0b5a7cb5a09161b560451648866bd
selected_execution.py 043223f350e9ff21ccc67603594101d6dcba473b90684e462c128fea59923e88
backend.py 9f54448addcd7a2e6f36ae9c72f45ac82e7cc3303e4bcad57982016ca8ec6745
```

This is fixture/code acceptance, not an actual Journal or live MCP receipt. A parent Step/Workflow already recorded as interrupted remains incomplete; the Release-only recovered-Run capability was not widened. The broader selected-execution receipt remains 18 of 20, with two current graph-manifest positive cases blocked by stale repaired Action bindings. Frozen bindings were not rewritten to conceal that gate.

### Declared Core portfolio integration

The Operator explicitly selected Core Meta-model by itself. Project Configuration and enabled Extensions do not alter the native meaning of these projections. The provider and graph namespace retain `declared_core_model`; this is not project-effective applicability.

Independent bounded reviews accepted the current Term profile, candidate-only Entity profile, three native Relation Kind registry records, closed fact-context validator, and candidate-only Term relation integration. The Term profile binds twelve current authorities, preserves source-owned Scope evidence and rejects structural Scope copies. The Entity profile binds seventeen current authorities but does not claim to perform Action/Workflow semantic admission. Registry Kind Status is explicit source content; Atom lifecycle Status is not transferred to a Kind or governed Entity. BEARS stays a declared derived inverse, not a primitive registry Kind.

Fresh local verification: 170 graph tests passed through uv-selected Python 3.14 without writing bytecode. Seven integration cases check isolated Core context, current source lineage, determinism, display boundaries, candidate-only relation output, and the absence of native facts inferred from registry metadata. Existing recording/status acceptance remains the separate 26-fixture receipt above. The source-backed context validator checks exact closed fields, canonical digests, contribution references, coverage counts and safe structured diagnostics before the private factory mints a context.

The fresh read-only Core check bound 951 discovered Carriers and selected 908 exact-Active Core-owned Atoms. It did not publish a graph or create a Run/Journal receipt:

| Family | Candidates | Admitted facts | Coverage |
|---|---:|---:|---|
| Term definitions | 77 | 32 | unknown |
| Term relations | 12 | 0 | unknown |
| Entity admissions | 26 | 0 | unknown |
| Entity Properties | 26 | 0 | unknown |
| Entity relations | 0 | 0 | unknown |

Current derived context digests:

```text
terms 058700ebd7de6d1e3d85c587cc5ba6f203debd0a3d1c012bceaa876b0b2b0410
entities 98e09939d85713eb49d955b9813abbf7f15b165c36f70a1df6c3b9b10084c5b7
```

Accepted implementation pins:

```text
graph_fact_context.py fb263671bca3cdad58018983a9cd771a7e3df2fc93703aaae398af24bb0b0427
strict_graph_request.py b2a9c3a5323c8a2101d11833d91ca17b92431b1c02fd621d6ecf0267522491c4
core_entity_admission.py a54ad6e8f2780e0ea51bbd7f72e8f50ff8545653ce30daf4306e7fa3446662a6
core_relation_candidates.py 8d3db0a80e447cad6e8b8bc14bc466a12359addf1c568cd0df29d341e4e094c4
core_relation_registry.py c15b66ad1e2d0d8466fe67e9bfd44f9b7a39388b833232945d322aaf3b69adce
core_term_admission.py 823d5976e0095ea43c05c2386e1b04f5f5318d093ab3ad69d2fce1cb90735ece
fact_context_contract.py 2568204b360bd33e49aee2d9e9100230b474783ca386fe53e6e0b6ae1530e3e3
```

Remaining boundaries: the Operator question about ontology concepts versus explicitly declared Entity instances is unanswered. Native Entity/Property admission and complete Term relation admission remain unperformed; unresolved candidates do not become facts. Full-positive graph Evaluation, current manifest admission, runtime activation and durable live delivery remain separate gates. Exact-Active selection is not proof that every Content Role's lifecycle family is fully implemented. Historical partial receipts above describe their earlier snapshots, not current full coverage. This Task and the Epic remain Active.

### Definition of Done

the Plan is **not** Done **if** ((the repaired RMED+O packet or preliminary code reconciliation is rejected, unresolved or unverified) **or** (any required finding is rejected, unresolved **or** unverified) **or** (a required check has not been performed) **or** (any direct decomposing Plan is **not** Done)).
