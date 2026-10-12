---
atom_id: CA-P-1959
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 18
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Term, Property, Carrier, Revision, Scope Unit, Projection, Plan, Tool, Journal, Operator]
version: 52
updated_at: "2026-10-12 04:30:14 +0400"
relations: {}
---
# Summary

Improve entity model — Stage 2

## Objective

The Core Meta-model has consistent Entity origins in RMEDO Subjects, then consistent Summary, Substance, Scope and Details, in that order.

## Details

### Order

1. Complete CA-P-2167 first: review/update the remaining Tool RMEDO, independently verify the contracts, implement the bounded gaps, then independently verify the actual Tools on isolated fixtures.
2. Refresh current source evidence and review the proposed Subject mappings against candidate #3 and the latest Operator decisions. Then complete CA-P-1909–1912's shared accepted-graph, sealed-preview, migration and reproduction gates. Independent design/review preparation may run while the Tools are prepared; affected mapping execution and final packets wait for the Tool receipt.
3. Only after the complete Subject gate passes, review/update and independently verify affected Step-2 RMEDO. Prepare and verify the Terms compiler, identity/filename consumers and Applicable Methodology compiler before their affected content or consumer usage. Derived Terms compilation stays in Step 2.
4. Update Core Summary, Substance, Substance Scope and Details, including optional Semantics where adopted, in that order through reviewed bounded batches.
5. Verify the final sources, reproducible graphs and the identity, filename, Applicable Methodology and Terms Graph acceptance cases below.

The Operator added CA-P-1978 as the first Task: review and update the Tools' Requirements, Methods, Evaluations, Delivery and Operations before implementation. This exception covers only Tool-governing RMEDO in their declared Engine Scope Units. Core entity-model Subjects, grammar and ordinary content stay behind their existing gates. Creating or updating this Epic records work; it does not execute the repair or migration.

CA-P-1978 and the completed lookup/preview/selector Tasks remain historical Done receipts. The Operator's latest tools-first request adds CA-P-2167 for the remaining gaps: patch-preview eligibility for current non-archived originals rather than literal `Active`; an explicit approved notation profile at the public graph entry point; and an admitted Subjects-only application route. Each affected implementation waits for updated, independently verified RMEDO. Independent fixture verification precedes use. The existing standalone apply guard remains until the route is intentionally implemented under those contracts; it is never bypassed. Tool readiness does not approve a live source packet.

### Source and model boundary

- Select Core Meta-model by itself, not Core plus Project Configuration or Extensions. The current declared authoring root is `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL`. Reopen `project_structure.toml` before execution and pin the actual current original sources. Delivered/installed/Applicable Methodology copies are not editable authority.
- Step 1 concerns R, M, E, D and O Subjects: `governs` and `depends_on`. Scope ownership and Substance applicability stay distinct. Atom incidence is not a native Entity or Term relation.

