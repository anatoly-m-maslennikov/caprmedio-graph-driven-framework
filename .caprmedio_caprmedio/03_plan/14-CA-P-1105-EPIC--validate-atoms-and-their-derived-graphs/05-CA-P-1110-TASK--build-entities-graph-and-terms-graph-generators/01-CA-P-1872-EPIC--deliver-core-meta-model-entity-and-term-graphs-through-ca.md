---
atom_id: CA-P-1872
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: Projection
  depends_on:
    - Entity
    - Term
    - Atom
    - Property
    - Scope Unit
    - Tool
    - MCP
    - Workflow
    - Action
    - Journal
    - Plan
version: 9
updated_at: "2026-10-10 01:39:46 +0400"
relations:
  is_decomposition_of:
    - CA-P-1110
---
# Summary

Deliver Core Meta-model entity and term graphs through ca

## Objective

Make the existing entity and term graph builders usable through the Project MCP for the current `CORE_META_MODEL` Scope Unit. Deliver two separate, source-backed graph projections without changing the meaning of their source Atoms.

## Details

### Latest Operator sequence: Subjects first

The Operator replaced the immediate execution plan on 2026-10-09. Do these steps one by one. Finish and verify one step before starting the next. The source is the Core Meta-model by itself, not Project Configuration or Extensions.

1. **Build mechanically from existing Atoms.** Read their current Subjects, using only the existing `/` and `:` syntax. Preserve complete Subject paths, supporting prefixes and exact source references. Keep `/` steps unclassified. `:` links an allowed value to its qualified Property; it is not an assignment. Do not infer relations from Main Content, rewrite Subjects, normalize to the proposed new notation or create source-Atom nodes as model objects. Output a derived graph and the literal Term components. Verify deterministic output and unchanged Core source bytes.
2. **Review the current graph and design its structure.** Use current Active Core Atom content to interpret old slash paths, group Continuant/Occurrent and inherit common constraints. Review every Entity for duplication, redundancy, emptiness, lack of meaning or possible generalization. Mark proposed drops, consolidations and generalizations; do not apply them. Record a complete source-occurrence ledger for old relations, including qualified prefixes and unchanged `:` links, not only deduplicated graph edges. Keep source evidence and every old identity traceable. Ask the Operator below 90% confidence. Do not change the step-1 graph or Atom Subjects.
3. **Give the Operator the new graph candidate.** Present the grouped, inherited and visibly marked candidate in compact notation using `/`, `.`, `:` and `@`. Use NARROWER_THAN, IS_BORNE_BY, IS_ALLOWED_VALUE_OF and IS_CARRIED_BY with correct directions and qualified identities. Hand off its complete relation ledger, node dispositions, exact source pins and candidate hash. Preserve the baseline. Candidate delivery is not acceptance. Only after an explicit Operator decision tied to that candidate may CA-P-1909 apply accepted decisions to a separate derived graph and verify it.
4. **Update Atom Subjects.** Only after explicit Operator acceptance and verification of the separate accepted graph may CA-P-1910 prepare the exact migration preview. CA-P-1911 may write the confirmed `/`, `.` and `:` notation and required grammar/revision changes only after separate Operator authorization of that sealed preview. CA-P-1912 then rebuilds and verifies reproduction of the accepted graph with its source-backed relation evidence. The display operator `@` is not automatically added to Subject grammar.

Step **1 is complete**. Step **2 is in progress**: CA-P-1905's current baseline review is Done; CA-P-1906 candidate design is next. Steps 3–4 remain pending. Earlier classification drafts and migration code are preparation only, not accepted decisions or source updates. The approved compact graph notation is `/` for broader-to-narrower, `.` for bearer qualification, `:` for allowed values and `@` for IS_CARRIED_BY; step 1 does not apply it to old `/` occurrences. Exact `@` bindings identify the carried state and Carrier rather than assigning a Property value.

This sequence governs the immediate local work without MCP. A mechanical projection is not native semantic admission, a live MCP Run or completion of the whole Epic. The existing MCP delivery work remains separate and pending.

#### Step 1 acceptance receipt

