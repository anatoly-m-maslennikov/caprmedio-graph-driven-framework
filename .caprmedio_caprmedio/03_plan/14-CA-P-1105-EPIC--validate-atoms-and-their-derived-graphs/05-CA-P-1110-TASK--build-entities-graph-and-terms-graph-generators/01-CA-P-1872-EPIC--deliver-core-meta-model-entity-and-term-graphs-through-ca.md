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
version: 6
updated_at: "2026-10-10 00:36:36 +0400"
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
2. **Review the current graph and design its structure.** Use current Active Core Atom content to interpret old slash paths, group Continuant/Occurrent, inherit common constraints and mark excessive entities for dropping or consolidation. Keep source evidence and every old identity traceable. Ask the Operator below 90% confidence. Do not change the step-1 graph or Atom Subjects.
3. **Give the Operator the new graph candidate.** Present the grouped, inherited and visibly marked candidate in compact notation using `/`, `.`, `:` and `@`. Use NARROWER_THAN, IS_BORNE_BY, IS_ALLOWED_VALUE_OF and IS_CARRIED_BY with correct directions and qualified identities. Preserve the baseline. Candidate delivery is not acceptance; apply accepted decisions to a separate derived graph before any source migration.
4. **Update Atom Subjects.** After graph review, write the confirmed `/`, `.` and `:` notation into the authoritative Subjects. Reconcile affected grammar contracts, revisions and source references. Rebuild only to verify that the updated Subjects reproduce the reviewed graph.

Step **1 is complete**; step **2 is next and has not started** under this sequence. Steps 3–4 remain pending. Earlier classification drafts and migration code are preparation only, not accepted decisions or source updates. The approved compact graph notation is `/` for broader-to-narrower, `.` for bearer qualification, `:` for allowed values and `@` for IS_CARRIED_BY; step 1 does not apply it to old `/` occurrences. Exact `@` bindings identify the carried state and Carrier rather than assigning a Property value.

This sequence governs the immediate local work without MCP. A mechanical projection is not native semantic admission, a live MCP Run or completion of the whole Epic. The existing MCP delivery work remains separate and pending.

#### Step 1 acceptance receipt

- Builder: `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_ENTITY_GRAPH/mechanical_subject_graph.py`, reusing the existing pinned Subjects reader and snapshot support. Its default is read-only; `--persist` creates three fixed files without overwrite.
- Outputs: `.caprmedio_caprmedio/_projection/core-subject-notation/step1.graph.json`, `step1.entities.graph.dot` and `step1.terms.graph.dot` in the same directory. The earlier `before.graph` files remain unchanged.
- Selection: 908 exact-Active owned-Core sources out of 951 captured source files; 43 excluded sources retain their pins. Extraction is complete: 4,534 Subject occurrences, no unresolved selected sources.
- Graph: 706 full-path/prefix nodes, 294 unclassified `/` links, 66 allowed-value `:` links and 534 literal Term components. The Terms view has no inferred taxonomy links.
- Graph fingerprint: `0ea18486fd43ccd546a5d09888e98bc42f56d42d392e5669fecee19fa25f93d1`. JSON file SHA-256: `57cba13073aa0de34876a734c784a43d124f09ff03584de03252b9d12a89ac0b`.
- Checks: 197 graph/acceptance tests plus 10 builder tests passed. Matching before/after pin-set fingerprints verify all 951 Core source files unchanged. Publication file hashes match their receipt.
- No Main Content classification, dot interpretation, Atom Subject rewrite, native semantic admission, MCP execution or Run/Journal recording was performed.

### Current graph review and candidate Tasks

The Operator added this work on 2026-10-10. Task creation is not execution. Run the new Tasks one by one, with their explicit BLOCKS chain:

`CA-P-1905 → CA-P-1906 → CA-P-1907 → CA-P-1908`

