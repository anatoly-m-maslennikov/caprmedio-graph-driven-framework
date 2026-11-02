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
version: 103
updated_at: "2026-10-23T13:02:52+0400"
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

Carry the retained binding/model generation through nested and asynchronous work, effects and recovery. Qualify caches, locks, Runs, receipts, Journal/log storage, outputs and record lookup by Project identity so identical local record IDs cannot collide. Preserve current lifecycle authorization and safe effect/recovery checks. Journal recording is not an admission gate; the business Journal stores business records only. No OS-level isolation between mutually hostile workloads is claimed.

### Technical diagnostic logging decision — 21 October 2026

Technical warnings and other operational diagnostics are emitted as structured
records to Docker `stderr` for the selected runtime. Every record includes the
validated Project prefix from Project settings; the prefix is never guessed from
the filesystem path, container, process, or caller. Docker's local logging driver
uses bounded rotation `max-size=10m` and `max-file=3`, `mode=non-blocking`, and
`max-buffer-size=1m`; when full, new technical messages may be dropped so logging
cannot stall the primary operation. Docker logs are removed with the container. No separate
`.caprmedio_runtime/logs/` directory is created, and technical diagnostics are
never appended to the business Journal. A logging failure remains observable
without silently breaking the primary operation.

The Project prefix is read from the existing bound Project selection and canonical
prefix-field validation in the selected immutable settings view. This decision adds
no settings carrier and does not claim full SettingsReader conformance; that
pre-existing reader gap remains a separate readiness caveat.

This decision resolves the sink-policy question for CA-P-2555. P2555 is now Done
at the source/configuration/focused-evidence boundary: six logger checks, 94
AtomSearch tests with no skips, ten MCP protocol tests in 3.990 seconds, four
Docker logging checks plus 21 related checks, and an isolated source-mounted
Docker inspection verified two Project prefixes, redaction, bounded
non-blocking backpressure and no Atom contents. The source-mounted inspection
used the existing version 0.4.4.10 image and is not new-image or deployment
acceptance. CA-C-572 remains Active pending that boundary and the pre-existing
full SettingsReader/M284 conformance gap.

### Current readiness and next queue — 21 October 2026

CA-P-2555 is Done for the bounded source/configuration/evidence scope; CA-P-2552
remains Active because its new-image/deployment/readiness boundary is open. The
production container remained healthy and unchanged; no image build, deployment,
full-suite release or public-release acceptance is claimed. The next queue is
new-image/runtime acceptance of the logging path, followed by the
separate full SettingsReader/M284 conformance gap. Preserve the Docker
`stderr`/Project-prefix, `max-size=10m`, `max-file=3`, `mode=non-blocking`, and
`max-buffer-size=1m` contract while keeping technical diagnostics out of the
business Journal. CA-C-572 remains the active readiness Problem until those
boundaries are independently closed.

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

### Current bounded caller lanes

P2494 is Active@4 and supersedes its earlier Backlog checkpoint. Reviewed pure planner P2497 is Done: 6 semantic tests and 10 adjacent discovery tests passed; independent APPROVE after malformed identity/status refusal was added. P2498 remains Active: initial fixture self-check was not accepted because live Atom/projection reads violate the frozen-corpus requirement; C553 records the defect and a dedicated frozen-source correction is in progress. P2499 is Active for the narrow technical coordinator, P2500 for pure source-derived preview scope sealing, and P2501 for actual MCP/provider/status wiring. These are separate own-work bounds of at most15minutes; split before extending. P2495 remains dependent acceptance, not yet a completion receipt.

The reviewed implementation direction preserves ordinary one-Atom lifecycle admission. Only root MCP preview adds an independently source-derived sibling observed.container_lifecycle seal. Its immutable queued request is a technical authorization envelope, never a fabricated O127 Run. Every descendant and the final parent get distinct fresh ordinary preview/freeze/dispatch admissions, with exact subset authorization, Initiative and actual lineage preserved. Inline member dispatch avoids deadlock in the existing concurrency-one DBOS queue. No currentness exception, extra mode, per-child confirmation, generic orchestrator or new queue is authorized. Marked aggregate status must distinguish technical coordinator identity from actual Source Runs, retain partial effects and stop without replay on an uncertain frontier.

Exclusive lanes: P2500 admission module/tests; P2499 composition module/tests; P2498 frozen fixture/corpus; backend/status owned by the backend worker; root owns MCP/provider entrypoints, planning and integration. Functional acceptance prepares only isolated disposable Projects and waits for these freezes. C551/C539 remain Active; no caller completion, production MCP use, release, deployment or migration is claimed.

### MCP health visibility and authorized local release — 2026-10-21

The Operator requested diagnosis of the currently failing MCP, a same-listener `/health` browser page with health checks, recent Tool calls, recent Workflow statuses and useful safe errors, followed by the normal local release. This latest instruction authorizes that local release after isolated verification and all normal release gates, superseding earlier no-release wording only for this bounded continuation. It authorizes no public release, push/merge, held-batch replay, unrelated Scope Unit mutation or production mutation testing. The normal local release commits all eligible current checkout changes before its gates; preserve unrelated work and report any gate failure without bypass.

Fresh connected discovery returned `outcome: uncertain` / `Implementation call failed; no automatic replay`, while the read-only Gateway status succeeded and reported a serving process. This proves partial failure, not a total outage or completed repair. The current JSON `/health` checks only generation task availability; it does not prove Tool, Workflow or worker health. Do not replay that failed/uncertain call or the prior pending selected Run.

Implement the smallest bounded read-only observation path: preserve the existing JSON ready/status contract for default and machine clients, and render escaped HTML for explicit browser Accept on the same `/health` route and port. Reuse loopback Host/Origin protection. Retain at most 32 process-local Tool observations and 32 Workflow observations derived from actual Gateway calls/results; label since-start coverage and unknown/unobserved/stale state. Keep scheduler state separate from actual Workflow outcome/disposition. Show safe error categories, not raw arguments, outputs, credentials, paths or provider exception text. A health GET does not invoke Tools/Workflows, initialize DBOS/Docker, read broad Journals, reload/recover or create authority/effects. Persistent or cross-process history is outside this first increment.

Update active MCP R/E/D before implementation, using the PROGRAMMATIC M/E/D projections as supplemental guidance and the current originals as authority. Independently test positive and negative behavior using synthetic isolated fixtures, not the live port or mutable Atom corpus. Record real blockers as C/Problems and semantic uncertainty as C/Questions. Existing C545/C551/C554 and C533 are not resolved by a dashboard or a source edit. Each Task below owns at most15 minutes and must be reviewed/split before extending. After each completion, review/update its dependent successor before execution. Root owns governed records, Git/index and release; Luna workers own disjoint code/test lanes.

- [x] [CA-P-2508 — Diagnose MCP failures and admit the health contract](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/68-CA-P-2508-TASK--diagnose-mcp-failures-and-admit-the-health-contract.md)
- [x] [CA-P-2509 — Observe bounded MCP Tool and Workflow outcomes](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/69-CA-P-2509-TASK--observe-bounded-mcp-tool-and-workflow-outcomes.md)
- [x] [CA-P-2510 — Render the same-port MCP health page](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/70-CA-P-2510-TASK--render-the-same-port-mcp-health-page.md)
- [x] [CA-P-2511 — Verify MCP health and history in isolated fixtures](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/71-CA-P-2511-TASK--verify-mcp-health-and-history-in-isolated-fixtures.md)
- [x] [CA-P-2512 — Prepare the authorized local release gate](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/72-CA-P-2512-TASK--prepare-the-authorized-local-release-gate.md)
- [x] [CA-P-2513 — Run local release and verify the installed MCP health page](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/73-CA-P-2513-TASK--run-local-release-and-verify-the-installed-mcp-health-page.md)

### Health contract admitted and implementation lanes opened

P2508 is Done after bounded live/read-only diagnosis and canonical publication of Active MCP R2007/E640/D639 plus Active Problem C555. The actual failed connected request used scope_unit=MCP, not an invalid scope field. Native discovery succeeds from current and deployed code; only the gateway-child call boundary is implicated, and the exact inner cause remains unknown. Preserve that uncertainty rather than asserting a provider-code or image defect. A local release is now explicitly authorized to deliver the health increment after the complete normal gates, not as an unverified cure.

The reviewed source semantics inherit actual Workflow/Step/Tool-call meanings from Core through R1848. Registry observations use only existing generation.tools/snapshot state, never a health probe. New E evidence is fixture/test and post-release observation evidence, not a Journal prerequisite or an additional release gate. P2509 and P2510 are Active with disjoint observer versus HTTP-view ownership; P2511 is Active for independent fixture preparation and waits for their reviewed code before acceptance. P2512/P2513 remain Backlog until dependent review. Use the new PROGRAMMATIC M/E/D views as supplemental guidance; formal packets still require current full source bindings. No code, health-page deployment or release success is claimed by this planning checkpoint.

### Release precheck blocker and independent continuation

The fresh isolated C554 precheck passed3/5 but failed positive Archive(interrupted_pending) and target-Done(partial) with unchanged candidate/fixture hashes. Its frozen D378 pin is already correct; exact nested refusal is still under diagnosis. Reuse Active P2507/C554 for a bounded fixture/expectation repair only when current evidence confirms that cause; do not waive checks, modify live source Atoms as fixtures, weaken production admission or invent an ID naming rule. This is not a failure of the new health page and does not establish a production incident.

P2510 source work is frozen with7 existing HTTP tests and bounded renderer/negotiation checks passed; independent HTTP/security review and P2511 integrated acceptance are pending. P2509 observations continue independently. P2512/P2513 remain dependent on their reviewed outcomes, the C554 precheck and the complete normal local-release gates. The Operator's explicit local-release authorization remains recorded; no release has started, no live mutation test or uncertain-call replay occurred. Root remains sole planning/Git/release owner.