- Builder: `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/mechanical_subject_graph.py`, reusing the existing pinned Subjects reader and snapshot support. Its default is read-only; `--persist` creates three fixed files without overwrite.
- Outputs: `.caprmedio_caprmedio/_projection/core-subject-notation/step1.graph.json`, `step1.entities.graph.dot` and `step1.terms.graph.dot` in the same directory. The earlier `before.graph` files remain unchanged.
- Selection: 908 exact-Active owned-Core sources out of 951 captured source files; 43 excluded sources retain their pins. Extraction is complete: 4,534 Subject occurrences, no unresolved selected sources.
- Graph: 706 full-path/prefix nodes, 294 unclassified `/` links, 66 allowed-value `:` links and 534 literal Term components. The Terms view has no inferred taxonomy links.
- Graph fingerprint: `0ea18486fd43ccd546a5d09888e98bc42f56d42d392e5669fecee19fa25f93d1`. JSON file SHA-256: `57cba13073aa0de34876a734c784a43d124f09ff03584de03252b9d12a89ac0b`.
- Entities DOT file SHA-256: `2754760bde5bce25b9500682d2af71a819b34df342e1da5cf4a91ec2a5cf48dd`.
- Terms DOT file SHA-256: `41dc2e8befbf0a91b40cf5ca90858e4916c8c08e98fac16ff7555d0ce7ee6ebc`.
- Checks: 197 graph/acceptance tests plus 10 builder tests passed. Matching before/after pin-set fingerprints verify all 951 Core source files unchanged. This self-contained receipt identifies all three Step 1 file hashes above; it does not refer to an unlinked external receipt.
- No Main Content classification, dot interpretation, Atom Subject rewrite, native semantic admission, MCP execution or Run/Journal recording was performed.

### Current graph review and candidate Tasks

The Operator added this work and broadened Task 3 on 2026-10-10. Task creation is not execution. Run the new Tasks one by one, with their explicit BLOCKS chain:

`CA-P-1905 → CA-P-1906 → CA-P-1907 → CA-P-1908 → CA-P-1909 → CA-P-1910 → CA-P-1911 → CA-P-1912`

- Review the current Entities Graph derived from exact-Active Core-owned Atoms. Recheck current pins instead of treating the saved step-1 counts as permanent.
- Give the Operator a new graph candidate grouped by Continuant and Occurrent, separating definitions from actual executions.
- Inherit common constraints through justified narrower-than specializations. Declare shared Carrier obligations and other common rules once; show only subtype additions or differences. Do not inherit another Entity's concrete Carrier.
- Use as few genuine root entities as possible without losing distinctions or inventing relations. Explain retained roots and distinguish display groups from independent model roots.
- Check every Entity for duplicates, redundancy, an empty definition, no distinct meaning or possible generalization. Mark each proposed drop, consolidation or generalization visibly; do not delete nodes, governing Atoms, source Subjects or history. Revision is an explicit drop/consolidation candidate in favor of Version Number and Updated At, with exact historical references preserved.
- Check Applicable Methodology as a generalization candidate under Projection: the same pattern as compiling all applicable Method Atoms for a Scope Unit into one prompt document. Evaluate Applicable Methodology as one compiled document, not a set of source Atoms. Keep the source set and derived document distinct; identify any applicability, authority or other constraints that the general Projection model must preserve. This is a candidate to review, not an accepted Core change.
- Use `/`, `.`, `:` and `@` in the compact candidate display: narrower-than, bearer qualification, allowed value and IS_CARRIED_BY. Reuse CARRIES as the inverse direction of the Carrier binding; do not add an equivalent primitive.
- Use concept names such as `Version Number`, `Updated At` and `Status`, not YAML keys. Present the candidate with plain two-space indentation and compact cross-link statements. Preserve qualified identities and graph ownership.
- Every baseline identity needs a traceable retain/move/inherit/consolidate/generalize/drop-candidate/question disposition. Give root counts before and after, count marked candidates separately, and expose uncertainty instead of forcing a smaller graph.
- Every original relation occurrence needs a row with the source Atom/revision/hash, Subject field/index/path/segment, old qualified endpoints, graph kind and disposition. An evidenced proposal records its operator/relation/direction/endpoints and Main Content evidence. An unresolved or not-native row has no asserted native relation proposal; record the missing-evidence or inapplicability reason, what was checked and any required Operator question. Preserve these reasons through candidate changes and handoff; do not invent native edges from syntax or Atom incidence. Additional candidate relations need their own source evidence, not fabricated old occurrences. CA-P-1907 must keep this ledger complete when marking generalizations or consolidations.