- Review the current Entities Graph derived from exact-Active Core-owned Atoms. Recheck current pins instead of treating the saved step-1 counts as permanent.
- Give the Operator a new graph candidate grouped by Continuant and Occurrent, separating definitions from actual executions.
- Inherit common constraints through justified narrower-than specializations. Declare shared Carrier obligations and other common rules once; show only subtype additions or differences. Do not inherit another Entity's concrete Carrier.
- Use as few genuine root entities as possible without losing distinctions or inventing relations. Explain retained roots and distinguish display groups from independent model roots.
- Check excessive and redundant entities. Mark each proposed drop or consolidation visibly; do not delete nodes, governing Atoms, source Subjects or history. Revision is an explicit drop/consolidation candidate in favor of Version Number and Updated At, with exact historical references preserved.
- Use `/`, `.`, `:` and `@` in the compact candidate display: narrower-than, bearer qualification, allowed value and IS_CARRIED_BY. Reuse CARRIES as the inverse direction of the Carrier binding; do not add an equivalent primitive.
- Use concept names such as `Version Number`, `Updated At` and `Status`, not YAML keys. Present the candidate with plain two-space indentation and compact cross-link statements. Preserve qualified identities and graph ownership.
- Every baseline identity needs a traceable retain/move/inherit/consolidate/drop-candidate/question disposition. Give root counts before and after, count marked candidates separately, and expose uncertainty instead of forcing a smaller graph.

These Tasks refine steps 2–3 above. Their outputs remain proposals for Operator review; they do not accept a new ontology, update the step-1 graph or Core Subjects, rename YAML keys, implement a runtime, or complete the Epic. `@` is approved compact graph notation, not an automatically admitted Subject-path serialization operator.

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
| [CA-P-1905](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/21-CA-P-1905-TASK--review-current-entities-graph-from-active-core-meta-model.md) | Review current Entities Graph from Active Core Meta-model | 15 min |
| [CA-P-1906](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/22-CA-P-1906-TASK--design-continuant-occurrent-groups-and-inherited-constraints.md) | Design Continuant Occurrent groups and inherited constraints | 15 min |
| [CA-P-1907](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/23-CA-P-1907-TASK--mark-entity-drop-and-consolidation-candidates-without-deleting.md) | Mark Entity drop and consolidation candidates without deleting | 15 min |
| [CA-P-1908](01-CA-P-1872-EPIC--deliver-core-meta-model-entity-and-term-graphs-through-ca/24-CA-P-1908-TASK--present-compact-entities-graph-candidate-for-operator-review.md) | Present compact Entities Graph candidate for Operator review | 15 min |

Each child owns its immediate is_decomposition_of relation. A prerequisite owns blocks; folder order is navigation, not dependency authority.

Shared graph code/fixtures have one integration owner or sequential edits; no concurrent writes to shared files. Read-only reviews may share inputs. New required defects get separately admitted bounded fix Tasks and fresh affected checks.

Required relation gaps found by the coverage Task become direct children of its group and block golden fidelity. That group cannot be Done while such required work remains.

### Definition of Done

the Plan is **not** Done **if** ((either graph is missing **or** cannot be reproduced through its admitted MCP route for the same current pinned Core selection) **or** (a required node, relation, Property owner/value, constraint **or** source reference is omitted, invented, mixed across graph kinds **or** unresolved) **or** (a required test **or** independent review is failed, blocked **or** incomplete) **or** (the serving implementation is not bound to the reviewed code **or** the required runtime is unavailable) **or** (output publication **or** a required Run/Journal receipt is unconfirmed) **or** (source Atoms **or** unrelated work changed without authorization) **or** (any direct decomposing Plan is **not** Done)).

An `incomplete`, `conflicting`, `stale`, `blocked`, `failed` or recording-pending result remains that result. A valid no-op needs current selection, matching prior output evidence and the required actual receipts. A generated file, a queued Run or a successful reload alone does not satisfy this Definition of Done.

### Review disposition

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