### Final health review and release dependency checkpoint

The bounded C554 fixture repair now passes all5 functional and5 adjacent composition cases. Independent review approves the contract-aligned fixture correction: Objective/Details headings, preserved requested Run identity and canonical Done/canceled relocation expectations. Frozen production and D378 source hashes remain unchanged. This is bounded fixture acceptance, not resolution of the wider recursive-caller or installed-runtime Concerns.

P2510 HTTP/security review is APPROVE after explicit Accept specificity and generation-only readiness wording were corrected. Fourteen focused health tests passed including cancellation propagation, but final observer review found Action results with a parent workflow_run_id could be mistaken for actual Workflow outcomes. P2509 and P2511 remain Active for a minimal identity gate and three isolated regressions; never infer Workflow outcome from an Action or technical coordinator. The final hash-bound gate, dependent Task review, full local release and installed read-only verification remain pending. No release has started and no uncertain call or held Run has been replayed.

### Final source acceptance and release activation

P2509/P2510/P2511/P2512 and bounded fixture-repair P2507 are Done with exact predecessors retained. Final frozen health18/18, existing hot-reload21/21, HTTP7/7, native container functional5/5 and adjacent composition5/5 all pass; overlapping checks are not summed. Independent observer/HTTP and fixture-diff reviews APPROVE. Actual Workflow identity is validated and cannot be inferred from nested Action/Step/coordinator results, invalid identities or scheduler SUCCESS. Health implementation/test hashes are stable across root acceptance.

P2513 is Active after dependent review for the explicitly authorized normal full local release, run ID local-20261021-mcp-health-0434. Use the selected locked launcher virtualenv and all existing commit/full-test/build/install/startup gates; include all eligible current nonignored changes as authorized. Only one production MCP container is running, healthy at127.0.0.1:56317. The gateway-child discovery cause C555 is still unknown; the release delivers new visibility and is not a claimed causal cure. No release has started at this checkpoint. No production mutation test, held Run or uncertain-call replay, public push/merge or Stage2 Scope Unit operation is authorized.

### First release stopped; selected environment repaired before retry

Run local-20261021-mcp-health-0434 committed eligible changes at01ec043df and validated inputs, but the full suite immediately exposed missing dependencies in the selected launcher virtualenv. Root stopped only the verified owned release process (exit130); its failure report/log and local commit remain intact. No package/image install, production startup or replacement occurred. Focused health acceptance had used the separately populated .venv, so its positive evidence was not evidence that the launcher environment was ready.

CA-C-556 records and resolves this bounded preparation issue: synchronize the actual launcher virtualenv from unchanged uv.lock/all groups, select the existing project-local cache rather than the broken inherited shared-cache entry, and smoke-import the real selected dependencies through the exact no-sync launcher invocation. These checks now pass. P2512 has the corrected preflight; P2513 remains Active after renewed dependent review for fresh run local-20261021-mcp-health-verified-env with every normal gate rerun. No failures are waived; C555 remains Active. Production is still the original healthy container, and no held Run or uncertain call was replayed.

### Full-suite fixture mismatch recorded before repair

The fresh environment-verified release remains in its complete test phase, collecting results; its first confirmed failure is a stale expected Plan predecessor path in test_subject_intent_materialization.py (archive rather than canonical archived). Independent read-only diagnosis confirms current shared production resolver and D461/E502 agree on03_plan/archived. A second scan found the same likely issue in test_selected_subject_apply_portfolio.py paths(), where Requirement must retain archive while Plan uses archived. Deliberate legacy-history fixtures are excluded from the repair.

Active Problem C557 and Backlog Task P2514 record this bounded test-only repair. No production or test source edits occur until the current suite finishes; then review the complete failure set, activate/split P2514 as needed and preserve all assertions except the obsolete expected destination. P2513 stays Active and cannot claim acceptance from this failing run; a fresh normal full release is required after focused tests and independent review. The production MCP remains unchanged; no gate waiver, live mutation testing or held/uncertain replay.

- [x] [CA-P-2514 — Repair stale Plan predecessor expectations](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/74-CA-P-2514-TASK--repair-stale-plan-predecessor-expectations.md)

### Full-suite repair lanes expanded without changing production

The complete environment-verified suite is still collecting results. Six failing module reports are now known: intent predecessor path, independent Plan subject portfolio paths, primary bundle owner/fault setup, independent flat bundle history/fault targets, W04 fixture old Plan archive target and W04 Plan Draft selected-binding freshness. The 12-case selected-workflow Docker module passed with zero skips; new health/registry tests remain passing. No final full-suite acceptance or installed runtime change is claimed.

C557@2 records the additional evidence. Backlog P2514 owns only intent/portfolio expected paths. Backlog P2515 owns the two status-bundle fixtures: exact synthetic ownership and flat owning-scope Plan history, preserving Operations/Step local history, recovery assertions and all injected faults. Backlog P2516 owns W04 fixture path/fresh-binding diagnosis, preserving29/8/8 matrix totals and production currentness guards. Two independent reviews found no production recovery regression in the bundle failures. No source edits start until the current full suite finishes; review the complete failure set before activation, then independently accept each repair and review P2513 before a fresh complete normal local release. Each Task owns at most15minutes; split before extending. Production remains the original MCP, with no held/uncertain replay or live mutation tests.

- [x] [CA-P-2515 — Repair Plan bundle ownership and flat history fixtures](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/75-CA-P-2515-TASK--repair-plan-bundle-ownership-and-flat-history-fixtures.md)

- [x] [CA-P-2516 — Repair the canonical Draft predecessor lookup](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/76-CA-P-2516-TASK--repair-the-canonical-draft-predecessor-lookup.md)

### Complete failed gate reviewed; bounded repairs activated

Run local-20261021-mcp-health-verified-env finished with424 modules,3796 tests,zero skips,six failed modules; launcher integration passed. The report and complete log are retained; no package/image installation, MCP replacement or public effects occurred. P2513 remains Active but has no release-success receipt.

P2514 and P2515 are Active for independently confirmed test/fixture corrections only. P2516 is Active under a corrected production scope: Draft demotion successfully publishes a Plan then wrongly reconstructs its predecessor as local/archive, causing a post-effect lookup failure. Reuse the canonical predecessor owner, audit callers, add a focused regression and preserve exact history/recovery/non-Plan semantics. Do not change fixture expected paths to conceal this defect. The earlier assumption that both W04 failures were fixture-only is superseded. The distinct masked Plan preview refusal remains under diagnosis by a separate bounded follow-up P2517 before any related production fix; declaration/observation digest labels alone were not proof of source drift. New C/Problems will retain these two findings separately from C557 fixture drift.

Three disjoint ready implementation lanes are expectation pair, bundle fixtures and canonical Draft predecessor lookup; a fourth independent lane diagnoses the masked preview refusal. Root owns governed records/Git/release. After each reviewed repair, update P2513 before a fresh complete normal local release. No gate waiver, production mutation test, held/uncertain replay or Stage2 Scope Unit operation.

### Separate production findings and fourth diagnosis lane admitted

C558 and C559 are now canonically admitted Active Problems; Active P2517 is admitted for an isolated exact-cause reproduction of the hidden Plan preview refusal before proposing a production change. C557@3 is explicitly fixture-only under P2514/P2515. P2516 retains its identity but is renamed Repair the canonical Draft predecessor lookup; its source owner reuses the publisher's exact canonical history resolver before demotion instead of reconstructing a path after the effect. Existing API, non-Plan local history and exact predecessor semantics remain unchanged.

Four disjoint lanes are running: intent/portfolio expected paths, bundle fixture ownership/flat fault targets, canonical Draft predecessor caller plus regression, and masked Plan preview diagnosis only. The complete failed gate424/3796/zero skips/six failed modules and successful launcher integration are retained, not waived. P2513 remains dependent Active; no next release has started. Source fixes are not deployed evidence and production remains unchanged.

- [x] [CA-P-2517 — Diagnose and restore Plan status preview compatibility](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/77-CA-P-2517-TASK--diagnose-and-restore-plan-status-preview-compatibility.md)

### Fixture-only release repairs accepted

P2514 and P2515 are Done with exact predecessors and current done paths; C557 is Resolved@4 for its bounded fixture-only defect. Release-env focused receipts: intent10,portfolio6,adjacent subject10,bundle24,flat14 all pass; independent final reviews APPROVE without weakening native guards or recovery/byte assertions. P2513 has been reviewed/updated after these completions and still waits for C558/P2516 and C559/P2517 source/regression acceptance plus final frozen integration before a fresh full release. No failed gate is waived; no installed replacement has occurred.

### Canonical Draft lookup accepted; frozen closure diagnosis retained

P2516 is Done and C558 Resolved@2: shared predecessor owner before demotion, exact nested Plan owner-history regression, independent source/test APPROVE, bounded9 checks and fresh root model-driven20/20 in38.153s. The worker's interrupted broader attempt was not counted; the root fresh run passed. P2513 has been reviewed/updated accordingly; no installed/full-release receipt is inferred.

P2517/C559 diagnosis confirms Plan Draft preview was blocked by12 missing frozen containment-frontier authority pins, including D434, not by compared route/outer-manifest digests. Only existing frozen corpus materialization is approved; no live Atom fallback or currentness weakening. A later Plan transition exposed by closure still needs exact-cause diagnosis and full29/8/8 acceptance. Keep P2517 Active and split further before exceeding15minutes own work. Final integration/fresh complete local release still wait; production is unchanged.