CA-P-1905–1908 refine steps 2–3 above. Their outputs remain proposals for Operator review; they do not accept a new ontology, update the step-1 graph or Core Subjects, rename YAML keys, implement a runtime, or complete the Epic. `@` is approved compact graph notation, not an automatically admitted Subject-path serialization operator.

### Current local execution evidence

- CA-P-1905 is Done and placed in this Epic's local `done` container. Its fresh review and complete inventory are under `.caprmedio_caprmedio/_projection/core-entity-review/`.
- The current Step 1 graph and all source/profile pins reproduce exactly. Independent inventory acceptance covers all 706 nodes, 360 edges, 4,534 occurrences and 3,093 source-level relation segments.
- There are 346 syntactic qualification roots (53 branching and 293 standalone) and 74 repeated leaf-label groups. These are diagnostic counts, not independent ontology roots or accepted duplicates.
- No candidate classification, source migration, native graph admission or MCP Run has been completed. The Epic remains Active.

### Candidate acceptance and migration gates

CA-P-1909–1912 own the previously missing follow-on work. They are created as Active Plans, but their work is deferred until their start conditions are met. Creating or fixing this Epic is not candidate acceptance or migration authorization.

- CA-P-1909 starts only after CA-P-1908 is Done and the Operator records accepted decisions tied to the candidate hash, source pins and complete ledgers. Build and verify a separate accepted graph; preserve the Step 1 baseline and every disposition.
- CA-P-1910 starts only after CA-P-1909 is Done. Prepare a sealed preview of exact Subject changes and any required grammar/revision/history changes. Do not write authoritative sources. Candidate approval is not approval of this preview.
- CA-P-1911 starts only after CA-P-1910 is Done and the Operator separately authorizes the exact sealed preview. Recheck pins and authority before writing only approved changes. New Claim meanings, YAML-key renames, unapproved deletions and automatic `@` Subject serialization remain outside that authorization.
- CA-P-1912 starts only after CA-P-1911 is Done. Rebuild separately, compare qualified identities and relations with the accepted graph, verify allowed source changes and preserve unchanged sources and history. Carrier bindings retain their independently governed evidence.

Each required Plan dependency is explicit in BLOCKS. The two Operator decisions are additional readiness conditions, not facts inferred from Task Status or folder order. Changed pins require a fresh preview and affected approval. The older MCP delivery work remains separately pending under its current admission/runtime gates; completing these local Tasks does not resume it automatically.

### RMED and Operations review gate

The Operator added this prerequisite on 2026-10-09: review and fix entity and term graph RMED+O first, then continue implementation.

- CA-P-1897 independently reviews the current packet and its exact source pins.
- CA-P-1898 repairs confirmed, bounded RMED+O defects; uncertain semantic choices below 90% require an Operator question.
- CA-P-1899 independently verifies the repaired packet and reconciles preliminary local edits before implementation resumes.
- CA-P-1899 blocks CA-P-1873. Existing execution dependencies then govern the remaining work. Navigation numbers do not imply execution order.
- Preliminary local code/tests remain unaccepted work until this gate passes. A source-pinned independent review is required by CA-D-540; preparation reviews alone do not satisfy that gate.
- The current Operator authorization permits local implementation and graph RMED+O repair without MCP. It does not bypass the MCP admission gate, authorize unrelated source changes, or claim live graph delivery.

The independent review rejected the pre-repair packet. CA-P-1898 now decomposes into five bounded repair/inventory children. The Operator approved a derived, source-pinned fact-context design; no new source authority or admission proof is implied.

