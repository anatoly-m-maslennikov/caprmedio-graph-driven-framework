---
atom_id: CA-P-2401
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 5
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Property, Relation, Artifact/Carrier, Project Structure, Tool, Workflow]
relations: {}
version: 28
updated_at: "2026-10-20T21:23:49.586Z"
---
# Summary

Make Atom and Scope Unit Actions Good

## Objective

Make the PROGRAMMATIC Atom actions complete, coherent and usable through the existing connectors, Workflows and MCP. Scope Unit operations, structure validation/reconciliation and topology mutations are deferred to separate peer Epic CA-P-2480, Make Atom and Scope Unit Actions Good — Stage 2. This Epic records the Operator's decisions from this session; it is not evidence that the implementation already provides them. Its operating-context work now also covers configurable model composition and a shared multi-Project Docker/MCP runtime, with explicit adoption and implementation gates.

## Details

### Agreed PROGRAMMATIC structure

The target structure is:

```text
PROGRAMMATIC
├── TOOLS
│   ├── CONNECTORS
│   └── CAPRMEDIO_TOOLS
├── PROJECT_TOOLS
└── APPS
    ├── WORKFLOW_ORCHESTRATOR
    └── MCP
```

All shown Scope Units are unordered; individual Tool Scope Units belong under the appropriate Tool group.

- TOOLS contains reusable capabilities delivered with the framework, rather than maintenance specific to this repository.
- CONNECTORS contains logical storage access and file/folder mechanics. Backend-specific implementations are adapters within CONNECTORS, not another peer feature group. Connectors do not choose Atom identity, lifecycle or Workflow sequencing.
- CAPRMEDIO_TOOLS contains reusable CAPRMEDIO domain actions, including the Atom and Scope Unit actions in this Epic, usable in any CAPRMEDIO-managed project.
- PROJECT_TOOLS contains only the build, test, release and maintenance operations specific to developing the caprmedio framework repository itself. It is a sibling of TOOLS, not a child of CAPRMEDIO_TOOLS.
- APPS contains WORKFLOW_ORCHESTRATOR and MCP as peers. The orchestrator owns Workflow execution and coordination using Tools. MCP owns discovery and transport for Tools and Workflows; it does not own orchestration or duplicate domain behavior. Preserve other existing Apps; this tree highlights the agreed boundary.

The implementation tasks must reconcile existing TOOLS, CONNECTOR_TOOLS, TOOL_WORKFLOWS, PROJECT_TOOLS, APPS and MCP declarations and contents with this target, reusing capabilities rather than creating duplicate owners. Align applicable RMEDO, project_structure.toml and both governing/delivery bindings during that migration. This Epic update records the target only; it does not itself rename or move folders, change scope declarations, or implement Tools.

### Atom actions

- Find Atoms using filters on any supported Atom property, including nested properties and relations; do not restrict Find to Subjects or a fixed small property whitelist. Validate typed filters and report invalid sources or incomplete coverage rather than silently ignoring them.
- Create any Content Role and applicable Type directly in any status admitted by that Role/Type model, filling and validating all mandatory fields. Do not require intermediate statuses, complete Journal history or retained Draft lineage.
- Update by publishing the next revision file and archiving the exact predecessor. Preserve same identity where current change-classification rules allow it; identity-changing replacement remains distinct. An actual edit advances revision metadata; a no-op does not create a revision or archive.
- Promote ID-free Drafts to Active with a fresh unused identity; no restoration of a previous ID or history/Journal admission gate.
- Cover ordinary file Atoms and folder-backed Plan and Operations containers, including Plan/Epic, Workflow and Step. Preserve exact prior bundles and current container semantics; compose explicitly selected per-Atom operations for bulk work rather than promising a cross-Atom transaction.

### Scope Unit actions — deferred to Stage 2

CA-P-2480 owns Scope Unit create/rename/move/delete, Project Structure and governing/delivery folder validation/reconciliation, and physical/declaration topology migration. Its first inventory Task CA-P-2483 is Backlog. The empty-only deletion decision remains binding there. Historical completed Scope Unit audits retain their original parent/history and are reused as evidence, not moved or claimed as Stage 2 completion.

### Validation and reconciliation

Validate YAML syntax, applicable Role/Type keys, mandatory properties and typed values; exact Markdown heading set and order; and coherence among carried properties, filename and actual placement. Stage 1 consumes existing valid Scope Unit bindings for Atom placement safety; Scope Unit and Project Structure validation/reconciliation belong to Stage 2. Deferral does not waive normal Atom placement or unsafe-binding refusal.

Validate registered relation/placement invariants. For example, the current task membership of an Epic's folder must equal its declared direct decomposition membership, applying reserved status-directory and current-revision rules. Use the registered direct relation and derive inverses; do not add a second independent child list, infer Workflow control flow from containment, or count archived predecessor files as extra current members.

Separate mismatch detection from repair. Support three explicitly selected reconciliation policies: files/folders canonical (repair properties and applicable relations), properties canonical (repair filenames and folder placement), or manual (report differences and make no repair). Canonical means the selected repair direction for this mismatch, not permission to bypass validation, invent identity/semantics, overwrite collisions or discard content. Ambiguous or unsafe repairs remain visible without effects.

### Shared design

Reuse the current coherent connector interface and existing storage owners. Keep domain rules in one owner and file/folder mechanics in adapters. Provide one logical property-update entry point whose mapping resolves whether a property is carried in YAML or in its named Markdown section; do not duplicate values or bypass lifecycle/revision rules.

Represent supported schema/declaration data in versioned external files rather than scattered hard-coded property/heading rules. Preserve protected Content Role meanings while allowing the admitted Type, Relation Type and Graph Rule extension points. Choose the format explicitly; JSON is a candidate. External data must retain its governing authority and not become an independent conflicting source. Cover property location, mandatory/allowed keys, values and body layout.

### Current planning checkpoint — 2026-10-20