- For the later Core Subject migration, the allowed roles are exactly Requirement, Method, Evaluation, Delivery and Operations. Report Concern, Analysis, Plan and other roles as excluded. Check both the declared Core source path and `current_scope_unit: CORE_META_MODEL`; a mismatch is a finding, not a silent inclusion or exclusion. CA-P-1978 and its children instead select the declared Engine Tool Scope Units and their actual owning scope; the Core filter does not apply to that Tool-RMEDO repair.
- The prospective target is [candidate #3](../_projection/core-entity-review/presentation/operator.model.candidate-3.md), reconciled with the latest Operator decisions: Entity has Object, Term and Selection branches; Object has Occurrent and Continuant branches. History groups Revision and Journal under Continuant. Carrier is also under Continuant. Dependent Objects share their bearer's lifecycle. A Selection expression is distinct from a saved definition or materialized Projection. Candidate paths and categories are not automatically admitted native grammar or arbitrary GOVERNS targets.
- Keep the captured review frozen at commit `a971d0e00c33c779f485fc8cad63194894d440fb`. The [older seven-root candidate](../_projection/core-entity-review/presentation/operator.entity-graph.candidate.json) and [consolidated review](../_projection/core-entity-review/consolidated/contract.md) remain historical evidence, not the prospective target. Their 442 display proposals are not executable replacements, and 149 follow-ups must not be guessed or hidden. CA-P-1966 must review existing proposals against candidate #3, including `Atom.ID`, `Scope Unit.ID`, History and Object/Term/Selection distinctions, before the shared acceptance/preview route. Keep historical layers unchanged; rebind current source pins and record which proposals remain supported, change or stay unresolved.
- Latest Operator input wins. Use the existing 90% threshold: investigate missing evidence; ask only when a concrete unresolved decision remains below it.

Latest notation correction: compact model notation uses only `/`, `.` and `:`. `@` is not a Subject/carrier Relation operator. It separates Atom ID and Version in the agreed filename convention, `AtomID@Version-SCOPE_NAME--summary.md`, for all Atom file statuses. Use the owning Scope Unit's name, not its label or full path. Stored Atom ID and Version remain separate fields. D-policy and filename-consumer adoption belongs to Step 2; this Plan does not rename current or archived carriers.

The Operator clarified: Atom.Substance is the shared field; Claim, Question and Issue are labels, not separate dependent Entities or allowed values. Preserve the owning Atom's Content Role. Exact Atom/Claim can map to Atom.Substance where it refers to primary content; compound paths retain their separate owner/domain checks. CA-P-2047 records the actual answer as an additional pinned decision, without rewriting the frozen review inputs. Rename body labels later, in Step 2.

### Simple execution boundary

The Operator approved the five-definition grammar exception during Step 1. CA-P-1977 records the actual answer; CA-P-2059 adopts only those exact grammar definitions and their replacement/history effects. All other ordinary content stays in Step 2. Native slash admission and live Subject migration remain separate.

- [CA-P-2059 — Adopt the approved Subject grammar definitions](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/15-CA-P-2059-TASK--adopt-the-approved-subject-grammar-definitions.md)

Reusable Tools operate correct files only: structural Subject lookup and exact pinned Subject-only preview/update. Repair broken carriers and migrate notation with small ad-hoc scripts. Do not build a reusable repair/migration framework. This latest Operator direction narrows the older Tool work below; it does not waive source pins, exact approval or the existing live-write guard. Commit after each completed Task.

### Tool audit and safe cutover

The initial audit found that ATOM_SEARCH searched whole-carrier text and ATOM_UPDATE replaced complete frontmatter, so supplying only Subjects lost other metadata. It also found a preview-only migration planner. These are historical findings; later Subject Tool completion receipts below describe the bounded repairs. Reopen the actual current implementation and guards before preparing a live preview.

Lookup must target exact Subject fields and return occurrence/source pins. Preview must use explicit replacements, preserve unrelated bytes and account for Version +1, updated_at, history and Journal effects. No full-frontmatter rewrite, guessed mapping, new unguarded writer or bypass of existing admission is allowed.

Tests must preserve every unrelated frontmatter field and body byte, not just named sections. Use a separately authored expected occurrence/edge ledger; the verifier must not call the producer's graph builder. A deliberate wrong output must fail the check. After grammar support changes, CA-P-1975 rechecks the exact implementation before any final migration preview.

The five-definition grammar exception is approved and adopted by CA-P-2059: / is broader-to-narrower, . is bearer-to-dependent, : remains Property-to-allowed-value, and @ is outside Subject syntax. Current original Subjects remain unchanged. CA-P-1965 must implement the approved profile before the final migration preview. All other body work stays Step 2; native slash admission and selector grammar are not authorized by this exception.

Live application needs a separately approved exact sealed packet, current pins and the existing admitted mutation boundary. Candidate approval and Tool approval are not that packet approval. Changed pins require a fresh preview. Preserve current Atom identities and history; do not delete entities, fabricate relations or rewrite archived history.

For each identity-preserving current Atom update: keep its ID, set Version to exactly old Version +1 and use the actual Project-time effect timestamp. Current means non-archived, not necessarily `Active`; preserve its intended Status unless the approved change explicitly changes Status. Classify the predecessor as Archived history without incrementing that predecessor's Version again. At most one non-archived original exists per Atom ID; archived originals may share that ID at different Versions. An Active-only default view remains a filter, not the definition of currentness. Existing Tool source restrictions still apply and must not be bypassed. The sealed packet must define how execution-time metadata is bound and hashed; an illustrative preview timestamp is not an execution receipt. Preserve exact prior contents/versions through Git. An archive Carrier is a historical location, not a second editable source. Journal records identify actual effects/Atom IDs, not duplicate contents; missing required recording prevents success.

### Ownership and reuse

Own work: none. This Epic is completed through its direct decomposing Plans.

Preparation Tasks do not complete a mapping, application or content-update group. Their bounded work children must exist and finish, and the group's real output/effect checks must pass. Waiting for an Operator decision is a gate, not 15 minutes of assigned work.

This Epic owns the Operator's new Subjects-first/content-second sequence. Reuse CA-P-1872's existing builders. CA-P-1909–1912 retain the sole accepted-graph, preview, application and reproduction route: CA-P-1967 prepares its candidate packet only after CA-P-1909 is Done; CA-P-1910 owns the one final approvable sealed preview; CA-P-1968 organizes batches executed only under CA-P-1911's authorized application; CA-P-1969 consumes CA-P-1912's one verification receipt and checks the content-update gate. No second preview approval, source execution or competing completion receipt is created. If this shared route is unavailable or its current gates conflict, stop before the affected stage. Creating this Epic does not close or rewrite those older Plans.

Use MCP only when its advertised, admitted execution capability supports the exact operation. If MCP does not support it, do not use MCP or invent a binding. Use an already admitted, authorized local method if one exists; otherwise report the unsupported operation. Local work must not bypass an MCP-required sealed envelope, approval, source pin or write guard.

The Terms Graph, identity/filename and Applicable Methodology contracts and their affected consumers described below are in scope for Step 2. The Terms Graph remains separate from the Entities/Objects Graph. Keep MCP delivery, Apps/viewers, unrelated native fact admission, release/install/runtime activation and unrelated source/structure work out of scope. Direct authoring and isolated preparation remain without MCP/FPF under the retained Operator instruction. Live writes still require the admitted mutation route and exact approval; if that route is unavailable, stop. No raw internal call, fabricated authorization or Run/Journal receipt is allowed.

One integration owner controls shared-state changes and Git. Parallel workers may own disjoint source reviews, implementation modules or tests. Own-work Tasks fit at most 15 minutes; groups have no own implementation work and must gain bounded child Tasks before execution. BLOCKS records Plan prerequisites; actual Operator decisions/approval, current pins and the admitted route are additional gates. Navigation numbers and Active Status grant no readiness. Scratch/cache files belong in `.caprmedio_tmp`.

Step 2 must classify proposed edits before writing. Changing Atom Type creates an entirely new Atom with a new Atom ID and archives its predecessor; it is not a same-ID Version update. Current authority also requires a new Atom ID when Summary changes; that rule has not been repealed. Preserve predecessor/successor lineage. Identity-preserving Substance/Scope/Details changes use Version +1. Neither semantic display names (`Atom.ID`, `Scope Unit.ID`) nor the filename convention rename `atom_id` storage or lowercase `atom(...)` selector keys.

### Identity, delivery and Applicable Methodology adoption

CA-P-1970 owns this work after CA-P-1969; CA-P-1974 prepares bounded review, source-change, consumer-alignment and independent-verification Tasks. These are planned changes, not completed adoption:

- Review and align lifecycle, identity, history and D rules before changing affected writers, lookup, filename/reference handling or validation. Historical Atom references use Atom ID plus a separate Version Number. `@Version` belongs only to the filename convention, not stored identity or a new lookup/Subject shorthand. Plan exact carrier/reference changes and preserve history; do not mass-rename files as part of Subject-only application.
- Applicable Methodology selects only current, non-archived versions of eligible selected sources. Non-archived does not by itself make an otherwise ineligible source admissible. Older archived source versions remain history.
- Each projected member preserves its source Atom ID, Version Number and authored content. Only its projection-local Status and provenance may differ. An excluded member may be projected to Archived; that disposition is distinct from a historical source version and does not mutate its source.
- Authored content corrections belong in Project Configuration, then enter the Projection as selected source Atoms. The whole Projection has one lifecycle. Its members do not gain independent source authority or their own version increments.
- Review the governing Core and Engine RMEDO, then align the existing Applicable Methodology compiler and affected consumers. Test Core/Extension/Configuration selection with isolated fixtures without widening the Core-only Subject migration to installed or projected sources. No live Applicable Methodology publication, installed-copy refresh or release is implied.

CA-P-1971 must verify that updates preserve a non-Active current Status; no duplicate non-archived originals are admitted; archived versions keep the same bare ID; archiving does not add a second Version increment; Type changes replace identity; and all-status filename/reference handling follows the agreed D rule. Applicable Methodology checks must reject historical or otherwise ineligible inputs and content/ID/Version drift, permit only the declared projected Status/provenance differences, and preserve Config-authored corrections and source provenance.

### Terms Graph — agreed direction and planned work

The Operator asked to update this Epic before applying the Terms Graph changes to active Core. The [Terms Graph section of candidate #3](../_projection/core-entity-review/presentation/operator.model.candidate-3.md#33-terms-graph--definitions-from-real-cases) records the agreed direction; neither that candidate nor this Plan is a completed Core adoption or implementation receipt. The following decisions supersede the earlier exclusion of Terms Graph work and the candidate's former single-definition-owner proposal:

- Derive definitions from real uses in selected source Atoms, including their Semantics where present. Do not require a separate layer of Term-definition Atoms or one owning Atom for each Term's meaning.
- Compiled definitions belong to the Terms Graph Projection. They can be reused when creating Atoms or other Projections and can reveal conflicts, gaps and incoherence. Source Atoms remain authoritative; reuse does not turn derived wording into source authority.
- Preserve contributing Atom IDs, Version Numbers, source passages, applicability scopes and declared source coverage. Correct conflicting source content, then rebuild affected Projections. Preserve uncertainty instead of inventing a settled meaning.
- Preserve different meanings in different scopes. Flag a conflict where incompatible meanings apply to the same case; uncertain overlap remains unresolved.
- A shared meaning does not require identical allowed-value sets. `*.Status` selects actual Status uses; it does not create properties. `Scope Unit.Status` does not exist in the candidate. Keep bearer-qualified properties distinct from the shared Term.

CA-P-1970 owns this work after CA-P-1969 passes; CA-P-1974 prepares its bounded children with the Terms Tools before affected content or consumer usage. First review current Terms Graph RMEDO, author the required replacements/revisions, and independently verify the actual contract packet. Start with CA-R-1335, CA-R-126, CA-R-1319, CA-R-1279, CA-M-114 and CA-R-1454, then follow their affected authoring, Evaluation, Operations and Delivery rules. Preserve useful source Claims and native Relation admission; do not delete Definition Atoms merely because the separate-definition requirement changes. No new derived Terms compilation or ordinary Core content change is pulled into Step 1.

After the affected RMEDO is reviewed and accepted, align the existing graph extraction, compilation and diagnostic code and its fixtures. Reuse CA-P-1872's builder work and account for its existing Terms Graph plans instead of creating a competing generator or completion route. In particular, reconcile CA-P-1875's definition-extraction contract and CA-P-1877's recognition work with the new contract; their former single-definition-owner checks cannot substitute for the new acceptance cases. Engine changes are limited to the affected graph capabilities and their governing RMEDO in the declared Engine scopes; they are not part of the Core-only Subject source selection.

Required acceptance cases: a definition compiled from multiple source cases; reusable output with source traceability; equal meaning with different allowed-value sets; distinct meanings in disjoint scopes; incompatible meanings in an overlapping case; unresolved scope or missing evidence; and a source correction reflected by rebuilding. Also reject invented Status properties, authoritative projected definitions, unsupported native edges and silently resolved conflicts. CA-P-1971 checks the independently verified results. Updating this Epic schedules that work; it does not begin content changes, builder execution or live migration.

### Decomposing Plans

- [CA-P-2167 — Finish Tools before Stage 2 execution](18-CA-P-1959-EPIC--improve-entity-model-stage-2/30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution.md)
- [CA-P-1978 — Review and update RMEDO for Subject Tools](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/01-CA-P-1978-TASK--review-and-update-rmedo-for-subject-tools.md)
- [CA-P-1960 — Define safe Subject Tool contracts](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/02-CA-P-1960-TASK--define-safe-subject-tool-contracts.md)
- [CA-P-1961 — Implement field-aware Subject lookup](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/03-CA-P-1961-TASK--implement-field-aware-subject-lookup.md)
- [CA-P-1962 — Implement sealed Subject patch previews](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/04-CA-P-1962-TASK--implement-sealed-subject-patch-preview.md)
- [CA-P-1963 — Verify Subject Tools on isolated fixtures](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/05-CA-P-1963-TASK--verify-subject-tools-on-isolated-fixtures.md)
- [CA-P-1964 — Resolve the Subject grammar cutover boundary](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/06-CA-P-1964-TASK--resolve-the-subject-grammar-cutover-boundary.md)
- [CA-P-2061 — Review grammar-aware Subject Tool contracts](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/16-CA-P-2061-TASK--review-grammar-aware-subject-tool-contracts.md)
- [CA-P-2062 — Align Subject Tool grammar contracts](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/17-CA-P-2062-TASK--align-subject-tool-grammar-contracts.md)
- [CA-P-1965 — Support the approved Subject grammar in Tools](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/07-CA-P-1965-TASK--support-the-approved-subject-grammar-in-tools.md)
- [CA-P-1975 — Verify grammar-aware Subject Tool readiness](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/14-CA-P-1975-TASK--verify-grammar-aware-subject-tool-readiness.md)
- [CA-P-1966 — Map current Core Subject origins](18-CA-P-1959-EPIC--improve-entity-model-stage-2/08-CA-P-1966-EPIC--map-current-core-subject-origins.md)
- [CA-P-1967 — Seal the exact Subject migration preview](18-CA-P-1959-EPIC--improve-entity-model-stage-2/09-CA-P-1967-TASK--seal-the-exact-subject-migration-preview.md)
- [CA-P-1968 — Apply approved Subject migration batches](18-CA-P-1959-EPIC--improve-entity-model-stage-2/10-CA-P-1968-EPIC--apply-approved-subject-migration-batches.md)
- [CA-P-1969 — Verify Subjects before content updates](18-CA-P-1959-EPIC--improve-entity-model-stage-2/11-CA-P-1969-TASK--verify-subject-migration-before-content-updates.md)
- [CA-P-1970 — Align Atom content after Subject migration](18-CA-P-1959-EPIC--improve-entity-model-stage-2/12-CA-P-1970-EPIC--align-atom-content-after-subject-migration.md)
- [CA-P-1971 — Verify the Stage 2 entity model](18-CA-P-1959-EPIC--improve-entity-model-stage-2/13-CA-P-1971-TASK--verify-the-stage-2-entity-model.md)

### Current planning checkpoint

CA-P-2166 records the completed selector/metadata increment and its zero-quarantine inventory in [the increment receipt](../_projection/core-entity-review/stage2/approved-implementation/current-increment.md). Those recorded results supersede the older open-selector/eight-quarantine reports below; they are not a fresh scan performed by this plan update. Candidate #3 and the latest decisions are now the prospective target. CA-P-1966's current-source re-pin and candidate-compatibility review remain pending, as do accepted graph, sealed preview, live Subject migration and Step-2 adoption. No historical mapping receipt establishes readiness for those steps.

CA-P-2167 now gates affected mapping execution and the shared graph/preview/application/reproduction stages. Each affected implementation waits for independent current contract verification, and production use waits for independent fixture verification. Parallel edits require disjoint files. Preview and application share UPDATE contracts, so one file owner serializes those changes and re-pins/re-verifies affected packets after a revision. Current source adaptation/re-pinning is still pending. Live application still needs CA-P-1910's separately Operator-approved exact sealed packet and current pins. Navigation number 30 preserves the historical folders; the new group is first in execution order.

The Operator chose to extend the existing admitted MCP update action with Subjects-only application. CA-P-2170 aligns that exact route's RMEDO, then independent current contract verification gates CA-P-2173's bounded implementation. This choice grants no local transport exception, completed admission or live Core effects; CA-P-1910's exact sealed migration packet still needs separate approval and current pins.

CA-P-2168/2169 are Done after [independent preview/currentness and public graph contract acceptance](../_projection/core-entity-review/stage2/tools-first/contract-acceptance.md). CA-P-2170/2171 are Done after [fresh independent acceptance of the seven-source MCP application packet](../_projection/core-entity-review/stage2/tools-first/application-contract-acceptance.md), committed as `89da2e93d`. The new receipt covers the overlapping UPDATE revisions rather than inheriting their old pins. It releases CA-P-2178–2180 only when their concrete dependencies are ready; any later source change requires renewed acceptance. CA-P-2172/2175/2176 complete the bounded preview/graph increment in [its verified snapshot](../_projection/core-entity-review/stage2/tools-first/preview-graph-verification.md). CA-P-2167/2174 remain Active: application implementation, combined independent fixtures, runtime readiness and live migration approval stay pending; later intent/materialization changes need fresh verification.

### Historical checkpoint — CA-P-2144–2155

CA-P-2144–2155 complete this bounded increment: eight independently accepted reviews cover 204 origins across 145 owners, adding 59 supported mappings and retaining 145 explicit nulls. The actual saved ledger passes independent current-source verification: 907 sources, 4534 references, 1928 proposed, 1540 unchanged and 1066 unresolved. All 329 distinct relevant tests pass (33 focused, 296 native), plus 112 report controls, four frontier-audit controls and ten complete-ledger wrong-output controls. Original Core and frozen evidence are unchanged. Eight quarantines, selector grammar and final graph/preview/application/content gates remain open. Evidence: `_projection/core-entity-review/stage2/checkpoint-unqualified-integration-2144-2151.json`. This is verified mapping progress, not a completed Epic or source migration.

The checkpoints below are retained history. Their words "current" and "latest" describe the state at the recorded time, not today's source pins or pending decisions.

CA-P-2082–2085 are Done and committed separately: 93 additional disjoint occurrences have 59 independently supported candidate targets and 34 explicit nulls. The supported targets cover Claim Target Scope Unit, Atom ID, Scope Unit Type/order and generic Operator roles. Current definitions, not only the candidate display, supplied the evidence; independent review corrected fourteen initially conservative Atom-ID nulls.

CA-P-2058 is also Done: the original 43 Actor Type correction candidates have accepted targets (33 Operator, 10 AI Agent). This composes existing reviewed evidence; it does not double-count those seven new Operator reviews as another source effect. Raw evidence and the baseline ledger remain unchanged.

Current isolated suites pass: graph 219, lookup 44, update/preview 33 (296 total). Original Core Subjects and ordinary content have no diff since the registry Task was registered. The source migration, accepted graph and content-update gates remain open. Exact checkpoint evidence is `_projection/core-entity-review/stage2/checkpoint-field-research-2026-10-11.json`.

- [CA-P-2081 — Align the closed Core registry authority path](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/18-CA-P-2081-TASK--align-the-closed-core-registry-authority-path.md)

CA-P-2081 is Done: the registry's one closed Core path matches the current declaration. Independent review passed and Root ran all 219 graph tests successfully. The nine source pins, three kinds and closed path guards remain unchanged; the retired root is explicitly rejected. This resolves the previously reported registry path failure, not a modeling or migration gate. Older receipts retain their actual historical results.

CA-P-1965 and CA-P-1975 are Done: the selected-profile lookup, sealed preview and internal graph parser are implemented, independently verified and committed. This is ordinary Tool readiness, not semantic mapping or a live migration receipt. Original Core Subjects and ordinary content are unchanged.

CA-P-2072–2077 completed five independent mapping reviews and one source-drift audit, each with a separate commit. Of 573 proposed follow-up occurrences, 433 have supported candidate meanings, 62 are rejected and 78 remain unresolved. This does not settle the original unresolved research or authorize source edits. The current drift audit matches only the five approved grammar effects; raw stale grammar references and eight quarantined sources stay visible.

CA-P-2078–2080 then checked 52 selected rejected/unresolved cases. Independent review supports ten generic Carrier references and two Applicable Methodology-as-Projection targets; 40 cases remain null. Earlier review files and the baseline ledger are preserved, not rewritten. These are additional supported candidate meanings, not applied Subject edits.

The 27 named Workflow/Step cases expose an identity-qualification gap as well as the existing role/type-owner gap: generic Atom/Workflow or Atom/Step would lose a named definition or binding. Current notation admits neither selectors nor singleton kinds for this purpose. A new Operator question asks whether Atom selectors should cover named and qualified owners; the earlier subtype-only recommendation is insufficient for those named cases. No answer or grammar adoption is inferred.

A confirmed remaining modeling choice affects 220 role/type-qualified mappings across 123 sources: Type, Status and similar fields remain Atom-owned, but selecting a role/type-qualified owner needs either explicit narrower Atom kinds or new selector syntax. The Operator question is unanswered. Do not reinterpret the allowed value Plan as the bearer of those fields or invent a mapping.

Current integration checkpoint: CA-P-2094–2102 are Done. The six independently accepted reports cover 180 current origins across 134 owning sources (80 proposals, 100 explicit nulls). Their findings are now included in the live-verified derived ledger: 1548 proposed, 1540 unchanged, 1446 unresolved across 907 sources and4534 occurrences. Eighteen verifier tests and296 ordinary tool tests pass; ten complete-ledger wrong-data controls reject bad variants. Original Core Subjects/content remain unchanged; eight quarantined sources and the unanswered selector choice remain open. Exact evidence is `_projection/core-entity-review/stage2/checkpoint-subject-families-2094-2099.json`. This is progress, not full mapping or migration approval.

Current integration checkpoint: CA-P-2103–2111 are Done. Their six independently accepted reports cover183 exact current origins (100 proposals,83 nulls). The live-verified derived ledger now has1648 proposed,1540 unchanged and1346 unresolved references across907 original Core sources and4534 occurrences. All317 relevant tests pass (21 focused verifier,296 native tool tests), plus ten complete-ledger wrong-data controls and66 report controls. Accepted proof fields and live supporting evidence are retained; arbitrary non-Core files are rejected. Original Core Subjects/content remain unchanged. Eight quarantines, the selector choice and final migration/content gates remain open. Exact evidence is `_projection/core-entity-review/stage2/checkpoint-subject-families-2103-2108.json`; this is progress, not complete mapping or source adoption.

Latest integration checkpoint: CA-P-2112–2120 are Done. Six independently accepted reports cover 137 exact origins across 101 distinct current sources (87 proposals, 50 explicit nulls). The persisted derived ledger now has 1735 proposed, 1540 unchanged and 1259 unresolved references across 907 original Core sources and 4534 occurrences. All 319 relevant tests pass (23 focused verifier, 296 native), plus ten complete-ledger wrong-data controls and 66 report controls. Original Core remains unchanged; eight quarantines, the selector decision and final migration/content gates stay open. Exact evidence is `_projection/core-entity-review/stage2/checkpoint-subject-families-2112-2117.json`. This is progress, not complete mapping or source adoption.

Latest integration checkpoint: CA-P-2121–2131 are Done. Eight independently accepted reviews cover205 exact origins across148 distinct current sources:71 supported mappings and134 explicit nulls. The persisted ledger now has1806 proposed,1540 unchanged and1188 unresolved references across907 original Core sources/4534 occurrences. All321 relevant tests pass (25 focused and296 native), plus88 report controls andten complete-ledger wrong-data controls. Corrected emission preserves accepted proof exactly; rejected interim hypotheses stay out. Original Core remains unchanged; eight quarantines, the unanswered selector decision and final migration/content gates remain open. Exact evidence is `_projection/core-entity-review/stage2/checkpoint-subject-domains-2121-2128.json`. This is progress, not complete mapping or source adoption.

Latest integration checkpoint: CA-P-2132–2143 are Done, with one commit per completed Task. Eight accepted reviews cover 195 exact origins across 148 current owners: 63 supported mappings and 132 explicit nulls. The saved ledger has 1869 proposed, 1540 unchanged and 1125 unresolved references across 907 original Core sources and 4534 occurrences. All 326 fresh relevant tests pass (30 focused, 296 native), plus report controls and ten complete-ledger wrong-data controls. CA-P-2133 now uses a separately accepted Core-only successor; the withdrawn raw report and receipt remain unchanged as history. Live contract and predecessor proof checks pass. Original Core remains unchanged. Eight quarantines, the selector choice and final migration/content gates remain open. Exact evidence is `_projection/core-entity-review/stage2/checkpoint-subject-domains-2132-2139.json`. This is progress, not complete mapping or source adoption.

CA-P-2144–2152 are Done and separately committed. All 204 selected unqualified origins across 145 owners passed independent semantic acceptance and 112 exact report controls: 59 supported proposals, 145 explicit nulls. Four actual frontier-audit wrong-data controls reject defects. Corrected Projection/Journal false nulls, inverse-kind admission and the Principle omission are reflected only in final accepted reports; unsupported audit claims and display-only prefix rejection are not accepted. Current saved ledger remains 1869/1540/1125 until CA-P-2153–2155's separate integration passes. Original Core remains unchanged; full mapping, selectors, quarantines and migration/content gates remain open. Evidence: `_projection/core-entity-review/stage2/checkpoint-unqualified-research-2144-2152.json`.

### Historical remaining-gate audits

Four bounded read-only audits check remaining coverage, genuine model choices, source quarantines and the shared execution route. They do not authorize selector syntax, source repairs, native admission or body work. Do not create filler work after safe independent checks are exhausted.

- [CA-P-2156 — Audit the remaining Subject frontier](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/19-CA-P-2156-TASK--audit-the-remaining-subject-frontier.md)
- [CA-P-2157 — Identify the remaining entity-model decisions](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/20-CA-P-2157-TASK--identify-the-remaining-entity-model-decisions.md)
- [CA-P-2158 — Audit quarantined Core source carriers](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/21-CA-P-2158-TASK--audit-quarantined-core-source-carriers.md)
- [CA-P-2159 — Audit Stage 2 execution gates](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/22-CA-P-2159-TASK--audit-stage-2-execution-gates.md)

Recorded remaining-gates checkpoint (CA-P-2156–2159): all four bounded read-only audits are complete; this does not complete the Epic. The current working ledger remains 907 sources / 4534 occurrences: 1928 proposed, 1540 unchanged, 1066 unresolved. The frontier separates 242 baseline-only qualified cases from 824 other reviewed nulls, without treating all nulls as selector gaps. Eight carriers / 35 occurrences remain quarantined. The Operator has now chosen migration of the six legacy Atom IDs to new canonical IDs, and quoted updated_at timestamps with explicit UTC offsets. CA-P-2160 records both actual choices; successor IDs, policy alignment and source effects are not yet applied. The Operator also approved qualified/named Atom selectors with case kept significant: Atom is the Entity type; atom(...) is selector notation, not an alias. CA-P-2161 records the actual answer. The three decision questions are answered; grammar alignment, implementation, remaining mapping and exact source-effect gates are not completed by these records. Preserve the captured inventory: its one replacement path and four changed common source rows are the expected five-definition grammar delta. No original Core Subjects/content, native admission or live migration changed. Do not begin Step 2 body work before the complete Subject gate.

- [CA-P-2160 — Record approved quarantine decisions](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/23-CA-P-2160-TASK--record-approved-quarantine-decisions.md)

- [CA-P-2161 — Record case-sensitive Atom selector approval](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/24-CA-P-2161-TASK--record-case-sensitive-atom-selector-approval.md)

### Historical approval — completed implementation increment

The Operator answered all three questions and then requested implementation. Implement case-sensitive atom(...) selectors, migrate the six audited legacy original IDs to fresh canonical CA IDs, and align quoted updated_at values with explicit UTC offsets. This permits only the necessary selector grammar/Tool RMEDO and timestamp-policy exceptions plus the audited metadata/identity repairs; it does not authorize a general body sweep or mass Subject migration. Keep Atom (Entity type) distinct from atom (selector token). Review/align RMEDO before selector code. Preserve frozen evidence; current source effects make old live pins historical, never silently current.

- [CA-P-2162 — Align RMEDO for case-sensitive Atom selectors](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/25-CA-P-2162-TASK--align-rmedo-for-case-sensitive-atom-selectors.md)
- [CA-P-2163 — Implement case-sensitive Atom selectors](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/26-CA-P-2163-TASK--implement-case-sensitive-atom-selectors.md)
- [CA-P-2164 — Migrate six legacy Core Atom identities](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/27-CA-P-2164-TASK--migrate-six-legacy-core-atom-identities.md)
- [CA-P-2165 — Use explicit offsets for Atom timestamps](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/28-CA-P-2165-TASK--use-explicit-offsets-for-atom-timestamps.md)
- [CA-P-2166 — Verify the approved selector and metadata increment](18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/29-CA-P-2166-TASK--verify-the-approved-selector-and-metadata-increment.md)

Post-ID checkpoint (CA-P-2164): six legacy current Core identities now use CA-R-1932 and CA-E-620–624, with Version +1 and quoted actual offset timestamps; CA-R-1677's one current inbound relation is relinked. Seven exact prior carriers are archived and 21 actual schema-v3 Journal observations/effects are validated. Independent verification preserves all other Core files and all bodies/Subjects. Current inventory remains 907 sources / 4534 references, with only the two naive timestamp quarantines left. Earlier mapping ledger/current-pin claims are historical after these identity effects; rebind through the exact approved delta before later mapping or source application.

### Selector grammar checkpoint — CA-P-2162

The separately approved selector increment supersedes the earlier no-selector boundary for the explicit approved profile only. Four Core grammar and ten Engine Subject Tool RMEDO revisions now permit the reviewed initial lowercase `atom(...)` syntax; `Atom` remains the distinct Entity-type Term. All14 exact predecessors are preserved. Independent source/delta verification passed; actual changes are in Journal part7. Current pins are in `selector-tools.current-contract.json`. CA-P-2163 owns code alignment. This is not ordinary Subject migration, native admission or body-sweep approval.

### Timestamp checkpoint — CA-P-2165

The explicit-offset timestamp policy and operative emitters are aligned. CA-D-390 has its exact approved Claim revision; CA-R-1873 and CA-D-559 have new Version2 metadata-only updates. Their old naive bytes are preserved, not assigned guessed historical offsets. Independent source and static code review passed; Root's171 targeted checks passed. Graph timestamps respect bound or selected Settings and reject invalid declared Settings; truly absent standalone Settings retain the local-aware path. This changes no Subject values or ordinary bodies.

### Selector implementation checkpoint — CA-P-2163

The explicit approved profile now parses the reviewed initial lowercase `atom(...)` forms in structural lookup, sealed Subject preview and internal graph/source parsing. `Atom` remains the case-significant Entity-type Term. YAML quote/list serialization is decoded before grammar validation; full literal selected-owner paths remain distinct. Lookup/preview needed no new write path. Independent code/negative checks and Root's418-test combined run passed. Legacy/default behavior, frozen snapshot, source pin sealing and standalone apply rejection remain intact. Current original Core Subject values are still unchanged; native admission and actual Source migration are separate gates.

### Approved increment integration checkpoint — CA-P-2166

CA-P-2162–2166 are complete and committed separately. The final independent original-Core/history/Journal check and Root's418-test run passed with stable production code pins. Fresh Core inventory has907 sources,4534 Subject occurrences and0 carrier quarantines. All24 declared source effects,48 current/archive pins and58 actual Journal events were verified. Original Subjects and frozen captures remain unchanged. `_projection/core-entity-review/stage2/approved-implementation/current-increment.md` records the bounded result. This Epic remains Active: refresh current mapping/evidence, complete the shared accepted-graph/sealed-preview/application/reproduction gates, then perform ordinary content alignment. The old mapping ledger remains historical, not source-fresh approval.

### Definition of Done

The Epic is **not** Done if any decomposing Plan is not Done; affected Tool implementation began before updated RMEDO and independent contract verification, or affected use began before CA-P-2167's independent fixture verification; Subject origins remain unaccounted for or accepted mappings lack current-source and candidate-#3 compatibility checks; a source effect lacks exact approval or current pins; Step 2 began before complete Step-1 verification; ordinary Core entity-model content changed during Step 1 or grammar-body changes exceeded the exact approved exception; required history/records are missing; validation or graph reproduction fails; Terms Graph RMEDO still requires the rejected separate-definition layer; Step-2 content/consumer usage precedes affected Tool readiness; the identity, filename, Applicable Methodology or Terms Graph contracts/consumers remain unaligned or their acceptance cases lack evidence; or completion claims exceed the actual evidence.
