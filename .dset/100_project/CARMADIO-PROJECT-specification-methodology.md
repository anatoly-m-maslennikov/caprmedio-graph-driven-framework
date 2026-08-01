# Requirement connections and delta — DSET 0.3

Already accepted behavior is not redefined in this Change. The table connects
the implementation scope to its current layer-owned Requirement owners.

| Capability | Current Requirement owners |
|---|---|
| Framework-first self-hosting and bounded recursion | `CARMADIO-REQUIREMENT-OPS-003`, `CARMADIO-REQUIREMENT-TOOL-004` |
| Repository-owned rules, fail-closed ownership, customization, and one owner | `CARMADIO-REQUIREMENT-GOV-014..017` |
| Separate test/eval proof | `CARMADIO-REQUIREMENT-META-007` |
| Thin wrappers, local-rule following, lifecycle-mode entrypoints, runs, budget, continuity, shared runtime, and selectable implementation preparation | `CARMADIO-REQUIREMENT-SKILL-002..009`, `CARMADIO-REQUIREMENT-SKILL-011`, `CARMADIO-REQUIREMENT-SKILL-013` |
| Release transaction, RC/final gate, and coordinated version identity | `CARMADIO-REQUIREMENT-OPS-004..007` |
| Intake routing and stable layer-qualified IDs | `CARMADIO-REQUIREMENT-GOV-018..019` |
| Neutral repository or Work Area scope | `CARMADIO-REQUIREMENT-META-011` |
| Atomic authority, compiled projections, absorption, commit provenance, and session provenance | `CARMADIO-REQUIREMENT-GOV-020..022` |
| Governance constitution, dependency/precedence separation, and authority/assurance boundary | `CARMADIO-REQUIREMENT-GOV-023` |
| Generated project health and portable Markdown rendering | `CARMADIO-REQUIREMENT-GOV-024`, `CARMADIO-REQUIREMENT-TOOL-018` |
| Independent external review packet/report and explicit finding reconciliation | `CARMADIO-REQUIREMENT-GOV-025` |
| One explicit or inherited priority for every governed artifact | `CARMADIO-REQUIREMENT-GOV-026` |
| Workflow-independent Problem, Question, and Conflict semantics | `CARMADIO-REQUIREMENT-GOV-027` |
| Recommended optional rationale for Decisions and other atomic artifacts | `CARMADIO-REQUIREMENT-GOV-028` |
| Independent MECE artifact classification and Analysis Report boundaries | `CARMADIO-REQUIREMENT-GOV-029` |
| Type-first artifact names and independently selectable subtype-name capability | `CARMADIO-REQUIREMENT-GOV-038` |
| Medium/high immutable-artifact admission strictness | `CARMADIO-REQUIREMENT-GOV-039` |
| Hidden control-plane root, one settings/manifest carrier, distinct ignored runtime state, disposable host scratch, explicit path bases, and direct ownership roots | `CARMADIO-REQUIREMENT-GOV-043` |
| Current-only project control plane with inert historical aggregates and completed migrations outside skill discovery | `CARMADIO-DECISION-GOV-028` |
| Repository legal files outside `.dset`, with deterministic legal-only provenance resolution | `CARMADIO-DECISION-GOV-029` |
| Executable product contracts in TOOL, development realization in IMPL, and post-implementation operation in OPS | `CARMADIO-DECISION-GOV-031`, `CARMADIO-DECISION-IMPL-001`, `CARMADIO-DECISION-OPS-013` |
| Selected Local Python Tools environment, coding, QA-implementation, portability, dry-run, diagnostics, and visible documented-constant rules | `CARMADIO-REQUIREMENT-IMPL-001..003` |
| Repository text-byte configuration and portable code/path/Test realization | `CARMADIO-DECISION-TOOL-001`, `CARMADIO-DECISION-IMPL-002..005` |
| Visibly ordered layer directories with stable logical layer IDs | `CARMADIO-REQUIREMENT-GOV-044` |
| Horizontal feature Contracts and forward-only layer authority | `CARMADIO-REQUIREMENT-GOV-045` |
| One-level-down project/group/feature/layer architecture views | `CARMADIO-REQUIREMENT-GOV-031` |
| Narrowest-common-scope ownership for project, group, feature, and layer truth | `CARMADIO-REQUIREMENT-GOV-032` |
| Parent-to-child artifact inheritance, local implementation/cancellation, and direct fallback | `CARMADIO-REQUIREMENT-GOV-033` |
| Many-to-many child-owned lineage and derived reverse/transitive traceability | `CARMADIO-REQUIREMENT-GOV-034` |
| Six flat Version lifecycle subtypes | `CARMADIO-REQUIREMENT-OPS-013` |
| Role-aware handling for every governed conflict pairing, with priority selection only where permitted | `CARMADIO-REQUIREMENT-TOOL-019` |
| Evidence-derived TypeScript candidate profile and promotion boundary | `CARMADIO-REQUIREMENT-TOOL-021` |
| Framework-reference versus project-applied TypeScript profile authority | `CARMADIO-REQUIREMENT-TOOL-022` |