Latest bounded implementation evidence is recorded in CA-P-1899. The Operator chose Core Meta-model by itself, not Core as applied through Project Configuration and Extensions. The local portfolio passed 170 graph tests and admitted 32 source-backed Term definitions; Entity and native relation coverage remain incomplete. The Operator then selected model objects addressed by Subjects, not source Atom records, and the Subjects-first sequence above. These are partial implementation receipts, not completed graph delivery. The Epic remains Active.

### Creation and execution state

- These Active Plan carriers are created directly in the project at the Operator's request, without MCP.
- The Epic directly decomposes CA-P-1110. Child identities and dependency relations are explicit.
- No MCP creation Run or Journal receipt is claimed. Plan creation is not implementation, runtime activation, admission repair or graph publication.
- Live source/runtime admission remains a graph execution prerequisite; local code work follows the repaired RMED+O gate and the Operator's without-MCP authorization. Recheck the current state before work; an earlier investigation snapshot is not a live admission receipt.
- The effective Author is Anatoly Maslennikov. Each own-work leaf has one Assignee, AI Agent. Groups have child work only.

### Reuse and existing work

- Reuse `GENERATE_ENTITY_GRAPH`, the selected Workflow executor, shared Run recording, and the existing `build_entities_graph` and `build_terms_graph` MCP routes.
- Entities: CA-O-133 Workflow, CA-O-135 Step, CA-O-134 Action.
- Terms: CA-O-136 Workflow, CA-O-138 Step, CA-O-137 Action.
- These bindings and builders already exist. Do not create a second graph engine or a second executor.
- CA-P-1110 already covers Core-only input, current extraction, Atom incidence and tested generators under CA-P-1105. This Epic is a direct decomposition of CA-P-1110, not a competing root workstream. Reuse their existing builders and verified evidence; own only the remaining Core compatibility and MCP handoff gaps listed here. The Epic owns `is_decomposition_of: [CA-P-1110]` and uses the matching parent Plan container. Do not edit the parent's Summary, Status or duplicate an inverse relation. Confirm the current parent and its explicit blockers before execution; overlapping work has one owner.
- The installation/release work in CA-P-1848 is separately owned and currently changing related authority. Do not edit its files or refresh its source bindings without coordination and explicit authority.

### Investigation findings to recheck and address

1. The investigation found a stale private Release carrier pin preventing global selected-manifest admission. This hides graph execution bindings and blocked MCP Atom creation in the investigation snapshot. The six graph Workflow/Step/Action pins checked in the investigation matched their source bytes; adding duplicate bindings is not the fix.
2. Discovery drops the admission failure, then reports unresolved execution with no useful reason. Preserve a safe, actionable diagnostic while remaining fail-closed.
3. Current Core definitions use governed Requirement Claims containing `means`. The builder recognizes only legacy `Definition` metadata. A Claim containing `means` is a candidate, not proof of a unique definition; recognition must follow the admitted Claim grammar and preserve source evidence.
4. Current Core term hierarchy uses `NARROWER_THAN`; the builder and synthetic fixtures assume `SUBKIND_OF`. Resolve the current graph-qualified relation contract before changing extraction. Do not silently treat old syntax as an admitted alias.
5. Atom Subjects, Atom incidence, entity relations and native term relations are different things. A matching spelling or Subject dependency does not authorize a native term edge. Keep Atom/Carrier metadata attached to its source owner: governing an Entity does not make the source Atom's author, content role or other metadata a Property of that Entity. Native Entity Property facts need their own admitted source evidence.
6. `scope_unit_names` currently selects structure records but does not resolve the requested Atom set. Select current Active Atoms owned by `current_scope_unit: CORE_META_MODEL`, using current Project Structure and explicit Properties. Keep `claim_target_scope_unit` separate; foreign-owned Atoms do not enter the native set just because they target Core. Record admitted support sources and external references separately. Do not infer scope from folder nesting.
7. Selected execution injects actual recording context at the outer parameter level. Keep the admitted request shape; a nested request must not lose that context or substitute caller-authored recording claims.

The investigation snapshot contained 951 active Core carriers. This count is background evidence, not a hard-coded completion criterion. Bind and verify the actual selected source snapshot when work starts.

### Boundaries

