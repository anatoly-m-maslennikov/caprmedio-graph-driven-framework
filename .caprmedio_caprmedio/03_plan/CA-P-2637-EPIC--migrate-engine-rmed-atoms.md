---
atom_id: CA-P-2637
ref_id: CA-P-2637
role: Plan
form: Plan
label: Epic
current_scope_unit: caprmedio
claim_target_scope_unit: FRAMEWORK_ENGINE
author: Anatoly Maslennikov
status: Active
topics:
  main_subject: Subject
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
version: 10
updated_at: 2026-11-02 20:36:56 +0400
tier: 3
container:
  scope_unit: CA-SU-00
carrier_destination:
  file:
    name: CA-P-2637-EPIC--migrate-engine-rmed-atoms.md
    path: .caprmedio_caprmedio/03_plan
---
# Summary

Migrate Engine RMED Atoms

## Objective

After the Methodology migration is complete, revise the Engine Subject system
and Scope Unit structure, then migrate all Current Engine RMED Atoms,
including PROGRAMMATIC, APPS, TOOLS and the other Engine descendants.


### Engineering Subject cleanup — next prerequisite

[P2665](CA-P-2665-EPIC--refine-engineering-subject-branch.md) now owns the focused Engineering Subject cleanup across the Current RMEDO source set. It reviews Continuant, Occurrent and Aspect placement, duplicate Git Subjects and scattered Implementation topics before drafting and applying accepted corrections. Consume its checked branch and source mappings here; do not repeat the same review or treat it as completion of this Engine Epic. Broader Scope Unit revision and the remaining Engine migration stages remain pending.


### First task completed — checked source application

P2638 applied the approved Subject structure and Domain/Engineering temporal
distinction. Readback checks3,961 Current PRMEDO sources:3,886 updates with normal
predecessors and75 unchanged heads. Only the three required taxonomy/Subject
definitions and this Epic/Task's progress bodies changed; other content stayed
unchanged. R2149's operative Subject reference follows the same rename without
changing its condition.

The actual Core, project Methodology and Engine Subject projections were
regenerated with stable IDs006–008 and source counts800/411/1027. C603 is
Resolved2 with the Operator's dual Domain/Engineering decision. Pure Engineering
topics remain direct Engineering where no temporal classification was justified.
The164 noncanonical source literals retain their prior dispositions; this
structural task neither invents their meanings nor reports them migrated.

No other Engine migration stage, Scope Unit change, code, runtime, MCP, test
suite, release or Git operation was executed. Existing Drafts/Archives were not
migrated; newly created predecessor archives are the normal update history.

### Approved runtime distinction — first-task update

The Operator resolved C603: Domain and Engineering both have Continuant and
Occurrent branches. Modeled Action/Step/Workflow Runs belong to Domain/Occurrent;
technical sessions and actual tool/app runtimes belong to Engineering/Occurrent.
Technical components and carriers use Engineering/Continuant. UX remains a
Graph Node branch for MCP interface and health-page appearance, not backend code.

This supersedes the earlier temporary deferral and extends only this first
structural task. It does not start the other Engine migration stages. Abstract
Engineering policy topics may stay directly under Engineering; do not invent
temporal classifications for them. Generic Node and Node.Type move to Graph
Node and Graph Node.Type, not to Domain-specific properties.

### First task — reshape the Subject graph roots

Execute [CA-P-2638](CA-P-2637-EPIC--migrate-engine-rmed-atoms/done/01-CA-P-2638-TASK--reshape-subject-graph-roots.md)
before the remaining Engine migration stages. The Operator approved this structure:

```text
Subject
    Graph Node
        Domain
            Continuant
            Occurrent
        Engineering
        Documentation
        Product
    Graph Relation
    Graph Rule
```

Migrate the corresponding canonical prefixes in Current P/R/M/E/D/O Subjects
across the actual source set so the graph has one coherent root structure.
Update only the defining taxonomy rules needed by this approved change and
rebuild the three existing Subject projections. Keep the Product specialization
and all remaining path suffixes. Do not turn this into general content,
instance-name, Terms Graph, Scope Unit, code, tool or runtime migration.
Preserve existing Drafts and Archives; create normal predecessors for Current
updates. This explicit first task permits the bounded cross-selection prefix
change; the rest of this Epic remains Engine RMED-only and follows the order below.

### Coordinated authority cutover — accepted 2026-10-25

The Operator approved Core for reusable authority definitions and Project
Configuration for this project's application. The connected Engine Evaluation
changes belong to this later Epic, not an ancestry waiver in CA-P-1959.

Carry this bounded Methodology follow-up with the Engine consumer migration:

- Review R029's project-application placement in Project Configuration and
  R030's reusable strict-mode authority placement in Core. Keep their stable
  identities unless Summary or Content Role changes.