The canonical text lives in the accepted META, GOV, TOOL, SKILL, IMPL, and OPS
evergreen package fragments under `.dset/101_layer_meta/` through
`.dset/106_layer_ops/`. This Change
owns implementation and proof for those accepted requirements, not duplicate
normative prose.

Connected accepted IDs are `CARMADIO-REQUIREMENT-META-007`,
`CARMADIO-REQUIREMENT-META-011`, `CARMADIO-REQUIREMENT-TOOL-004`,
`CARMADIO-REQUIREMENT-GOV-014`, `CARMADIO-REQUIREMENT-GOV-015`,
`CARMADIO-REQUIREMENT-GOV-016`, `CARMADIO-REQUIREMENT-GOV-017`,
`CARMADIO-REQUIREMENT-GOV-018`, `CARMADIO-REQUIREMENT-GOV-019`,
`CARMADIO-REQUIREMENT-GOV-020`, `CARMADIO-REQUIREMENT-GOV-021`,
`CARMADIO-REQUIREMENT-GOV-022`, `CARMADIO-REQUIREMENT-GOV-023`,
`CARMADIO-REQUIREMENT-GOV-024`, `CARMADIO-REQUIREMENT-GOV-025`,
`CARMADIO-REQUIREMENT-GOV-026`, `CARMADIO-REQUIREMENT-GOV-027`,
`CARMADIO-REQUIREMENT-GOV-028`,
`CARMADIO-REQUIREMENT-GOV-029`,
`CARMADIO-REQUIREMENT-GOV-031`, `CARMADIO-REQUIREMENT-GOV-038`,
`CARMADIO-REQUIREMENT-GOV-039`,
`CARMADIO-DECISION-GOV-028`,
`CARMADIO-DECISION-GOV-029`,
`CARMADIO-DECISION-GOV-031`,
`CARMADIO-REQUIREMENT-GOV-043`, `CARMADIO-REQUIREMENT-GOV-044`,
`CARMADIO-REQUIREMENT-GOV-045`,
`CARMADIO-REQUIREMENT-GOV-032`,
`CARMADIO-REQUIREMENT-GOV-033`,
`CARMADIO-REQUIREMENT-GOV-034`,
`CARMADIO-REQUIREMENT-TOOL-018`,
`CARMADIO-REQUIREMENT-TOOL-019`,
`CARMADIO-REQUIREMENT-TOOL-021`,
`CARMADIO-REQUIREMENT-TOOL-022`,
`CARMADIO-REQUIREMENT-SKILL-002`, `CARMADIO-REQUIREMENT-SKILL-003`,
`CARMADIO-REQUIREMENT-SKILL-004`, `CARMADIO-REQUIREMENT-SKILL-005`,
`CARMADIO-REQUIREMENT-SKILL-006`, `CARMADIO-REQUIREMENT-SKILL-007`,
`CARMADIO-REQUIREMENT-SKILL-008`, `CARMADIO-REQUIREMENT-SKILL-009`,
`CARMADIO-REQUIREMENT-SKILL-011`, `CARMADIO-REQUIREMENT-SKILL-013`,
`CARMADIO-DECISION-TOOL-001`,
`CARMADIO-DECISION-IMPL-001`, `CARMADIO-DECISION-IMPL-002`,
`CARMADIO-DECISION-IMPL-003`, `CARMADIO-DECISION-IMPL-004`,
`CARMADIO-DECISION-IMPL-005`, `CARMADIO-REQUIREMENT-IMPL-001`,
`CARMADIO-REQUIREMENT-IMPL-002`, `CARMADIO-REQUIREMENT-IMPL-003`,
`CARMADIO-DECISION-OPS-013`,
`CARMADIO-REQUIREMENT-OPS-003`, `CARMADIO-REQUIREMENT-OPS-004`,
`CARMADIO-REQUIREMENT-OPS-005`, `CARMADIO-REQUIREMENT-OPS-006`,
`CARMADIO-REQUIREMENT-OPS-007`, and `CARMADIO-REQUIREMENT-OPS-013`.