The agreed topology above is still a migration target, not the observed Project Structure. The current declaration retains CONNECTOR_TOOLS, TOOL_WORKFLOWS and MCP as direct PROGRAMMATIC children; APPS currently declares WORKFLOW_ORCHESTRATOR. Reconcile those declarations with TOOLS/CONNECTORS, TOOLS/CAPRMEDIO_TOOLS and APPS/MCP, preserving existing capabilities and exact history rather than adding duplicate owners. CA-R-1187 already requires MCP and WORKFLOW_ORCHESTRATOR as APPS peers; the declaration mismatch must be resolved before claiming topology completion. Preserve the separate PROJECT_TOOLS boundary. Other Apps, especially GRAPH_UI, remain outside this Epic's implementation scope.

For every affected Scope Unit, reconcile the declared parent, unordered classification, name/prefix and admitted relative governing/delivery bindings with actual carriers and callers. Update applicable ownership/tier metadata only under its current rules. A delivery place is not another Scope Unit. Do not infer the tree from folders or create unused content-role directories. Preserve the distinction between declarations, intentional non-materialization and actual drift.

### Configurable model workstream

Plan PROGRAMMATIC consumption of the protected base meta-model, activated installed Extensions and the selected Project Configuration. Protect Atom identity/meaning, Content Role meanings and source-bound internal/external distinctions. Installed does not mean activated. Expandable Type, Relation Type and Graph Rule declarations may support explicit permitted overrides, but a Draft or lower-tier configuration does not grant permission to replace Core. Resolve any required Core permission and override-precedence decisions through governed source work before activation.

The accepted planning inputs are the following saved Standard Drafts, not Active requirements or implemented capabilities:

- [Model R](../04_requirement/draft/CA-R--PROGRAMMATIC-STANDARD--compose-expandable-and-overridable-model-declarations.md)
- [Model M](../05_method/draft/CA-M--PROGRAMMATIC-STANDARD--resolve-one-provenance-bearing-effective-model.md)
- [Model E](../06_evaluation/draft/CA-E--PROGRAMMATIC-STANDARD-EVALUATION_APPROACH--check-model-extension-override-and-refresh-contracts.md)
- [Model D](../07_delivery/draft/CA-D--PROGRAMMATIC-STANDARD--deliver-model-inputs-effective-generation-and-limits.md)

Choose the supported versioned file format, extension/configuration admission and precedence, composition site and refresh policy before implementation. JSON is a candidate, not an adopted format. Target supported declaration changes without editing code or rebuilding the image; distinguish data changes from unsupported engine-semantic changes. Preserve exact provider/revision/input-digest provenance, one complete effective-model generation per operation and explicit diagnostics for conflicts or invalid/stale refresh. Effective models and graph views remain non-authoritative derived data.

### Shared multi-Project Docker/MCP workstream

Target one running standalone Docker container and one MCP endpoint serving multiple explicitly bound Projects. This replaces neither the existing per-Project baseline nor its deployment until independently implemented and accepted. No Kubernetes dependency or Graph UI work is included.

Use these saved Standard Drafts as planning inputs only:

- [Shared-runtime R](../04_requirement/draft/CA-R--PROGRAMMATIC-STANDARD--serve-multiple-projects-through-one-mcp-runtime.md)
- [Shared-runtime M](../05_method/draft/CA-M--PROGRAMMATIC-STANDARD--bind-caller-context-and-carry-project-identity.md)
- [Shared-runtime E](../06_evaluation/draft/CA-E--PROGRAMMATIC-STANDARD-EVALUATION_APPROACH--check-shared-runtime-routing-and-state-isolation.md)
- [Shared-runtime D](../07_delivery/draft/CA-D--PROGRAMMATIC-STANDARD--deliver-multi-project-mcp-binding-contract.md)

Select request-bound versus connection/session-bound routing and its client protocol. Codex knowing the directory is not transmission to MCP. Bind the authoritative prefix together with validated Project/root/control-root identity and admitted host-to-container mapping; never route or authorize by prefix alone or silently use the process directory. Define registration, ambiguity, rebind, mount-change and drain/removal behavior. Container recreation needed for mounts is distinct from image rebuilding.

Carry the retained binding/model generation through nested and asynchronous work, effects and recovery. Qualify caches, locks, Runs, receipts, Journal/log storage, outputs and record lookup by Project identity so identical local record IDs cannot collide. Preserve current lifecycle authorization and safe effect/recovery checks. Journal recording is not an admission gate; technical/business logs may use their declared local or remote Journal backend. No OS-level isolation between mutually hostile workloads is claimed.

### Approved Draft-format implementation — 20 October 2026

The Operator has authorized implementation after this Epic update. Bind the bounded increment to Core07 originals D288@21, D378@16, D446@16, D276@21, D568@8 and D570@12. Preserve optional ID-free Drafts; support the new-Atom marker `<PREFIX>-<ROLE>-draft`, the proposed-version marker `<canonical-ID>@<version>-draft`, and legacy `<canonical-ID>@draft`. Carried markers must match filenames and remain Draft-only. Version-qualified markers must match the proposed Version. Canonical Current/Archived identity and one-Current uniqueness remain unchanged.

Work packages, each at most 15 minutes of own work per Task: freeze the identity contract; implement parser/Create/Update handling; implement source-pinned Subjects staging/publication compatibility; implement validators and directly consumed authority fixtures; verify functional/golden cases; align Engine RMEDO and C533; independently review integrated evidence. Record each Task separately and review dependent work before execution.

Retain fresh next-unreused identity for ordinary ID-free promotion and the explicitly source-pinned Subjects-only same-ID publication. The Operator has explicitly authorized generic existing-Atom Draft promotion: `CA-R-123@4-draft` updates canonical `CA-R-123` to Version 4 and archives its exact Current predecessor. Bind the exact target and proposed next Version, and refuse stale, mismatched or colliding targets before effects; do not allocate another identity. This is distinct from ordinary ID-free promotion. Do not add Draft relation eligibility, retained-history/Journal gates, a registry, or an executor protocol.