### Final frozen repairs accepted; fresh full release activated

P2517 is Done and C559 Resolved after restoring only the missing frozen containment closure and the synthetic Archived @3 suffix. W04 matrix29/8/8 and independent fixture review APPROVE. R1608 historical-registry mismatch was withdrawn after checking that registry entries locate current source re-reading; no blind authority repinning or live Atom fixture fallback. P2514/P2515/P2516/P2517 are all accepted; P2513 has been reviewed after each completion.

The final frozen candidate passes14 unique modules/101 tests/zero skips, covering every previously failed module, native Draft predecessor regression, model/status guards and health. Source/fixture hashes remain unchanged and diff check is clean. The first coordinator passed13 modules/100 tests but lacked the Docker context needed to import the matrix; fresh intended native invocation passed the matrix1 test in74.636s. The configuration error is retained, not counted as acceptance. Fresh normal local release local-20261021-mcp-health-reviewed is now activated under existing authorization, rerunning every full gate before actual installation/startup. No source writers remain. Production is unchanged at this checkpoint; C555 remains Active and no installed success or causal cure is inferred.

### Image names and version/build-date tags — Operator-prioritized increment

The Operator explicitly prioritizes readable names and tags for CAPRMEDIO Docker images before resuming the recursive-container queue. Canonical Tasks P2518–P2521 are admitted below; each owns at most15minutes of own work and is split before extending. P2518 is Active; later Tasks are dependent Backlog. Four ready read-only lanes cover canonical build/callers, regression preparation, source contracts and exact live-image/version provenance. Root alone owns governed records, Git and Docker mutation. Current Project runtime remains untouched.

Reuse repository `caprmedio-runtime`. Carry one additive display tag `<framework-version>-<UTC-build-date-YYYYMMDDTHHMMSSZ>-<first12-image-sha>`. Version comes from the exact safe source/package `version.toml` included in the source fingerprint and OCI `org.opencontainers.image.version` build label. Build date comes from the inspected image's actual Docker `Created`, including cache hits, never tag-maintenance time. Source fingerprint and full immutable sha256 remain the only admission/launch boundary; tags are display metadata, not a mutable override or compatibility proof. New builds and validated reuse share the canonical naming owner; the development builder and disposable test/release callers must be covered without duplicate policy. Do not add latest/local moving aliases. An already bound same-digest display tag is a no-op; an occupied other-digest tag is retained and reported, never moved. Build date is not a source fingerprint input.

The same explicit instruction authorizes adding these display tags to existing positively identified CAPRMEDIO images only after verifying original build timestamp and exact version from embedded/release/source evidence. Unknown historical versions are deferred and reported, never guessed as the current version. No deletion/pruning, image overwrite, container stop/restart/replacement, new release or production mutation test is included. Amend R1901/M356/D594/E600 and release delivery at their current Standard tiers to make this additive metadata permission precise before implementation. Missing current-Step/inner parameters in recovered MCP context remain the existing C545 gap; use the standing Operator-authorized manual fallback for planning/contract records, retaining exact prior bytes and actual provenance, never guessed MCP effect payloads.

The earlier local release `local-20261021-mcp-health-reviewed` completed as version0.4.4.9:425modules/3797tests/zero skips/zero failed modules and launcher integration passed; one installed healthy MCP container and same-port JSON/HTML plus fresh SDK/connected discovery were observed. Its receipt and Journal event dd73c633-b340-4af4-b0d7-cf122710b91e close P2513's execution; this checkpoint reconciles its stale Active carrier rather than rerunning release. C555 original cause remains unknown and discovery coverage diagnostics remain separate. After the naming increment, review the unfinished P2499/P2501/P2503/P2506/P2495 container implementation/functional acceptance frontier before continuing. Stage2 Scope Unit operations and held/uncertain replay remain excluded.

- [x] [CA-P-2518 — Implement versioned and dated CAPRMEDIO image names](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/78-CA-P-2518-TASK--implement-versioned-and-dated-caprmedio-image-names.md)
- [x] [CA-P-2519 — Verify CAPRMEDIO image name and build metadata](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/79-CA-P-2519-TASK--verify-caprmedio-image-name-and-build-metadata.md)
- [x] [CA-P-2520 — Name existing verified CAPRMEDIO images](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/80-CA-P-2520-TASK--name-existing-verified-caprmedio-images.md)
- [x] [CA-P-2521 — Accept image naming and resume container queue](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/81-CA-P-2521-TASK--accept-image-naming-and-resume-container-queue.md)

### Image contract aligned; exclusive source and test lanes activated

R1901@4/M356@4/D594@6/E600@5 now carry the exact version/date/digest display-tag contract and narrow additive permission with unchanged immutable admission. Prior revisions are retained byte-for-byte under each role's archive. D564 ownership-safe cleanup is unchanged: name/version/date never authorize removal. P2518 owns the canonical build/helper/development caller; P2519 is Active for disjoint test/fixture preparation and waits for reviewed source before acceptance. Four investigation lanes completed their initial reports; the historical-inventory lane continues bounded evidence recovery without guessing18currently unknown versions. Docker inventory:29CAPRMEDIO-labelled images all untagged;11versions currently source-proven. No Docker change/restart, new release, public effect or held/uncertain replay has occurred.

### Image review follow-up split before acceptance

P2518's initial source increment is frozen; disjoint P2519 tests are still preparing/running and no integrated acceptance or Docker mutation is claimed. Independent review exposed a development build-to-start digest handoff and Project-temp gap; new child P2522 splits that narrow follow-up before extending P2518's own-work bound. It also closes ambiguous tag-inspection and tag-length boundary details without changing the accepted display/admission contract. Root check found exactly the same3inherited C901 diagnostics in current and HEAD (_bounded_run12, _verify_context11, runtime.main11), not a clean-global-lint claim.

C560 records the image naming defect. Its one native create attempt stopped before publication on the final Project-boundary read-I/O timeout; after target/identity absence checks it was manually saved under the standing fallback, and C561 separately records that postponed admission-performance issue. No validator/time-budget change or blind create replay. Read-only recovery completed with29images,11verified versions and18unknown; the Operator is asked how to display unknown historical versions. Current runtime remains unchanged. Final P2519 acceptance, reviewed existing-image maintenance P2520 and container-queue continuation P2521 still wait.

### Operator decision: remove the eighteen version-unknown historical images

The latest direct answer is just remove them. This supersedes the earlier unknown-version display question and no-deletion bound only for the exact18version-null image IDs in the retained inventory. New Active P2523 owns fresh positive identification, non-force image-only removal and exact readback. No age/name glob, prune, force, container/volume/cache removal, known-version image removal or current-runtime restart is included. Container-referenced images are preserved/reported pending separate authority, not forcibly deleted. P2520 continues additive naming for the11verified historical/current images and the new builder result. No version is guessed and no unknown-tag label will be added. Root remains the sole Docker/Git/record owner; source/tests are frozen after review, with final broader fixtures and isolated build readback pending.

- [x] [CA-P-2523 — Remove the explicitly selected version-unknown images](05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/82-CA-P-2523-TASK--remove-the-explicitly-selected-version-unknown-images.md)

### Final naming acceptance and exact stopped-container cleanup authorization

Root final focused gate109/109 passed in6.495s after the actual formatting/final fixture changes; independent P2522 review APPROVE. A real isolated canonical Docker build produced sha256:650023dd711fad2e48a3446b2780733d20881adbe088a8f63a09af48f938fd83, OCI version0.4.4.9, actual DockerCreated2026-10-21T09:25:17.76190551Z and caprmedio-runtime:0.4.4.9-20261021T092517Z-650023dd711f. Same immutable-ID reuse and full source-fingerprint stability24e231511e70d70e0eff59997694fdb01b706c93e54ddfb2f6d317dd083d1384 passed; no container started/replaced. This is not a new local release or installed runtime adoption.

P2523 image-only pass removed16unknown-versionimages and retained2referencedby6stoppedtestcontainers. The Operator now separately explicitly authorizes those exact6container removals and then those2image removals. Updated P2523@2 binds the exact receipt IDs, fresh stopped/image checks, non-force/non-volume deletion and unchanged running MCP. No other stopped container, known-version image, volume/cache or runtime may be removed. P2520 verified naming follows using the reviewed canonical helper. Docker lacks atomic tag compare-and-create: occupied-tag checks/readback protect the stated canonical-owner scope, not arbitrary hostile external writers; no lock framework or absolute external-writer guarantee is claimed. C561 and legacy ProjectMCP temp-root plumbing C562 remain separate deferred Problems.

### Approved cleanup completed; historical naming and continuation reviewed

P2518/P2522/P2519/P2520/P2523 are Done; P2521 is Active for final acceptance/continuation review. All18exact version-unknown images and separately approved6stopped test containers were removed non-force, no volumes/prune; production e81250f8ed4c remains same08f26a9b8b14image healthy. All11verified historical/current images now carry caprmedio-runtime tags with source-proven version and actualDockerCreatedUTC; the isolated new650023dd711fbuild is likewise named. Final109testgate/realbuild/reuse receipts are in current Tasks. A tiny696-byte schema1 scratchimage27b9017daa69 without Created was additionally observed during final inventory; verify its origin separately, do not invent a build date or infer deletion authority. Two read-only Luna lanes now review pending recursive-container source composition and functional acceptance before implementation. C561/C562 remain deferred. No release/deployment, production mutation test, held replay or Stage2 scope work.

### Recursive-container continuation: acceptance before speculative code changes

