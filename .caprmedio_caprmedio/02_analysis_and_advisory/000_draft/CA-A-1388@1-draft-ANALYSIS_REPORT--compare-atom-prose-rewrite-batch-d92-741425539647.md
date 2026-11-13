---
identity:
  atom_id: CA-A-1388
  ref_id: CA-A-1388@1-draft
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
  updated_at: '2026-11-12T15:39:30.311822+00:00'
destination:
  file:
    name: CA-A-1388@1-draft-ANALYSIS_REPORT--compare-atom-prose-rewrite-batch-d92-741425539647.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory/000_draft
---
## Summary

Compare Atom prose rewrite batch d92 741425539647

## Details

````json
[
  {
    "ref": "CA-O-169",
    "version": 24,
    "summary": "Promote candidate and retire exact prior image\n\n## Action\n\nInstall selected Framework Methodology and refresh Project MCP **means** the final local Action that replaces the installed Framework with the exact verified `LAYER_1_FRAMEWORK_METHODOLOGY` product, installs the bound `ca` Skill, and restarts or reuses the current Project MCP for a smoke check.\n\n## Scope\n\nThe Action requires CA-O-164's current validated active sources, passing local-release tool tests under the declared validation scope (complete by default; focused only with an explicit current record), exact compiled product, and the exact verified package, runtime, `ca`, and candidate image prepared by the same Workflow. Under one installation lock it preserves protected settings and Project state, clears only replaceable installed Framework members, and copies `LAYER_1_FRAMEWORK_METHODOLOGY` as-is into `.caprmedio_caprmedio/000_CAPRMEDIO_framework/`. It then installs that same package/runtime and bound `ca` payload, and restarts or reuses the current Project MCP for the declared smoke check. First installation has no required prior image or installed package; an existing installation is preserved until its replacement is ready.\n\n## Details\n\nCommit the successful installed clear and product copy separately, staging only each transition's owned changes. These checkpoints remain separate within this Action. Other successful state-changing installation steps also retain their own scoped commit; unchanged or read-only steps record results without empty commits. A failed transition or commit stops before the next transition.\n\nThis Action considers all accumulated obsolete release-owned containers and images for the current Project, not only the immediate predecessor. Before Project-MCP startup, it may remove exactly identified stopped obsolete containers so retained old containers do not prevent startup. The existing exact-prior Project-MCP replacement path may stop and remove that prior container through its ownership checks; accumulated cleanup does not stop other running containers. After installed-package verification and successful Project-MCP startup/smoke, repeat eligible stopped-container cleanup and remove the now-unused obsolete images.\n\nDerive each exact immutable image/container identity, Project-root ownership and noncandidate status from actual release, build, launcher or start evidence and matching Docker inspection. A tag prefix or version age alone proves neither ownership nor eligibility. Preserve the exact promoted candidate, running containers outside the existing exact-prior replacement path, unrelated or other-Project resources, required protected references, and images retained by any container. Unknown ownership, unknown code identity or unavailable inspection means retain and report, including unproven orphan images. Never force-delete containers or prune globally. Record each target's ownership and code evidence, use/protection check and actual removal or retention outcome through the shared Run/Action Journal evidence. Blocked or failed cleanup is reported as pending; successful installation does not imply complete cleanup.\n\nThe Action never copies from an installed tree as source authority, broadens the active source set, creates another Workflow, pushes, opens a PR, removes unrelated Project state, or retries an uncertain effect. A failed copy, Skill installation, MCP restart/reuse, or smoke check stops with actual evidence and leaves no claim of completed installation.\n\nThe Operator-selected retention scope is this Project only, not all CAPRMEDIO images on the host. The retained image is the exact current-Version candidate admitted by this successful release, whose canonical version/build-date/digest naming was prepared after the green declared local validation scope; the complete suite remains the default and CA-O-188 public release remains full-suite. Other digests do not earn retention merely from equal fingerprints or Versions. Image removal requires inspected matching Project identity, host Project root and control root plus valid runtime schema/fingerprint; a prior container link is not image ownership. The existing exact-prior Project-MCP replacement path may stop/remove its positively owned container when its digest differs from the candidate even if fingerprints match. All other running containers remain untouched. Image cleanup requires positive exact-candidate launch and smoke verification, including first installation; otherwise skip removal and report pending. Preserve all container-referenced images and foreign/unowned resources. Actual effect completion is independent of Journal completeness; append observed facts without a Journal receipt gate.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-D-339",
    "version": 29,
    "summary": "Serialize the shared Project Journal",
    "prose_claim": "The shared Project-control Work Journal's serialization.\n\nThe shared Project Work Journal **must** serialize its ordered event Records as append-only NDJSON File Carrier segments **in** `.caprmedio_<project_name>/_journal/` **or** its registered subdirectories. These segments materialize its logical event table. They **must** remain Carriers of the same Journal, **not** separate Journals for Scope Units, Content Roles, workflows, **or** derived log views. Describing the Journal as a table does **not** replace this registered serialization **or** require a database Carrier.",
    "details": "This serialization governs the Project-control Work Journal, not every runtime technical or business Journal. Runtime Journal Delivery may use configured local or remote databases and logging sinks.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-M-439",
    "version": 4,
    "summary": "Write Term Definition Content",
    "prose_claim": "Authoring the content of a Method Atom of Type Term Definition for a reusable lexical Term.\n\n**To** write a Term Definition, the Author **must** identify **`=1`** reusable word **or** phrase as its Term. Write an explicit Claim that states its applicable meaning directly. Do **not** substitute an inventory of entity uses, agreement among Entity Definitions **or** Semantics, a generated dictionary, **or** an inferred common substring for the defining Claim.\n\nWrite Claim Scope **to** state the definition's applicability **without** introducing an alternative meaning for the same Term **or** an exception **to** canonical full-name uniqueness. When clarification is needed, write Semantics **to** explain the declared meaning, necessary distinctions, **and** its consistent composition. Do **not** make Semantics the sole carrier of a missing defining Claim. Write Details **to** record source support **and** explanatory examples **without** inventing a second authoritative meaning **or** an entity for a lexical component.\n\nExpress permitted reuse with the same Term meaning across different full canonical entity names. Distinguish the reusable Term from the complete name that identifies **`=1`** canonical entity. Outside the Term branch, a Term **must not** alone constitute the complete entity name; the Subject root `Entity` is the sole exception. Use the complete admitted expression for every other such entity. Preserve exact complete canonical names **in** **all** authored references **to** their entities. Repeated references do **not** create entities **or** naming collisions.\n\nUse the existing body headings **and** Method authoring conventions. Write only the definition content **and** its source-backed explanations. This Method **must not** allocate an entity identity, admit a Relation Type by parsing, invent a part-of-speech schema, require a lookup table **or** Projection, **or** redefine identifier lifecycle semantics from example spelling.",
    "details": "Term Definition is the dedicated Method Type for lexical meaning and requires its own admitted Type declaration; CA-R-2468's Requirement Type declaration does not establish it. This Method explains how to write definition content; separate Evaluation authority determines how to check definition well-formedness and Term usage. Authoring instructions alone do not prove implementation, source admission, or successful validation.\n\nThe lexical forms `Package`, `Eval Package` and `Runtime Package` illustrate reuse of the Term `Package`; `Scope Unit` and `Code Unit` illustrate reuse of `Unit`. They are components of separately admitted full qualified entity expressions, not complete entity names outside the Term branch. Write each component Term's meaning explicitly in its authoritative Term Definition. A component alone does not introduce another entity.\n\nThe schematic chain `Entity/Object/Continuant/Package <+ Module <+ Code Unit` connects three entities. Preserve each entity's full source-admitted qualified expression in authored references; a short displayed component alone is not its complete name. Do not replace an admitted Module expression with “component” for stylistic variation. A separately defined entity requires its own full expression and source binding. The complete chain is a structured expression, not automatically another full name or entity.\n\nFor the identifier example, write the Term `ID`'s meaning as a unique identifier used to find an entity instance. It applies across Continuant and Occurrent instances; the uniqueness boundary uses matching identifier prefixes. The contextual topic/code spellings `atom.id` and `projection.id` distinguish their respective ID Properties using that same meaning. They are not alternative complete canonical Subject names or case-folded aliases; authored Subjects use their full admitted expressions. The dot remains syntax. `CA-P-123`, `CA-P-123@1-draft`, and `CA-P-123@3` are spelling examples, not proof of lifecycle semantics. No new case-normalization or alias mechanism is specified by this example.\n\nExisting naming conflicts, missing definitions, unknown coverage, and actual validation outcomes are not resolved by authoring instructions. No automatic code identifier, path, or quoted external source rewrite is authorized.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-R-2969",
    "version": 1,
    "summary": "Declare Step.Content.Claim.Mermaid Scheme",
    "prose_claim": "Mermaid Scheme semantics: [Workflow Mermaid Scheme declaration](CA-R-2962-CORE_META_MODEL-DECLARATION--declare-workflow-content-claim-mermaid-scheme.md#semantics).",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-D-407",
    "version": 25,
    "summary": "Store Default Settings with the Core Meta-Model source",
    "prose_claim": "The authoritative TOML File Carrier of the Default Settings Artifact.\n\nThe Default Settings Artifact **must** use `caprmedio_framework_default_settings.toml` **at** the root of the CORE_META_MODEL source Scope Unit as its **`=1`** authoritative TOML File Carrier.",
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-E-626",
    "version": 14,
    "summary": "Verify independent Atom workflow effects\n\n## Scope\n\nWorkflow admission owns identity, Version/time, lifecycle and complete schema decisions. Connector calls use CA-D-625 only to verify the supplied request, source preconditions and permission and to perform the explicit mechanical operation. A connector does not choose those decisions.\n\nRequired future checks for ordered independent Atom workflows, fresh-ID Summary replacement and explicit reference handoffs.\n\n## Claim\n\nA workflow stops at its first failed Atom action, retains earlier completed actions and leaves the remaining targets untouched. All-or-nothing successful completion within one admitted Atom action remains required; there is no cross-Atom transaction. The selected Subject publication failure envelope below is not crash-atomic and does not change other Actions' safety boundaries.\n\n## Details\n\n1. Prepare ordered explicit targets A, B and C with exact ID/Version/source pins. Complete A, then make B fail validation, currentness, permission or publication. Independently observe A's retained effect, B's truthful failure/uncertainty and C's unchanged bytes with no invocation.\n2. Test successful actions and truthful no-ops without implicit rollback, widened selection or invented results. An action-local failure must honor that action's admitted restoration boundary; it cannot undo A. A claimed restoration needs observed proof.\nFor selected one-target Subject publication under CA-R-866/CA-O-030, inject caught publication/postcondition errors within the confirmed exclusive window. Require an attempt to restore the verified mutable before-frontier and remove attempt-owned history, preserving pre-existing history and accepted Journal evidence. Observed exact restoration reports a failed attempt, not update success; failed or unverified restoration is partial/unknown. Abrupt process crash or interruption may leave partial files: retain interrupted disposition and inspect actual affected current/history files and Run evidence before any separately admitted continuation. Never automatically replay an Atom effect or claim crash-atomic publication.\n\n3. Apply a wording-only Summary replacement using full Atom IDs corresponding to illustrative target 100 and successor 200. Require a fresh ID and predecessor archival; ordinary same-ID Modify fails. Completed output identifies target 100, created 200 and archived 100 with exact observed state evidence. A changed predecessor archival state is N+1; exact prior history remains at N. A fresh successor starts at its admitted initial Version.\n4. Make independent successor Create complete and predecessor Archive fail. Retain the observed created successor and report incomplete replacement; do not serialize a proposed archive as completed or erase the earlier action.\n5. Keep incoming references to 100 unchanged. Use a separate Find workflow for actual referrers and a separate Modify workflow for explicit referrer targets with their own source pins/permission. A replacement result alone cannot authorize those changes.\n6. A requested new-workflow resume/retry is explicitly deferred. Existing shared recording-only handling never authorizes replay of an Atom effect. Do not assert concurrent publication or stronger backend guarantees without separate proof.\n\n### Acceptance and failure disposition\n\nCompare independent invocation/effect ledgers and source/history observations. Retain completed actions, the first failure and unperformed remainder with currentness/permission and known/unknown effect evidence. Reject false batch atomicity, automatic reference rewriting, implicit retries and completion without actual effects/recording. These are required cases, not observed test passes or implementation claims.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-M-309",
    "version": 25,
    "summary": "Write Plan Claims with the Plan CCE Profile",
    "prose_claim": "Plan content written with the Plan CCE Role Profile.\n\nFor Work Report, write factual descriptions of the Task’s actual execution in Details. Distinguish performed work, observed results and remaining gaps. Copy the Task’s Summary.\n\nThe following intended-work profile applies to other Plan Forms.\n\n\n**to** write a Plan Claim with the Plan CCE Role Profile, the Author **must** perform **all** of:\n\n1. state the Plan's primary contribution as intended work, an intended outcome, **or** their governed composition under CA-M-306-CORE_META_MODEL-GENERAL-METHOD--author-plan-atoms.\n2. **if** the Plan has own work, identify the action, its object, intended result, Assignee, **and** applicable boundary explicitly. modality, condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators **may** qualify that intended work.\n3. **if** the Plan is supported **only** by decomposition, state its intended outcome **without** inventing own work.\n4. keep reusable procedure authority, normative product boundaries, current realization facts, **and** reusable operational behavior outside the Plan's primary contribution.\n5. write the Definition of Done as the subordinate falsifying Condition Expression under CA-M-123-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-definitions-of-done. condition, temporal, quantification, logical, predicate, restriction, **and** comparison Operators **may** occur **in** that slot **only** to determine whether the Plan remains **not** Done.\n6. keep optional Details subordinate **to** the same intended work **or** outcome; Details **must not** introduce another intended outcome **or** a second Definition of Done.",
    "details": "An action word **in** a Plan identifies intended work. It does **not** define a reusable Operations Action.",
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-O-222",
    "version": 8,
    "summary": "Append Journal change records\n\n## Scope\n\nAn authorized Project-local APPEND_CHANGE_RECORDS request containing supplied actual Journal observations.\n\n## Claim\n\nAppend Change Records **means** the reusable Action that appends supplied actual observations through the shared Project Journal library, **without** performing the recorded source/lifecycle operation **or** a Git effect.\n\n## Action\n\n1. Bind the actual authorized Project caller **and** existing Journal location inputs. Treat supplied record values as observations, **not** permission **or** proof; do **not** invent an Actor, session, time, prior event, baseline, result **or** replacement reference.\n2. Dry run changes nothing. Authorized apply appends the supplied data through the existing shared library. Each explicit append is an append, including repeated data; no prior-history, chain, schema/digest validation, canonical receipt, deduplication, retry **or** recovery prerequisite applies.\n3. Preserve existing entries as recorded **and** retain truthful I/O failure **and** any observed partial append. Do **not** automatically retry, replay a source effect, acquire a Git-effect lease, alter the index **or** create a Commit.\n\n## Details\n\nCA-R-812 **and** CA-R-1491 govern plain append/read; CA-D-009, CA-D-340 **and** CA-D-435 serialize supplied observations. Existing Journal readers return stored data **without** migration, repair **or** historical replay. The supplied source-authoring action identity is payload data, **not** silently replaced by this Action definition's ID. The appender creates no additional Workflow Run, Session **or** approval record. Source mutation, replacement correctness, permissions **and** Git effects retain their independent governing rules.",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-R-1622",
    "version": 17,
    "summary": "Implement Atom Carrier Validation **in** VALIDATE_ATOMS\n\n## Scope\n\nthe `VALIDATE_ATOMS` Tool's implementation of the Check Atoms methodology Action.\n\n## Claim\n\nthe `VALIDATE_ATOMS` Tool **must** implement **=1** methodology Action, Check Atoms under CA-O-087-CORE_META_MODEL-ACTION--check-atoms.\n\n- that Action is the sole authority for operational behavior, selection, findings, **and** result meanings; the Tool's RMED specifies its Implementation **without** copying that authority.\n- a Workflow invokes the Action through a Step; the Tool does **not** implement **or** own the Workflow graph **or** impose a Workflow on direct Action calls.\n- return the Action's results faithfully, including failed **and** incomplete assessments; do **not** add repair, promotion, archive, **or** semantic-review behavior.\n- this binding follows CA-R-1516-PROJECT_CONFIGURATION-REQUIREMENT--bind-each-tool-to-one-methodology-action **and** CA-R-1517-PROJECT_CONFIGURATION-RULE--keep-tool-operational-authority-outside-its-own-subtree. this binding **must not** declare a new Scope Unit **or** require a particular Workflow **to** build the Tool.\n- supported mechanical coverage **must** include Author membership **in** the Project's Operator registry **and** the current Content Role-specific body Property contracts. effective Plan Assignee resolution is deferred, **not** a membership check against this registry. distinguish an implemented check blocked by unavailable context from a deferred implementation; neither outcome establishes conformance.\n\n## Details",
    "prose_claim": null,
    "details": null,
    "semantics": null,
    "operation": null
  },
  {
    "ref": "CA-E-806",
    "version": 2,
    "summary": "Verify native Tool exposure eligibility",
    "prose_claim": "Only active native code configured for the bound Project is exposed. Inactive, disabled or blocked Tools, internal CONNECTORS/adapters and PROJECT_TOOLS cannot become callable through stale publication. Unrelated Atom edits or removals do not trigger a generic freshness scan.",
    "details": null,
    "semantics": null,
    "operation": null
  }
]
````