Acceptance requires positive and negative golden cases, exact predecessor preservation, stale/tamper rejection, compatibility, and no canonical number allocation at Draft creation. Tests use synthetic/disposable Projects, never production MCP traffic. Implementation and test evidence do not imply runtime deployment. Excluded: deployment/release, live staging/publication/migration, Methodology 22-source-map repinning, held-batch replay, and other chat-owned Core edits. C533 stays open until implementation and independent review pass.

### Dependency-ordered work packages

These are unchecked planning packages, not newly created child Task Atoms or execution results. Before executing a package, create its own Task/subtask files under this Epic's matching directory; split until each has at most 15 minutes of own work and one observable acceptance condition. Keep registered direct decomposition and actual folder membership synchronized; do not invent a contains list for files that do not exist.

1. [ ] Deferred to CA-P-2480 Stage 2: capture current scope/binding/caller inventory and reconcile the agreed unordered topology and affected RMEDO. Acceptance: one reviewed target mapping with no duplicate owners, plus verified governing/delivery and declaration changes when separately executed.
2. [ ] Resolve model adoption dependencies: protected definitions, Core permission, configurable override surfaces and precedence. Acceptance: explicit source-bound decisions or C/Question holds; no silent adoption of the four Drafts.
3. [ ] Specify model carrier/composition/refresh and its functional acceptance corpus. Acceptance: versioned contract and independent positive/negative golden cases, including inactive providers, conflicting configuration and torn/invalid refresh.
4. [ ] Implement the smallest supported effective-model path against the admitted contracts. Acceptance: exact-input provenance and generation consistency; verify the claimed no-code/no-image-rebuild data-change boundary rather than assume it.
5. [ ] Specify multi-Project client binding, registration, state ownership and Docker mount lifecycle. Acceptance: an explicit supported protocol and two-Project denial/interleaving cases before runtime changes.
6. [ ] Implement shared Docker/MCP routing and Project-scoped dependent execution, reusing the existing orchestrator and Tools. Acceptance: one container/endpoint actually serves two Projects with correct identity and no cross-Project fallback/effects.
7. [ ] Verify scoped Atom operations, applicable Workflows and MCP through the delivered Docker path; Scope Unit operation acceptance belongs to CA-P-2480. Acceptance: functional evidence for supported Role/Type/status/container cases and two-Project model/state isolation, identical record IDs, continuation/rebind, refresh/removal and path-escape refusals.
8. [ ] Deliver contracts, operational instructions and attributable acceptance records; perform deployment/release only under separate explicit authorization. Acceptance: actual supported limits and unresolved gaps are visible, without turning projections or test reports into source authority.

After every completed Task/subtask, review and update its dependent successor before execution. Blocked work is postponed and recorded as a C/Problem; unresolved decisions are C/Questions. This Epic update starts none of these packages, promotes none of the eight Drafts and claims no new runtime capability. Prefer cohesive implementation of each R/D in one module/few code units under CA-M-393, without sacrificing complete realization or forcing inappropriate coupling.

### Five-day scoped MCP audit — 2026-10-20

The Operator requested review of project sessions over [2026-10-15 14:13:44 +0400, 2026-10-20 14:13:44 +0400), exactly 120 hours. Read only actual MCP calls and paired results for: (1) Scope Unit/project_structure validation, (2) Atom structure and YAML/body/filename/placement coherence, (3) Atom create/promote/archive/status/update/move including P/O containers, and (4) Scope Unit create/move/rename/other updates. Use all relevant project sessions, not only Luna-authored sessions. Keep expected invalid-input refusals, caller mistakes, manual workarounds, missing coverage and actual defects distinct. Freeze exact call/response IDs, timestamps, target/revision and evidence before drawing conclusions.

Register/reuse concrete C/Problems with historical evidence, then check whether they are still active. Separate historical symptoms from current observations and classify active/resolved/unverified honestly; no false resolution from a plan, a code edit or a local test alone. Search for existing matching Problems before creating duplicates. Uncertain effects are inspected, never replayed. No implementation repair, release or deployment is authorized by this audit.

Hard isolation gate: every MCP reproduction/test must use an isolated nonproduction instance, a distinct verified port, isolated project/root/control-root fixture and state/locks/caches/Runs/receipts/Journal namespace. Use independent golden data rather than mutable production Atoms. Never send test effects to production, stop/reload/restart/redeploy production, reuse its state or fall back to its endpoint. If isolation is unverified, block reproductions and continue safe historical/read-only work. Normal governed record publication is not test traffic.

Use as many Luna workers as the independent ready lanes and available slots support: four historical families, isolated harness, and bounded verification/Concern work when inputs are ready. Respect exclusive write scopes and dependency gates; no filler workers. Each Task owns at most 15 minutes and must split before exceeding that budget. After each completion, review and update dependent next Tasks. These current child Task files declare their direct parent; this list is navigation, not a second authoritative inverse Relation.