Two independent Luna reviews find production coordinator, per-member admission and MCP/provider wiring present. Pure34checks pass; native Archive/Done tests exist, but refreshed native run exceeded90seconds in currentness scanning and was interrupted, not accepted. P2499/P2501/P2503 stay pending acceptance; do not infer completion from old plan claims. P2502/P2506 updated before continuation. New bounded Tasks P2524 (native fixture readiness diagnosis, fixture-only correction if concrete) and P2525 (native per-member lineage/partial-stop assertions) are Active with disjoint file ownership; final native execution waits for readiness and independent review. Existing C551/native composition concerns remain open; no source guard/timeout waiver, live Atom fallback, new release, production mutation test or held replay.

### Image-naming priority closed with exact final readback

The Operator separately authorized removal of unreferenced696-byteimage27b9017daa69; fresh exact metadata/reference checks, non-force removal and absence readback passed. Final12CAPRMEDIOimages allnamed with version/build-date/sha12, zero unnamed. Original production e812/08f runninghealthy unchanged; no runtime adoption/release. C560Resolved@2 and P2521Done@4 complete the naming priority, source/tests/contracts, actual maintenance/provenance and next-queue review. Earlier18unknownimage/6stoppedcontainercleanup boundary is distinct from this1additionalartifact. Main implementation/provenance saved locally ecffab7b9; no push. P2524/P2525 continue accepted scoped native verification; C561/C562 remain deferred, other container acceptance Tasks stay pending. Deleted container logs/writable state and removed images have no backup/undo.

### Native fixture readiness accepted without changing runtime guards

P2524Done@3: concrete E467defaulttemp correction,2pathchecks and nativeauth-tamper1check pass5.558s (wall6.69), independentfixtureAPPROVE. Historicalrelease logs show original5nativechecks passed49.324/54.998s; the prior90secondinterruption is not evidence of an infinitehang. No currentness/budget/productioncode change. P2525 updated before nativeexecution: readiness review caught failed-member Journal expectation error before running; testowner fixes event mapping and assertion cohesion, then executes current7nativechecks. Full P2495matrix remains unaccepted; no release/deployment. Naming completion and12taggedimages remain unaffected.

### Native lineage and partial-stop increment accepted; remaining matrix explicit

P2524/P2525/P2506 are Done after independent final review. Current native7/7 pass67.783s; root finalpartial1/1 pass10.710s; adjacentpure/path36/36 pass0.071s. Functionalfile634eed485a1cbeba0967d16cffea8372309e203e757666201c55f8eb0020dd27; fixture3d5be57a57b34ade4e83e7b1712f049e82dc17b71d2d522ce9a2b57f94fa0623. Two earlier test-only failedattempts and correct canonicalhandler seam are retained in P2525, not concealed or countedgreen. No productionlifecycle/sourceguard change; fixturetemp compliance and bounded functionalassertions only. P2495 reviewed/updated before futureactivation and staysBacklog: external-reference, unsupported/collision native refusals, uncertainfrontier no-replay and lateruntouchedmembers remain. P2502/P2499/P2503/P2501/P2494 and relevant Concerns remain pendingfullacceptance; no wholeEpiccompletion. Imagepriorityalreadycomplete12named/0unnamed, originalMCPunchanged; no newrelease/push/deployment/productiontest/heldreplay.

### Automatic image maintenance in Local release — new Operator decision

The Operator requests image naming and cleanup as normal Local release work after the full suite is green, retaining only the last rebuild of the current version, not one image per historical version. P2526/P2528 are Active for contract alignment and independent ordering tests; P2527/P2529 are dependent Backlog. Canonical ImageManager already names the candidate after the suite; do not duplicate that owner or invent a tag timestamp. Image removal remains after verified replacement MCP smoke, preserving the working runtime if replacement fails. Retain the exact admitted candidate digest and preserve all container references without force. Host-wide unused CAPRMEDIO versus selected-Project cleanup scope is awaiting the Operator's answer before deletion semantics change. Existing pending/error disposition remains; no release execution, Docker mutation, broad prune, foreign-container stop or push is authorized. Three bounded read-only lanes mapped flow, contracts and tests; ordering-test preparation can proceed independently.

### Post-green release ordering/proof accepted; retention scope awaits one decision

P2528 is Done: root59/59 focused checks in6.330s, worker overlapping32/40 portfolios, independent review APPROVE. Canonical naming already occurs after a green suite; regressions now bind candidate/installed/launch/cleanup order and failed-suite/preparation stops. Corrected the empty-prior-image gap: no image scan/removal without current_image == candidate_image, with existing pending disposition. No actual release or Docker operation was run. Confirmed desired retention is only the last rebuild of the current version. C563 asks host-wide unused CAPRMEDIO images versus selected-Project images; until answered, P2526/P2527 remain incomplete, new retention semantics and active source-contract changes are held, and P2529 remains Backlog. Current ownership/fingerprint guards are unchanged except the stricter positive-launch proof. This accepted safety/test increment is not a claim that candidate-only retention is implemented. Earlier naming cleanup/native lifecycle results remain independently accepted.

### Project-only retention decision and source alignment accepted

The latest Operator answer selects the second option: only positively identified images owned by this Project, not other Projects or all runtime-labelled images on the host. C563Resolved@2; P2526Done@3 aligns R1878/M332/E573/D564 and O164/O169/O178/O179 before implementation. Retain this successful release's exact current-Version candidate; no second slot for another digest with the same fingerprint. Preserve unknown/foreign ownership and every container reference; image ownership cannot be inferred solely from an old container link. Naming stays after the green full suite, cleanup after verified exact candidate smoke, with no force/prune/replay. No actual release or Docker mutation is authorized here.

P2527 remains Active, split into bounded child Tasks P2530/P2531 for images/stopped containers while the parent owns exact-prior MCP matching and regression integration. P2529 stays dependent Backlog until isolated checks and independent review pass. Earlier accepted naming/native/ordering increments are unchanged.

### Project-only implementation frozen; independent acceptance active

P2530/P2531Done@2 implement inspected complete Project-only image ownership and eligible stopped noncandidate containers, including same-fingerprint rebuilds. Root integrated102/102 functional checks pass16.084s across10modules, including canonical image naming and strict candidate launcher behavior. P2527 owns local_release.py plus identity-helper definitions; P2531 exclusively removed cleanup.py imports/calls first. The separate regression lane covers exact prior same-fingerprint/different-digest replacement. P2529 is Active for independent final review and frozen rerun; P2527 remains Active until acceptance closes integration. No actual release/Docker mutation, deployment, version bump, push or held replay. Inherited release-runner Ruff/size debt is not a clean-global-lint claim.

### Automatic selected-Project image maintenance accepted

P2526/P2527/P2528/P2529 are Done; P2530/P2531 remain Done within P2527's matching Done container hierarchy, with exact predecessors retained for carrier-only relocation. C563 is Resolved. Independent code safety and planning reviews APPROVE; root final frozen10-module synthetic gate102/102 passed9.632s after integration (earlier102/10216.084s separately). Normal Local release now retains only its exact current-Version candidate among eligible selected-Project images, including no fingerprint-only exemption for old rebuilds. Canonical version/date/digest naming remains post-green; image cleanup remains post-verified candidate smoke. Complete owner labels and all container references are enforced; other Projects, unowned resources and uncertainty are preserved/reported, no force/prune/retry.

C564 is Active for exact current source-conformance evidence: inherited runner Ruff scores13/13/59 plus E731 are unchanged versus HEAD; the old703line/C90158 exception is stale, and changed test files225/235lines need applicable bounded evidence or separate cohesive splitting. No clean-global-lint, E539 acceptance, full release, Docker mutation, version bump, deployment, push or held replay is claimed. Earlier recursive-container backlog P2495/P2502/P2499/P2503/P2501/P2494 and C561/C562 remain separate; this closes image-retention implementation, not the whole Epic.

### Requested Local release failed before delivery; diagnosis activated

The Operator requested Local release then Epic continuation. Run local-20261021-retention-110232 reached the full suite, where the selected-subject crash test reported2subcase timeouts at its existing30second child budget. The owned failed attempt was interrupted before delivery; report records failed/tests/KeyboardInterrupt and the test log preserves the preceding errors. Version0.4.4.9 and original e812/08f production MCP remain unchanged/healthy. Four exact-attributed disposable test containers and their attempt-bound test image were cleaned non-force, no volumes/prune; retained host evidence and actual cleanup readback remain separate from release completion. C565Active/P2532Active now own isolated diagnosis; no blind timeout increase, guard bypass or release replay.

Parallel read-only continuation reviews found P2499/P2503/P2501's existing admission and provider wiring present; C551's old mocked-pass description is historical, not proof that code is absent. Current Run/Journal evidence need not be duplicated into new aggregate fields. Native acceptance gaps remain external references, unsupported model, occupied destination, uncertainty/frontier no-replay and later untouched members. Preserve their existing dependency gates and record exact freeze/handoff before future execution. No recursive-matrix implementation or whole-Epic completion is claimed.

### Crash-probe diagnosis accepted; canonical suite scheduling repair active

P2532Done@2: isolated exactcrashtest passes60.255s; clean4copy comparison hit diagnostic90second parent limits under unchanged30second child deadlines, with retained phase/stack evidence; finalserialrecovery passes48.594s and all diagnostic processes exited. Firststressbatch's overlapping root listing is a declared confound, not causalproof. C565@2 remains Active; this is timing-sensitivity evidence, not4completed unittest failures or exact full-suite equivalence.

P2533Active, with disjoint P2534source/P2535tests, will run the existing expensive selected-subject module once before submitting remaining2+2pool work. Preserve all tests/counts/failure continuation/cancellation/launcher behavior and existing30/1800deadlines; no productionguard/cache change or global lock. Root owns README/provenance/integration. A fresh real Local release still requires its full suite after reviewed repair; no release completion or production replacement is claimed.