- Select the declared `CORE_META_MODEL` Scope Unit only. It currently has no declared descendants. Do not add recursive scope selection or a new query grammar unless its current authority requires it.
- Keep entity and term namespaces separate. Preserve graph-qualified relations, direction, roots, constraints, external references and source traceability.
- Keep projections derived and non-authoritative. Do not edit source Atoms to satisfy parser assumptions, fabricate definitions or suppress unresolved references to claim success.
- Publish each graph to a distinct admitted JSON destination under the configured projection root. Do not overwrite an unrelated global graph or another Run's output.
- Reuse an existing viewer if it can display the outputs. A new graph app, HTML renderer, database, plugin or frontend is outside this Epic.
- Runtime activation is a separately admitted prerequisite after checks, owned by the Project runtime/release owner. It must use the existing admitted mechanism and retain the selected package/image or implementation generation/fingerprint and its binding to the reviewed source snapshot. Fixture proof and live handoff must each identify the implementation they actually execute. A reload receipt alone is not that proof. If activation requires a new package/image or promotion, request it through the existing release workstream; do not turn this Epic into another release cycle. Do not start a worker implicitly, install dependencies globally, delete caches or state, push, or create a PR as a side effect.
- If the selected runtime, source authority, permission, recording context or current manifest is unavailable, report the blocker. Do not bypass the admission gate or replay uncertain effects.

### Execution prerequisites

Before live graph execution:

1. Recheck current Release admission. If it is still stale, its source owner resolves it through the governing source/review path. Record the exact current discrepancy and accepted repair; do not rewrite a manifest hash as a substitute. This externally owned repair is not this Epic's executable child work.
2. Confirm the CA-P-1110 decomposition and ownership disposition above, including its current prerequisite Plans. Reuse existing evidence only where it proves the exact current work.
3. Obtain current admitted graph execution contexts and verify these locally created Epic/Task identities, canonical carriers, direct decomposition and dependency relations. Manual Plan creation needs no invented MCP lifecycle receipt. Required graph execution receipts still come from actual admitted Runs.

Read-only preparation may continue while execution admission is blocked. It is not completed implementation work. The child Plan carriers below exist, but none of their work is accepted merely by creating them.

### Work decomposition

Each leaf has one AI Agent Assignee and <=15 minutes of hands-on work. Composite groups have no separately executable own work. Split a leaf before execution if its current inputs, output and check cannot fit that bound. Use the Operator's explicit 90% confidence threshold and current retry rules. This latest direction replaces the older inherited 99% threshold for this Epic.