- [ ] [CA-P-2402 — Freeze the exact five-day project-session MCP call corpus](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/01-CA-P-2402-TASK--freeze-the-exact-five-day-project-session-mcp-call-corpus.md)
- [ ] [CA-P-2403 — Audit Scope Unit and project_structure validation calls](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/02-CA-P-2403-TASK--audit-scope-unit-and-project-structure-validation-calls.md)
- [ ] [CA-P-2404 — Audit Atom YAML, body, filename and placement validity calls](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/03-CA-P-2404-TASK--audit-atom-yaml-body-filename-and-placement-validity-calls.md)
- [ ] [CA-P-2405 — Audit Atom lifecycle and container action calls](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/04-CA-P-2405-TASK--audit-atom-lifecycle-and-container-action-calls.md)
- [ ] [CA-P-2406 — Audit Scope Unit create, move, rename and update calls](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/05-CA-P-2406-TASK--audit-scope-unit-create-move-rename-and-update-calls.md)
- [ ] [CA-P-2407 — Register and deduplicate concrete C/Problems](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/06-CA-P-2407-TASK--register-and-deduplicate-concrete-c-problems.md)
- [ ] [CA-P-2408 — Establish and verify the isolated nonproduction MCP harness](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/07-CA-P-2408-TASK--establish-and-verify-the-isolated-nonproduction-mcp-harness.md)
- [ ] [CA-P-2409 — Recheck current concern state and reconcile the planning boundary](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/08-CA-P-2409-TASK--recheck-current-concern-state-and-reconcile-the-planning-boundary.md)
- [ ] [CA-P-2460 — Reconcile the update-atom lifecycle handoff request schema](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/49-CA-P-2460-TASK--reconcile-update-atom-handoff-request-schema.md)

Planning-only manual publication was explicitly authorized because the connected MCP discovery/context reads returned implementation-call failures. Preserve exact v3 history; do not extend that exception to Concern or implementation writes. The audit starts only after this Epic revision and its Task files are saved and checked.

### Delivery plan and execution rules

Align affected project-local, methodology-source and PROGRAMMATIC/connector/Workflow RMEDO before implementing newly decided behavior. Reuse existing capabilities and keep changes bounded; do not reopen settled fresh-ID, optional-history or deletion decisions.

Decompose into separate Task files under this Epic's matching directory, each with an estimated own-work budget of at most 15 minutes and an observable acceptance condition. Split any larger task before execution. After completing each task, review and update dependent next tasks before starting them. Record actual results; a plan or local fixture pass is not implementation or release acceptance.

Use functional/integration/golden-corpus checks as the primary proof, with only narrowly useful unit tests. Test data must be independent from mutable live project Atoms. Include valid Role/Type/status cases, negative validation, predecessor preservation, no-op, P/O containers, arbitrary property filters, relation/folder mismatches, all three repair policies and nonempty deletion refusal.

Creation of this Epic and its task records does not start implementation, a full suite, deployment or a release.

### Definition of Done

Stage 1 is not Done while a scoped Atom operation, Atom validation/reconciliation invariant or container behavior lacks aligned current contracts and independently checked functional evidence, or required predecessor/body/filename/property/placement coherence is lost or unreported. Atom connector, Tool, Workflow and MCP ownership must be coherent against existing valid declarations; deferred physical topology migration is not a Stage 1 completion requirement.

Configurable-model adoption and the claimed shared Docker/MCP Atom path remain Stage 1 responsibilities with attributable acceptance and declared limits. Scope Unit CRUD, Project Structure/folder validation and repair, empty-only Scope Unit deletion and topology mutations are owned by CA-P-2480 Stage 2. Neither Epic is completed by this split or by its Drafts.

### Operator-authorized manual fallback — 2026-10-20

The Operator confirmed the general rule: if MCP cannot do the job, continue manually. This replaces the earlier planning-only manual exception; it is not permission to bypass source/schema rules, overwrite conflicts, fabricate MCP effects or replay uncertain mutations. Preserve actual prior revisions and record actual provenance. Normal MCP authoring remains usable where it succeeds; recovered discovery/context or an outer preview does not prove carrier-admission success. Production MCP test/reproduction traffic remains prohibited.

The reviewed audit Problems are CA-C-525 (current graph-authority pin mismatch), CA-C-526 (historical uncertain CA-P-1959 update) and CA-C-527 (historical interrupted CA-P-1911 status Run). CA-C-528 separately records the current Concern-status authority gap discovered during authoring. They were saved manually after unchanged local full-carrier preflight refused; no create execute or uncertain historical effect was replayed. One current source problem does not establish deployed impact, and historical symptoms remain unverified today. See the Concern records and .caprmedio_tmp/mcp-audit-20261020/report.md.

### Bounded continuation — 2026-10-20

The Operator requested continuation. Tasks CA-P-2420 through CA-P-2424 independently own the two current validator repairs, exact retained-history reconciliation for the two historical symptoms, and isolated functional-check preparation. CA-P-2425 is a dependent current-source runtime acceptance gate; it cannot start from queued work, unreviewed changes or a stale fixture image. This does not authorize production tests/restarts/reloads/deployment or historical mutation replay. Each Task has at most15minutes own work and must be split before extending it.

### Continuation checkpoint and successor review

Tasks2420-2424 completed their bounded source-repair, historical-reconciliation and preparation deliverables; this is not Epic or deployed completion. Concern identity repair passed516validator tests and source-root/D305 repair passed33focused/related tests. Historical CA-P-1959 failure is now precisely a failed preview, with no lasting source change observed at retainedv90; CA-C-526 remains Active for its unexplained failure, not as an executed mutation claim. CA-P-1911 remains effect-uncertain; CA-C-527 stays Active.

CA-P-2426 found15remaining graph binding drifts, four with changed behavioral sections. New bounded Tasks2427(canonical Concern frozen corpus) and2428(current graph Claim/adapter reconciliation) are prerequisites for reviewed CA-P-2425 isolated acceptance. No automatic pin refresh, production test, deployment or replay is authorized or claimed. The PROGRAMMATIC M projection drove small single-owner changes and frozen functional coverage, not live-corpus tests.

### Current source and runtime checkpoint — 2026-10-20

The earlier15binding-drift statement is catalog-verification evidence, not proof of native admission refusal: current source self-consistency verification does not enforce the manifest expected digest. All26approved graph entries were reconciled only after Claim review. Frozen current graph semantics and canonical Concern/Plan consumers pass their bounded checks; the full validator suite passed525tests before the final Current-target and PlanDraft follow-ups.