- Inspect the complete connected authority closure, including R037/R038,
  R1430/R833 and Core R1671/R1672. Local ownership is not content applicability.
  Preserve generic Core independence from a project-specific application;
  retain, rebind or remove links only when their actual governing meanings
  support it. Do not infer a new parent or permission from folder placement.
- Repair the Engine evaluation consumers E120/E122/E149 as part of that
  coordinated cutover. They currently target Project-root R030 as an ancestor;
  moving R030 alone to Core would make those links invalid across branches.
- Re-read all incoming and outgoing current endpoints before publication.
  Keep ancestry and numeric Tier constraints, the sole admitted Config→Core
  prerequisite, coverage and applicability intact. Add no broader waiver.
- Preserve predecessors and rebuild the affected source-derived views after
  the complete accepted cutover. Record actual effects separately from Drafts.

R029→R1430 and R030→R833 remain known present conflicts until this work is
performed. Neither is reported applied or passing by its Methodology transfer.
No source cutover, Engine change, code or runtime action is authorized by merely
recording this follow-up. Existing Methodology-first ordering remains.

This is a separate Epic from CA-P-1959. Do not start Engine migration while
Methodology is unfinished. Preserve previous applied work and existing proposals.

First review the Subject system and Scope Units. Propose their boundaries and
placement before moving or rewriting Atoms; do not infer Subjects from Roles
or folders. Do not introduce new Domain entities without the Operator.

Then execute in order:

1. Migrate Subjects under the reviewed Subject and Scope Unit model.
2. Add missing RMED Atoms.
3. Archive obsolete RMED Atoms with affected consumers accounted for.
4. Fix properties and the necessary Governing Configuration data.
5. Update Content last.

Use new Drafts and refine them in iterations. Record source application
separately from preparation. Preserve existing Drafts, Archives, protected
owners, Terms/instance-name deferrals and unrelated changes. A Current update
creates its usual predecessor archive; existing history is not migrated.

No code, tools, tests, runtime, MCP deployment or release implementation is
included. Existing C/A and Engine P instance migration are not added by this
RMED-only scope. Spec needs no named Selection: directly select Active RMED
Atoms in the specified Scope Unit.

### Deferred Scope Goal follow-up

[CA-P-2702](CA-P-2637-EPIC--migrate-engine-rmed-atoms/backlog/CA-P-2702-TASK--reconcile-deferred-engine-scope-goals.md) records the four legacy Engine Scope Goals not changed by P2701. Resolve them with this Epic’s Subject/Scope Unit revision; no new Scope Units, code or runtime change is implied.


### Published sample/authoring-method handoff — 30 October 2026

Record this source handoff and the bounded downstream consumer inventory, not
implementation work within this RMED migration Epic. P2702 remains only the
four deferred Scope Goals described above. Runtime adoption belongs to a
separately authorized PROGRAMMATIC pass, including the existing P2577/P2636
follow-up; neither this checkpoint nor the source receipt expands this Epic
to code, tests, deployment or release.

#### Source evidence and identity succession

- Completed receipt:
  `.caprmedio_tmp/p2701-sample-corrections/completed-result.json`.
  State `complete`; 104 applied rows: 20 sample successors, three
  writing-method successors and 81 reference-only updates.
  SHA-256:
  `d5bb7cd8c28819d45e05b29257e9c27fc5aba0ac1d4e3e365ba3c0449f6f7e6c`.
- Durable review:
  `.caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/sample-20-content-corrections.md`,
  SHA-256
  `af121989c4bbcc3a6c886983e647590fa8038fa4b8f463ae20bd45d954579e4a`.
  Its thin `.tsv` has SHA-256
  `761b3e5f8a18320f88d3ec1fe1c8a2d11803d0aa7da228525d633b66b3bd91c7`.
- Read-only source inspection matched all 104 Current file hashes with no
  duplicate IDs/paths and confirmed all 23 successor mappings. That verifies
  this bounded source frontier, not full graph/schema/runtime conformance.
- Preserve recovery provenance: the initial `publication-result.json`
  stopped after 25 rows with a `'status'` error at CA-C-278. The completed
  `reference-completion-result.json` supplies 79 further rows; the final
  aggregate is complete. Do not replay the stopped batch or describe the
  initial attempt as uninterrupted success.

The predecessor column is historical identity context, not a list of live
dependencies or permission for automatic runtime aliases:

| Historical predecessor | Published Current successor |
|---|---|
| CA-R-1625 | CA-R-2429 |
| CA-R-1184 | CA-R-2430 |
| CA-M-003 | CA-M-440 |
| CA-M-002 | CA-M-441 |
| CA-R-1604 | CA-R-2431 |
| CA-R-1183 | CA-R-2432 |
| CA-R-1182 | CA-R-2433 |
| CA-R-2007 | CA-R-2434 |
| CA-O-225 | CA-O-236 |
| CA-O-230 | CA-O-237 |
| CA-E-477 | CA-E-663 |
| CA-R-1803 | CA-R-2435 |
| CA-R-1490 | CA-R-2436 |
| CA-E-660 | CA-E-664 |
| CA-R-1188 | CA-R-2437 |
| CA-D-276 | CA-D-656 |
| CA-R-707 | CA-R-2438 |
| CA-R-1600 | CA-R-2439 |
| CA-R-2155 | CA-R-2440 |
| CA-E-662 | CA-E-665 |
| CA-M-111 | CA-M-442 |
| CA-M-115 | CA-M-443 |
| CA-M-301 | CA-M-444 |

Successor chains also matter: historical CA-E-210 passed through CA-E-660 to
CA-E-664; CA-E-655 passed through CA-E-662 to CA-E-665. CA-R-2440 is the
successor of the previously normalized external Project Goal CA-R-2155.
Re-resolve Current authority rather than treating an earlier handoff's
intermediate ID, version, path or digest as the latest admitted source.

The source owner reports three Methodology/project RMED views rebuilt from
1,261 Current sources. That is not the same artifact as the runtime-read
SHARED_CONTEXT frontier projection below, and is not runtime or full-suite
acceptance. This record does not overwrite or rebuild either selection.

#### Actual bounded consumer findings

The checked production/source-binding scope has direct uses of predecessor
O225/O230, D276, R1803 and M301; M002/M003 were found in migration-only scripts.
No direct active matches for the other 16 predecessors or in PROJECT_TOOLS
were found within that scan. Negative literal search is not proof about
dynamic lookups, installed images, every projection or runtime admission.

The Current implementation Workflow is CA-O-016@27, entry CA-O-231; its
review route reaches Step CA-O-237@1, which invokes Action CA-O-236@1 in
Integrated context. Observed source hashes are:

- O016@27:
  `495e046f49d8cbe1aaeb877c847230b9888b6003edafded34caa5cc716182447`.
- O237@1:
  `1e1724560d5b5960b9d9fa927d3b0e03ad2e9f7a4c1327d56a804baebae6d2f7`.
- O236@1:
  `7d62144f52ec3b507c82a2eb474d19bd62cc820cbce477b6945f0e6075e60ca2`.

The following are candidate implementation follow-ups, not completed work:

1. Workflow Orchestrator code still carries O230-to-O225 review identities.
   Under `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/`,
   inspect `selected_implementation_packet.py` (review tuples/observations),
   `shared_context_validation_sources.py` (CURRENT_ACTIONS, version profiles,
   source bindings), `shared_context_validation.py` (phase/packet validation)
   and `selected_integrated_action_outcome.py` (review postcondition).
   Dispatch/profile/resume consumers include
   `selected_integrated_dispatch_profile.py`,
   `selected_integrated_dispatch.py` and `selected_integrated_resume.py`.
   The MCP adapter `204_MCP/selected_route_workflow_profiles.py` consumes those
   profiles. Current graph admission requires a semantic/source review; merely
   adding version 27 to an allowlist or replacing two strings is not proof.
2. The runtime prompt/frontier boundary under
   `102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/IMPLEMENTATION_WORKFLOW/`
   includes `SHARED_CONTEXT/CA-O-230.prompt.md`,
   `SHARED_CONTEXT/definition_frontier.projection.json`,
   `SHARED_CONTEXT/README.md` and `implementation_actions.py`.
   Orchestrator `selected_integrated_action_contract.py` reads the frontier.
   Bound IDs, paths, versions and digests must match one admitted generation;
   do not bypass exact-source validation or infer activation from rendered views.
3. D276 remains in validator authority/field consumers:
   `201_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/registry.json`,
   `check_schema_extended.py`, `check_structure_extended.py`,
   `registry_refresh.py` and `proposed_carrier.py`.
   `201_TOOLS/GENERATE_ENTITY_GRAPH/core_entity_admission.py` also pins its
   path/digest. Review these against Current CA-D-656 and the complete
   applicable authority closure, not a filename-only replacement.
4. Under the Agentic `ACTION_PROMPTS/RMED_ATOM_REVIEW/` boundary,
   `source_bindings.json` still names D276, R1803 and M301 with old source
   pins. The corresponding users include `evaluate_properties.prompt.md`,
   `evaluate_cce.prompt.md`, `repair/propose_repair.prompt.md` and the
   associated README files. Reconcile them with D656, R2435 and M444 in the
   separately authorized consumer pass.