### Reviewed scheduler repair accepted; fresh requested Local release active

P2533/P2534/P2535 Done after independent APPROVE. Root17scheduler checks pass0.807s and14adjacent checks pass2.588s; pinned Ruff/diff checks pass, no daemon tests in this cohort. Selected-subject module now completes once before remaining2ordinary+2Docker submissions; all coverage/counts/deadlines/cancellation preserved. C564@2 records exact245/272line source/test size debt without waiver; C565 stays Active until the real gate succeeds. P2536Active now owns fresh Local release local-20261021-isolated-gate-114321, with actual full suite before version/image/adoption and Project-only maintenance after verified candidate smoke. Original0.4.4.9 runtime remains installed at this checkpoint; no release completion claimed.

### Latest actual checkpoint

Fresh actual suite passed the isolated25test publication/crash module397.444s with unchanged budgets; C565Resolved@3. Docker integration then failed creating anonymousHTTPtest networks with all predefined address pools fully subnetted; not an Atom validation or MCPproduction failure. ExactownedreleasePID96380 was intentionally interrupted after knownerror; failedreport/testlogretained. P2536 remains Active pending successful freshgate; C566Active/P2537Active now own network diagnosis. No delivery/version/adoption occurred. ChildP2538read-onlyinventory, P2539read-onlycleanupsource, P2540read-onlyregressiondesign are disjoint evidence lanes; root owns all Docker mutation/Git/governedrecords. No worker may delete, test, release, replay or touchproduction. Native matrix continuation remains queued behind repair/release terminal acceptance.

### Actual result and next boundary

P2537/P2538/P2539/P2540 are Done after bounded read-only diagnosis and root-owned approved recovery. Current normal fixture teardown is already scoped and correct; no speculative production rollback or generic network garbage collector was added. Exactly 25 separately approved empty unknown-owner networks were removed with fresh identity/labels/zero-endpoint/all-container-reference checks and absence readback. Failed-attempt two containers/one network/one image were separately cleaned; no volumes or host evidence deleted. Production stays the same healthy e812/08f runtime. C566 remains Active until actual recovery validation; C567 records potential launcher no-container/forced-interruption edge cases for separate reproduction. P2541 Active now owns affected isolated Docker checks, followed by P2536's NEW full Local-release Run. No version bump/deployment or whole-Epic completion claimed.

### Recovery verification

P2541 Done after real isolated Docker3/3 pass94.378s (module96.201s), zero skips. Approved25-network recovery is verified; exact five-network set and original production container/image/network unchanged after tests, unused attempt image removed. C566 Resolved@3; C565 already Resolved from actual25-test crash-module pass; C567 Active separately records unproven interruption/launcher startup edges. No speculative source cleanup changes were made. P2536 now activates fresh complete Local Run local-20261021-network-recovered-120901 after source freeze and commit; full suite still required, no release completion yet. Native container-lifecycle acceptance resumes after terminal release verification.

### Remaining-suite failure collection before bounded fixture correction

Fresh full suite now records one real failure in test_image_override: the runtime fallback assertion references runtime.IMAGE, but runtime imports only IMMUTABLE_IMAGE/image_reference from the canonical image_reference module. Repo caller search finds this is the only runtime.IMAGE reference; canonical IMAGE remains caprmedio-runtime:local. C568Active/P2542Active own a bounded test-owner correction after the current source-frozen suite terminates. No production compatibility export or fallback behavior change is requested. Continue this already-failed suite to collect all remaining failures before one fresh repair/release attempt. No delivery/runtime replacement can proceed from this failed gate; original production remains unchanged.

### Selected-workflow module deadline reached after observable progress

Current Run collected a second blocker: selected_workflows_docker_e2e hit its unchanged1800second module deadline. Retained partial output shows several preceding cases completed and the later W01 role/status matrix was executing at timeout; this is not proof of an initial startup hang or semantic failure. C569/P2543 now own read-only case/fixture work mapping before any proposed cohesive test partition; no deadline increase, source guard bypass, reduced matrix or test skip. Keep source frozen while the current failed suite finishes collecting results. C568's stale fallback-test repair remains separately bounded.

### Reviewed diagnosis and dependent work

P2543 Done after read-only partition review. New P2544/P2545 are dependent Backlog until the running failed suite reaches terminal state. Minimal planned test-only move: existing29-status W01 matrix gets one own _docker_e2e module with composed current harness; old11+new1 equals previous12 tests. No reduced matrix, inherited test duplication, runner/API/production change or deadline extension. Root owns C568's two-line canonical-constant test repair; Luna source owner exclusively owns old/new W01Docker files, verification owner owns disposable proof only. Full next release times both modules and remains the runtime acceptance gate; focused discovery is not a green-release claim.

### Latest Operator decision

The Operator explicitly authorizes either removing the module limit or setting60minutes, and requests faster parallel execution with shared-image containers. Choose finite3600seconds per module, not unlimited; retain30second isolated crash-probe and1980second launcher budgets. Live resource readback: host8CPUs/16GiB; Docker4vCPUs/3052277760bytes (~2.84GiB), current testworker119.2MiB/testagent60.36MiB, productionMCP202.7MiB; these are samples, not peak guarantees. Raise ordinary host module capacity2to4, keep Docker capacity2 to avoid expanding the constrained VM pool without peak evidence. Existing same immutable image is already shared across disposable containers; separate W01matrix enables independent scheduling. Current Run still uses old source/deadlines and remains failed; new settings apply only after terminal, reviewed repair and a NEW full gate. No Docker daemon configuration or production parallelism change.

### Execution handoff after terminal failed gate

Run local-20261021-network-recovered-120901 terminated naturally failed/tests/LocalReleaseError/exit1 after427modules,3806countedtests,0skips,2failedmodules: stale runtime.IMAGE test and selected Docker aggregate1800s timeout. Launcher all-groups integration passed. Complete log/report retained; no version/delivery/adoption. Source freeze is now lifted for disjoint P2544 W01testpartition, P2545 disposable discovery proof, P2546 root runner profile and P2547 scheduler tests. Root also owns tiny P2542 fallback-test correction, README, all Docker/Git/planning and next actualrelease. Latest Operator profile3600seconds/module,4host+2Docker with isolated crash module supersedes old future1800/2+2 contracts. Actual next gate, not static checks, proves new timing. Separate attempt cleanup remains ownership-checked; no broad prune.

### Latest focused-only validation instruction

Latest Operator instruction: after these fixes, DO NOT rerun the full suite; run only broken and related checks. This supersedes all earlier next-full-gate clauses in this current Task/Epic. Focused acceptance includes stale image-reference tests/related image selection, scheduler regression portfolio and the original11-test plus new1-test W01Docker modules (all29statuses). Use3600second module budget,4host+2Docker capacity, isolated crash-probe scheduling; no unrelated test rerun or production mutation test. Report focused results accurately; do not call the current HEAD full-suite green or invoke the normal Local-release command that automatically reruns it.

### Focused source acceptance and next boundary

Source repairs accepted after independent review and41fast related checks:14image0.280s,17scheduler0.598s,10image/context0.160s. W01partition discovery11+1=12,status29 and17assertions preserved; opt-in/no-context guard proved skip with0Docker calls. Final matrix165lines withbounded newhelpers. Root profile3600seconds,4host+2Docker and isolated crash module; no production behavior change. P2548Active now owns actual two-module focused Docker proof with one shared image; source frozen until terminal. DO NOT rerun all427modules or invoke normal Local-release CLI; do not claim full green HEAD/deployment. C568Resolved; C569 pending actualmatrix success; C564/C567 remain separate.

### Actual focused verification completed

P2542–P2548 are Done for the bounded test/profile repair and verification increment. Final independent source review APPROVE; 41 fast related checks plus 12 opted-in Docker tests pass, zero skips, with all 29 W01 status cases retained. Matrix 269.220 seconds and original portfolio 629.254 seconds ran concurrently on one image; this is not a full-suite speedup benchmark. Same two pre-existing containers/five networks and healthy original production are restored exactly; unused test image is absent. C568/C569 are Resolved. C564 source-conformance debt and C567 interruption/startup lifetime follow-up remain Active. No post-fix full rerun or deployment was performed. P2536 stays Active pending C570's explicit release-path choice because the normal CLI automatically runs the prohibited full suite. Native container failure-matrix queue P2495/P2502/P2499/P2503/P2501/P2494 remains separate and unclosed; no whole-Epic completion is claimed.

### Focused Local-release continuation is answered; release/adoption remains pending

C570Resolved@3 records the Operator-approved one-run focused Local-release continuation through the existing host PROJECT_TOOLS/release.py local entrypoint with repeatable --test-module arguments; the complete discovered suite remains the default. P2549 is Done at 89-CA-P-2536-TASK--run-fresh-local-release-after-isolated-suite-repair/done/09-CA-P-2549-TASK--admit-and-prove-focused-local-release-validation.md after the canonical admission proof of exactly 16 selected host modules, 131 tests, zero skips and zero failures; the exact module list is retained in .caprmedio_tmp/local-focused-admission-20261021.log. The prior 53-test Docker/related proof is reused from .caprmedio_tmp/focused-release-repair-20261021/focused-summary.json after exact Engine/runtime/pyproject/uv.lock/version no-diff verification; the expensive 12 Docker tests are not rerun. P2550 is Active at 89-CA-P-2536-TASK--run-fresh-local-release-after-isolated-suite-repair/10-CA-P-2550-TASK--execute-focused-local-release-and-adopt-candidate.md for fresh Run local-20261021-focused-adoption-01 with the same 16 module arguments, actual Local release/adoption and installed MCP smoke. O164@20/O165@9/O169@11 now reconcile the complete-suite default with the explicitly recorded focused local path; CA-O-188 public release remains full-gate. C564 remains Active/unresolved. No version bump, installed replacement, release success or whole-Epic completion is claimed in this planning increment.