The Operator settled any-Content-Role Concern targets; C530 is Resolved and R1022v17 now explicitly requires canonical Current Atom targets (including admitted Done/Canceled/etc, excluding Draft/Archived), with actual affectedness left semantic. P2432 implements this narrow admission; it must not add Journal, retained-review or incoming-link cleanup gates.

New actual child Tasks P2431-P2435 cover frozen graph/status consumers, Concern admission, installedparser diagnosis and DoneTask placement. P2436 reconciles D461PlanDraft placement and its directly broken frozen consumers. P2437 prepares frozen public MCP Concern/Subject regression cases. P2438 builds an immutable reviewed candidate; P2439 executes isolated Docker/MCP proof; P2440 owns separately coordinated deployment after success. Each Task is one file and <=15minutes ownwork; split before extending. CompletedTasks are carried in localdone perD461, exact history preserved.

The installedimagea44ad091 runs older source9fc7a3e and lacks the already-fixed // parser; C532 remains Active until actual deployment proof. The Operator expressly approved replacing the running MCP AFTER isolatedtests pass, without replaying the stoppedbatch. This does not authorize production test traffic or replay/reset/cancel of the inspection-required stage. The only existing canonical replacement flow also commits all checkout changes and runs a full localrelease. The Operator separately expressly approved that full flow, including otherchat current changes, AFTER isolatedtests pass. Coordinate source/Git freeze before starting; approval is not an execution receipt. Epic remains Active; existing historical C526/C527 remain unresolved.


### Reviewed regression and archive-policy checkpoint — 2026-10-20

The final host validator passed 535 tests and frozen Subject notation passed 12. P2441–P2444 completed Current-target identity, qualified Type, inherited Status-base and explicit root Plan-path corrections. These are source/host proofs, not deployed acceptance. The first isolated three-case gate passed all29supported Markdown Role/Status creation pairs but failed Concern creation and errored Subject staging; C540 records the exact receipts. P2445/P2446 narrow fixture preparation and diagnosis do not close P2439. The corrected Subject test connects before client access; the Concern fixture materializes its existing frozen D378 identity authority. Strict validation/effect assertions are unchanged. A fresh immutable image and complete three-case run are required before P2440; no production endpoint or uncertain historical request may be tested/replayed.

The latest Operator decision is flatten archived Plans. D461v15 and E502v13 now place each archived Plan carrier directly in its owning Scope Unit 03_plan/archived folder, without archived parent/child hierarchy. C536 is resolved as a policy question; C539 records separate unimplemented archive-layout work. No physical archive migration, auxiliary-file policy, incoming-link repair or non-Archived status/nesting change is claimed. C533 legacy edit-draft markers, C537 non-ActiveCurrent RMED extension handling and C538 non-Archived suffix validation remain explicit independent limits.

The Methodology source/Git freeze is held for candidate testing and the separately approved full local release. Production replacement and Git checkpointing remain conditional on isolated success; no root Git or production lifecycle effects have occurred at this checkpoint. The Epic remains Active.


### Final isolated acceptance and release handoff

The final selected Docker/MCP gate passed all three tests in 229.835 seconds, with zero failures/errors/skips and protected production equality. Receipt: .caprmedio_tmp/mcp-audit-20261020/isolation/execute/p2439-1q3i92q7/receipt.json. Candidate image sha256:2c2c218b561ff9868d2e6648c32b6ac0c6bb7df587d340cf6134e54bee03c427; source fingerprint d08ba9be7c5d275a5c72e77c24e8a3994cf63ab194f88ff71a4b2426ee0591e6. Coverage is exactly 29 supported Markdown Role/Status creation pairs, Current Concern targets Active/Done/Canceled, and approved double-slash Subject preview/staging with canonical bytes unchanged. No production endpoint was tested, and the uncertain historical batch was not replayed. Fixture failures were fixed without weakening source validation. P2439 and P2425 may close for this bounded evidence; C540 closes for the corrected fixture failures, not as a production-defect or deployment claim.

The Operator-approved normal full local release is now eligible under the coordinated source/Git/runtime freeze. P2440 remains a separate actual replacement responsibility: require its full suite, source/image provenance and fresh readiness before claiming deployment. The all-current-changes Git checkpoints are expressly approved, but have not occurred at this handoff. Current source fixes do not close installed-runtime Problems until replacement proof. The Epic remains Active for wider Atom/Scope Unit operations, topology, model/shared-runtime adoption and C539 flat nested archival; this selected gate is not that broader acceptance.


### Broad-suite fixture repair and retry gate

The first full local release local-20261020-current-target-parser-repair-1412 made authorized checkpoint c1dfc37e4, then exposed a shared legacy Subject fixture missing frozen base Atom.Status authority R1947 after Plan R1539 inherited it. Root intentionally interrupted the already-failing suite; canonical report records tests/KeyboardInterrupt130, not a completed full-suite result. No copy/install/replacement phase ran. C541 records the fixture cause; the production Status/frontier validators were not weakened. One shared test-helper tuple now also copies R1947. All128 affected host checks passed (66 plus lifecycle48 plus staging14).

Four detached worker/agent test services with the exact owned full-suite attempt label remained. Root verified ownership, stopped only those services, retained their containers/data/images, and reverified original production container432d276a/imagea44ad091/running/127.0.0.1:56317. P2451 closes that bounded manual teardown; C542 remains Active for automatic interruption cleanup. No broad cleanup or production MCP request occurred.

P2452 admitted fresh image sha256:febd5bcc189e3eda2b4926206beb23f26d26c7757092580b0ddf56705ac0aac9 with fingerprint b71c2770aef150235984df90e4e0984e17d2b7e8d7a8169ac8de15b3763a15b8. P2453 repeated all three isolated cases with zero failures/errors/skips in217.438s and exact protected production equality; receipt .caprmedio_tmp/mcp-audit-20261020/isolation/execute/p2439-e7s6sznn/receipt.json. Reused historical wrapper labels are not new completion claims for earlier Tasks. P2454 is the dependency-reviewed successor for the same expressly approved all-current-changes full local release. Its broad tests and actual replacement/readiness remain required before closing P2440 or installed-runtime Problems. The Epic and broader uncovered operations remain Active.