## ADDED — CARMADIO-REQUIREMENT-SKILL-013 Selectable implementation preparation

Public skills accept a desired outcome rather than requiring the operator to
invoke every prerequisite skill manually. Repository-local lifecycle rules own
entry criteria, allowed prerequisite workflows, exit criteria, and stops. Each
transition must satisfy a missing criterion and re-read authority; no progress,
repeated state, cycles, ambiguity, failure, or a new authorization boundary
stops the finite closure.

`.dset/dset_settings.toml` selects `workflows.implement.mode`. Lazy mode invokes
`decisions` first, conditionally prepares separate Test/Evaluation and
implementation plans, and implements only after all entry criteria are
satisfied. Strict mode performs implementation only and stops on missing
accepted prerequisites. Session history is candidate evidence rather than
authority, so reconciliation never invents acceptance or edits immutable atoms.

## ADDED — CARMADIO-REQUIREMENT-GOV-029 MECE artifact classification

Every governed carrier must have one primary artifact type and at most one
allowed direct artifact subtype, independently from the four semantic Types.
The project-local artifact-type registry owns the eleven development roles,
their primary questions, direct subtypes, fallback behavior, and path rules.
Analysis Report is non-authoritative and permits Solution Landscape,
Root-Cause Analysis, Proposal, Technical Investigation, and External Audit
Analysis. Unknown, mismatched, nested, missing, or ambiguous classifications
fail closed.

Roadmap, Version Scope, Change, Release Plan, Readiness Record, and Release
Record are direct subtypes of Version and share the `VERSION` identity
sequence for newly emitted carriers.

**Scenario CARMADIO-SCENARIO-GOV-030:** A Proposal recommends one candidate; a
separate Decision accepts it; Specification/Design compiles it; Evidence Record
captures a Test run; Verification assesses the evidence; and Readiness Record
makes the explicit release gate disposition without any workflow-derived
reclassification.

## ADDED — CARMADIO-REQUIREMENT-GOV-032 Structural-scope ownership

Every claim and compiled artifact belongs to the narrowest common structural
scope containing all affected owners and subjects. Project-level truth owns
only genuinely cross-child or whole-project concerns—shared outcomes and
requirements, Contracts and semantics, end-to-end QA, cross-cutting policy,
integration architecture, release/readiness, and cross-owner unresolved work.
High-level wording does not promote a child-owned claim, and parents link rather
than duplicate child detail.

## ADDED — CARMADIO-DECISION-GOV-013 Typed artifact relations

Consequential forward edges use `child_of`, `analysis_of`, `projection_of`,
`implementation_of`, `check_of`, `evidence_for`, `resolution_of`,
`override_of`, `replacement_of`, or fallback `relates_to`. Reverse edges are
derived and never authored. One source-target pair has one primary relation;
`child_of`, scoped `override_of`, and complete `replacement_of` never overlap.