### Focused Local adoption observed; cleanup and policy queues remain

Root observed Run `local-20261021-focused-adoption-01` complete with
`completed_with_cleanup_pending`, CLI1, no failed step, exactly 16 selected
host modules, 131 tests, zero skips and zero failures. Version `0.4.4.10` is
installed from candidate tag
`caprmedio-runtime:0.4.4.10-20261021T131557Z-0555ed0be341`; container
`649228a677661439d12d9771d606652525480ab4a2f5ef2131036b451a1cae7e` is
healthy, `/health` is ready, and connected `discover_operations` reports
O164 v20. The launcher matches fingerprint `80fc2b4` and the current Project.
Receipt: `.caprmedio_runtime/simple_local_release/reports/local-20261021-focused-adoption-01.md`.

The old Project container and owned images were removed, while unknown,
incomplete, foreign or otherwise unproven resources were retained; cleanup is
therefore pending, not silently complete. The selected-workflow cleanup Run was
officially cancelled after ENQUEUED observation with no child cascade or observed
effect. P2550 is Done, P2536 remains Active, P2551 is Backlog and C571 is Active
for the remaining ownership evidence.

The current Epic queue records P2552 Active (AtomSearch warning/Journal boundary),
P2553 Done (implementation), P2554 Done (focused proof), P2555 Done (Docker
technical-log source/configuration increment), P2556 Backlog (selected-workflow
dispatch diagnosis), C572 Active and not deployed, and C573 Active. C564 remains
unresolved source-conformance debt. C570 is already Resolved for the focused
path choice. CA-O-188's public release remains a separate full-gate requirement;
this observed focused adoption does not close Stage 2 Scope Unit work or the
whole Epic.

### Shared failure handling — current implementation queue

CA-M-396 through CA-M-400 are Active: all failures remain observable; only real
runtime failures may block runtime/service operation or emit technical ERROR.
Invalid input and Project artifacts emit WARNING diagnostics plus explicit errors
in the public response, without disabling a healthy service. Preserve verified
partial results before error details. Technical stdout/stderr is separate from
actual business Workflow started/failed/completed Journal events.

CA-P-2557 owns the bounded shared error-boundary implementation, with child Tasks
CA-P-2558 (shared classifier/decorator), CA-P-2559 (canonical Tool/MCP callers),
CA-P-2560 (partial AtomSearch responses), and CA-P-2561 (functional acceptance and
independent review). Each child has at most 15 minutes own work; revise dependants
after its predecessor completes. Reuse the existing logger and caller-owned
result schemas, preserve sync/async cancellation and effect safety, and add no
automatic retry, repair, rollback, fabricated Workflow or hidden Journal writes.
CA-P-2557@2 and children CA-P-2558@5, CA-P-2559@3, CA-P-2560@3 and
CA-P-2561@2 are Done for this bounded source increment. Shared sync/async handling
now reaches registered Tools, selected MCP callers, workflow_orchestrator, Atom
CLI and AtomSearch. Partial lookup data is retained with explicit schema_invalid
errors and complete:false; request failures produce technical WARNING, and only
explicitly classified blocking runtime failures produce ERROR. Cancellation and
caller-owned result schemas remain intact. The decorator adds no retries or
technical Journal records.

Focused evidence covers 117 unique passing cases across ten modules. The initial
64-case Tools run found one stale empty-error test assertion; the corrected
provider module passed 10 cases while prior passing results were retained. The
53-case MCP group passed. After the final review fix to omit invented exception
classes on synthetic warnings, 32 related cases passed again in 1.823 seconds.
Repeated runs are not additional unique coverage. Independent final review
APPROVED; exact commands and evidence are retained in CA-P-2561. Core/logger Ruff
and changed-file F checks pass. Existing non-failing fixture ResourceWarnings and
tracked source-conformance debt are not broader acceptance.

No full suite, new image, release, deployment, production endpoint test or push
occurred. New source is not active in the installed MCP yet. P2552/C572 readiness,
P2556/C573 dispatch, ownership cleanup and the native container failure matrix
remain open, as does the Epic. Scope Unit operations stay in Stage 2.

### Docker-image-wide error handling — Operator scope correction

The Operator clarified that shared failure handling covers everything first-party
shipped for execution in the Docker image: all Tools, all Workflow executors,
service/process entrypoints, MCP, agent requests and supporting Apps. It is not
limited to AtomSearch, current registered MCP calls or the running container.
CA-M-400@2 makes this coverage explicit while retaining M396–399 classification,
partial-result, business-Journal and cancellation boundaries. The preceding
P2557 acceptance remains bounded to its recorded surfaces; it is not image-wide
acceptance.

CA-P-2562 owns the extension, with inventory P2563, Tool boundary P2564, Workflow
boundary P2565, service/App boundary P2566 and dependent focused acceptance P2567.
Derive coverage from the Dockerfile, executable modes and actual dispatch owners;
reuse existing packaging inventories rather than adding a runtime registry.
Preserve explicit mutation-target refusals and atomicity; invalid unrelated input
must not disable healthy independent work. Actual business Workflow lifecycle
recording remains with its executor, not the generic decorator. Third-party
library internals are not rewritten. Each leaf has at most 15 minutes own work;
split before expanding it. Independent read-only lanes are running; implementation
waits for their bounded findings and exclusive scopes.

Use only broken/related isolated functional checks. This increment authorizes no
production test/restart, deployment, full-suite rerun or historical batch replay.
An image/source coverage check is not proof of image build or production adoption.
Known C573 selected-workflow dispatch remains unresolved; under the Operator's
standing fallback these source/planning updates are manual with exact predecessors.

### One host MCP for all Projects — accepted Operator direction

The Operator selected one shared MCP for all Projects. Mount My_Repos through
CAPRMEDIO host/container configuration outside every Project, not through a
Project's settings. The client path is Codex session -> project-local ca Skill ->
request carrying the explicit Project root -> shared MCP. Validate each supplied
root against the configured host mount and its own Project declarations; derive
the prefix from the selected Project rather than a caller-provided label. Keep
request contexts independent during concurrent work; no process-global selected
Project and no silent fallback. Project settings still own that Project's model,
tools, methodology and delivery locations; host settings own the shared mount and
service configuration. This decision does not itself deploy or replace production.

CA-P-2576 owns this increment with children P2569–P2575: reconcile the prior
implementation, align source contracts, implement host settings/launch material,
implement request routing, update the thin ca client, verify two-Project routing,
and independently review/handoff. Existing image-error Task P2562 remains Active
until its real normal-import checks and review pass. A mechanical __main__ wiring
error introduced empty callbacks across fifty changed Python files; C574 records
our introduced damage, not an unrelated pre-existing defect. P2569 repairs only
those tails while preserving the other workers' domain edits, then reruns affected
checks without import stubs. No full suite, uncertain mutation replay or production
replacement is included in this source increment.

The new host Task was initially assigned CA-P-2568 concurrently with the
Methodology chat's earlier Project-level relation-migration Epic. Preserve that
Epic unchanged and assign only this new host Task CA-P-2576. Exact original
planning bytes and child-relation predecessors are retained; C575 records the
resolved collision. The two chats have been explicitly informed of write/identity
ownership. No uncommitted work from the other chat is included in this increment.

## Source checkpoint — 2026-10-21T20:45:37Z

Shared-host source packet now includes Active R2008@1, M401@1, E641@2 and D640@1, with conflicting legacy MCP instance-binding wording reconciled and exact predecessors retained. P2576 owns source implementation and the remaining adoption handoff. Actual host settings are external to all Projects; the container was not built, started or replaced. Root verified the new full 23-Method projection against current bytes and used its refreshed guidance in the implementation review. Final root source portfolios passed 50 shared-runtime and 59 image/error-boundary checks; real native child MCPs were used behind one isolated ASGI endpoint.

The newly proposed Project-prefix selector, Codex hook and universal harness are being compared before any further contract change. No alias registry or hook activation is implied. Continue with the source/provenance handoff and candidate-image/client adoption gates; retain C572/P2552 and C573/P2556 independently. The Methodology chat's unrelated Project Epic CA-P-2568 remains untouched.


### Shared-context native implementation — 22 October 2026

The Operator approved implementing the current O016@17 shared-context graph and validating it through isolated functional/native MCP tests, without release, deployment or production MCP replacement. CA-P-2577 owns this increment, with leaf Tasks CA-P-2578–CA-P-2584 for source/test preparation, strict current input validation, Action/review dispatch, continuation/retry integration, binding/fixture reconciliation, isolated functional acceptance and independent review. Each leaf is one file and at most 15 minutes own work; split before extending and review/update dependants after each observed result.

Use the refreshed 39-Method and 62-Evaluation source frontier, full Method contents and source hashes; do not treat declared-reference coverage as conformance. Reconcile stale current implementation bindings (including CA-R-1843) without rewriting the old frozen oracle from live Atoms. All eight current Steps are explicitly Integrated; select the adapter using trusted Workflow/definition/entry binding because three Step IDs overlap the legacy graph. Retain substantive R/M/D-to-E coverage, preliminary review before final tests, final same-candidate review, affected-evidence invalidation, one existing retry count and truthful separate release continuation. Standalone O223 remains a separate read-only Workflow, not a new MCP route.

Current discovery did not advertise create_atom. Under the Operator's standing fallback, these planning records are saved manually with the exact Epic predecessor preserved; no MCP Run, runtime activation, test success or release is fabricated. Runtime implementation and acceptance are pending. Source-size exceptions, if needed for bounded legacy integration, require explicit acceptance; new runtime logic must remain cohesive and small.