### Historical second full local-release failure and repair chain — as of 2026-10-20T15:18:47Z

The second full local-release terminal `local-20261020-current-target-parser-repair-1438` failed before replacement. Exact log: `.caprmedio_tmp/simple_local_release/local-20261020-current-target-parser-repair-1438-tests-a71g3vcj.log`; matching report: `runtime/reports/runid.md`. It covered 410 modules and 3555 tests with zero skips and 12 failed modules: nine `VALIDATE_ATOMS` fresh-child import failures and three shared frozen Plan-status mismatches in `test_proposed_relation_admission`, `test_relation_fixture_isolation` and `test_status_bundle_publication_independent`. Root recorded checkpoint `ac1952165`; no replacement phase ran and these results are not production guard failures.

CA-C-543 records the fresh-child runner/import cause and CA-C-544 records the shared frozen-fixture cause. Active repair Tasks CA-P-2455 and CA-P-2456 own those bounded checks. Their Backlog successors are CA-P-2457 (fresh immutable build), CA-P-2458 (three isolated cases with protected production equality) and CA-P-2459 (approved full-local-release retry). CA-P-2454 records the failed retry and delegates to CA-P-2459 without claiming completed delivery; CA-P-2440 now depends on CA-P-2459 and remains unexecuted. Preserve all prior candidate/isolated receipts and historical failure checkpoints. The Epic remains Active; no deployment, release completion or broader capability acceptance is claimed.

### Historical focused repair, fresh build and isolated gate checkpoint — as of 2026-10-20T15:18:47Z

CA-C-543 and CA-C-544 are resolved for their scoped test-environment causes. CA-P-2455 passed runner13/13 and former fresh-child modules133/133 with zero skips and independent review `APPROVE`; CA-P-2456 passed fixture25/25 (relation8, isolation2, status15) plus2 current Plan-placement checks with strict validation and current D461 placement unchanged, no production guard change, and independent review pending. CA-P-2457 then admitted fresh image `sha256:a26b88751f9e8eb57132f648e114f0af4d0c25ff5acf66a6f891f7d05fb4fab3` with fingerprint `b95525f5be4b87c9b342f52199cd8f9260ff4206c2f130090cf63f4cc3e38f76`; its prelaunch source/image/compose inputs were unchanged, production snapshot equality was true, and independent fixture review was `APPROVE` with no findings.

CA-P-2458 passed the isolated gate in `215.658s`: 3 tests, zero failures/errors/skips, protected production equality true, `production_endpoint_tested: false`, and `historical_replay: false`. CA-P-2459 is now Active and eligible after the required source/Git/runtime freeze, but remains unexecuted. The second full-suite failure and its 410-module/3555-test/12-module boundary remain retained; P2454 and P2440 remain Active. No installed deployment, release completion or Epic completion is claimed.

### Current verified full local release checkpoint — 2026-10-20

The approved release completed successfully. Proof `.caprmedio_tmp/mcp-audit-20261020/continuation/local-release-verified-20261020.json` and canonical receipt `.caprmedio_runtime/simple_local_release/reports/local-20261020-current-target-parser-repair-1521.md` record version `0.4.4.8`, 410 modules, 3680 tests, zero skips/failures and a passing final isolated launcher. The released image is `sha256:a26b88751f9e8eb57132f648e114f0af4d0c25ff5acf66a6f891f7d05fb4fab3` with source fingerprint `b95525f5be4b87c9b342f52199cd8f9260ff4206c2f130090cf63f4cc3e38f76`; healthy container `b1676bbd01e451f6bf5b32237bdc0d44147dbcc7f9da43638ca8de724a939d44` serves port `56317`, the prior container is absent and its old image was removed by the approved release. Parser `6b377172306c9a6aa662f8436885aeee51922e9980606d08d70b0dc2273c0329` was verified in the released package and container. P2459, P2454 and P2440 are now Done for their bounded release responsibilities; C525, C528, C529, C532, C534 and C535 are Resolved only for their repaired deployment blockers. C539, C542, C545 and other unrepaired or historical concerns remain open. This checkpoint claims neither historical batch replay, public release/merge nor full Atom/Scope Unit, topology, model/shared-runtime or Epic completion.

### Draft implementation execution checkpoint

CA-P-2461 completed source-contract review; dependent Active Tasks CA-P-2462 through CA-P-2465 own parser/Create/Update, Subjects staging, validation/frozen authority and functional/Engine-contract alignment. CA-P-2467 owns the latest same-ID generic promotion decision. CA-P-2466 remains Backlog for independent integrated review after those dependencies. Each is a separate actual Task file, at most 15 minutes own work.

Native Update saved Epic v18 successfully with six terminal Runs. Fresh Task Create Run `candidate6-activation-001-f146b92b0c85551f` interrupted with LifecycleError before any Task carrier was observed; preserve its inspect-or-recover-only evidence at `.caprmedio_tmp/draft-format-implementation-20261020/tasks/step-1/dispatch.json`. The batch stopped. All seven Task records were then saved under the Operator-authorized manual fallback, after verifying their destinations absent. No failed Run or held batch was replayed. This checkpoint is planning/execution attribution, not implementation acceptance.

### Marker promotion completion decisions and task split

The Operator has now explicitly confirmed both remaining marker rules: a new-Atom role-only marker such as `CA-R-draft` promotes with a fresh canonical ID; compatible `CA-R-123@draft` promotes to the same canonical Atom using the explicitly supplied proposed Version. Qualified `CA-R-123@4-draft` remains same-ID promotion with exact Current predecessor preservation. ID-free promotion remains fresh-ID. Require exact target/source and canonical predecessor bindings; do not infer a target from a nonunique marker.

