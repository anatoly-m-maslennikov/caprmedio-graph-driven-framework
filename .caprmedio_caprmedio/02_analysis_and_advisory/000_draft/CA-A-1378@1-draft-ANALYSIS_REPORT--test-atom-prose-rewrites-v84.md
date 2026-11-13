---
identity:
  atom_id: CA-A-1378
  ref_id: CA-A-1378@1-draft
context:
  role: analysis_and_advisory
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+
      Authoring
  form: Analysis Report
  tier: 3
  container:
    scope_unit: CA-SU-00
state:
  version: 1
  status: draft
  updated_at: '2026-11-12T15:06:17.907513+00:00'
destination:
  file:
    name: CA-A-1378@1-draft-ANALYSIS_REPORT--test-atom-prose-rewrites-v84.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory/000_draft
---
## Summary

Test Atom prose rewrites v84

## Details

````json
[
  {
    "ref": "CA-E-652",
    "version": 22,
    "summary": "Check shared-context test-first implementation and Method learning",
    "prose_claim": "The shared-context implementation and Method-learning Workflow check **must** reject any definition or Run that conflates their separate completion conditions or bypasses their evidence gates.\n\n- Exercise selected R/M/D obligations with missing substantive E coverage, an unrelated green linter, and stale optional Method/review projections. Reject false coverage. Require current direct source rows, justified inapplicability or current predicates, selected checks, and evidence for each applicable obligation.\n- Exercise `preliminary_clear` with pending checks. It must not complete or pass the candidate. Require final tests and final read-only review on the same candidate and bindings. Inject a review finding, repair, changed test definition, or changed authority. Affected earlier evidence must become stale, and the required review/check phases must rerun through existing finite diagnosis/retry control.\n- Exercise terminal completion followed by an explicitly requested separate release handoff. Reject a cross-Workflow Step route, implicit release execution, missing release admission, and acceptance from definition-only checks. Standalone CA-O-229 remains Isolated.",
    "details": "- require selected active R/D as implementation targets **and** applicable E as separate check authority. require direct full `requirements`, `methods`, `evaluations`, and `delivery` rows, original full source content, exact source bindings, and complete explicit declared-universe verification. exercise an omitted applicable Method, a summary substituted for its full content, stale source bytes, and conflicting identities; **every** case **must** block readiness rather than silently weaken authority. An optional legacy `method_projection` neither replaces direct rows nor blocks readiness when absent; Methods outside the selected work do not become applicable merely by inclusion.\n- require P/Plan work, falsifiable Definitions of Done, actual dependencies, bounded work, and explicit Integrated Steps for CA-O-016; MCP is **not** required.\n- check that implementation Evaluation preparation follows applicable Methods **and** Evaluation policy **before** behavior implementation, with **only** explicit minimum prerequisites admitted. require at least one prepared check capable of failing against absent **or** incorrect behavior at its selected observable boundary. **when** PROGRAMMATIC policy applies, require a portfolio admitted by the applicable PROGRAMMATIC Core Evaluation authority; neither unit-level nor end-to-end evidence has default priority.\n- exercise expected initial failure, a genuine code defect, test-code defect, an environment blocker, **and** incorrect governing expectations. require distinct diagnoses; do **not** turn **every** failure into a Method lesson.\n- require relevant targeted reproduction/regression checks for discovered defects **and** the complete admitted current-candidate Evaluation portfolio **after** repair. preserve confidence, permission, retry accounting, **and** no-progress termination.\n- complete CA-O-016 with **all** required implementation work **and** checks satisfied **without** creating an M Atom. reject `methods_ready`, Method drafting, Method promotion, **or** CA-O-098 as an internal completion dependency of that graph.\n- invoke CA-O-102 separately with retained issue/test/diagnosis/fix evidence. verify deduplication against existing Methods, Standard Draft creation **only** for a justified missing Method, no assigned Draft ID, **and** no automatic broader-policy generalization.\n- keep a Method Draft non-authoritative **until** its correction **and** regression are verified, current authority is checked, **and** applicable confidence/permission/Operator approval gates pass. a blocked learning Run **must not** turn a completed implementation Run into an incomplete one.\n- reject activation from stale evidence **or** tests alone **without** a supported lesson. a newly accepted Method changes future authority bindings; it does **not** silently reclassify old results as checked against that new authority.\n- distinguish graph-definition conformance from real Run evidence; defining tests **or** Workflows is **not** proof of execution.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-E-600",
    "version": 25,
    "summary": "verify Project MCP image and runtime admission",
    "prose_claim": "The Evaluation **must** prove that only a matching immutable image and a healthy same-Project runtime published on the fixed Project Settings port can be used.",
    "details": "### Image, lock, and runtime checks\n\n- Verify private Buildx `BUILDX_CONFIG` state/logs use only the build-attempt sibling `buildx/`; secret environment variables are excluded, the manifest remains exact, no `~/.docker/buildx` write occurs, and no worker starts.\n- Test the ordered source manifest/fingerprint with changed explicit Engine, dependency, Dockerfile/ignore, platform, and argument inputs; each change must alter the fingerprint. Project carriers, credentials, installed state, generated outputs, and unrelated repository source remain outside it.\n- Exercise mutable/missing/wrong-schema/fingerprint-mismatched/correct image references. Missing matching images build only under default `build_if_missing=true`; `--no-build` refuses. Capture and re-inspect an immutable digest without moving tags or replacing images; evaluate additive display metadata separately.\n- A packaged launcher missing Engine/Docker/dependency input returns `IMAGE_INPUT_UNAVAILABLE`, requests `--source-root`, preserves runtime N, and does not start Release/package replacement/Framework promotion. Under held, healthy matching, unhealthy, and live-mismatch per-Project locks/runtimes, only the healthy matching case reuses; all other live cases preserve service and return a non-success disposition.\n- Test `[project_mcp] http_port` valid, missing, non-integer, boolean, zero, and out-of-range values; invalid values fail before Docker and `--port` must equal Settings. Test two Projects with different ports, exact reuse, wrong publication, and occupied port: no random port, pre-reservation, or Workflow. Verify the uv bootstrap forwards only selected Project and port.\n- With Docker available, start/reuse one `mcp-http` and verify exactly one `127.0.0.1:<http_port>` publication to `8092`, equal to Settings, without host pre-reservation. Docker absence/denial is incomplete/failed real-Docker evidence, not a pass. Test clean install/upgrade of `.caprmedio_runtime/start_mcp.py`: tracked package bytes, refreshed upgrade, unchanged config/state, no startup during installation, and explicit invocation against installed package without Engine checkout.\n- Verify no worker, queue, Agent, Workflow, Tool call, proxy, or Release action starts.\n\n### Readable metadata and dependency acceptance\n\nUse frozen synthetic fixtures and the canonical naming boundary. Require and fingerprint exact `version.toml`; version changes alter identity and unrelated Project/runtime state stays excluded. New builds carry OCI version; absent/invalid version or malformed/unavailable Docker `Created` fails truthfully. Assert `caprmedio-runtime:<framework-version>-<UTC-build-date-YYYYMMDDTHHMMSSZ>-<first12-image-sha>` from inspected timestamp, including cached/reused images. Check absent-tag addition, same-digest no-op, occupied-other-digest refusal, mutable/wrong-schema/platform/fingerprint refusal, and full immutable-SHA launch. Exercise development, release, and disposable-test callers with isolated cleanup; historical maintenance requires exact identity/version/date and defers unknown evidence. Real Docker uses isolated disposable builds/readback, never production mutation or mock-only success.\n\nCheck the Dockerfile copies lock/manifest before installation, uses BuildKit uv cache, and copies Framework version after installation. Two isolated builds must demonstrate reuse of dependency-installation layer while version changes image identity. Verify `/opt/venv/bin/python` is the direct entrypoint with no retained `uv run` supervisor; MCP serves implementations in one process without an implementation-generation child. Keep locked groups, Project admission, MCP startup/health/query behavior, and report launcher memory separately from cache memory.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-O-195",
    "version": 12,
    "summary": "Push the public closure and upsert `main` PR\n\n## Step\n\nAfter the content prompt, this Step invokes CA-O-196 once to commit and push the prepared closure on `amm/dev`. It then finds the one matching open `main` PR or creates it as Draft. It converts an existing matching open PR to Draft before editing its body.\n\n## Details\n\nThe Step records the pushed commit and the actual Draft PR identity. It cannot merge, retarget, or silently retry an unknown push or PR effect.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-M-266",
    "version": 26,
    "summary": "Follow the Operator-selected implementation mode",
    "prose_claim": "To implement within a Task, follow the Operator-selected mode: evaluate and fix, full rebuild, refactoring, or another authorized approach. Keep the selected mode within the Task permissions and governing RMED. Do not infer permission for a full rebuild from an evaluation-and-fix request. The reconstruction equivalence governed by CA-M-262 applies regardless of mode. It does not require identical code or a no-change rerun.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-D-708",
    "version": 1,
    "summary": "Deliver replayable software Evaluation records",
    "prose_claim": "One replayable Evaluation carrier records the target/source frontier, checked claim/applicability, canonical config and digest, Python/tool versions, CA-M-285 technique, applicable seed/minimized case, result/diagnostics/replay command, and distinct outcomes. Use the CA-D-250 location. Temporary output uses CA-D-437. Valuable evidence remains recoverable. Journal, provenance, and claim evidence stay distinct.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-R-2962",
    "version": 1,
    "summary": "Declare Workflow.Content.Claim.Mermaid Scheme",
    "prose_claim": "The scheme shows all Workflow Steps, including nested Steps.",
    "details": null,
    "semantics": "The value is exactly one `mermaid`-labelled fenced Markdown block. A Mermaid Scheme is a visual Minto summary of its owning Claim's text. Removing it must leave the text's specification complete and unchanged. It may repeat the text.",
    "operation": null
  },
  {
    "ref": "CA-R-1111",
    "version": 24,
    "summary": "Delegate MCP calls to canonical Tools",
    "prose_claim": "Every MCP Tool invocation **must** delegate to the selected canonical Tool executable. It **must not** reimplement Tool decisions, project meaning, target resolution, validation, mutation, recovery behavior, or lifecycle semantics inside the MCP carrier. MCP owns only transport admission, canonical Tool selection, delegation, and result transport.\n\nEvery Finder and every Doer dry run **must** remain independently executable without MCP. A direct executable invocation of a CAPRMEDIO Markdown Atom Doer with `--apply` **must** reject the request unless it carries the authorized project-local MCP delegation and its sealed Initiative action envelope. Introducing MCP **must not** create a Tool dependency on MCP or another APPS unit.",
    "details": "For an exposed validated Tool request, select the canonical Tool executable from the current registry, forward it without substituting MCP behavior, and transport the Tool result with every failure and side-effect boundary. Stop when canonical selection, request validation, or delegated execution fails.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-O-126",
    "version": 15,
    "summary": "Assess prepared result conformance\n\n## Operation\n\nAssess Prepared Result Conformance **means** the optional read-only Action that independently compares one exact caller-selected prepared Artifact set with its complete bound governing intents **and** criteria, then returns source-specific semantic-conformance evidence **without** approving, adopting, releasing, **or** changing the result.\n\n1. bind the caller's exact selected Artifact set **and** final Revisions, complete applicable accepted sources/intents/criteria with their Revisions, producer evidence, original review points with provenance, requested assessment scope, **and** untouched unselected frontier. a report, proposal, Plan, subEpic, **or** related Artifact set is assessed within this bound scope, **not** as an automatic whole-stage gate.\n2. assign a reviewer distinct from the producer of the selected result. the reviewer reads the whole selected meaning **and** complete governing intents, including **all** applicable conditions **and** exceptions; a producer's validation announcement **or** prior assessment is evidence, **not** an independent assessment of the exact final output.\n3. establish the current applicability of the bound sources **and** criteria. reuse CA-O-005 for source-authority conflicts; retain unresolved authority, missing source selection, **or** ambiguous applicability as incomplete evidence rather than inventing precedence **or** adopting another truth source. preserve prior producer findings **and** their source bindings instead of silently replacing them.\n4. compare **every** bound intent, condition, exception **and** original review point with the selected result's actual passages **and** evidence. assess substantive coverage, dispositions, assumptions, scope, handoff **and** falsifying completion criteria **when** they are part of the caller's criteria. record conforming support, contradictions, omitted conditions, unsupported claims, gaps **and** uncertainty with exact source/result references; registry grouping, literal-span techniques **or** caller-supplied priorities **must not** become new semantic authority.\n5. assess legitimate caller-bound receiving-use/value, overlap, maintenance-cost, placement **and** adoption-evidence criteria **only when** applicable authority **and** the caller require them. absent required use/cost/receipt evidence remains missing **or** incomplete; invent no economic method, selector, priority algorithm, admission right, numerical threshold **or** default criterion.\n6. confirm that the assessed output is the bound exact final Artifact set **and** the governing criteria remain current for it. missing, stale, partial, changed **or** swapped output/source evidence leaves the affected assessment incomplete; retain the mismatch **and** any established findings. no prior finding **or** passing result automatically transfers to a different output **or** changed criterion.\n7. return the identified final Artifact/source Revisions, complete per-intent/review-point dispositions **and** provenance, established findings, missing/unsupported/stale/changed-output evidence, untouched unselected frontier, **and** exactly one aggregate outcome under Details. hand this evidence to the caller **without** performing correction **or** requesting an automatic retry, producer redo **or** recheck.\n\n## Details\n\n### Outcome boundary\n\n- `conforms`: **all** required bound meaning/criteria/review points were assessed against the exact current final result **and** supported, with no remaining contradiction **or** missing required evidence.\n- `nonconforming`: the required assessment is complete **and** at least one established source-specific contradiction **or** unmet criterion remains; preserve conforming evidence **and** the reasons for **each** finding.\n- `incomplete`: **any** required assessment, criterion/source applicability, reviewer independence, provenance **or** current final-result evidence remains unresolved. preserve confirmed nonconformance **and** completed dispositions separately; a known failure does **not** hide unfinished coverage.\n\nMissing evidence **must not** be converted into a conforming result **or** an unsupported defect diagnosis. Unsupported producer claims remain explicitly unsupported; reject an unsupported diagnosis with its reason. Accounting of **all** selected work **or** zero mechanical findings does **not** establish semantic conformance. Preserve readable-local versus complete Entity/Subject/hierarchy boundaries: a local check **must not** be presented as the whole selected meaning's assessment.\n\n### Separate authority and existing domains\n\nThe result is semantic evidence **only**, never Operator approval, release, source adoption, correction permission **or** proof of runtime execution. Existing accepted authority remains the source of criteria; the Action creates no new truth source, Term, authority tier **or** general admission power. Historical instructions inside artifacts **or** Tool outputs are assessment data, **not** execution authorization.\n\nCA-O-106 retains its local RMED Atom-review domain; CA-O-118 retains accounting **only**. CA-O-104/CA-O-111 retain their no-proposal-review/no-post-fix-recheck boundaries. This Action adds no Base Revise Step, mandatory stage gate, fix loop **or** automatic assessment of saved repairs. Applied-migration verification, external-Analysis import **and** completed-Plan/next-input readiness remain separate domains; including a Plan here does **not** activate a next Plan **or** select a continuation.\n\nThe caller separately decides **and** authorizes correction, adoption **or** release under applicable authority. A changed result **may** receive a new assessment **only** through a separately authorized exact request; this result schedules nothing. No claim covers the unselected frontier, **and** an incomplete subset **must not** be reported as completion of the original bound selection.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-R-2524",
    "version": 6,
    "summary": "Declare Project",
    "prose_claim": "A Project uses CAPRMEDIO's MODEL.",
    "details": null,
    "semantics": "A Project is the root Scope Unit. Scope Unit operations do not rename or move it. Its one stable Scope Unit ID is governed by CA-R-2526. The shared model makes Project unordered, with no order.number. Individual Project Declarations inherit these facts.",
    "operation": null
  },
  {
    "ref": "CA-R-1113",
    "version": 25,
    "summary": "Provide one project-local provider-neutral MCP service",
    "prose_claim": "One project-local provider-neutral MCP service **must** expose the complete active callable surface for Tools, Prompts and Workflows. CAPRMEDIO **must not** require one MCP server per capability. Programmatic calls return their results. Prompt calls return the selected prompt and its invocation envelope for the main session. Workflow calls start or resume the applicable Workflow Run and return the next programmatic result, interactive Step invocation, Operator request, completion or failure state. Every exposed capability **must** remain usable headlessly without GRAPH_UI or an agent-host plugin. Agent-host plugins **may** package or connect to MCP but **must not** own provider-neutral MCP, Tool, Prompt or Workflow behavior.\n\nEach MCP Tool call **must** be bound to the one trusted ProjectSelection of the service before native Tool dispatch. The Codex hook may carry a top-level project_root assertion. In single-Project mode it is optional for compatibility. Omission uses the fixed bound Project; a supplied value must match that Project's canonical host/container mapping and identity. In shared mode project_root is required and must select the already admitted ProjectSelection. A malformed or mismatched value is rejected before Tool execution and never switches the Project. The MCP boundary removes this hook field before passing native Tool arguments. MCP protocol operations such as initialize and tools/list are not treated as Tool-call argument envelopes. Workflow and Prompt wrappers keep their normal native dispatch.\n\nScope check: one project-local service binds each operation to one resolved Project frontier. A shared host may serve multiple explicit Project bindings through one service under CA-R-2008. This requirement does not impose a process-global one-Project restriction or a global current_project.",
    "details": "### Server lifecycle\n\nFor a Project exposing its generated Tool surface through MCP:\n\n1. Bind one provider-neutral project-local service to one immutable ProjectSelection; a shared service may serve multiple explicit bindings.\n2. Treat the Codex hook's top-level project_root only as a selection assertion. Omit it in single-Project mode to use the fixed selection; when supplied, validate canonical host path, container mapping, and identity. Require and validate it in shared mode. Do not wrap initialize/tools/list in this Tool-call envelope; Prompt and Workflow wrappers retain native dispatch.\n3. Reject malformed, escaping, symlink-substituted, foreign, or mismatched assertions before native Tool dispatch, source or Journal effects, then remove the hook field from native Tool arguments.\n4. Expose every eligible Tool without requiring GRAPH_UI or an agent-host plugin; no request may select another Project after binding. The complete callable surface remains headless, project-local, and provider-neutral.\n\nStop if an additional service becomes a competing authority, an assertion mismatches the bound selection, or a capability depends on App presentation. Do not introduce a process-global Project selector.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-D-506",
    "version": 18,
    "summary": "Give every non-ephemeral Entity a Carrier",
    "prose_claim": "Every represented non-ephemeral Entity has at least one declared Carrier or a location within a shared Carrier. Reusable D Policies may define that binding for an entire Object kind and its dependent properties. Individual D Decisions govern bounded exceptions. The governed Subject names the represented Entity, not an extra representation node.",
    "details": "A binding **may** use a shared Carrier or a location within it. A carried Property does not require a separate file or authored CARRIES edge. Its representation follows the applicable owner/property Policy. A derived property can be represented in a Projection without making the Projection authoritative for its source. Occurrents themselves are excluded. Retained information about them follows CA-D-654.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-E-610",
    "version": 12,
    "summary": "Validate public-release request admission\n\n## Scope\n\nOne public-release request before execution.\n\n## Claim\n\nThe Operator **must** verify that missing fields, unknown fields, bad digests, unsafe refs, a malformed Run graph, a stale preview, and absent or stale authorization all stop before a native binding is invoked.\n\n## Details\n\nUse a disposable Project and mock bindings. A valid preview alone is not execute success.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-E-253",
    "version": 27,
    "summary": "Verify changed component technical-contract conformance",
    "prose_claim": "#### Claim checked\n\nOne changed PROGRAMMATIC Tool, App backend service, or MCP component conforms to the Python, runtime, and dependency selections owned by accepted Methods, as materialized in current configuration and Implementation.\n\n#### Applicable conditions\n\nApply when such a component is added or materially changed and no bounded technical-contract exception is proposed.\n\n#### Test case\n\nEvaluate one changed component against the applicable Method-owned selections. Compare its configuration and Implementation carriers with those selections.\n\n#### Acceptance criteria\n\nPass only when the component conforms to every applicable Method-owned selection, its materializations agree, and no configuration, Implementation, or Delivery carrier claims independent selection authority.\n\n#### Failure disposition\n\nReject admission or release of the component until it conforms or enters the separate bounded-exception evaluation.\n\n#### Sources\n\n- [CA-M-415 — Implement PROGRAMMATIC components in Python](../05_method/CA-M-415-PROGRAMMATIC-ENG_POLICY--implement-programmatic-components-in-python.md)",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-D-342",
    "version": 29,
    "summary": "Serialize External Project Goal References",
    "prose_claim": "Every Reference to a Current external Project Goal Atom **must** use its canonical Current Atom ID, not its current Carrier filename stem.\n\nA Reference to an Archived external Project Goal Atom **must** use its canonical Atom ID qualified once with its unchanged numeric Version when historical identity is required. A Current Project Goal reference **must not** omit the canonical ID or fall back to a filename stem. This Delivery creates no ID-less Current exception.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-D-632",
    "version": 15,
    "summary": "deliver the bounded TOMLKit materializer dependency\n\n## Scope\n\nthe technical dependency exception **and** private pure TOML materializer Carriers selected by CA-M-383. this Delivery does **not** change the common logical connector interface **or** install a runtime.\n\n## Claim\n\nthe bounded TOMLKit dependency record **must** bind its selecting Method CA-M-383, capability, exact canonical configuration/lock evidence, private interface, boundary cost, Operator selection **and** Evaluation evidence under CA-E-635 **and** CA-E-254.\n\n- the canonical technical configuration remains root `pyproject.toml`. its named `connector-toml` dependency group carries the exact TOMLKit pin; root `uv.lock` carries the matching resolved package **and** artifact hashes. `required_runtime_dependencies = []`, existing groups **and** supported Python selection remain unchanged. another dependency **or** widened consumer requires separate admission.\n- the private Implementation Carrier is `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/connector_toml_carrier.py`. its in-memory `materialize_toml` interface receives complete source bytes, explicit pure delta **and** private key bindings; it returns proposed bytes, complete native values **and** effective diff **or** a truthful refusal. the path is the existing TOOLS implementation boundary, **not** activation of CONNECTOR_TOOLS' future Delivery root.\n- source bytes **and** native TOML values stay private inputs/results. the callable creates no public typed TOML encoding, logical target, schema authority, permission reference, outer service envelope **or** observed write effect.\n- adjacent focused tests **and** `tests/test_connector_toml_carrier_independent.py` carry literal before/proposed byte ledgers, complete type/value checks, refusal **and** no-op controls. test execution **and** dependency caches use Project Temporary State, **not** governed source **or** runtime state.\n- the boundary cost is one scoped third-party parse/edit/serialization dependency for changed pure materialization. Read **and** no-op retain the standard-library path; no launcher, installer, existing unrelated group **or** runtime image is changed by this Delivery. packaging retains upstream license notices **when** that separately admitted distribution includes the dependency.\n\n## Details\n\nthe Operator-approved selection is recorded under CA-P-2307. this active source record defines the exception; it does **not** substitute for its accepted materialization. actual configuration, lock, Implementation **and** execution evidence are PENDING. each later acceptance record identifies exact source/code/configuration/lock/test pins, interpreter/dependency version, command, result **and** limits; absent evidence remains unavailable.\n\nCA-D-250 retains ownership of the technical configuration Carrier **and** its declared dependency-record/Evaluation locations. this Delivery does **not** relocate those roots **or** claim they are installed. CA-E-254 blocks an incomplete exception. independent source acceptance **and** the affected Operator-approved FPF review precede dependent implementation; local tests do **not** establish installed admission.\n\nCA-D-625 **and** CA-D-631 remain unchanged. receiving Project Structure **and** Project Settings Workflows retain source/schema/currentness/permission decisions; storage publication, Run recording, live routing, Core migration **and** stronger publication guarantees remain outside this exception.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-M-412",
    "version": 13,
    "summary": "Declare one Python and software configuration boundary",
    "prose_claim": "Select the stable CPython `3.14.*` series. Require one project-owned technical configuration boundary for interpreter, formatting, linting, typing, evaluation, and packaging. CA-D-250 owns the current carrier placement and encoding in the root `pyproject.toml`. Configuration and Implementation materialize this Method's selections there. Keep that technical configuration separate from CAPRMEDIO project settings.",
    "details": "### Scope\n\nApply when Python source or a development workflow depends on an interpreter, dependency, formatter, linter, type checker, evaluator, or packager setting.\n\n#### Procedure\n1. Resolve the current Delivery carrier. Then materialize the selected interpreter series and admitted development-tool profiles through that boundary.\n2. Keep one value for every setting. Make local and automated workflows read that value rather than reproduce it.\n3. Change the interpreter series or a selected tool profile only through its accepted Method before changing configuration.\n4. Verify the selected stable series before using version-specific behavior.\n5. Keep runtime project settings outside `pyproject.toml` and expose them only through the shared Settings Reader.\n\n#### Outcome\n\nThis Method owns one set of Python workflow selections. Delivery owns its carrier. Configuration and Implementation reproduce the selections without becoming another methodological authority.\n\n#### Failure or stop\n\nStop when two carriers disagree, a moving `latest` label replaces the selected series, the materialization conflicts with its Delivery, or technical and CAPRMEDIO project settings are mixed.\n\n#### Sources\n\n- [Python 3.14 release notes](https://docs.python.org/3.14/whatsnew/3.14.html)\n- [PyPA: `pyproject.toml` specification](https://packaging.python.org/en/latest/specifications/pyproject-toml/)\n- [CA-A-054 — Validate the Python 3.14 contract upgrade](../02_analysis_and_advisory/CA-A-054-PROGRAMMATIC-ANALYSIS_RPRT--validate-the-python-3-14-contract-upgrade.md)",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-M-241",
    "version": 28,
    "summary": "Derive Canonical Scope Signatures **without** Source Rewrite",
    "prose_claim": "To derive Canonical Scope Signatures from one caller-selected Atom Carrier folder, the Tool **must**:\n\n- Inspect only active Carriers with **`=1`** unwrapped Scope Expression in one `## Scope` section.\n- Resolve every atomic identity against active Atom IDs in that selected folder.\n- Derive a signature only if the Scope Expression satisfies the restricted Canonical Scope Signature grammar.\n- Emit source identity, source revision, source Carrier digest, source frontier digest, source expression, signature, and exclusion diagnostic.\n- Make no source-Carrier rewrite, lifecycle change, Claim merge, authority decision, or dependency relation.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-O-10023",
    "version": 2,
    "summary": "Atom Lifecycle_Update Atom Directly",
    "prose_claim": "This Workflow's Purpose is Runtime; its scheme follows [CA-R-1570](../../CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1570-CORE_META_MODEL-RULE--keep-workflow-graphs-separate-from-step-bindings.md).\n\n#### Input\n\nOne exact Atom selector and the requested property changes.\n\nThe `projectContext` input port binds the Project and applicable model.\n\n#### Output\n\nThe `savedAtom`, warnings, and failure result.\n\n#### Step handoffs\n\n| Step | Receives | Produces |\n| --- | --- | --- |\n| [Apply the requested Direct Atom Update](./CA-O-10023-PROJECT_CONFIGURATION-WORKFLOW--atom-lifecycle-update-atom-directly/CA-O-10022-PROJECT_CONFIGURATION-STEP--apply-the-requested-direct-atom-update.md) | selected Atom, requested changes, and `projectContext` | `savedAtom`, warnings or a failure result |\n\n#### Logical switches\n\n| Condition | Behavior |\n| --- | --- |\n| Entry | Run Apply the requested Direct Atom Update. |\n| `savedAtom` is returned | Complete successfully. |\n| A failure result is returned | Stop and report the explicit failure. |\n\nIf an Action requests additional input, return its short explanation and requested input dictionary. Keep the Workflow pending. Resume with the supplied dictionary. Cancellation is allowed while waiting and does not interrupt an Action.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-O-211",
    "version": 14,
    "summary": "Query declared Scope Units\n\n## Operation\n\nQuery declared Scope Units **means** the reusable effect-free connector Action that executes one explicit Scope Unit Query under CA-R-1937-CONNECTOR_TOOLS-RULE--query-declared-scope-units and CA-D-626-CONNECTOR_TOOLS-ENG_DECISION--deliver-declared-scope-unit-query-data. It is independent of Read or Modify and has no mandatory enclosing Workflow.\n\n### Inputs **and** preconditions\n\nRequire the common `query` request, explicit canonical-name frontier and predicates, bound owning Project/source view, applicable declaration-schema evidence, read authorization, and any supplied exact expected state. Project Settings is the source authority for the root; Project Structure is the source authority for non-Project declarations. Do not infer identity or authority from physical nesting or a Projection.\n\n### Behavior **and** result\n\nValidate the admitted shape and bindings. Resolve the explicit frontier uniquely, check the selected declaration graph, and apply the supplied predicates without defaults. Return the exact empty, singular, or multiple matching identities and requested facts, deterministic ordering, observed source-state evidence, and truthful coverage under the common result roles. Query does not return full declarations or call Read/Modify implicitly. Required effects are none.\n\n### Stops\n\nReturn the declared structured errors for invalid input, unresolved or ambiguous frontier, invalid schema/graph, stale expected state, denied read permission, or backend/incomplete evidence. No error becomes successful empty coverage, guessed historical state, a repaired declaration, or effect authority.\n\n## Details\n\nCA-M-377-CONNECTOR_TOOLS-ENG_DECISION--construct-a-declared-scope-unit-query-adapter is the construction convention. CA-E-629-CONNECTOR_TOOLS-EVAL_CASE--verify-declared-scope-unit-queries owns future checks. A real Run still requires an independently verified realization and applicable existing context/recording. This Action definition introduces no runtime route, new Workflow wrapper, retry/resume, or migration.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-M-492",
    "version": 7,
    "summary": "Use Tabulator for the Workbench read-only result grid",
    "prose_claim": "Use Tabulator 6.7.1 directly in Svelte. Add neither a wrapper nor a second grid engine. The grid is read-only: no cell/row editors or mutation actions. Consume the backend View/grid/page contract over the complete materialized cache. Filtering, multisort, one-column grouping, and exact row/group counts are global. The frontend consumes page slices and never reruns View SQL. In standalone and embedded modes, each Tab holds one query for execution under CA-R-2728. Historical View API identifiers remain compatible.\n\nExpose only Cell Copy value, Cell Show full value, Row Copy row, Column Sort ascending/descending, Group by, Filter, and Clear filter. Group by is one column. Preserve positional columns and duplicate/dotted labels. Add no nested grouping, pivot, collaboration, persisted grid state, or context-menu export. Adaptive/Fixed and Full/Limited are presentation-only. Cache values remain unchanged and shared result-file delivery stays outside this menu.\n\nEach instance owns callbacks. Wait for Tabulator public table-built before data update. Invalidate queued refresh before destroy and target deferred work only to its live instance. Use public lifecycle APIs without renderer patches.",
    "details": null,
    "semantics": null,
    "operation": null
  }
]
````