| Plan | Work | Estimate |
|---|---|---|
| [CA-P-1897](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/18-CA-P-1897-TASK--review-entity-and-term-graph-rmed-and-operations.md) | Review entity and term graph RMED and Operations | 15 min |
| [CA-P-1898](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/19-CA-P-1898-EPIC--fix-reviewed-entity-and-term-graph-rmed-and-operations-gaps.md) | Fix reviewed entity and term graph RMED and Operations gaps | Child work only |
| [CA-P-1899](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/20-CA-P-1899-TASK--verify-repaired-graph-rmed-and-operations-before-implementation.md) | Verify repaired graph RMED and Operations before implementation | 15 min |
| [CA-P-1873](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/01-CA-P-1873-TASK--verify-graph-admission-and-local-plan-integrity.md) | Verify graph admission and local Plan integrity | 5 min |
| [CA-P-1874](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/02-CA-P-1874-TASK--expose-selected-route-admission-failures-in-discovery.md) | Expose selected-route admission failures in discovery | 15 min |
| [CA-P-1875](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/03-CA-P-1875-TASK--record-the-current-definition-extraction-contract.md) | Record the current definition extraction contract | 15 min |
| [CA-P-1876](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/04-CA-P-1876-TASK--record-graph-qualified-relation-and-property-ownership-contracts.md) | Record graph-qualified relation and Property ownership contracts | 15 min |
| [CA-P-1877](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/05-CA-P-1877-TASK--implement-current-source-backed-definition-recognition.md) | Implement current source-backed definition recognition | 15 min |
| [CA-P-1878](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/06-CA-P-1878-EPIC--complete-term-extraction-and-admitted-relation-coverage.md) | Complete term extraction and admitted relation coverage | Child work only |
| [CA-P-1879](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/06-CA-P-1878-EPIC--complete-term-extraction-and-admitted-relation-coverage/01-CA-P-1879-TASK--implement-current-term-hierarchy-extraction.md) | Implement current term hierarchy extraction | 15 min |
| [CA-P-1880](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/06-CA-P-1878-EPIC--complete-term-extraction-and-admitted-relation-coverage/02-CA-P-1880-TASK--check-admitted-relation-coverage-and-record-bounded-gaps.md) | Check admitted relation coverage and record bounded gaps | 10 min |
| [CA-P-1881](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/07-CA-P-1881-TASK--separate-native-graph-facts-from-atom-incidence-and-metadata.md) | Separate native graph facts from Atom incidence and metadata | 15 min |
| [CA-P-1882](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/08-CA-P-1882-TASK--prepare-the-explicit-owned-core-source-selection.md) | Prepare the explicit owned-Core source selection | 15 min |
| [CA-P-1883](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/09-CA-P-1883-TASK--bind-graph-inputs-destinations-and-actual-run-recording.md) | Bind graph inputs destinations and actual Run recording | 15 min |
| [CA-P-1884](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/10-CA-P-1884-TASK--add-current-form-golden-graph-fidelity-cases.md) | Add current-form golden graph fidelity cases | 15 min |
| [CA-P-1885](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/11-CA-P-1885-EPIC--complete-graph-determinism-failure-and-recovery-verification.md) | Complete graph determinism failure and recovery verification | Child work only |
| [CA-P-1886](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/11-CA-P-1885-EPIC--complete-graph-determinism-failure-and-recovery-verification/01-CA-P-1886-TASK--verify-graph-determinism-no-op-and-source-drift.md) | Verify graph determinism no-op and source drift | 15 min |
| [CA-P-1887](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/11-CA-P-1885-EPIC--complete-graph-determinism-failure-and-recovery-verification/02-CA-P-1887-TASK--verify-conflicting-incomplete-and-invalid-graph-inputs.md) | Verify conflicting incomplete and invalid graph inputs | 15 min |
| [CA-P-1888](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/11-CA-P-1885-EPIC--complete-graph-determinism-failure-and-recovery-verification/03-CA-P-1888-TASK--verify-graph-publication-failure-and-recording-recovery.md) | Verify graph publication failure and recording recovery | 15 min |
| [CA-P-1889](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/12-CA-P-1889-TASK--verify-both-graph-routes-through-real-mcp-in-an-isolated-fixture.md) | Verify both graph routes through real MCP in an isolated fixture | 15 min |
| [CA-P-1890](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/13-CA-P-1890-EPIC--complete-independent-graph-semantic-and-operational-review.md) | Complete independent graph semantic and operational review | Child work only |
| [CA-P-1891](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/13-CA-P-1890-EPIC--complete-independent-graph-semantic-and-operational-review/01-CA-P-1891-TASK--independently-review-graph-semantics-and-fidelity-evidence.md) | Independently review graph semantics and fidelity evidence | 15 min |
| [CA-P-1892](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/13-CA-P-1890-EPIC--complete-independent-graph-semantic-and-operational-review/02-CA-P-1892-TASK--independently-review-graph-admission-recording-and-runtime-evidence.md) | Independently review graph admission recording and runtime evidence | 15 min |
| [CA-P-1893](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/14-CA-P-1893-TASK--verify-selected-live-graph-runtime-readiness.md) | Verify selected live graph runtime readiness | 5 min |
| [CA-P-1894](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/15-CA-P-1894-TASK--generate-the-current-core-entity-graph-through-mcp.md) | Generate the current Core entity graph through MCP | 10 min |
| [CA-P-1895](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/16-CA-P-1895-TASK--generate-the-current-core-term-graph-through-mcp.md) | Generate the current Core term graph through MCP | 10 min |
| [CA-P-1896](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/17-CA-P-1896-TASK--verify-and-hand-off-both-core-graph-outputs.md) | Verify and hand off both Core graph outputs | 5 min |
| [CA-P-1905](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/done/21-CA-P-1905-TASK--review-current-entities-graph-from-active-core-meta-model.md) | Review current Entities Graph from Active Core Meta-model | Done |
| [CA-P-1906](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/22-CA-P-1906-TASK--design-continuant-occurrent-groups-and-inherited-constraints.md) | Design Continuant Occurrent groups and inherited constraints | 15 min |
| [CA-P-1907](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/23-CA-P-1907-TASK--mark-entity-drop-and-consolidation-candidates-without-deleting.md) | Mark Entity drop and consolidation candidates without deleting | 15 min |
| [CA-P-1908](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/24-CA-P-1908-TASK--present-compact-entities-graph-candidate-for-operator-review.md) | Present compact Entities Graph candidate for Operator review | 15 min |
| [CA-P-1909](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/25-CA-P-1909-TASK--build-and-verify-the-accepted-core-entities-graph.md) | Build and verify the accepted Core Entities Graph | 15 min |
| [CA-P-1910](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/26-CA-P-1910-TASK--prepare-the-accepted-core-subject-migration-preview.md) | Prepare the accepted Core Subject migration preview | 15 min |
| [CA-P-1911](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/27-CA-P-1911-TASK--apply-the-approved-core-subject-migration.md) | Apply the approved Core Subject migration | 15 min |
| [CA-P-1912](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/28-CA-P-1912-TASK--verify-the-migrated-core-graph-reproduction.md) | Verify the migrated Core graph reproduction | 15 min |