Original Core D446@17 is published and independently checked (SHA-256 `189cc02e8a9e085d4e49bc59148bfc013d64ad14d660bc48c17fa66a86272d5c`); its qualified-marker rule requires Current+1 for an actual change and no Version/time/archive churn for an exact no-op. The other two defaults above are explicit Operator/Engine decisions, not an inference from that Core rule's scope. Other five pinned Core originals are unchanged.

P2467 is split into actual child Tasks P2468 (binding/preflight), P2469 (shared safe publication), and P2470 (both-entry acceptance), each at most 15 minutes own work, with dependent review before execution. Parser and validator lanes produced bounded positive evidence; full integrated acceptance still depends on promotion and frozen fixture closure completion. Source/RMEDO alignment is prepared; no deployment or held-Draft publication is implied.

The earlier Task Create interruption was independently attributed to the caller's Done Plan path outside its required done/ folder. The corrected planning carrier is under done/. No product defect is inferred; the interrupted Run remains inspect-only, with no replay.

### Verified execution checkpoint

Source validation passed the complete 542-test validator suite and 28 CLI E2E checks; these are frozen synthetic/host proofs, not deployment acceptance. Source/Engine strict metadata and exact HEAD predecessor archives passed independent audit. ID-free reviewed edit Draft compatibility P2471 is Done; a separate carried-YAML-Version mismatch is assigned to P2473. P2469 Active-only publication passed same-ID archive/no-op and injected cleanup recovery checks, but remains partial. Its new child P2472 completes destination-aware non-Active Current publication/recovery before P2470 acceptance. Prepared native tests exposed further role-only/no-op/recovery cases under diagnosis; no failing case is waived or claimed complete. P2466 independent integrated review and the expressly approved scoped local commit wait for all bounded checks. No release, push, deployment, live test traffic, migration or held-batch replay is authorized by this increment.

### Verified execution checkpoint

The bounded published-Draft source increment is implemented and accepted. ID-free, role-only, qualified edit and legacy marker forms work through staging/parsing/promotion and validation; same-ID publication preserves exact predecessor bytes, correct Current-status placement and canonical child bundles. Exact no-op is mutation-free; failure recovery refuses to overwrite concurrent edits. Independent final review is APPROVE. Receipts: validator 542, CLI E2E 28, native 8, marker 6, model 20, exact source pins 1, full promotion 22, Atom cohort 30, staging 16, contract 5 and workflow 10; overlapping suites are not summed. Frozen source inputs, not live Atoms, were used.

P2462-P2466 and bounded promotion children are Done with exact history and complete container moves. P2467/P2477 remain Active for C546/P2478 residual source-quality follow-up: configured C901 is 12 versus HEAD 13, no newly complex function remains, but _run_create 13->14 and update_atom_action 61->71 are explicit retained increases. No lint-clean or all-work-complete claim is made. C533 remains Active for separately authorized installed-runtime adoption/held-carrier reconciliation. The six Core dependencies and P1959 v130 Journal clarification are verified and included in the expressly approved scoped local commit.

This checkpoint authorizes no release, push, deployment, installed-mirror refresh, migration or held-batch replay. Production tests were not used. Full release suite and full live-project validation were not run for this source increment; the earlier settings-limit invocation failure was caller configuration, not proven project corruption. Root is sole Git/index owner; the local commit follows this accepted evidence. The broader Epic remains Active.

### Current queue and Stage 2 deferral

The latest Operator decision defers Scope Unit operations to separate peer Epic CA-P-2480 (Backlog), with first inventory Task CA-P-2483. This split overrides the broader Stage 1 scope in historical checkpoints and earlier topology paragraphs. No Scope Unit mutation, audit reparenting or completion is claimed. Atom file/container operations, including flat Plan archival, remain Stage 1. Configurable models and multi-Project runtime remain here insofar as they do not execute deferred Scope Unit operations.

Current queue after this verified increment: P2484-P2487 implement and independently accept C539 flat Plan archival in bounded dependent Tasks. C545 retains the narrower current-Step/parameters handoff gap; P2460 diagnosis is Done and the supported route-name context lookup is confirmed. C542 interruption cleanup remains Active after P2482 source diagnosis. Wider audit/planning, model and multi-Project runtime acceptance continue afterward; runtime adoption under C533 still requires its separate authorized flow. C548 tracks inherited lifecycle typing debt, not a new regression. P2478/P2477/P2467 and P2488 are Done; C546 and C547 are resolved. Stage 2 P2480/P2483 remains Backlog.

Fresh discovery and O127/O145 context still return input_schema=null, so planning records use the standing Operator-authorized manual fallback. No effect packet, guessed route or Run replay was sent. Every Task has at most 15 minutes own work; source writes are exclusive and root owns planning/Git integration. No release, push, deployment, migration, production test traffic or held-batch replay is authorized by this continuation.

### Verified Stage 1 increment and next dependency review

Final frozen independent acceptance passed 124/124: native promotion 8, semantic assessment 7, Draft promotion golden 22, Atom cohort 30, selected lifecycle 48 and version history 9. Every final receipt is a fresh run bound before/after to atom_operations SHA-256 4d25dae0e7efb8e6d36755902af1ae11178d18a982f54d6a926e7aa71d11d31e, lifecycle_intents 568516545c8bbd870d9022d157bcdb6382a394da46420458251cd341a7aff4ea and shared fixture 79925d47d09c43a524bab2cb0928460e0dad308b009029743a3db6059daf92be. Independent exact-diff review passed. P2488 repaired only the frozen D288/D378 materialization gap; exact HEAD reproduced the prior failure set. No production guard relaxation, live port, MCP effect, Docker, release, deployment, migration or held-batch replay.