Evergreen `projection_of` normally records one semantic-Type/exact-scope range
through a globally ordered immutable `ATOMIC-RECORD` frontier. A newer
applicable atom makes the projection stale. Sealed legacy `child_of` remains
compatibility input; new artifacts use `relations`.

## ADDED — CARMADIO-REQUIREMENT-OPS-012 Integration delivery is the default

Every applicable DSET project must use its configured local integration branch,
remote integration branch, and integration-to-protected release PR as the base
delivery flow. A Change may opt into a separate branch-backed worktree when
parallelism, risk, or conflicting work needs stronger isolation. That branch
must integrate into the configured integration branch before release. Workspace
mode never changes Change identity, scope, authorization, or proof ownership.

**Scenario CARMADIO-SCENARIO-OPS-013:** This repository works locally on `dev`,
pushes remote `dev`, and opens PR `dev` to `main`. A parallel high-risk Change
selects `branch-worktree`, reviews that branch into `dev`, and then participates
in the same protected release flow without creating a permanent layer branch.

## ADDED — CARMADIO-REQUIREMENT-GOV-020 Artifact roles

DSET must classify durable artifacts as atomic authority sources, evergreen
compiled projections, transactional context/evidence, or implementation-layer
artifacts so reviewers do not confuse rationale, evidence, code, or generated
views with accepted source truth.

**Scenario CARMADIO-SCENARIO-GOV-021:** An accepted Decision owns its atomic choice,
the spec and proof plans compile the current consequences, and implementation
cites the Decision without becoming authority. If projection and Decision
differ, the Decision wins and the projection is stale.

## ADDED — CARMADIO-REQUIREMENT-GOV-021 Atomic-source compilation

Accepted, active, applicable Requirements, Contracts, Decisions, and other
normative atoms must compile their current behavioral consequences into the
owning evergreen specs, plans, runbooks, or governing rules. Atomic artifacts
are immutable; later state is append-only. A new atom may explicitly and
acyclically absorb older ones while preserving or replacing every applicable
consequence. Only a fully retired atom may move byte-for-byte to `archive/`.

**Scenario CARMADIO-SCENARIO-GOV-022:** A resolved Question produces a Decision, the
Decision compiles into the relevant projection, and review rejects a code-only
change that leaves the spec stale. A successor Decision explicitly absorbs its
immutable predecessor rather than winning because it is newer.

## ADDED — CARMADIO-REQUIREMENT-GOV-022 Commit and session provenance

Commits that change evergreen truth or implementation artifacts must cite the
Decision or Decisions they implement. A Problem, Question, QA atom, or Change
may be cited as additional provenance but never substitutes for authorizing
Decision authority. Newly emitted atomic artifacts and
append-only lifecycle events expose explicit unique host-prefixed
`llm_session_ids` when an LLM helped produce them, or an explicit empty/`none`
disposition for human-only work. Review, correction, and status changes emit
linked records instead of revising atoms. Missing provenance is invalid. The
rule applies to Changes, intake items, Decisions, promoted proofs, skill-run
records, and session checkpoints.

**Scenario CARMADIO-SCENARIO-GOV-023:** A commit body contains
`Implements: CARMADIO-DECISION-GOV-001`, and the Decision artifact records the
Codex session IDs that produced or materially revised it.

## ADDED — CARMADIO-REQUIREMENT-GOV-023 Governance constitution

`CARMADIO-RULE-ARCHITECTURE` remains the sole dependency-free governance root.
Every rule declares separate acyclic dependency and conflict-precedence
relations. Rule authority comes from accepted active atomic sources compiled
into the applicable current local governing document; a mismatch selects the
source and makes the projection stale. Active Decisions explain and authorize
changes, provenance identifies origin, and tests/evals/reviews/evidence assess
assurance without becoming authority.

**Scenario CARMADIO-SCENARIO-GOV-024:** A precedence cycle or missing precedence
owner fails closed. Stale evidence leaves the affected assurance claim stale
and blocks its relying gate without silently erasing the applicable rule.