Each child owns its immediate is_decomposition_of relation. A prerequisite owns blocks; folder order is navigation, not dependency authority.

Shared graph code/fixtures have one integration owner or sequential edits; no concurrent writes to shared files. Read-only reviews may share inputs. New required defects get separately admitted bounded fix Tasks and fresh affected checks.

Required relation gaps found by the coverage Task become direct children of its group and block golden fidelity. That group cannot be Done while such required work remains.

### Definition of Done

the Plan is **not** Done **if** ((either graph is missing **or** cannot be reproduced through its admitted MCP route for the same current pinned Core selection) **or** (a required node, relation, Property owner/value, constraint **or** source reference is omitted, invented, mixed across graph kinds **or** unresolved) **or** (a required test **or** independent review is failed, blocked **or** incomplete) **or** (the serving implementation is not bound to the reviewed code **or** the required runtime is unavailable) **or** (output publication **or** a required Run/Journal receipt is unconfirmed) **or** (source Atoms **or** unrelated work changed without authorization) **or** (any direct decomposing Plan is **not** Done)).

An `incomplete`, `conflicting`, `stale`, `blocked`, `failed` or recording-pending result remains that result. A valid no-op needs current selection, matching prior output evidence and the required actual receipts. A generated file, a queued Run or a successful reload alone does not satisfy this Definition of Done.

### Review disposition

The 2026-10-10 repair adds the complete relation-occurrence ledger and sealed candidate handoff, four bounded follow-on Tasks with explicit acceptance/migration gates, and both DOT hashes. This records Plan repairs only; no candidate, migration, Core Subject change or graph execution has been performed by fixing the Epic.

Independent reviews covered graph semantics, execution/admission and Plan structure. This revision adds explicit Property ownership and owned-Core selection, separates manual Plan creation from admitted execution, resolves overlap through CA-P-1110 decomposition, binds live runtime identity to reviewed code, splits broad work into bounded leaves/composites, and uses a parenthesized Definition of Done.

The proposal's independent reviews are retained as planning evidence, not implementation acceptance or MCP admission. These carriers are created manually; source/runtime admission and required owner actions remain execution prerequisites.

### Evidence pointers

- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/generate_entity_graph.py`
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/capability_discovery/service.py`
- `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_routes.py`
- `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json`
- CA-D-539: strict graph request/result contract.
- CA-R-1835–1838: graph fidelity, outcome and shared recording requirements.
- CA-R-1246, CA-R-1454, CA-R-1435 and CA-R-1347: graph-qualified term relations and hierarchy.
- CA-M-306, CA-D-460, CA-D-469, CA-D-470, CA-D-481 and CA-R-1599: Plan authoring, carrier layout, direct decomposition and mandatory Definition of Done.