The Operator subsequently refused the proposed integration-only source-size exception and selected refactoring the oversized legacy files first. P2585/P2586–P2590 own SelectedExecution decomposition; P2591/P2592/P2593 own route/request/manifest decomposition; P2594 owns Agent transport decomposition. P2595 verifies preserved behavior and source boundaries before native feature Tasks resume. Keep public interfaces and the existing frozen oracle stable; preserve unrelated dirty work. No size/complexity exception, release, deployment or production testing was accepted.

CA-P-2578 preparation and CA-P-2594 Agent transport refactoring are now Done with actual focused checks and independent review; the refactor-first gate remains open. Source readback additionally confirmed that current R1527@7 requires an actual current-session Integrated prompt/result continuation, not a separate ephemeral CLI supplied with prior results. No public continuation seam exists in current native dispatch. CA-C-576 records that implementation gap; CA-P-2581 is decomposed into seven <=15-minute children CA-P-2596–CA-P-2602 for durable pending state, prompt return, submitted-result validation, no-replay resumption, public MCP continuation, isolated functional proof and independent review. Keep these Backlog until predecessor acceptance. Ordinary technical envelope details remain implementation choices within existing source authority; no release or deployment is admitted.

### Refactor-first reviewed checkpoint — 22 October 2026

CA-P-2591 and its children CA-P-2592/CA-P-2593 are Done: selected route/request/manifest responsibilities are bounded and independently reviewed. CA-P-2586 source/admission extraction and CA-P-2589 graph-loop extraction are also Done. CA-C-577 is Resolved for the latter's recovery, diagnostic, typed retention, cohesion and terminal-write findings; durable focused parity tests and independent review close those findings, not the complete executor gate.

The current bounded 76-file extraction/test target set passes strict Mypy, real pinned Ruff format/lint/C901 and the <=200 physical-line / <=40 cohesive executable-statement check. Every one of the 39 Method projection source hashes was rechecked against current authority bytes. This checkpoint excludes the still-oversized public executor and unfinished production caller/test-seam integration; CA-P-2590 and CA-P-2595 remain unaccepted. The unchanged legacy Action-observation source is outside this changed-source refactor, not an accepted size exception.

Final executor integration must preserve canonical lifecycle outputs and changed-effect filtering, the shared tracker's Subject-batch route, frozen manifest-reader test isolation and graph reconciliation's zero-write/readback boundary. Keep frozen source data and behavioral assertions intact while moving incidental test seams to canonical owners. Current native shared-context feature Tasks remain Backlog until the refactor gate passes. No full suite, release, deployment, production MCP traffic or Git publication occurred.

### Refactor-first gate accepted — 22 October 2026

CA-P-2585 and all five decomposition children are Done, as are the independently reviewed selected-route and Agent refactors. CA-P-2595 accepts the complete refactor-first gate. The executor/route/Agent entry files are 197/126/135 formatted physical lines rather than 2,856/1,081/425. All 83 admitted bounded files pass strict Mypy and pinned Ruff format/lint/C901, remain <=200 physical lines and have <=40 logical lines per executable unit (maximum 38); cohesive 26–40 units received separate review. No source-size or complexity exception was used.

The full preserved executor baseline passed 23/23, Subject-batch execution 7/7, graph completion 12/12, lifecycle composition 7/7, container composition 5/5, MCP routes 21/21, the retained MCP error-consumer regression 1/1 and isolated queue repair 5/5. Dedicated graph recovery/revisit/diagnostic/write-order and zero-write reconciliation checks also pass. These portfolio counts are individual evidence, not an invented disjoint aggregate. Source and test-seam reviews returned PASS; frozen golden data, source/digest, replay, effect and terminal assertions were preserved.

CA-C-577, CA-C-578 and CA-C-579 are Resolved after repairing graph extraction parity and public error/Run-ID compatibility. RUN_ID has one canonical definition. Unchanged oversized container source and unchanged legacy test complexity remain outside this increment; the MCP confirmation carrier received only its canonical import migration and was not silently admitted to strict formatting/typing. Exact Plan/Concern predecessors and the completed Plan container hierarchy are retained.

CA-P-2577 remains Active. CA-P-2579 is reviewed as the next ready Backlog Task after preparation and refactor acceptance; current packet validation, shared-context Action dispatch, actual current-session Integrated continuation, native bindings and isolated current-graph acceptance are not yet implemented. CA-C-576 remains Active. The legacy CLI/Isolated path is not misrepresented as Integrated. No full suite, image build, runtime admission, commit, release, deployment or production service replacement occurred.

### Operator priority — shared-context MCP implementation first

The Operator now prioritizes CA-P-2577 before new Subjects-aware/task-specific projection implementation. Complete the actual interactive Integrated loop: MCP returns verified Tool outputs and the admitted current Action prompt, inputs and result contract to the participating session; that session performs or explicitly delegates the work; a later result submission is validated and recorded before the executor chooses the next Step. Returning instructions leaves the Step pending. Never silently invoke a separate CLI Agent as an Integrated fallback; preserve explicitly Isolated execution independently.

CA-P-2579 is Active after its completed preparation/refactor dependencies. Then review CA-P-2580 and CA-P-2581, whose children CA-P-2596–CA-P-2602 own durable pending state, prompt return, result validation, no-replay resume, the public MCP surface, isolated functional proof and review. Reuse existing packet, Project, Run, Step/Action, source, candidate, permission and retry fields. Keep actual Tool results and partial failures visible, reject stale/conflicting/cross-Project submissions before effects, and preserve completed effects on resume. Review each dependent Task before execution; every leaf remains bounded to 15 minutes own work and is split when necessary.

Fresh read-only MCP inspection resolves O016@17 but reports unresolved availability, null execution schemas and invalid selected-route binding evidence. ATOM_UPDATE advertises Subject preparation only, not this full Plan edit. These planning revisions use the Operator's standing manual fallback with byte-exact predecessors; no business Workflow Run or successful MCP effect is invented. Implementation acceptance uses frozen functional/native MCP worlds on isolated endpoints, never the production port. No full suite, commit, image build, release, deployment or production replacement is included.

Projection naming was checked against Active CA-D-635@5 and CA-R-1943@5: `<PROJECT_PREFIX>-PROJ-<ID>-<CURRENT_SCOPE_NAME>--<PROJECTION_TYPE>--<NAMED_SELECTION>.md`. The Operator explicitly accepts using named selections for task-specific projections: include the persistent Task ID in the named selection rather than adding a new filename field. The same Type, named selection and source of truth retain their Projection ID across rebuilds; a different task-bound selection receives a different Projection identity. This decision does not allocate IDs, rebuild views, infer evaluation coverage from Subjects or replace source/tier/lifecycle checks. Defer task-specific projection implementation until the shared-context increment is accepted.

### Shared-context validator accepted — 22 October 2026

CA-P-2579 is Done after independent review and 15 focused frozen-fixture checks, pinned Ruff format/lint/C901 and strict Mypy. Its strict packet boundary now checks current source authority and complete externally trusted Method membership while preserving no-Plan intake, read-only review, valid exhausted-retry outcomes and field presence. Exact predecessor carriers are retained. CA-P-2580 has been reviewed against this actual API and remains the next ready Backlog leaf.

CA-P-2577 and CA-C-576 remain Active: the Integrated prompt/result loop, durable continuation, public MCP submission/status and isolated current-graph acceptance are not yet implemented or admitted. Prepared Action/frontier contracts are deliberately outside ordinary test discovery until their production modules exist; no missing-module import is presented as a test failure or success. No full suite, commit, image build, release, deployment or production replacement occurred. Task-specific projections still use the accepted named-selection segment; their implementation stays behind the shared-context priority.

### Interactive implementation increment and Method selection — 22 October 2026

The Operator asks to implement the Integrated MCP loop. CA-P-2580 is Done after independent Action-surface PASS and 14 root-run focused tests. CA-P-2603 is Done after independent store review and 14 root-run frontier checks. CA-P-2596 is split into a zero-own-work container with separate <=15-minute checkpoint/save and restore/no-replay leaves CA-P-2604/2605; existing graph/transport prerequisites remain actual acceptance gates. The canonical evidence writer now stages through Project Temporary State, and the store/checkpoint share one bounded no-follow byte-reader owner. None of these bounded checks proves a complete real-session Workflow or release admission.

The Operator resolves the Method-universe question with manually authored named selections. For an implementation target PROGRAMMATIC/TOOLS/TOOL1, the declared selection includes applicable PROGRAMMATIC policies, applicable TOOLS policies, all TOOL1 Methods, and applicable abstract Project-parent Methods. Do not limit the product to this repository's current 39-Method root bundle or authenticate completeness from the request packet's own subset. MCP independently resolves current admitted sources and compiles/validates the explicitly selected inventory. Existing scope ancestry and Method parent/child relations may assist selection/review; the Operator's suggestion does not introduce automatic transitive inheritance, a new relation type, a tier-equals-policy shortcut or new authority for Subjects/Projections. Check the existing source rules before choosing the named-selection definition carrier or a new inheritance mechanism.

Current Step prompts/results, durable canonical Run checkpointing, strict bound submissions, no provider replay, unchanged finite retries, public MCP status/submit exposure and isolated frozen-fixture journey remain distinct responsibilities. No production traffic, full-suite rerun, commit, build, release or deployment is authorized or claimed in this increment. Preserve the explicitly Isolated legacy adapter and keep task-specific Projections in the accepted named-selection naming segment.

### Parent-chain Method compilation decision — 22 October 2026