The three read-only investigations are Done: P2460 route-name context diagnosis, P2481 flat archive source boundary, and P2482 ownership-safe interruption cleanup boundary. Their findings are retained in the Task files and bounded P2484-P2487 archive follow-ups. Stage 2 P2480 is the separate Backlog Epic Make Atom and Scope Unit Actions Good — Stage 2; P2483 owns its first inventory. The independent planning review accepted the split. No Project Structure declaration, Scope Unit governing/delivery topology or Scope Unit operation was changed.

Exact current predecessors are retained. This turn uses only new shared flat 03_plan/archived Plan history carriers; older legacy archive/ trees are not migrated or rewritten. Completing P2467 moved its matching current Plan container with 20 byte-identical contained/history files, not Scope Units. Manual planning/provenance publication is within the Operator-approved fallback; no native effect or release receipt is fabricated. Changes remain uncommitted and no new release/deployment authority is inferred.

### Flat Plan archival continuation started

Operator requested continuation. P2484 is Active for the shared Plan archive destination resolver; P2485 bundle safety, P2486 validation/Subject prediction alignment and P2487 independent acceptance remain dependent Backlog work. Four initial ready lanes cover publication owner implementation, frozen functional tests, read-only validator inspection and read-only Subject-history predictions. A fifth independent read-only lane adjudicates optional container assets/history boundaries before P2485 behavior is admitted. Root alone owns planning/provenance and Git. Source changes remain uncommitted; all prior P2478/P2488 edits and exact histories are preserved.

Current Core D461@15 and E502@13 govern flat owning-scope Plan archive placement; General R1521@9 does not restore a conflicting Archived Plan hierarchy. Non-Archived hierarchy, separate descendant actions, exact older bytes, immutable legacy trees and Scope Unit deferral remain unchanged. MCP discovery and route-name context were refreshed read-only: the envelope is available but current-Step/inner parameters remain incomplete under C545. Use the standing manual planning fallback, never guessed effect payloads. The selected locked managed CPython 3.14 environment was synchronized; tests use disposable frozen Project fixtures and no production port. No release, deployment, migration or held-batch replay.

### Latest container lifecycle decision — no modes

The Operator rejected an optional with/without-descendants mode. Archive a container always selects all recursively contained latest Atoms, including descendants already Done, for independently admitted Archive Actions. Requesting Done on a container leaves contained latest Plans already Done unchanged and requests Canceled for every other contained latest Plan. This is a target-Done rule, not an exception for a Done container being archived. Preserve exact older Revision bytes and metadata; retained-history subtrees and non-Atom assets may move byte-for-byte with their matching Directory Carrier. References outside containment are not cascade targets. Keep newly Archived Plan Markdown flat in the owning shared 03_plan/archived area. No new mode, per-child confirmation, transition matrix, cross-Atom rollback, migration or deployment is introduced.

C549 is answered. Reconcile original Methodology R1521/D461/E502 before dependent Engine contracts and implementation. P2485 remains the low-level no-silent-current-child-move guard; new bounded P2494 owns the always-recursive calling Workflow and P2495 its focused frozen functional acceptance. The existing mechanical P2491/P2486 changes have positive bounded checks but final integrated acceptance remains pending. No current request claims this new recursive Workflow implemented or installed.

### Latest accepted mechanical increment and next queue

This checkpoint supersedes earlier pending/blocker/queue notes for the bounded flat-archive mechanics. P2484-P2487 and P2489/P2490-P2493/P2496 are Done. The final replacement freeze passed independent native14+48+9, Subject12+4+5, validator544 and CLI11; exact-code review APPROVE. Prior positive receipts were not accepted after C552 exposed an uncovered branch: one shared Status-predecessor owner fixed it and fresh tests covered non-Plan markerActive, nested Plan markerDone and byte-exact cleanup rollback. Production atom_operations537863a8261c38cf560098949d44a057b0fa7b95cf203c6b6b0a123ca5245284 and lifecycle9e8f56400d8141f1e190f19dd499f2a39dd6346330e383d46ea7be1067107f0d are unchanged across final acceptance. Configured C901 remains12 inherited diagnostics; no lint/type-clean claim is made.

The latest Operator simplification is recorded in project planning, original Core R1521@10/D461@16/E502@14, lifecycle O127@15/O128@15, then Engine O029@10/E306@15. There is one recursive behavior, no mode or per-child confirmation: Archive selects all contained latest Atoms, including Done; target Done leaves contained latest Plans already Done unchanged and cancels other contained latest Plans. Exact older bytes and metadata remain unchanged. C549 is Resolved@3; C550/C552 are Resolved@3 for bounded source defects. Resolved carriers are correctly under resolved/ with exact predecessor histories. Completed P2484/P2487 matching directories moved with all5 contained files byte-identical.

Next dependency is still Backlog P2494@2, then P2495@1, under Active C551: implement the missing narrow O127 calling-Workflow composition above SelectedExecution.freeze/dispatch, keeping each Action/Run single-Atom, deepest descendants first with fresh rebinding after preceding moves. The singleton safety guard is not that caller; recursive execution and target-Done composition are NOT implemented or accepted. C539 remains Active for full user-facing nested archival until this gap is closed. Review/split P2494 before extending15minutes own work, and review P2495 after implementation before execution. C545/C542/C533/C548 remain separately open. Stage2 P2480/P2483 is Backlog.

No new commit, release, push, deployment, installed-mirror refresh, production test traffic, Scope Unit mutation, legacy migration or historical/held-batch replay occurred. All source changes remain uncommitted. The Epic remains Active.

### Recursive caller continuation started

P2494 is Active after dependency review. Four independent read-only lanes establish the actual ingress, reusable containment boundary, frozen functional fixture and applicable source/Method constraints before exclusive implementation. The previous mechanical increment remains accepted at atom_operations537863a8261c38cf560098949d44a057b0fa7b95cf203c6b6b0a123ca5245284; all prior dirty work and exact histories remain preserved. P2495 stays Backlog until reviewed implementation; C551 and C539 remain Active. No new release, deployment, production tests, migration or replay is authorized by this continuation.