5. `201_TOOLS/migrations/distribute_project_principles_across_rmedo.py` and
   `reorder_project_principle_filename_segments.py` contain M002/M003.
   These are migration-only references; do not treat them as an active
   runtime dependency or run them unchanged against Current sources.

Tool paths abbreviated with `201_TOOLS/` above are relative to
`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/`. Agentic source paths are the
existing implementation paths, not instructions to move Scope Units.

#### Follow-up boundaries

Preserve deliberately frozen workflow worlds, historical projections, quoted
paths and hash-bound evidence. A versioned fixture may legitimately retain
O225/O230 or other predecessor IDs. Separate a new Current-source case from
that historical fixture rather than performing a blanket identity rewrite.
The selected-workflow binding JSONs had no direct predecessor literals in the
bounded scan; that does not establish their version/path/hash freshness.

Source publication does not authorize consumer edits, tests, an image build,
deployment or release. P2702's deferred R1186/R1601/R1602/R1606 review remains
unchanged; do not create or restore Scope Units to fit those old Goals, and do
not reactivate the separately deferred GIT/FPF Goals. No runtime implementation
or readiness is claimed by this source/backlog handoff.



### P2703 Text Writing Style and held adapter proposal — 30 October 2026

Current CA-R-2441@1 defines the Aspect `Entity/Aspect/Text Writing Style`;
it does not create another Property identity or a File Carrier. Current
CA-M-445@1 is the readable-model-name Eng Policy owned by
METHODOLOGY_SOURCES. Its applicability is authored Methodology Sources and
their applicable children: use governed readable model names, and identify
technical spellings as Carrier keys or serialization examples. It does not
authorize renaming Engine keys, values, canonical concepts or runtime schemas.

Observed Current source hashes:

- CA-R-2441@1:
  `bfa31288a296f184387554be6d107d46a833d1bf1ccfcb3c00f1abfcdab819e7`.
- CA-M-445@1:
  `036a02805d7431214aec70314b2636d8852f68f14e5140b0c536d5240fcdd612`.

The separate Engine ADAPTERS Draft is not Current and has not been edited
by this handoff. Its reviewed replacement body/header are proposal
`index: 5`, disposition `Hold`, in
`.caprmedio_tmp/p2703-review/style/handoff.json`, SHA-256
`ea5435069219844cdc913078bfc880ad064c2fd3d28bba9163314c498945f8b3`.
The unchanged shared Draft is:

`.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/007_FEATURE_GROUP_ADAPTERS/05_method/draft/text-writing-style/CA-M-draft-ADAPTERS-ENG_DECISION--normalize-metadata-key-spelling-in-file-adapters.md`

Its source hash still matches the review packet:
`f6be5f96ba6663e4e58c1a52890fc14781537f5b64384a674e4b971fd9ce33c6`.
The proposed header addresses the same Text Writing Style Aspect; the proposed
body/header must not be mistaken for an applied Draft revision or a Current
Method.

For a later Engine disposition, the candidate concerns key spelling in the
Markdown file adapter's YAML Frontmatter and the TOML adapter only:

- lowercase English letters, replace spaces with underscores, then remove
  characters outside `a-z`, `0-9` and underscore;
- require a nonempty key and reject collisions between distinct source names
  within the same destination mapping/table; do not add suffixes or aliases;
- convert declared nested keys separately, preserving nesting and values;
  do not normalize readable model names or flatten Property paths;
- retain admitted field mappings and Delivery-controlled field placement,
  encoding, quoting and syntax. A generated spelling neither creates a field
  nor authorizes renaming an existing governed field. TOML does not acquire
  Markdown's Frontmatter/Content regions.

P2703 remains Active pending Operator disposition and coordinated
Term/classification preparation. Preserve the shared Draft and re-resolve
applicable Current field mappings before any later Engine proposal/adoption.
This note does not promote the Draft, rewrite Terms, migrate keys, change
parser/schema code, or authorize deployment. This Epic's source-only scope and
P2702's separate deferred Goal review remain unchanged.


## Details

### Definition of Done

- Methodology completion is recorded before Engine migration starts.
- Engine Subjects and Scope Units are reviewed and their accepted model saved.
- All Current Engine RMED sources are accounted for as migrated, retained,
  archived or explicitly deferred; proposals are not counted as application.
- The five migration stages and affected Subject views have checked evidence.
- No code/runtime implementation is included or implied.

## Deferred Workflow repair

[CA-P-2708](CA-P-2637-EPIC--migrate-engine-rmed-atoms/backlog/CA-P-2708-TASK--align-implementation-workflow-with-current-steps.md) records the Operator-deferred alignment of implementation prompts/runtime with Current CA-O-016 Steps. This specific repair is separate from the Scope Unit cutover and does not authorize a general Engine code rewrite.