The Operator confirms that a selected Method such as M3 must fetch its applicable active parent chain M2 and M1, then compile that chain into one paragraph without duplicating meaning. This supersedes the earlier manual-only inclusion discussion: the named selection may name target anchors; its compiled context must retain the explicitly resolved applicable source chain, not just leaf text. Applicable policies outside that chain remain separately selected; do not include unrelated sibling Tools or all physical ancestors by directory alone.

Compilation is a non-authoritative view, not a merge, replacement or rewrite of the source Atoms. State each shared semantic rule once, preserve every distinct constraint, scope, condition, exception and admitted specialization, and expose unresolved conflicts instead of smoothing them into a new rule. Keep exact source IDs, revisions, paths and hashes with the compiled paragraph so its membership/currentness and any evidence invalidation remain independently verifiable. Retain complete source authority for server validation; the paragraph does not authenticate its own source completeness. This records the accepted behavior, not a new named-selection storage schema or an implemented semantic compiler.

CA-P-2596 persistence is now Done with independently reviewed store/checkpoint surfaces and root focused verification; CA-P-2597 graph dispatch is Active against those accepted APIs. The public Integrated loop, named-selection compiler, current route admission and production runtime remain unfinished. Read-only MCP Tool discovery returned ATOM_UPDATE, but its exact Action context returned uncertain/Implementation call failed; no mutation or automatic replay was attempted. The standing manual fallback is used for these planning records. Preserve the Methodology chat's separately approved Subjects-only source edits and refresh affected source-bound Projections after its completed batch. No full suite, commit, build, release or deployment occurred.

### Current source-trace and interactive continuation checkpoint — 22 October 2026

CA-R-2117, CA-M-431 and CA-E-653 are now the direct active RMED authorities for implementation traceability. The implementation workflow may use one readable module/unit block with distinct citations for independent branches; optional projections remain views and never become authority. The source boundary excludes vendor, generated, frozen-fixture and legacy-history carriers unless explicitly admitted.

The continuation order is source-first Project Configuration for O016, then native MCP interactive continuation. The participating session receives the admitted prompt, inputs and expected result, submits the validated result through MCP, and remains in control of the next step or explicit delegation. A hidden CLI callback is not an Integrated substitute. Docker-free isolated MCP tests are preparation evidence only; the complete real-Manifest journey and runtime admission remain separate.

CA-P-2597 is Done only for bounded initial dispatch after seven focused reruns and an independent PASS. CA-P-2606 owns the source update, CA-P-2607 records the three completed RME source atoms, CA-P-2608 remains queued for direct-method runtime compatibility, and CA-P-2609 is Active for naked-harness verification. Existing CA-P-2598 through CA-P-2602 remain the continuation, public-route, journey and review queue; no duplicate decomposition is introduced.

### Final bounded implementation checkpoint — 22 October 2026

The shared-context native implementation lane has bounded acceptance evidence: CA-P-2581, CA-P-2598, CA-P-2599, CA-P-2600, CA-P-2601, CA-P-2602, CA-P-2608, CA-P-2609 and CA-P-2610 are Done; CA-C-581 is Resolved. Root recorded the real-SDK interactive MCP journey 4/4 in 31.770s against the current 41-Method fixture (pending 231→232→231, public status/privacy, next-call token, exact duplicate, conflict refusal, terminal blocked status, source drift, oversize and tamper), 52/52 integrated checks including 20 frontier response/concurrency/recovery checks, 28 validator checks, 4 packet checks, 8 route checks, 2 status checks, 30 legacy-orchestrator checks, independent guard/APP regressions, and the final Docker-free naked-stdio smoke with 23 valid tools and the exact preview path. These are bounded implementation and isolated-journey records, not full-suite, release, deployment or production-admission evidence.

The installed source-bound binding remains O016@13 with CA-O-091 and the old Core Meta Model source path. CA-C-576 therefore remains Active. CA-P-2582 is now the next Active candidate binding/fixture reconciliation task; CA-P-2583 owns current-Workflow isolated verification and CA-P-2584 owns independent review/handoff. Current Project binding, runtime admission and handoff remain separate gates. Keep CA-P-2401 Active; no live binding mutation, full-suite rerun, release or deployment is claimed by this checkpoint.

### Terminal-status correction checkpoint — 22 October 2026

The prior bounded implementation evidence remains retained, but final public continuation closure is withdrawn pending a current status/recovery repair. CA-P-2581 and CA-P-2601 are Active again; CA-C-582 records the observed defect where an accepted terminal/interrupted_pending result and interrupted_pending graph result are exposed as blocked until explicit recovery; CA-P-2611 owns the bounded read-only verification without replay. CA-P-2582 is postponed to Backlog until that gate is resolved. CA-C-576 remains Active, and the installed O016@13 / CA-O-091 binding, current Project binding, runtime admission, handoff, full-suite validation, release and deployment remain separate. No final public-loop or production-admission claim is made.

### Accepted terminal-status correction — 22 October 2026

The read-only interrupted-status defect is resolved: CA-C-582 is Resolved, CA-P-2611 is Done, CA-P-2601 and CA-P-2581 are Done, and CA-P-2582 is reactivated with CA-P-2612 first and CA-P-2613 deferred. Root evidence is bounded to the focused current-workflow portfolio: 64/64 checks, six observation guards, seven checkpoint checks, strict SDK 4/4 in 30.110s, final naked stdio with 23 tools, and Ruff/mypy green. The installed O016@13/CA-O-091 binding, current Project binding, runtime admission, handoff, full-suite validation, release and deployment remain separate. Production is unchanged.

### Source-contract checkpoint — 23 October 2026

CA-P-2612 is Done with accepted exact pins CA-R-1847@16, CA-R-1848@9, CA-D-547@12, CA-E-567@7 and CA-E-568@8, plus focused parser/body and independent-review checks. CA-P-2582 remains Active; CA-P-2613 remains Backlog pending the Operator's choice between all 15 non-target route pins plus both query admissions and the focused hold. CA-C-576 remains Active because the raw Project manifest still fails the retired O091 unique-current check. No candidate emission, A1142 edit, live projection mutation, current binding admission, runtime admission, full-suite validation, release or deployment is claimed.

### Full binding-review checkpoint — 23 October 2026

The Operator authorized review of all 15 non-target route pins plus both query admissions before publication. CA-P-2613 is Active as a zero-own-work review container with six Active read-only leaves CA-P-2614–CA-P-2619; CA-P-2582 and CA-P-2577 remain Active. CA-P-2612's five-source contract is accepted. CA-C-576 remains Active because the raw Project manifest fails the retired O091 unique-current check. No candidate emission, A1142 edit, live binding/projection mutation, runtime admission, Scope Unit implementation, full-suite validation, release or deployment is claimed.

### Semantic binding-review checkpoint — 23 October 2026

The authorized all-route review is complete. CA-P-2614 through CA-P-2619 are
Done as review-complete Tasks, with 8 PASS findings and 7 binding-closure HOLD
findings. The review created exactly two Active Problems: CA-C-583 for
Journal receipt/completion semantics against R1525@11, R1720@22 and D340@17,
and CA-C-584 for the exact 15-operation MCP contract versus optional
move_atom. CA-P-2613 remains Active; its conditional candidate-only leaves
CA-P-2620 and CA-P-2621 are Backlog. No candidate, A1142, live binding,
projection, runtime, Scope Unit, release or deployment change is claimed.

### Repair planning checkpoint — 23 October 2026

The semantic review now has a bounded repair queue under CA-P-2613. CA-P-2622
is Active for the read-only CA-C-583 source-reconciliation proposal;
CA-P-2623 is Active for compiler/refactor boundary preparation; CA-P-2624 is
Backlog for the separate focused regression plan because the combined repair
may exceed one 15-minute Task. CA-P-2625 is Active for the fresh public
MCP/Project frontier inventory, and CA-P-2626 is Active for the read-only
CA-C-584 reconciliation proposal. CA-P-2620 and CA-P-2621 remain Backlog and
blocked on actual CA-C-583/CA-C-584 disposition. These are planning and
read-only review records only: no source Atom, code, manifest, binding,
projection, runtime, release or deployment change is claimed.

### Current O016@20 compatibility checkpoint — 23 October 2026

The fresh inventory reports current O016@20 with body bytes unchanged from the
exact O016@18 archive. The Epic therefore adds two bounded lanes under
CA-P-2613: CA-P-2627 is Active for candidate-only current-20
compatibility/admission preparation, and CA-P-2628 is Active for focused
isolated current-20 tests. They preserve exact legacy-17/direct-18 support and
do not broaden the frontier to every version greater than 18. The public
15-operation route and live 16-operation Project manifest remain unchanged;
no binding, runtime, publication, release or deployment admission is claimed.

### R1317 Journal boundary and compiler follow-up — 23 October 2026

The Operator resolved CA-C-585: Journal recording is non-blocking for
methodology approvals and recovery; actual OperatorDecision and independent
Run/effect evidence remain required. The bounded generic-six source review is
Done in CA-P-2622 with exact current hashes and an independent review at 99%
or higher; it found no generic Journal gate, duplicate or graph-alias issue.

The remaining source/compiler queue is explicit: CA-P-2629 is Active for
R1317/O007/O155/O156 alignment, CA-P-2631 is Active for the seven current
compiler/shared-run RMED contracts R1840/R1841/R1842/E561/E562/D541/D542, and
CA-P-2630 is Backlog pending those reviews plus the open CA-C-586 decision on
whether O011 reuses the interactive MCP loop for the actual OperatorDecision.
CA-C-583 remains Active for this remaining methodology/Engine implementation
gap. No source, code, binding, runtime, publication, release or deployment
mutation is claimed by this checkpoint.
