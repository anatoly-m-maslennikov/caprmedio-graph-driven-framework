---
identity:
  atom_id: CA-A-1389
  ref_id: CA-A-1389@1-draft
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
  updated_at: '2026-11-12T15:39:42.410463+00:00'
destination:
  file:
    name: CA-A-1389@1-draft-ANALYSIS_REPORT--compare-atom-prose-rewrite-batch-a21-741425539647.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory/000_draft
---
## Summary

Compare Atom prose rewrite batch a21 741425539647

## Details

```json
[
  {
    "ref": "CA-E-500",
    "version": 28,
    "summary": "Validate Workflow scheme and Step carrier separation",
    "prose_claim": "Workflow representation; Step Carrier separation.\n\nThe Workflow representation Evaluation **must** reject a Carrier arrangement that duplicates definition authority **or** derives execution order from storage order.",
    "details": "- Require exactly one Step Kind: Input, Execution or Decision. This requirement is independent of Agentic Step Execution Context. Accept omitted Inputs and fixed parameters. Check declared outputs and passed bindings, including logical switches, against their contracts.\n- Require exactly one Workflow Claim Mermaid Scheme and at most one Step Claim Mermaid Scheme. Accept a diagram that repeats the complete self-sufficient Claim text. Reject a Claim whose text depends on the diagram for its specification. Accept a Workflow without a flow table when its text supplies the complete graph information.\n- A graph references separate Step Atoms. **Every** leaf Step RUNS **`=1`** Action **or** Workflow. A referenced Action is carried outside the entire Workflow **and** Step directory tree. A called Workflow retains its separate identity and reference. A containing Step contains **`1+`** leaf Substeps and RUNS neither an Action nor a Workflow. A leaf Step's bindings use only previous Step outputs, enclosing Workflow Run input, or values fixed by that Step. Accept two leaf Steps that reuse the same Action with different inputs **without** copying its behavior.\n- Place the Workflow Markdown Carrier beside an optional same-stem Directory Carrier containing its separate Step Markdown Carriers, **or** leave the Workflow **and** Steps separately addressable. Retain the same graph meaning.\n- Accept a Step Markdown Carrier beside its optional same-stem Directory Carrier containing its leaf Substep Markdown Carriers. Require the matching sibling Markdown Carrier for **every** Step directory. Reject a missing **or** mismatched sibling. This layout does not admit a Substep directory or another nested Step directory.\n- Retain the declared execution order when files **or** folder navigation are reordered **without** changing the graph.\n- Reject copied Step bindings in the graph, copied Action behavior in a Step, an unresolved Step reference, **or** another Workflow identity for the folder.\n- For a folder-backed Workflow, require **`=1`** sibling Workflow Markdown Carrier with the same filename stem **and** separately carried Step Atoms inside the Directory Carrier. Reject a missing **or** mismatched sibling, a second Workflow definition, an Action Atom Carrier anywhere inside the directory tree, **or** a folder that silently becomes their owning Scope Unit.\n- Reject a Step Relation, execution inheritance, **or** execution order derived from folder nesting instead of the declared graph **and** Step bindings.\n- When a Workflow **or** Step Directory Carrier moves **without** a Status-change request, retain the graph **and** carried Step and Substep Status values. Read each Step and Substep's own Status. Reject read-time inference from its parent **or** path.\n- When a Workflow **or** containing Step parent's Status changes to an admitted value, require independent single-Atom Actions for that parent **and** the latest Revision of every contained Step and Substep under CA-R-1521: a Workflow's direct Steps and their direct leaf Substeps, or a Step's direct leaf Substeps. Check each Atom's own model. Reject an invented target value **or** a multi-target Action.\n- Include Draft, Active **and** Archived transitions admitted by the selected model. Require the same requested Status for **all** contained latest Step and Substep Revisions. Leave separately placed referenced Steps **and** Actions outside the tree unchanged.\n- Retain the Workflow-to-Step-to-Substep descendants inside the parent Carrier tree, including Archived placement under CA-D-466 **and** CA-D-289. Preserve exact bytes, Version **and** Status of older archived Revisions. Reject their inclusion as cascade targets **or** their metadata rewrite. No migration of legacy `archive/` trees is implied.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-D-408",
    "version": 24,
    "summary": "Reuse framework parameter fields in Default Settings",
    "prose_claim": "Parameter values in the Default Settings TOML Carrier.\n\n**Every** parameter value in the Default Settings TOML Carrier **must** use the same registered section, field path, value type **and** allowed domain as the corresponding explicit Framework Instance Settings parameter. Do not introduce a separate defaults-field schema.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-M-284",
    "version": 31,
    "summary": "Read Engine settings through one shared boundary",
    "prose_claim": "Use one centralized Settings Reader for **every** applicable Tool, App **and** MCP component. The Reader reads the authoritative Project Settings Artifact and validates the complete input. It returns an immutable typed snapshot with the actual validated values, exact selected Project, physical source path, raw SHA-256 Digest **and** declared schema marker. The Reader **must not** query the Work Journal **or** determine logical Revision **or** currentness. The snapshot is derived. Project Settings is **not** a Projection.",
    "details": "### Scope\n\nApply **when** PROGRAMMATIC behavior depends on Project Settings.\n\n#### Procedure\n\n1. Read the authoritative Project Settings Carrier bound by CA-D-364 through the shared Reader. Do **not** infer a replacement from a legacy filename.\n2. Validate the complete carrier at the boundary **and** return structured diagnostics for invalid input.\n3. Pass the immutable snapshot explicitly **to** the consuming deterministic core **or** application service.\n4. Do **not** add component-specific parsers, default chains, environment fallbacks, semantic overrides **or** writes **to** the Reader.\n5. Make the control panel use the same Reader. Request changes **to** the authoritative Project Settings Artifact through its dedicated Doer, **not** through the Reader, its immutable snapshot **or** a Projection.\n\n#### Outcome\n\n**Every** component observes one validated settings snapshot **without** duplicating parsing **or** inventing a second control panel.\n\n#### Failure or stop\n\nStop **when** the authoritative Project Settings Carrier is missing **or** schema-invalid, mandatory physical source path **or** Digest provenance is absent, **or** a consumer would bypass **or** mutate the shared snapshot.\n\n#### Sources\n\n- [Python documentation: `tomllib`](https://docs.python.org/3.14/library/tomllib.html)\n- [Pydantic: strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)\n- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis_and_advisory/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-R-1718",
    "version": 39,
    "summary": "Preserve strict semantic distinctions",
    "prose_claim": "Independently governed meanings.\n\nIndependently governed meanings **must** remain distinct even **when** ordinary language, one Carrier, one workflow **or** one Implementation change presents them together:\n\n- An Entity is **not** its description **or** Carrier.\n- A Requirement is **not** its Method.\n- A Method is **not** its Implementation.\n- An Evaluation criterion is **not** its execution result.\n- Provenance is **not** evidence.\n- An observed fact is **not** authority for the desired state.\n\n**If** wording could resolve **to** multiple governed meanings, the intended meaning **and** its owning Type **must** be resolved **before** the Claim is admitted. This is an admission condition, **not** a definition of the recovery Action **or** Workflow.\n\nCo-location, readable presentation, automation **or** a Relation between meanings **must not** merge their identities **or** transfer their semantic force.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-O-10011",
    "version": 4,
    "summary": "Atom Lifecycle_Change Current Status",
    "prose_claim": "This Runtime Workflow accepts one exact Current Atom selector and an allowed Current `targetStatus`. The Engine binds the Project and applicable model and supplies a pinned Current tree. Attached Drafts stay outside the cascade.\n\nRun one Action per selected Atom. Enter shared Plan Backlog and reopen terminal Plans parent first. Moving a Backlog Plan to Active also activates every Current contained Task parent first. Otherwise, process descendants before the parent. To close a Plan to Done or Canceled, preserve terminal descendants and set the other Current descendants to Canceled. Each Action checks the model and source and derives the destination. The Workflow changes neither Version nor Updated At.\n\nOn success, return the saved Atom reference and confirmed effects. Report rejected fields before any write. At the first Action failure, return the failed Action, the reason, confirmed and uncertain effects, and any selected Actions left unrun.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-E-523",
    "version": 18,
    "summary": "Journal-view integrity",
    "prose_claim": "An Artifact-change view **and** a Workflow-execution view derived from the same declared Journal selection.\n\nThe Evaluation **must** assess Journal-view integrity using the following fixtures **and** result conditions.",
    "details": "This Journal-view check is independent of the aggregate storage-classification score. Truthfully declared incomplete **or** stale coverage does **not** itself fail integrity. A record of an outcome does **not** itself prove that outcome occurred.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-R-1359",
    "version": 30,
    "summary": "Define Claim Value Set",
    "prose_claim": "Claim Value Set expressions.\n\nA Claim Value Set **means** one Claim expression in the form `X: (A, B, C)`. X identifies **`=1`** Property. `(A, B, C)` identifies one finite unordered set of **`>=1`** unique canonical values allowed by X. Value order carries no authority. The complete set **must** have one authority unit **and** lifecycle: accept, replace **and** retire **all** values together as one Claim.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-M-116",
    "version": 31,
    "summary": "Derive navigation Projections from the CCE Claim",
    "prose_claim": "Navigation values derived from an Atom Claim.\n\nTo derive navigation values from an Atom Claim, the Generator **must** derive the concise human-readable Summary **when** creating the Atom. It **must** derive requested Translations directly from the Claim, **without** adding authoritative meaning. Choose wording under CA-M-294-CORE_META_MODEL-METHOD--use-simpler-words-without-losing-meaning. For an existing Atom identity, retain **and** check the Summary under CA-R-1273-CORE_META_MODEL-CORE-REQUIREMENT--keep-summary-source-faithful **and** CA-R-1464-CORE_META_MODEL-REQUIREMENT--keep-summary-fixed-for-atom-identity. Do not regenerate it as an independent Projection.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-D-354",
    "version": 18,
    "summary": "Bind Entity graph generator authority and delivery places\n\n## Scope\n\nPROJECTION_ACTIONS owns generation and optional persistence of non-authoritative graph Projections from selected source frontiers.\n\n## Claim\n\nThe Delivery Atom is governed under `.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-31_FEATURE_GROUP_SINGLE_ACTIONS/CA-SU-37_FEATURE_GROUP_PROJECTION_ACTIONS/`. The canonical executable Carrier remains at `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/GENERATE_ENTITY_GRAPH/generate_entity_graph.py`. Installed copies remain under `.caprmedio_runtime/tools` and mutable execution state remains under `.caprmedio_runtime`.\n\nPersisted non-authoritative view Projection destinations resolve from an explicit caller path or registered Project setting. They must remain beneath `.caprmedio_caprmedio/_projection/`. Reject a persistent destination outside that registered root.\n\nNative executable Implementation remains at its governed delivery place. It can supply actual-state facts without moving into _projection. Runtime technical and business Journals use their configured governed sinks. Preserve them during disposable-state cleanup.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-O-125",
    "version": 14,
    "summary": "Assess scoped Operator-choice applicability\n\n## Operation\n\nScoped Operator-choice Applicability Assessment **means** the optional read-only Action that matches supplied literal Operator input to its supported antecedent. It returns prospective choice boundaries and the still-independent choices within a caller-declared packet. An Operator or an AI Agent acting within existing permission may perform the assessment. Invoking it does **not** grant permission for any selected effect.\n\n### Inputs\n\n- Literal Operator input or annotation with actual provenance, its applicable target and prospective scope. Distinguish it from assistant reports, copied wrappers and inferred approval.\n- Exact question, proposal and alternative versions, including later explicit corrections and the current relevant source state.\n- The caller-bounded independent-choice list and its declared completeness, existing settled decisions and delegation, and current applicable Goal, Project-owned Tier 0 Atoms, authority and effective confidence requirements. Unknown antecedent or list completeness remains unknown.\n\n### Assessment\n\n1. Check existing settled decisions and complete applicable delegation before identifying a missing Operator choice. Do **not** manufacture a redundant question when existing authority already settles the allowed action. Its execution owner still validates the complete bounds.\n2. Match the literal input only to an evidence-supported antecedent and alternative. A short answer to one question does **not** settle another independent question. Preserve the actual answer and references. Do not substitute an assistant's interpretation for human provenance.\n3. Check applicability against the exact proposal, target, scope and current source/context frontier. Preserve later explicit corrections and their prospective bounds. Added benchmark, implementation or other effects are **not** covered by a research-only answer. A changed proposal or frontier does **not** inherit renewed approval. Distinguish the choice, permission, planned effect, actual effect and evidence for each.\n4. Return the supported match and its exact applicable boundaries with evidence references. Or identify missing, ambiguous, mismatched, superseded or changed applicability and the precise unresolved point. Return the still-independent unanswered choices within the declared list. Do **not** claim that all Project choices are known. If required input is unavailable or a check fails, return that limitation and any partial assessment without claiming a complete result.\n\n### Outcome and handoff\n\nThe result is an evidence-bound assessment, **not** approval or execution readiness. It identifies the assessed input and antecedent versions, applicable choice/bounds, corrections or currentness limitations, unresolved points and remaining independent choices. Reference required authoritative decision records; do **not** copy them. If the calling domain requires an absent record or prerequisite, return the absence. Do **not** fabricate it or impose Journal recording on every generic question.\n\nAn unresolved result **may** supply one consequential question for the caller. Include the relevant Concern, affected Atom, Goal, proposal/alternatives and evidence needed to understand the choice. This Action does **not** ask repeatedly, run a question loop or force another approval. The caller retains invocation, communication, persistence, permission and readiness gates.\n\n## Details\n\nReuse CA-O-007 for obtaining and recording source-correction decisions and CA-O-008 for authorized source effects. Return changed applicability to those owners; do **not** resolve it by copying or rewriting an old Journal record. Structural authorization remains CA-O-013. Priority resolution/activation and alternative selection remain CA-O-022 / CA-O-023: a matching answer does **not** resolve unknown parameters, invent a tie-break or activate a model. Warned-name acceptance remains CA-O-065, not independent naming approval by this assessment. CA-O-078 retains navigation-candidate preparation and its domain decision boundary. CA-O-118 retains coverage accounting, which a human-answer match does **not** turn into covered work or semantic correctness.\n\nConfidence is interpretation evidence, never authority. Current Operator authority and complete delegation remain governing. No result expands delegation, adopts a report, creates approval, activates priorities, mutates a target, appends or copies Journal truth, replaces or replays an effect, or authorizes rollback, automatic repair/recheck or Workflow invocation. This generic Action does **not** create a decision/history carrier, output schema or mandatory ceremony. Concrete question/report identifiers, result encoding, presentation and adapters remain caller/Project inputs. Actual effects and their proof stay with their existing owners.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  }
]
```
