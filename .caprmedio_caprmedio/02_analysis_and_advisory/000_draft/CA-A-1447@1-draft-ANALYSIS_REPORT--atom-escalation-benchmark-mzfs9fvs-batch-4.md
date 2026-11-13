---
identity:
  atom_id: CA-A-1447
  ref_id: CA-A-1447@1-draft
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
  updated_at: '2026-11-12T20:52:09.334643+00:00'
destination:
  file:
    name: CA-A-1447@1-draft-ANALYSIS_REPORT--atom-escalation-benchmark-mzfs9fvs-batch-4.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory/000_draft
---
## Summary

Atom escalation benchmark mzfs9fvs batch 4

## Details

```json
{
  "batch": 4,
  "atoms": [
    {
      "source_ref": "CA-E-483",
      "source_version": 21,
      "candidate": {
        "ref": "CA-E-483",
        "version": 21,
        "summary": "Validate the routing tree",
        "prose_claim": "The Evaluation of the CAPRMEDIO Routing Tree registered under CA-R-1640-PROJECT_CONFIGURATION-RULE--register-one-canonical-routing-tree **must** reject a routing tree if **any** of these conditions applies:",
        "details": "- its schema is invalid;\n- it contains an unknown target;\n- precedence is ambiguous;\n- a route identity is duplicated; or\n- an authority effect is **not** explicitly declared.",
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-E-483",
        "confidence": "high",
        "escalate": false,
        "reason": "The rejection trigger remains any listed defect: source says reject when “any” is present, and the candidate says “any” condition applies."
      },
      "final": {
        "ref": "CA-E-483",
        "version": 21,
        "summary": "Validate the routing tree",
        "prose_claim": "The Evaluation of the CAPRMEDIO Routing Tree registered under CA-R-1640-PROJECT_CONFIGURATION-RULE--register-one-canonical-routing-tree **must** reject a routing tree if **any** of these conditions applies:",
        "details": "- its schema is invalid;\n- it contains an unknown target;\n- precedence is ambiguous;\n- a route identity is duplicated; or\n- an authority effect is **not** explicitly declared.",
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-M-231",
      "source_version": 34,
      "candidate": {
        "ref": "CA-M-231",
        "version": 34,
        "summary": "Derive navigation projections from the CCE Claim",
        "prose_claim": "Derive an Atom's navigation values from its authoritative content, not from another navigation value.\n\n**To** derive an Atom's navigation values:\n\n- For a new Atom, derive its Summary from its finalized primary contribution within its applicability under CA-R-2499 **and** CA-M-442. For RMED, read Claim within Scope; do **not** use Scope alone.\n- Derive **every** requested Projection from its applicable, complete source content, including relevant textual applicability restrictions. Do **not** derive it from the Summary.\n- For an existing Atom identity, retain its Summary and check that it is faithful to the source. If the Summary must change, follow CA-R-1464. Do **not** apply that change as a same-identity refresh.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-M-231",
        "confidence": "high",
        "escalate": false,
        "reason": "The candidate preserves the Summary and Projection rules, including RMED “Claim within Scope” and the ban on same-identity refresh changes."
      },
      "final": {
        "ref": "CA-M-231",
        "version": 34,
        "summary": "Derive navigation projections from the CCE Claim",
        "prose_claim": "Derive an Atom's navigation values from its authoritative content, not from another navigation value.\n\n**To** derive an Atom's navigation values:\n\n- For a new Atom, derive its Summary from its finalized primary contribution within its applicability under CA-R-2499 **and** CA-M-442. For RMED, read Claim within Scope; do **not** use Scope alone.\n- Derive **every** requested Projection from its applicable, complete source content, including relevant textual applicability restrictions. Do **not** derive it from the Summary.\n- For an existing Atom identity, retain its Summary and check that it is faithful to the source. If the Summary must change, follow CA-R-1464. Do **not** apply that change as a same-identity refresh.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-R-1880",
      "source_version": 18,
      "candidate": {
        "ref": "CA-R-1880",
        "version": 18,
        "summary": "Preserve the prior release and report failures truthfully",
        "prose_claim": "Release Version **must** preserve the prior runtime until its prepared replacement is ready. It **must** report actual effects and failures truthfully. It **must not** automatically replay an uncertain effect.\n\nAfter a successful replacement and Project-MCP readiness, Release Version **must** retire only verified, superseded, release-owned images for the current Project. Their exact immutable identity and ownership must be known. They must have no retaining container or protected reference.\n\nLocal Release must support rebuilding the Engine from a known-good checkout and its generated assets, even if the current service cannot start or the prior image has been removed.",
        "details": "Preserve the current image and all unrelated, other-Project, or protected images. Establish current-Project ownership from actual build, launcher, or start evidence that contains the immutable image identity and Project identity. Check that evidence against Docker inspection. A tag prefix alone is insufficient. Cleanup includes the exact prior image if it is eligible. Report removed, protected, in-use, or unproven results. Do not force-remove containers. Do not claim complete cleanup while ownership or use remains uncertain.\n\nIf a failure follows a real effect, report the partial state and failed step for manual handling. Do not claim automatic rollback, restore a retired runtime selector, or replay an unknown effect. A request, test result, or prepared package does not establish release success. Preserve source data and unrelated configuration. A failure does not permit broad image pruning.\n\nJournal records describe what happened. Earlier records, baseline rows, terminal-recording recovery, and proof receipts are not prerequisites for a release or its first recorded change. A missing Journal record does not undo a real effect or change its outcome.",
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-R-1880",
        "confidence": "medium",
        "escalate": true,
        "reason": "The source requires ownership from “build/launcher/start evidence”; the candidate says “build, launcher, or start evidence.” The slash could require combined evidence, while “or” accepts any one source, changing the ownership proof threshold."
      },
      "final": {
        "ref": "CA-R-1880",
        "version": 18,
        "summary": "Preserve the prior release and report failures truthfully",
        "prose_claim": "Release Version **must** preserve the prior runtime until its prepared replacement is ready. It **must** report actual effects and failures truthfully. It **must not** automatically replay an uncertain effect.\n\nAfter a successful replacement and Project-MCP readiness, Release Version **must** retire only verified, superseded, release-owned images for the current Project. Their exact immutable identity and ownership must be known. They must have no retaining container or protected reference.\n\nLocal Release must support rebuilding the Engine from a known-good checkout and its generated assets, even if the current service cannot start or the prior image has been removed.",
        "details": "Preserve the current image and all unrelated, other-Project, or protected images. Establish current-Project ownership from actual build/launcher/start evidence that contains the immutable image identity and Project identity. Check that evidence against Docker inspection. A tag prefix alone is insufficient. Cleanup includes the exact prior image if it is eligible. Report removed, protected, in-use, or unproven results. Do not force-remove containers. Do not claim complete cleanup while ownership or use remains uncertain.\n\nIf a failure follows a real effect, report the partial state and failed step for manual handling. Do not claim automatic rollback, restore a retired runtime selector, or replay an unknown effect. A request, test result, or prepared package does not establish release success. Preserve source data and unrelated configuration. A failure does not permit broad image pruning.\n\nJournal records describe what happened. Earlier records, baseline rows, terminal-recording recovery, and proof receipts are not prerequisites for a release or its first recorded change. A missing Journal record does not undo a real effect or change its outcome.",
        "semantics": null,
        "operation": null
      },
      "terra_issues": [
        {
          "source": "build/launcher/start evidence",
          "candidate": "build, launcher, or start evidence",
          "reason": "The rewrite resolves an ambiguous slash as alternatives and could alter the evidence threshold.",
          "status": "repaired"
        }
      ]
    },
    {
      "source_ref": "CA-E-639",
      "source_version": 18,
      "candidate": {
        "ref": "CA-E-639",
        "version": 18,
        "summary": "Require complete change readiness before delivery",
        "prose_claim": "A PROGRAMMATIC change may be represented as ready for acceptance or delivery only if its known required affected-surface and dependency closure is reconciled as one coherent increment. During preparation, resolve known, mechanically checkable omissions in required consumers, contracts, schemas, configuration, dependencies, fixtures, or delivery carriers. Do not knowingly defer them for downstream acceptance tests to discover. An unresolved required obligation remains an explicit readiness gap. It is not a completed or ready result.",
        "details": "### Scope\n\nThis policy applies to preparation and readiness claims for new or changed PROGRAMMATIC implementation, including descendant Scope Units, before an acceptance or delivery attempt.\n\n- Judge completeness against the applicable governing specification and actual bounded affected surface. Do not require unrelated Project work, invent business rules, or silently expand the authorized change.\n- Include affected callers and adapters, parser and validator and registry bindings, configuration and dependency realization, test-world inputs, and delivery and packaging boundaries where the change affects them. A valid isolated component does not show that its affected consumers or delivered realization are coherent.\n- Distinguish a valid verification world from the behavior being evaluated. Known missing fixture or support inputs, contradictory source pins, or an unprepared required execution environment are preparation defects. Do not report their absence as successful behavioral verification. Deliberately invalid targets and intentional red or exploratory tests remain valid if their purpose and expected outcome are explicit.\n- Repair a known shared cause at its canonical owner and reconcile the affected paths. Fixing only the latest symptom does not establish readiness while that cause remains on those paths. Preserve applicable safeguards; do not weaken them to obtain a green result.\n- This policy does not guarantee a defect-free first attempt. It does not require every test to pass before any test may run. Unknown defects, exploratory failures, and genuine host or environment failures remain possible. Report them truthfully.\n- Readiness is not permission or execution completion. This policy adds no separate human approval, Journal-history or completeness prerequisite, live-Atom validation, release registry, or extra release workflow. Existing authority, effect, Evaluation-portfolio, and delivery boundaries remain in force.",
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-E-639",
        "confidence": "medium",
        "escalate": true,
        "reason": "The source calls for “parser/validator and registry bindings”; the candidate says “parser and validator and registry bindings.” The slash may denote a combined binding or alternatives, so spelling it as two conjunctive items could alter the required affected surface."
      },
      "final": {
        "ref": "CA-E-639",
        "version": 18,
        "summary": "Require complete change readiness before delivery",
        "prose_claim": "A PROGRAMMATIC change may be represented as ready for acceptance or delivery only if its known required affected-surface and dependency closure is reconciled as one coherent increment. During preparation, resolve known, mechanically checkable omissions in required consumers, contracts, schemas, configuration, dependencies, fixtures, or delivery carriers. Do not knowingly defer them for downstream acceptance tests to discover. An unresolved required obligation remains an explicit readiness gap. It is not a completed or ready result.",
        "details": "### Scope\n\nThis policy applies to preparation and readiness claims for new or changed PROGRAMMATIC implementation, including descendant Scope Units, before an acceptance or delivery attempt.\n\n- Judge completeness against the applicable governing specification and actual bounded affected surface. Do not require unrelated Project work, invent business rules, or silently expand the authorized change.\n- Include affected callers and adapters, parser/validator and registry bindings, configuration and dependency realization, test-world inputs, and delivery and packaging boundaries where the change affects them. A valid isolated component does not show that its affected consumers or delivered realization are coherent.\n- Distinguish a valid verification world from the behavior being evaluated. Known missing fixture or support inputs, contradictory source pins, or an unprepared required execution environment are preparation defects. Do not report their absence as successful behavioral verification. Deliberately invalid targets and intentional red or exploratory tests remain valid if their purpose and expected outcome are explicit.\n- Repair a known shared cause at its canonical owner and reconcile the affected paths. Fixing only the latest symptom does not establish readiness while that cause remains on those paths. Preserve applicable safeguards; do not weaken them to obtain a green result.\n- This policy does not guarantee a defect-free first attempt. It does not require every test to pass before any test may run. Unknown defects, exploratory failures, and genuine host or environment failures remain possible. Report them truthfully.\n- Readiness is not permission or execution completion. This policy adds no separate human approval, Journal-history or completeness prerequisite, live-Atom validation, release registry, or extra release workflow. Existing authority, effect, Evaluation-portfolio, and delivery boundaries remain in force.",
        "semantics": null,
        "operation": null
      },
      "terra_issues": [
        {
          "source": "parser/validator and registry bindings",
          "candidate": "parser and validator and registry bindings",
          "reason": "The rewrite changes the ambiguous slash construction and could alter the affected bindings.",
          "status": "repaired"
        }
      ]
    },
    {
      "source_ref": "CA-R-2634",
      "source_version": 2,
      "candidate": {
        "ref": "CA-R-2634",
        "version": 2,
        "summary": "Declare Project.Settings.Authority Modes.Project Authority Mode",
        "prose_claim": "The permitted values are `strict` and `casual`. Resolve the effective selection under the applicable authority-mode resolution.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-R-2634",
        "confidence": "medium",
        "escalate": true,
        "reason": "The source includes a formal_claim declaring the Project Authority Mode model, but the candidate has no formal_claim counterpart. The prose preserves “strict” and “casual” and the resolution rule, but whether it replaces the formal declaration is unclear."
      },
      "final": {
        "ref": "CA-R-2634",
        "version": 2,
        "summary": "Declare Project.Settings.Authority Modes.Project Authority Mode",
        "prose_claim": "The permitted values are `strict` and `casual`. The effective selection follows the applicable authority-mode resolution.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": [
        {
          "source": "The effective selection follows the applicable authority-mode resolution.",
          "candidate": "Resolve the effective selection under the applicable authority-mode resolution.",
          "reason": "The rewrite turns a declarative resolution rule into an instruction.",
          "status": "repaired"
        },
        {
          "source": "Project.Settings.Authority Modes.Project Authority Mode{::1}:: {::1};",
          "candidate": "formal_claim absent",
          "reason": "The formal declaration has no candidate counterpart; formal_claim is not an available edit field.",
          "status": "flagged"
        }
      ]
    },
    {
      "source_ref": "CA-O-181",
      "source_version": 15,
      "candidate": {
        "ref": "CA-O-181",
        "version": 15,
        "summary": "Run host-capable Candidate E2E\n\n## Action\n\nRun host-capable Candidate E2E **means** one explicitly authorized host-capable controller execution against the exact candidate image, package, source frontier, and N/N+1 bindings specified by CA-O-186.\n\n## Details\n\nThe host-capable Candidate E2E inventory is the current runtime-test set under `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/tests/`. Every declared testcase in that selected set must terminal-pass. A skipped, excluded, missing, or zero-coverage testcase is a non-pass.\n\nThe frozen Docker worker has no Docker socket and cannot claim this phase. A registered, explicit host-capable controller and its exact declared capability are required. A missing, denied, unsafe, unavailable, stale, non-passing, or unjournalable capability yields its actual non-pass outcome.\n\nThis Action never selects N+1, promotes or retires a candidate, mutates sources, expands mounts, exposes credentials, or substitutes a cached or focused result. It records one recoverable Journal result bound to the exact candidate and image identity.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-O-181",
        "confidence": "high",
        "escalate": false,
        "reason": "The candidate retains one explicitly authorized host-capable execution against the exact CA-O-186 bindings and preserves the all-testcases-pass and non-pass conditions."
      },
      "final": {
        "ref": "CA-O-181",
        "version": 15,
        "summary": "Run host-capable Candidate E2E\n\n## Action\n\nRun host-capable Candidate E2E **means** one explicitly authorized host-capable controller execution against the exact candidate image, package, source frontier, and N/N+1 bindings specified by CA-O-186.\n\n## Details\n\nThe host-capable Candidate E2E inventory is the current runtime-test set under `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/tests/`. Every declared testcase in that selected set must terminal-pass. A skipped, excluded, missing, or zero-coverage testcase is a non-pass.\n\nThe frozen Docker worker has no Docker socket and cannot claim this phase. A registered, explicit host-capable controller and its exact declared capability are required. A missing, denied, unsafe, unavailable, stale, non-passing, or unjournalable capability yields its actual non-pass outcome.\n\nThis Action never selects N+1, promotes or retires a candidate, mutates sources, expands mounts, exposes credentials, or substitutes a cached or focused result. It records one recoverable Journal result bound to the exact candidate and image identity.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-O-203",
      "source_version": 11,
      "candidate": {
        "ref": "CA-O-203",
        "version": 11,
        "summary": "Create one Scope Unit\n\n## Operation\n\nCreate One Scope Unit **means** the logical Action that adds exactly one explicitly requested Scope Unit to authoritative Project Structure under CA-R-1829. It does not infer a Scope Unit from a folder or create a connector or authority root. The workflow owns Scope identity and hierarchy, the complete structure schema, and admission decisions. A mechanical connector receives only the checked explicit target, delta, preconditions, and permission through D625.\n\n### Action\n\n1. Bind the explicit new Scope Unit identity, its declared parent, allowed type and properties, current Project Structure source pin, applicable current schema and authority, and exact permission. Before effects, reject duplicate identities, a missing or ambiguous parent, invalid hierarchy or root constraints, or an unsupported schema.\n2. Under CA-D-441 and the current structure authority, validate the complete proposed authoritative structure. Preserve all unrelated Scope Units and every protected field. The implicit Project root is not a duplicate `scope_units` row.\n3. Use the same shared TOML realization selected for O204. Resolve the Project Structure target privately; there is no separate TOML connector. Derive and expose this exact, mutation-free proposal before an independently admitted effect.\n4. Immediately before the safe one-Scope-Unit effect, recheck the source, authority, schema, and permission. Independently read back and schema-check the complete result. Report the actual identity and effects, or truthful failed, partial, or unknown evidence. Do not delete Atoms, automatically rewrite references, or make unsupplied structural changes.\n\n## Details\n\nThe separate governing Workflow and executable realization remain future-gated work. This Action does not introduce an additional Workflow or Step now. Current Project Structure dispatch semantics remain applicable. Storage paths and folders are private realization details, not the public Scope Unit selector.\n\nThese are normative source definitions, not executable bindings or live admission. Before any actual Run, resolve and independently verify the selected realization, current definition pins, applicable permissions, and shared Run recording under CA-R-1525/CA-R-1720. Missing, stale, unsupported, or incompatible bindings stop before dispatch. No new retry or resume decision, MCP activation, runtime manifest change, Core adoption, or Subject publication is authorized.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-O-203",
        "confidence": "high",
        "escalate": false,
        "reason": "The candidate preserves the one-unit limit, workflow-owned decisions, pre-effect checks, read-back, and prohibitions on deletion or unsupplied changes."
      },
      "final": {
        "ref": "CA-O-203",
        "version": 11,
        "summary": "Create one Scope Unit\n\n## Operation\n\nCreate One Scope Unit **means** the logical Action that adds exactly one explicitly requested Scope Unit to authoritative Project Structure under CA-R-1829. It does not infer a Scope Unit from a folder or create a connector or authority root. The workflow owns Scope identity and hierarchy, the complete structure schema, and admission decisions. A mechanical connector receives only the checked explicit target, delta, preconditions, and permission through D625.\n\n### Action\n\n1. Bind the explicit new Scope Unit identity, its declared parent, allowed type and properties, current Project Structure source pin, applicable current schema and authority, and exact permission. Before effects, reject duplicate identities, a missing or ambiguous parent, invalid hierarchy or root constraints, or an unsupported schema.\n2. Under CA-D-441 and the current structure authority, validate the complete proposed authoritative structure. Preserve all unrelated Scope Units and every protected field. The implicit Project root is not a duplicate `scope_units` row.\n3. Use the same shared TOML realization selected for O204. Resolve the Project Structure target privately; there is no separate TOML connector. Derive and expose this exact, mutation-free proposal before an independently admitted effect.\n4. Immediately before the safe one-Scope-Unit effect, recheck the source, authority, schema, and permission. Independently read back and schema-check the complete result. Report the actual identity and effects, or truthful failed, partial, or unknown evidence. Do not delete Atoms, automatically rewrite references, or make unsupplied structural changes.\n\n## Details\n\nThe separate governing Workflow and executable realization remain future-gated work. This Action does not introduce an additional Workflow or Step now. Current Project Structure dispatch semantics remain applicable. Storage paths and folders are private realization details, not the public Scope Unit selector.\n\nThese are normative source definitions, not executable bindings or live admission. Before any actual Run, resolve and independently verify the selected realization, current definition pins, applicable permissions, and shared Run recording under CA-R-1525/CA-R-1720. Missing, stale, unsupported, or incompatible bindings stop before dispatch. No new retry or resume decision, MCP activation, runtime manifest change, Core adoption, or Subject publication is authorized.",
        "prose_claim": null,
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-D-709",
      "source_version": 1,
      "candidate": {
        "ref": "CA-D-709",
        "version": 1,
        "summary": "Deliver shared diagnostic record carriers",
        "prose_claim": "PROGRAMMATIC operational diagnostics **must** use **`=1`** shared structured record representation at their declared diagnostic output boundary.\n\n- The delivered record schema represents the context required by CA-M-414 and the applicable production fields under CA-D-396. It preserves the severity and safety rules of CAPRMEDIO-GOV-REQU-315. It does not define another field meaning or severity vocabulary.\n- Carry canonical action or Event references unchanged when available. If a reference is absent, leave it absent; do not invent one for an exporter.\n- Derive a concise human rendering and any exporter-specific encoding from that record. They are representations of the record, not separately maintained diagnostic facts or schemas with competing meanings.\n- Place production records according to the declared Logging Policy sink. The Project Journal is not an alternative diagnostic output Carrier.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-D-709",
        "confidence": "high",
        "escalate": false,
        "reason": "The candidate retains the single shared record, unchanged-or-absent references, derived renderings, severity safeguards, and Logging Policy sink."
      },
      "final": {
        "ref": "CA-D-709",
        "version": 1,
        "summary": "Deliver shared diagnostic record carriers",
        "prose_claim": "PROGRAMMATIC operational diagnostics **must** use **`=1`** shared structured record representation at their declared diagnostic output boundary.\n\n- The delivered record schema represents the context required by CA-M-414 and the applicable production fields under CA-D-396. It preserves the severity and safety rules of CAPRMEDIO-GOV-REQU-315. It does not define another field meaning or severity vocabulary.\n- Carry canonical action or Event references unchanged when available. If a reference is absent, leave it absent; do not invent one for an exporter.\n- Derive a concise human rendering and any exporter-specific encoding from that record. They are representations of the record, not separately maintained diagnostic facts or schemas with competing meanings.\n- Place production records according to the declared Logging Policy sink. The Project Journal is not an alternative diagnostic output Carrier.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-D-463",
      "source_version": 26,
      "candidate": {
        "ref": "CA-D-463",
        "version": 26,
        "summary": "Give every Atom Revision one authoritative Carrier Bundle",
        "prose_claim": "Every Atom Revision **must** have **`=1`** authoritative Carrier Bundle on the Project filesystem. The bundle contains **`=1`** Markdown File Carrier and **`>=0`** additional Carriers admitted by its applicable Delivery authority.\n\nThe Markdown file carries the Atom's own Properties under CA-D-478 and CA-D-479. Additional Carriers represent that same Revision. They do not replace the mandatory file or independently redefine its Properties.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-D-463",
        "confidence": "high",
        "escalate": false,
        "reason": "The required counts and carrier roles remain: one bundle, one Markdown carrier, zero or more admitted additional carriers, and no independent Property definitions."
      },
      "final": {
        "ref": "CA-D-463",
        "version": 26,
        "summary": "Give every Atom Revision one authoritative Carrier Bundle",
        "prose_claim": "Every Atom Revision **must** have **`=1`** authoritative Carrier Bundle on the Project filesystem. The bundle contains **`=1`** Markdown File Carrier and **`>=0`** additional Carriers admitted by its applicable Delivery authority.\n\nThe Markdown file carries the Atom's own Properties under CA-D-478 and CA-D-479. Additional Carriers represent that same Revision. They do not replace the mandatory file or independently redefine its Properties.",
        "details": null,
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    },
    {
      "source_ref": "CA-M-407",
      "source_version": 14,
      "candidate": {
        "ref": "CA-M-407",
        "version": 14,
        "summary": "Allocate deterministic transformations to functions",
        "prose_claim": "Use a side-effect-free function as the default unit of PROGRAMMATIC behavior. Implement one deterministic transformation as a function **when** its result follows **only** from its declared inputs and the responsibility needs no identity across calls.",
        "details": "### Applicable when\n\nApply this policy **when** Tools, App backend services, or MCP components parse, classify, validate, plan, project, format, or otherwise transform explicit input into a result.\n\n### Procedure\n\n- Use a function **unless** the responsibility **must** own mutable state, an invariant across calls, a resource, a lifecycle, or a replaceable adapter.\n- Give the function a specific, intention-revealing verb phrase that states its one responsibility. Prefer clarity over brevity. Split a function if its accurate name requires multiple responsibilities.\n- State the function's input, result, and failure values explicitly.\n- Do **not** mutate inputs or shared state, perform I/O or logging export, or read the filesystem, process, clock, environment, network, persistence, or randomness.\n- Pass **every** required observation and setting as explicit input. Do not obtain them implicitly.\n- Group related functions in a specifically named module. Do **not** create a class only to provide a namespace.\n\n### Outcome\n\nBehavior is locally readable and reproducible from declared input, with no observable side effects. It can be reused, checked, or extended without constructing component lifecycle state.\n\n### Failure or stop\n\nStop treating the unit as a deterministic transformation **when** it applies an external effect. A bounded one-shot effect **may** remain a function under CA-M-425. Allocate an object **only** **when** identity across calls or owned state, an invariant, a resource, a lifecycle, or adapter behavior is required.\n\n### Sources\n\n- [Python Functional Programming HOWTO](https://docs.python.org/3.14/howto/functional.html)\n- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)\n- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis_and_advisory/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)",
        "semantics": null,
        "operation": null
      },
      "gate": {
        "ref": "CA-M-407",
        "confidence": "high",
        "escalate": false,
        "reason": "The candidate preserves the deterministic-function conditions, explicit-input and no-side-effect rules, and the stated exception for bounded one-shot effects."
      },
      "final": {
        "ref": "CA-M-407",
        "version": 14,
        "summary": "Allocate deterministic transformations to functions",
        "prose_claim": "Use a side-effect-free function as the default unit of PROGRAMMATIC behavior. Implement one deterministic transformation as a function **when** its result follows **only** from its declared inputs and the responsibility needs no identity across calls.",
        "details": "### Applicable when\n\nApply this policy **when** Tools, App backend services, or MCP components parse, classify, validate, plan, project, format, or otherwise transform explicit input into a result.\n\n### Procedure\n\n- Use a function **unless** the responsibility **must** own mutable state, an invariant across calls, a resource, a lifecycle, or a replaceable adapter.\n- Give the function a specific, intention-revealing verb phrase that states its one responsibility. Prefer clarity over brevity. Split a function if its accurate name requires multiple responsibilities.\n- State the function's input, result, and failure values explicitly.\n- Do **not** mutate inputs or shared state, perform I/O or logging export, or read the filesystem, process, clock, environment, network, persistence, or randomness.\n- Pass **every** required observation and setting as explicit input. Do not obtain them implicitly.\n- Group related functions in a specifically named module. Do **not** create a class only to provide a namespace.\n\n### Outcome\n\nBehavior is locally readable and reproducible from declared input, with no observable side effects. It can be reused, checked, or extended without constructing component lifecycle state.\n\n### Failure or stop\n\nStop treating the unit as a deterministic transformation **when** it applies an external effect. A bounded one-shot effect **may** remain a function under CA-M-425. Allocate an object **only** **when** identity across calls or owned state, an invariant, a resource, a lifecycle, or adapter behavior is required.\n\n### Sources\n\n- [Python Functional Programming HOWTO](https://docs.python.org/3.14/howto/functional.html)\n- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)\n- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis_and_advisory/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)",
        "semantics": null,
        "operation": null
      },
      "terra_issues": []
    }
  ]
}
```
