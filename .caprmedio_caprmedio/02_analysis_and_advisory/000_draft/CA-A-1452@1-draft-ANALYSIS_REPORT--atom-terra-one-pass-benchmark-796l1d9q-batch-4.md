---
identity:
  atom_id: CA-A-1452
  ref_id: CA-A-1452@1-draft
context:
  role: analysis_and_advisory
  form: Analysis Report
  tier: 3
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+
      Authoring
  container:
    scope_unit: CA-SU-00
state:
  version: 1
  status: draft
  updated_at: '2026-11-12T21:04:26.960676+00:00'
destination:
  file:
    name: CA-A-1452@1-draft-ANALYSIS_REPORT--atom-terra-one-pass-benchmark-796l1d9q-batch-4.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory/000_draft
---
## Summary

Atom Terra one-pass benchmark 796l1d9q batch 4

## Details

```json
{
  "batch": 4,
  "model": "gpt-6.1-terra",
  "effort": "medium",
  "candidates": [
    {
      "ref": "CA-E-483",
      "version": 21,
      "summary": "Reject invalid CAPRMEDIO Routing Trees",
      "prose_claim": "The Evaluation of the CAPRMEDIO Routing Tree registered under CA-R-1640-PROJECT_CONFIGURATION-RULE--register-one-canonical-routing-tree **must** reject a routing tree when any of the conditions in Details is present.",
      "details": "- An invalid schema.\n- An unknown target.\n- Ambiguous precedence.\n- A duplicate route identity.\n- An authority effect that is not explicitly declared.",
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-M-231",
      "version": 34,
      "summary": "Derive navigation values from authoritative content",
      "prose_claim": "To derive an Atom's navigation values, use authoritative content, not another navigation value:\n\n- Derive a new Atom's Summary from its finalized primary contribution within its applicability under CA-R-2499 and CA-M-442. For RMED, use Claim read within Scope, not Scope alone.\n- Derive every requested Projection from its applicable complete source content, including relevant textual applicability restrictions. Do not derive it from the Summary.\n- For an existing Atom identity, retain its Summary and check source faithfulness. A needed Summary change follows CA-R-1464 and **must not** be applied as a same-identity refresh.",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-R-1880",
      "version": 18,
      "summary": "Preserve the prior runtime and report release effects truthfully",
      "prose_claim": "Release Version **must** preserve the prior runtime until its prepared replacement is ready. It **must** report actual effects and failures truthfully. It must never replay an uncertain effect automatically.\n\nAfter successful replacement and Project-MCP readiness, Release Version **must** retire only verified superseded release-owned images for the current Project. Their exact immutable identity and ownership must be known. They must have no retaining container or protected reference.\n\nLocal Release must support rebuilding the Engine from a known-good checkout and its generated assets. It must do so even if the current service cannot start or the prior image has been removed.",
      "details": "Preserve the current image and unrelated, other-Project or protected images. Establish current-Project ownership from actual build/launcher/start evidence that contains immutable image identity and Project identity. Check this evidence against Docker inspection. A tag prefix alone is insufficient.\n\nCleanup includes the exact prior image when eligible. It reports removed, protected, in-use or unproven results. Do not force-remove containers. Do not claim complete cleanup when ownership or use remains uncertain.\n\nA failure after a real effect reports that partial state and the failed step for manual handling. It does not claim automatic rollback, restore a retired runtime selector or replay an unknown effect. A request, test result or prepared package is not release success. Preserve source data and unrelated configuration. No failure permits broad image pruning.\n\nJournal records describe what happened. Earlier records, baseline rows, terminal-recording recovery and proof receipts are not prerequisites for a release or its first recorded change. A missing Journal record does not undo a real effect or turn it into a different outcome.",
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-E-639",
      "version": 18,
      "summary": "Require complete change readiness before acceptance or delivery",
      "prose_claim": "A PROGRAMMATIC change may be represented as ready for acceptance or delivery only when its known required affected-surface and dependency closure is reconciled as one coherent increment.\n\nResolve known, mechanically checkable omissions in required consumers, contracts, schemas, configuration, dependencies, fixtures or delivery carriers during preparation. Do not knowingly defer them for downstream acceptance tests to discover. An unresolved required obligation remains an explicit readiness gap. It is not a completed or ready result.",
      "details": "### Scope\n\nPreparation and readiness claims for new or changed PROGRAMMATIC implementation, including descendant Scope Units, before an acceptance or delivery attempt.\n\n- Judge completeness against the applicable governing specification and the actual bounded affected surface. Do not require unrelated Project work, invent additional business rules, or silently expand the authorized change.\n- Where the change affects them, include affected callers and adapters, parser/validator and registry bindings, configuration and dependency realization, test-world inputs, and delivery/packaging boundaries. A valid isolated component is not evidence that its affected consumers or delivered realization are coherent.\n- Distinguish a valid verification world from the behavior under evaluation. Known missing fixture/support inputs, contradictory source pins or an unprepared required execution environment are preparation defects. Do not report their absence as successful behavioral verification. Deliberately invalid targets and intentional red/exploratory tests remain valid when their intended purpose and expected outcome are explicit.\n- Repair a known shared cause at its canonical owner and reconcile the affected paths. Fixing only the latest symptom does not establish readiness while that cause remains on those paths. Preserve applicable safeguards rather than weakening them to obtain a green result.\n- This policy does not guarantee a defect-free first attempt. It does not require every test to pass before any test may run. Unknown defects, exploratory failures and genuine host/environment failures remain possible and must be reported truthfully.\n- Readiness is not permission or execution completion. This policy adds no separate human approval, Journal-history/completeness prerequisite, live-Atom validation, release registry or extra release workflow. Existing authority, effect, Evaluation-portfolio and delivery boundaries remain in force.",
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-R-2634",
      "version": 2,
      "summary": "Declare the permitted Project Authority Mode values",
      "prose_claim": "The permitted values are `strict` and `casual`. The effective selection follows the applicable authority-mode resolution.",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-O-181",
      "version": 15,
      "summary": "Run one authorized host-capable Candidate E2E execution\n\n## Action\n\nRun host-capable Candidate E2E **means** one explicitly authorized host-capable controller execution against CA-O-186's exact candidate image, package, source frontier and N/N+1 bindings.\n\n## Details\n\nThe host-capable Candidate E2E inventory is the current runtime-test set under `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/tests/`. Every declared testcase in that selected runtime-test set must terminal-pass. A skipped, excluded, missing or zero-coverage testcase is non-pass.\n\nThe frozen Docker worker has no Docker socket and cannot claim this phase. A registered explicit host-capable controller and its exact declared capability are required. Missing, denied, unsafe, unavailable, stale, non-passing or unjournalable capability yields its actual non-pass outcome.\n\nThis Action never selects N+1, promotes, retires, mutates sources, expands mounts, exposes credentials or substitutes a cached/focused result. It records one recoverable Journal result bound to the exact candidate and image identity.",
      "prose_claim": null,
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-O-203",
      "version": 11,
      "summary": "Create one explicitly requested Scope Unit\n\n## Operation\n\nCreate One Scope Unit **means** the logical Action that adds exactly one explicitly requested Scope Unit to authoritative Project Structure under CA-R-1829. It does not infer a Scope Unit from a folder or invent a new connector or authority root. Scope identity/hierarchy, complete structure schema and admission are workflow-owned decisions. A mechanical connector receives only the checked explicit target/delta/preconditions/permission through D625.\n\n### Action\n\n1. Bind the explicit new Scope Unit identity, its declared parent and allowed type and properties, current Project Structure source pin, applicable current schema and authority, and exact permission. Reject duplicate identities, missing or ambiguous parent, invalid hierarchy/root constraints or an unsupported schema before effects.\n2. Validate the complete proposed authoritative structure under CA-D-441 and the current structure authority. Preserve all unrelated Scope Units and every protected field. The implicit Project root is not a duplicate `scope_units` row.\n3. Use the same shared TOML realization selected for O204, with the Project Structure target resolved privately. There is no separate TOML connector. Derive and expose this one exact mutation-free proposal before an independently admitted effect.\n4. Recheck source, authority, schema and permission immediately before the safe one-Scope-Unit effect. Independently read back and schema-check the complete result. Report actual identity/effects or truthful failed, partial or unknown evidence. No Atom deletion, automatic reference rewrite or unsupplied structural change follows.\n\n## Details\n\nIts separate governing Workflow and executable realization remain future gated work. This Action does not introduce an additional Workflow or Step now. Current Project Structure dispatch semantics remain applicable. Storage paths and folders are private realization details, not the public Scope Unit selector.\n\nThese are normative source definitions, not executable bindings or live admission. Before any actual Run, resolve and independently verify the selected realization, current definition pins, applicable permissions and shared Run recording under CA-R-1525/CA-R-1720. Missing, stale, unsupported or incompatible bindings stop before dispatch. No new retry/resume decision, MCP activation, runtime manifest change, Core adoption or Subject publication is authorized.",
      "prose_claim": null,
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-D-709",
      "version": 1,
      "summary": "Use a shared structured record for operational diagnostics",
      "prose_claim": "PROGRAMMATIC operational diagnostics **must** use **`=1`** shared structured record representation at their declared diagnostic output boundary.\n\n- The delivered record schema represents the context required by CA-M-414 and the applicable production fields under CA-D-396. It preserves the severity and safety rules of CAPRMEDIO-GOV-REQU-315 without defining another field meaning or severity vocabulary.\n- Carry canonical action or Event references unchanged when available. Absent references remain absent rather than being invented for an exporter.\n- A concise human rendering and any exporter-specific encoding are derived representations of that record. They are not separately maintained diagnostic facts or schemas with competing meanings.\n- Production record placement follows the declared Logging Policy sink. The Project Journal is not an alternative diagnostic output Carrier.",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-D-463",
      "version": 26,
      "summary": "Give every Atom Revision one authoritative Carrier Bundle",
      "prose_claim": "Every Atom Revision **must** have **`=1`** authoritative Carrier Bundle on the Project filesystem. The bundle contains **`=1`** Markdown File Carrier and **`>=0`** additional Carriers admitted by its applicable Delivery authority.\n\nThe Markdown file carries the Atom's own Properties under CA-D-478 and CA-D-479. Additional Carriers represent that same Revision without replacing the mandatory file or independently redefining its Properties.",
      "details": null,
      "semantics": null,
      "operation": null
    },
    {
      "ref": "CA-M-407",
      "version": 14,
      "summary": "Use functions for deterministic transformations",
      "prose_claim": "Use a side-effect-free function as the default unit of PROGRAMMATIC behavior. Implement one deterministic transformation as a function when its result follows only from its declared inputs and the responsibility needs no identity across calls.",
      "details": "### Applicable when\n\nApply when Tools, App backend services, or MCP components parse, classify, validate, plan, project, format, or otherwise transform explicit input into a result.\n\n### Procedure\n\n- Use a function unless the responsibility must own mutable state, an invariant across calls, a resource, a lifecycle, or a replaceable adapter.\n- Give the function a specific, intention-revealing verb phrase that states its one responsibility. Prefer clarity over brevity. Split a function whose accurate name requires multiple responsibilities.\n- State the function's input, result, and failure values explicitly.\n- Do not mutate inputs or shared state, perform I/O or logging export, or read the filesystem, process, clock, environment, network, persistence, or randomness.\n- Pass every required observation and setting as explicit input rather than obtaining them implicitly.\n- Group related functions in a specifically named module. Do not create a class only to provide a namespace.\n\n### Outcome\n\nBehavior is locally readable, reproducible from declared input, and free of observable side effects. It can be reused, checked, or extended without constructing component lifecycle state.\n\n### Failure or stop\n\nStop treating the unit as a deterministic transformation when it applies an external effect. A bounded one-shot effect may remain a function under CA-M-425. Allocate an object only when identity across calls or owned state, invariant, resource, lifecycle, or adapter behavior is required.\n\n### Sources\n\n- [Python Functional Programming HOWTO](https://docs.python.org/3.14/howto/functional.html)\n- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)\n- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis_and_advisory/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)",
      "semantics": null,
      "operation": null
    }
  ]
}
```
