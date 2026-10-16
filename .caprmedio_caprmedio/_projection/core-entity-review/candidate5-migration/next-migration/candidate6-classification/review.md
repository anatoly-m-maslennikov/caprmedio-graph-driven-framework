# Candidate #6 — Recalculated Subject review

Date: 2026-10-16. Status: review only; no source migration.

Eight workers classified all **511** Subjects in the saved inventory. An independent review checked cross-slice consistency; the identified classification inconsistencies were corrected. Representative source Atoms were inspected, not every occurrence.

## Results

| Disposition | Subjects | Meaning |
| --- | ---: | --- |
| Mapped | 194 | Candidate target identified; scope and source-specific checks may still be needed |
| Terms | 80 | Shared meaning belongs in Terms, not a new entity node |
| Remove | 18 | Obsolete concept/reference or dedicated rule; not whole-Atom deletion |
| Deferred | 14 | Explicitly outside current model work |
| Unresolved | 205 | 204 mapping-work entries and 1 entry flagging a possible Operator decision |
| Total | 511 | Every inventory index appears exactly once |

**205 unresolved does not mean 205 unanswered questions.** Most need per-source mapping, preserved instance identity, or handling of conflicting old content under already-approved decisions. After the recorded Operator decisions, 1 candidate decision entry remains: Structural Path. It remains a review finding, not automatically a required question.

[Complete review map](review-map.json) includes each Subject, candidate target, reason, evidence, affected source IDs and follow-up, including subsequent Operator decisions. The eight part files retain the original worker outputs, not later decisions.

## Highest-impact decision families

### Resolved: methodology-source ownership

Core Meta-model, Extensions and Project Configuration are the existing Scope Units. No extra source Object or named Selection is needed. Bind references to the exact Scope Unit; this is mapping work, not another representation question.

This resolves the ownership question for `Extension`, `Methodology Source`, `Methodology Source.Expansion Boundary` and `Project Configuration`, and guides Core source references.

### Resolved: Default Settings

Default Settings belongs in `project_settings.default.toml`, as specified by the Operator. Do not merge it into Framework Settings or infer a file location/rename. Per-source settings-versus-carrier mapping remains work.

### Resolved: installed-extension metadata

Extension metadata belongs to its existing Scope Unit; enabled-extension selection belongs to Project Settings. No separate `Installed Extensions Catalog Entry` entity. Exact field mapping remains work; mandatory metadata fields are not decided here.

### Resolved: project and framework names

Framework Instance is resolved: normally Project (`Entity/Continuant/Project`, as supplied by the Operator), or the appropriate Execution for an actual run. No separate Framework Instance entity. Per-source assignment remains mapping work; older Project paths must be reconciled explicitly during migration.

The project is `caprmedio`, named in Project Settings TOML. Its result is the framework `CAPRMEDIO`, named by a project-local Atom in Project Configuration. The framework-name rule is not `Project.Name` and does not belong in universal Core. Its exact project-local Subject remains mapping work; do not reopen the ownership decision.

### Resolved: execution outputs and evidence

Records of what happened during any execution—results, failures and evidence references—belong to History, not necessarily Journal. Authored analysis with rationale/conclusions is an Analysis Atom; compiled views are Projections. No new History subtype is needed now. Per-source assignment remains mapping work.

Subjects: `Evaluation Report`, `Proof Dependency Frontier`.

### Resolved: Consumer goals and producer results

These are old notation. Goals and Demands use Owning Scope Unit and Target Scope Unit; Substance states the result and Substance Scope limits applicability. No separate Consumer Goal / Producer Result entity or mandatory P objective is needed. Per-source field mapping remains work.

Subjects: `Consumer Goal`, `Producer Result`.

### Resolved: drop Exploration Mode

Drop the separate mode concept and mode-specific rules; no replacement mode or field. Existing permission rules retain the distinction between discussion and authorization. Source cleanup has not run.

Subjects: `Exploration Mode`.

### Resolved: retire Journal Revision

Retire the separate Journal snapshot/revision concept and archive CA-R-1372 during migration. Journal contains event records with their own timestamps; no replacement Journal revision or Journal.Updated At rule is needed. The existing History/Revision branch remains. Source retirement has not run.

Subjects: `Journal/Revision`.

### Resolved: defer Plan projections

Current projection work is RMED only. Defer Plan Graph mapping/type admission and implementation. Do not reopen the deferred CONTAINS graph or retire Plan Atoms, relations or governing rules through this decision.

Subjects: `Plan Graph`.

### Resolved: terminology projection name

Terms Graph is the newer name for the same terminology projection, not a separate output kind. M114's Subject maps to `Entity/Continuant/Projection/Type: Terms Graph`. Its obsolete Definition-Atom requirement stays for the later content repair using source Atoms and their Semantics. Do not add another Catalog type for this output or retire the generic Catalog type through this decision.

Subjects: `Terminology Projection Derivation`.

### Resolved: Invocation and Tool Call identity

Only Workflows, Steps, nested substeps and Actions are needed for operation definitions. Tool calls and prompts returned to the calling session fit that model; actual executions use existing Runs, and records belong to History. A later MCP call by the main session is optional. Do not add an Invocation/Tool Call entity layer or infer a completion protocol.

Subjects: `Step Run/Invocation`, `Tool Call`.

### Structural path

Is the ordered ancestry a derived Scope Unit property or a separate derived Selection/Projection?

Subjects: `Structural Path`.

## Unresolved mapping work

These entries need source-specific resolution, not renewed approval of the settled policies.

| Index | Subject | Remaining work |
| ---: | --- | --- |
| 6 | Admit Methodology Expansion Mapping | Mapping work: Retain CA-O-054 as the specific Action binding; this kind-level Subject must not replace instance identity or authorize all Actions. Resolve the exact kind-plus-instance Subject using that Atom ID; no new Core/configuration policy choice is needed. |
| 8 | Agentic Step Execution Context | Mapping work: Apply the approved owner split per occurrence across the 35 uses; mixed governing statements need separate Subjects or a bounded content split, not a new Operator policy decision. |
| 10 | Applicable Methodology Compilation | Mapping work: Create per-source replacements rather than one spelling-wide replacement; retain O011 identity and its workflow bindings. |
| 11 | Applicable Methodology Compilation Assess Step | Mapping work: Move to Project Configuration and preserve O153 identity, O011 containment and CA-O-005 invocation. Resolve the exact kind-plus-instance Subject using that Atom ID; no new Core/configuration policy choice is needed. |
| 12 | Applicable Methodology Compilation Correct Step | Mapping work: Move to Project Configuration and preserve O156 identity, O011 containment and CA-O-008 invocation. Resolve the exact kind-plus-instance Subject using that Atom ID; no new Core/configuration policy choice is needed. |
| 13 | Applicable Methodology Compilation Decide Step | Mapping work: Preserve the named Step identity and invocation/containment bindings during relocation. Resolve the exact kind-plus-instance Subject using that Atom ID; no new Core/configuration policy choice is needed. |
| 14 | Applicable Methodology Compilation Propose Step | Mapping work: Move to Project Configuration and preserve O154 identity, O011 containment and CA-O-006 invocation. Resolve the exact kind-plus-instance Subject using that Atom ID; no new Core/configuration policy choice is needed. |
| 15 | Applicable Methodology Compilation Publish Step | Mapping work: Move to Project Configuration and preserve O157 identity, O011 containment and CA-O-009 invocation. Resolve the exact kind-plus-instance Subject using that Atom ID; no new Core/configuration policy choice is needed. |
| 16 | Applicable Methodology Compilation Select Step | Mapping work: Move to Project Configuration and preserve O152 identity, O011 containment and CA-O-004 invocation. Resolve the exact kind-plus-instance Subject using that Atom ID; no new Core/configuration policy choice is needed. |
| 25 | Apply Approved Source Corrections | Mapping work: Preserve the exact O008 invocation/reference binding; kind-level Subjects must not replace a reference to that specific Action. Resolve the exact kind-plus-instance Subject using that Atom ID; no new Core/configuration policy choice is needed. |
| 26 | Apply Structural Change | Mapping work: Preserve the named O014 binding and move the definition to Project Configuration. Resolve the exact kind-plus-instance Subject using that Atom ID; no new Core/configuration policy choice is needed. |
| 27 | Approved Change Reversal | Mapping work: Preserve O131 identity and move it to Project Configuration; do not adopt its old extra execution safeguards merely by mapping the Subject. Resolve the exact kind-plus-instance Subject using that Atom ID; no new Core/configuration policy choice is needed. |
| 28 | Approved Change Reversal Step | Mapping work: Preserve O132 containment and O131 invocation; place the definition in Project Configuration. Resolve the exact kind-plus-instance Subject using that Atom ID; no new Core/configuration policy choice is needed. |
| 30 | Artifact | Mapping work: Complete the per-source owner assignment for the remaining uses. Broad cross-owner meaning rules route to their relevant Terms; unsupported generic links are removed, without deleting valid claims. |
| 36 | Artifact query and fetch execution | Mapping work: Preserve O160/O158 containment and O159 invocation in Project Configuration; actual runs remain Step Runs. Resolve the exact kind-plus-instance Subject using that Atom ID; no new Core/configuration policy choice is needed. |
| 37 | Artifact query and selected fetch | Mapping work: Retain O159 identity and its exact query semantics during relocation to Project Configuration. Resolve the exact kind-plus-instance Subject using that Atom ID; no new Core/configuration policy choice is needed. |
| 53 | Artifact/Revision | Mapping work: Assign historical versus current-source meaning per occurrence across the 74 uses. The History root decision is settled; remaining work is source-level classification, not another root question. |
| 55 | Artifact/Revision/Status: Archived | Mapping work: identify the actual supported Status owners and split this broad reference; do not invent a universal History.Revision.Status or narrow the whole claim to Atoms by guess. |
| 56 | Artifact/Revision/Version | Mapping work: separate the Atom version-number use from the broader archive naming rule before applying an owner-qualified mapping. |
| 58 | Assess Atom Update Identity | Mapping work: Split the map by source and keep the exact O067 reference; do not replace the Method/Evaluation governing thing with a generic assessment-procedure entity. |
| 59 | Assess Lineage Impact | Mapping work: Preserve O058 identity and its chosen lineage scope; move its concrete procedure to Project Configuration. Resolve the exact kind-plus-instance Subject using that Atom ID; no new Core/configuration policy choice is needed. |
| 60 | Assess Prepared Result Conformance | Mapping work: Preserve O126 identity and its caller-bound scope; relocate rather than broaden into a universal stage gate. Resolve the exact kind-plus-instance Subject using that Atom ID; no new Core/configuration policy choice is needed. |
| 61 | Assess Source Conflicts | Mapping work: Preserve the exact O005 invocation binding and move its procedure to Project Configuration; an Action-kind dependency alone does not identify O005. Resolve the exact kind-plus-instance Subject using that Atom ID; no new Core/configuration policy choice is needed. |
| 66 | Atom Carrier Validation | Mapping work: target Workflow kind plus the CA-O-080 instance; relocate the concrete Workflow and its check to Project Configuration. |
| 72 | Atom Change Classification | Mapping work: map RMED to the governed Atom/change meaning; keep CA-O-067 as a named Action instance in Project Configuration. |
| 76 | Atom Claim Projection | Mapping work: address the governed Summary and Translation outputs separately; do not map all of this rule to Projection. |
| 77 | Atom Collection | Mapping work: classify each use as named Selection, Directory Carrier, or Container Atom; remove the obsolete umbrella where no valid remap remains. |
| 78 | Atom Collection/Local Tier | Mapping work: map valid Plan/Workflow uses to their Atom Local Tier; remove only independently tiered non-Atom collection uses that cannot be remapped. |
| 80 | Atom Collection/Type: Ad Hoc | Mapping work: classify grouping occurrences as Selection or Directory Carrier where evidenced; remove only the obsolete classification with no valid remap. |
| 81 | Atom Content Authoring | Mapping work: represent the CA-O-103 Action instance and move its concrete definition to Project Configuration. |
| 86 | Atom Scope | Mapping work: assign each occurrence to Atom.Owning Scope Unit, Atom.Target Scope Unit, or Atom.Substance Scope from the source role. |
| 88 | Atom Tier Validation | Mapping work: use both Atom.Local Tier and Atom.Global Tier as governed properties, without a Validation entity. |
| 89 | Atom Tier Validation.Concrete Cases | Mapping work: map to each actual governed property/selection; move CAPRMEDIO-specific fixtures to Project Configuration. |
| 91 | Atom lifecycle/Assessment scope | Mapping work: identify its named Action/Workflow instance references; preserve this resolved historical Concern without introducing lifecycle entities. |
| 105 | Atom/Content Role: Operations/Type: Actor | Mapping work: split or remap permission-policy claims to appropriate RMED and Actor.Permissions; retain concrete participation details without an Actor Operations kind. The broad Actor permissions decision is already approved. |
| 129 | Authoritative Atom Carrier Bundle | Mapping work: use the represented Atom or Plan as the D/E Subject, preserving carrier-pair constraints in content; reconcile obsolete Revision wording separately. |
| 132 | Authorize Structural Change | Mapping work: preserve CA-O-013 identity under the Operations Action kind using admitted instance selection; relocate to Project Configuration. |
| 135 | Build Entities Graph | Mapping work: retain CA-O-133 instance identity under Operations Workflow; move concrete definition to Project Configuration. |
| 136 | Build Terms Graph | Mapping work: retain CA-O-136 instance identity under Operations Workflow; move concrete definition to Project Configuration. |
| 138 | CAPRMEDIO Framework Identity | Mapping work: place the framework-name rule in Project Configuration and determine its precise project-local Subject. Project name stays in Project Settings TOML. |
| 140 | CAPRMEDIO Framework Instance Carrier Root | Mapping work: resolve Framework Instance first, then govern that represented object/configuration rather than creating a Carrier Root entity; old directory placement needs separate content alignment. |
| 141 | CAPRMEDIO Graph | Mapping work: separate Term Graph, Projection instances/types and Relation domain properties per source; do not map every use to a new CAPRMEDIO Graph entity. |
| 142 | CAPRMEDIO Graph.Connectivity | Mapping work: map relation constraints to Relation and represented graph constraints to their Projection kinds; review obsolete General Artifact Graph assumptions separately. |
| 146 | CCE Claim and Projection Validation | Mapping work: retain separate governed targets Atom.Substance, Atom.Summary and requested Projection kinds; remove the procedure-like Subject name. |
| 149 | CCE Method | Mapping work: preserve the selected Method Atom applicability and separate the operator-registry target; generic Method kind alone would erase scope. |
| 153 | CCE Operator Registry | Mapping work: represent the derived registry output under the existing Projection branch, preserving source Atom authority; resolve its exact output type from source evidence without reopening the approved authority decision. |
| 155 | CORE_META_MODEL | Mapping work: preserve named source-set selection for Core Meta-model; distinguish this use from the abstract Core model Term. |
| 158 | Canonical Signature Derivation | Mapping work: align with the separate Atom Claim Canonical Signature mapping; do not invent a second signature hierarchy. |
| 159 | Canonical Signature Derivation Validation | Mapping work: reuse the resolved Atom Claim Canonical Signature target, dropping Validation as a separate entity. |
| 165 | Check Atoms | Mapping work: preserve CA-O-087 instance under Operations Action and relocate to Project Configuration. |
| 166 | Check Atoms Step | Mapping work: preserve CA-O-088 instance under Operations Step and relocate with its owning Workflow. |
| 182 | Construct Entities Graph Projection | Mapping work: preserve CA-O-134 instance under Operations Action; relocate to Project Configuration. |
| 183 | Construct Terms Graph Projection | Mapping work: preserve CA-O-137 instance under Operations Action; relocate to Project Configuration; old Definition Atom authority needs content correction. |
| 184 | Consumer | Mapping work: in these sources qualify the Demand Atom's Owning Scope Unit, not a new Consumer Actor or Scope Unit subtype. |
| 186 | Container Atom | Mapping work: map genuine container references to Atoms with enabled containment and retire obsolete Structural Entity collection claims only after preserving valid rules; do not map instances to the Container-enabled property. |
| 189 | Core Meta-Model | Mapping work: use Term Core Meta-model for its general meaning and preserve an admitted named source-set Selection where actual source Atoms are referenced. |
| 191 | Corrective Method Acceptance | Mapping work: preserve CA-O-090 instance under Operations Action; move to Project Configuration without duplicating its RMED rules. |
| 192 | Corrective Method Acceptance Step | Mapping work: relocate CA-O-098 to Project Configuration and preserve its instance identity under the generic Operations Step kind; replacing its Subject by the kind alone loses specificity. |
| 195 | DEPENDS_ON | Mapping work: separate Subject DEPENDS_ON from graph-qualified dependency-order depends_on per source and preserve each typed relation identity. |
| 203 | Dependency Order Derivation | Mapping work: map M/E to the derived ordered view and O017 to its concrete Action instance in Project Configuration; preserve explicit dependency-edge semantics. |
| 204 | Dependency Order Derivation Evaluation | Mapping work: reuse the output-side mapping for Dependency Order Derivation after separating it from O017; do not map the evaluated order to the Action definition. |
| 212 | Entities Graph Construction Step | Mapping work: express the CA-O-135 instance under Operations/Type: Step rather than replacing its named Subject by the generic Step kind alone. |
| 213 | Entity Carrier Binding | Mapping work: map Delivery-role content to Delivery, map actual storage rules to their stored thing, and retire the obsolete universal per-entity Carrier-binding property; inspect D257 rather than deleting the whole group. |
| 217 | Evaluate RMED Review Batch | Mapping work: relocate and retain the CA-O-106 Action instance under the generic Operations Action kind. |
| 220 | Evaluation Implementation | Mapping work: retain CA-O-018 as an Action instance in Project Configuration; do not create Object/Implementation or classify test preparation as a passing execution. |
| 221 | Evaluation Implementation Step | Mapping work: retain the CA-O-092 Step instance in Project Configuration and its Action reference. |
| 223 | Evaluator Evidence Calibration | Mapping work: relocate the CA-O-123 Action instance to Project Configuration and keep its evidence-calibration applicability. |
| 224 | Event/Type | Mapping work: place record classification in the Journal model and inspect D340; do not map mechanically to Entity/Occurrent/Event/Type. |
| 230 | Extension Installation | Mapping work: map the R to the Extension's resulting availability/selection under the decided representation; no Installation entity is needed. |
| 234 | Find and Fetch Artifacts | Mapping work: relocate CA-O-158 to Project Configuration under the generic Workflow kind while preserving instance identity and its O160 Step. |
| 235 | Find and Fetch Journal Events | Mapping work: relocate CA-O-161 to Project Configuration and retain its Workflow instance identity and O163 Step. |
| 236 | Find and Fetch Journal Events Query Step | Mapping work: retain the CA-O-163 Step instance in Project Configuration with its inputs and Action reference, rather than introducing a Query Step subtype. |
| 245 | Generator | Mapping work: map M114 to Terms Graph/terminology projection and M120 to Projection/Type: Direct Relation Registry; replace the obsolete mandatory Definition Atom compilation model in content later. |
| 251 | Graph Projection construction/Completion | Mapping work: bind the Concern to the named project operation instances it discusses; do not rewrite it as a generic Projection property or claim the runtime builder was tested. |
| 253 | Hub Atom | Mapping work: map Plan-container uses to Plan with Contains enabled, remove the extra Hub threshold precedence layer, and inspect navigation uses for Hub Projection rather than Hub Atom. |
| 254 | Hub Carrier.Navigation Entry | Mapping work: inspect the actual Hub carrier model and select Hub Projection or Directory Carrier as the governed thing; preserve stable-child-folder navigation constraints. |
| 260 | Implementation Evaluation | Mapping work: preserve the named instance in an exact supported Subject/scope expression and relocate it to Project Configuration; no new model decision is needed. |
| 261 | Implementation Evaluation Step | Mapping work: preserve the named instance in an exact supported Subject/scope expression and relocate it to Project Configuration; no new model decision is needed. |
| 262 | Implementation Failure Diagnosis | Mapping work: preserve the named instance in an exact supported Subject/scope expression and relocate it to Project Configuration; no new model decision is needed. |
| 263 | Implementation Failure Diagnosis Step | Mapping work: preserve the named instance in an exact supported Subject/scope expression and relocate it to Project Configuration; no new model decision is needed. |
| 266 | Implementation Preparation | Mapping work: preserve the named instance in an exact supported Subject/scope expression and relocate it to Project Configuration; no new model decision is needed. |
| 267 | Implementation Preparation Step | Mapping work: preserve the named instance in an exact supported Subject/scope expression and relocate it to Project Configuration; no new model decision is needed. |
| 270 | Implementation Repair | Mapping work: preserve the named instance in an exact supported Subject/scope expression and relocate it to Project Configuration; no new model decision is needed. |
| 271 | Implementation Repair Step | Mapping work: preserve the named instance in an exact supported Subject/scope expression and relocate it to Project Configuration; no new model decision is needed. |
| 272 | Implementation Retry Control | Mapping work: Map O definition references to the named Action; inspect R1488/E441/E473 uses for the actual retry property or governed Workflow. |
| 273 | Implementation Retry Control Step | Mapping work: preserve the named instance in an exact supported Subject/scope expression and relocate it to Project Configuration; no new model decision is needed. |
| 275 | Implementation Workflow | Mapping work: Preserve O016 as a concrete Workflow; split RMED references to their governed thing rather than blanket replacing every use by generic Workflow. |
| 279 | Journal Event query | Mapping work: preserve the named instance in an exact supported Subject/scope expression and relocate it to Project Configuration; no new model decision is needed. |
| 282 | Legacy Evidence and Provisional RMED Preparation | Mapping work: preserve the named instance in an exact supported Subject/scope expression and relocate it to Project Configuration; no new model decision is needed. |
| 283 | Lifecycle Tool authority/Scope Unit | Mapping work: Read C419 to distinguish the Tool's owning Scope Unit from its allowed authority; remove unsupported topic linkage rather than guess. |
| 284 | Lineage Impact Analysis | Mapping work: Keep the report under Analysis Atom applicability; distinguish the actual assessment Action. Review R1432/R1497/R1633 before one shared target. |
| 291 | Markdown Atom Carrier.Main Content | Mapping work: Map uses per source to the actual body property, or retain a carrier-content property if the rule truly governs the whole body. |
| 294 | Markdown Atom Carrier.YAML Frontmatter | Mapping work: Map property-specific uses to their Atom properties; decide one carrier-section target for genuinely general frontmatter rules rather than inventing a property hierarchy. |
| 296 | Materialized Representation | Mapping work: Split per-source meaning between Projection and Carrier; preserve exact regeneration/source-binding applicability. |
| 299 | Method Learning Workflow | Mapping work: preserve the named instance in an exact supported Subject/scope expression and relocate it to Project Configuration; no new model decision is needed. |
| 300 | Method Lesson Drafting | Mapping work: preserve the named instance in an exact supported Subject/scope expression and relocate it to Project Configuration; no new model decision is needed. |
| 301 | Method Lesson Drafting Step | Mapping work: preserve the named instance in an exact supported Subject/scope expression and relocate it to Project Configuration; no new model decision is needed. |
| 306 | Methodology Source.Expansion Mapping | Mapping work: Inspect E249/M298/O054 and distinguish a mapping result from the admission Action; no blanket new entity. |
| 307 | Migrate Atom CCE Representation | Mapping work: preserve the named instance in an exact supported Subject/scope expression and relocate it to Project Configuration; no new model decision is needed. |
| 309 | Navigation Projection Derivation | Mapping work: Split governed targets into Atom.Summary and Projection or retain an explicitly bounded compound target; do not force both to one thing. |
| 315 | Normative Authority Relation Pair | Mapping work: Represent both typed relations or direct child_of with inverse semantics in scope/content; choose per-source expression without dropping the inverse. |
| 317 | Obtain Source Correction Decision | Mapping work: preserve the named instance in an exact supported Subject/scope expression and relocate it to Project Configuration; no new model decision is needed. |
| 320 | Persist Atom Replacement | Mapping work: relocate CA-O-051 to Project Configuration and preserve its Action instance identity; generic Action alone is insufficient. |
| 324 | Plan Atom Carrier.Stem | Mapping work: use Plan for its shared Delivery rule, or split file/directory filename references by source; do not invent a Carrier Bundle kind. |
| 332 | Prepare Structural Change | Mapping work: relocate the Action to Project Configuration and bind references to CA-O-012, retaining the generic Action kind. |
| 338 | Producer Result.Flow Direction | Mapping work: after resolving Producer Result, govern the evidenced directed relation or Demand's owner/target pair, not an invented Flow Direction root. |
| 341 | Project Boundary Position | Mapping work: remove the obsolete bootstrap coordinate under the already approved retirement; retain or precisely remap any real project-membership claim after inspecting its remaining applicability. Do not reopen bootstrap-seed retirement. |
| 343 | Project Lexicographic Selection | Mapping work: keep comparison meaning in Terms, map the O reference to its named Action instance, and qualify the governed selection/result for RMED. |
| 345 | Project Normative Authority Graph | Mapping work: express this as a named Selection of governing authority relations, retaining its acyclicity requirement; check E481's exact selection before final target. |
| 347 | Project Priority Model Application | Mapping work: separate priority-model meaning from named Action definitions and actual Action Run results; retain project-specific rules in Project Configuration. |
| 351 | Project Settings/Revision Binding | Mapping work: separate retained historical revision links from obsolete read-admission checks; do not blindly keep Project.Settings.Revision Binding. |
| 352 | Project Structure Maintenance | Mapping work: map RMED to Project.Structure, preserve CA-O-015 as a concrete Workflow instance in Project Configuration, and map actual runs separately. |
| 353 | Project Structure Maintenance Application Step | Mapping work: relocate CA-O-143 to Project Configuration, preserving Step kind, instance ID and bindings. |
| 354 | Project Structure Maintenance Authorization Step | Mapping work: relocate CA-O-142 to Project Configuration, preserving Step kind, instance ID and bindings. |
| 355 | Project Structure Maintenance Candidate Assessment Step | Mapping work: relocate CA-O-141 to Project Configuration, preserving Step kind, instance ID and bindings. |
| 356 | Project Structure Maintenance Preparation Step | Mapping work: relocate CA-O-140 to Project Configuration, preserving Step kind, instance ID and bindings. |
| 357 | Project Structure Maintenance Result Assessment Step | Mapping work: relocate CA-O-144 to Project Configuration, preserving Step kind, instance ID and bindings. |
| 358 | Project Structure Maintenance Selection Step | Mapping work: relocate CA-O-139 to Project Configuration, preserving Step kind, instance ID and bindings. |
| 359 | Project Structure Maintenance/Step bindings | Mapping work: preserve CA-O-015 and its exact Step binding applicability; C/A content remains outside the migration repair scope. |
| 365 | Projection Rebuild | Mapping work: separate Action Run, terminal Event and Journal record applicability without inventing a Rebuild entity or equating the event with its record. |
| 370 | Propose Source Corrections | Mapping work: relocate to Project Configuration and preserve Action instance CA-O-006 in referring bindings. |
| 372 | Publish Reconciled Projection | Mapping work: relocate to Project Configuration and preserve Action instance CA-O-009 and its publication target. |
| 373 | RMED Atom Review Check Coverage Gate Step | Mapping work: preserve Step instance CA-O-120 and stage=check under Project Configuration. |
| 374 | RMED Atom Review Coverage Gate Action | Mapping work: preserve Action instance CA-O-118 in Project Configuration; do not duplicate it per Step. |
| 375 | RMED Atom Review Fix Coverage Gate Step | Mapping work: preserve Step instance CA-O-121 and stage=fix under Project Configuration. |
| 376 | RMED Atom Review Gather Coverage Gate Step | Mapping work: preserve Step instance CA-O-119 and stage=gather under Project Configuration. |
| 377 | RMED Atom Review Workflow | Mapping work: preserve Workflow instance CA-O-104 in Project Configuration; generic Workflow kind is not enough. |
| 378 | RMED Review Evaluation Step | Mapping work: preserve Step instance CA-O-109 and required context in Project Configuration. |
| 379 | RMED Review Repair Step | Mapping work: preserve Step instance CA-O-110 and required context in Project Configuration. |
| 380 | RMED Review Selection Step | Mapping work: preserve Step instance CA-O-108 and required context in Project Configuration. |
| 381 | RMEDO Conflict Resolution | Mapping work: preserve Workflow instance CA-O-028 in Project Configuration; map Evaluation to the affected Atom authority or selected run outcome rather than an invented procedure entity. |
| 383 | Reconcile Atom Properties and Addresses | Mapping work: preserve Action instance CA-O-077 in Project Configuration and its governed Atom/carrier targets. |
| 384 | Reconcile Navigation Numbers | Mapping work: O078 targets its own named Action; E510 governs navigation-migration results. Resolve the result versus Scope Unit.Navigational Order Number target per occurrence. |
| 385 | Reconcile Unfinished Work | Mapping work: Preserve the named Operation ID under its generic Operations kind in Project Configuration. The pseudocode instance target is not yet an executable full Subject grammar. |
| 390 | Relation Kind Metadata | Mapping work: Map each governed field where evidenced; decide whether any remaining bundle is only a named Selection. |
| 395 | Relational Atom/Type | Mapping work: Use the exact role-qualified types per source, or a named Selection of those kinds where the rule applies to the set. |
| 396 | Repair RMED Review Batch | Mapping work: Preserve the named Operation ID under its generic Operations kind in Project Configuration. The pseudocode instance target is not yet an executable full Subject grammar. |
| 399 | Requirement Implementation | Mapping work: Rehome the named Operation in Project Configuration and express its kind plus Atom ID without inventing a new executable instance grammar. The implementation entity deferral does not defer this named Operation. |
| 400 | Requirement Implementation Step | Mapping work: Rehome the named Operation in Project Configuration and express its kind plus Atom ID without inventing a new executable instance grammar. The implementation entity deferral does not defer this named Operation. |
| 401 | Resolve Operator Priorities | Mapping work: Map O references to atom CA-O-022; determine the exact priority model/result Subject for E207. |
| 402 | Resolve Project Initialization Inputs | Mapping work: Preserve the named Operation ID under its generic Operations kind in Project Configuration. The pseudocode instance target is not yet an executable full Subject grammar. |
| 403 | Revert Changes Workflow | Mapping work: Preserve the named Operation ID under its generic Operations kind in Project Configuration. The pseudocode instance target is not yet an executable full Subject grammar. |
| 405 | Runtime State | Mapping work: Distinguish stored checkpoints/caches from live execution and Journal records; select exact targets per source. |
| 410 | Scope Reference Validation | Mapping work: Inspect E240 to choose Atom.Owning Scope Unit, Atom.Target Scope Unit, or another precise reference; do not blanket-map. |
| 412 | Scope Unit Scope | Mapping work: Separate Owning Scope Unit from Substance Scope; do not treat the old combined Scope Unit Scope phrase as one property. |
| 414 | Scoped Operator-choice Applicability | Mapping work: Preserve the named Operation ID under its generic Operations kind in Project Configuration. The pseudocode instance target is not yet an executable full Subject grammar. |
| 415 | Screen Short Names | Mapping work: Preserve the named Operation ID under its generic Operations kind in Project Configuration. The pseudocode instance target is not yet an executable full Subject grammar. |
| 417 | Select Priority-Governed Alternative | Mapping work: O023 may use its instance; E207 must govern the selected alternative/result, not the procedure name. |
| 418 | Select RMED Review Batch | Mapping work: Preserve the named Operation ID under its generic Operations kind in Project Configuration. The pseudocode instance target is not yet an executable full Subject grammar. |
| 419 | Select Reconciliation Sources | Mapping work: Preserve the named Operation ID under its generic Operations kind in Project Configuration. The pseudocode instance target is not yet an executable full Subject grammar. |
| 420 | Selected Operations/Carrier | Mapping work: Inspect C415 to identify named Selection and carrier concern; do not collapse it into all Operations or Carrier. |
| 421 | Selected Workflow Step/Agentic invocation context binding | Mapping work: Preserve the selected Step identities and their required context-binding responsibility under Agentic Step.Context; use Step Run.Context only for separately evidenced actual supplied context. |
| 422 | Session-State Envelope | Mapping work: Is this the actual Session.Context or a persistent context package? Resolve without creating a new primary root. |
| 427 | Source Reconciliation | Mapping work: Preserve the named Operation ID under its generic Operations kind in Project Configuration. The pseudocode instance target is not yet an executable full Subject grammar. |
| 428 | Source Reconciliation Assessment Step | Mapping work: Preserve the named Operation ID under its generic Operations kind in Project Configuration. The pseudocode instance target is not yet an executable full Subject grammar. |
| 429 | Source Reconciliation Correction Step | Mapping work: Preserve the named Operation ID under its generic Operations kind in Project Configuration. The pseudocode instance target is not yet an executable full Subject grammar. |
| 430 | Source Reconciliation Decision Step | Mapping work: Preserve the named Operation ID under its generic Operations kind in Project Configuration. The pseudocode instance target is not yet an executable full Subject grammar. |
| 431 | Source Reconciliation Proposal Step | Mapping work: Preserve the named Operation ID under its generic Operations kind in Project Configuration. The pseudocode instance target is not yet an executable full Subject grammar. |
| 432 | Source Reconciliation Publication Step | Mapping work: Preserve the named Operation ID under its generic Operations kind in Project Configuration. The pseudocode instance target is not yet an executable full Subject grammar. |
| 433 | Source Reconciliation Selection Step | Mapping work: Preserve the named Operation ID under its generic Operations kind in Project Configuration. The pseudocode instance target is not yet an executable full Subject grammar. |
| 434 | Source Reconciliation Workflow Carrier layout | Mapping work: Inspect C350; proposed target atom CA-O-010, preserve carrier-layout issue without inventing a carrier property. |
| 435 | Source Reconciliation/Step bindings | Mapping work: Inspect C417 to select the affected Step instances/binding property, not blanket-map to Workflow. |
| 436 | Source verification evidence | Mapping work: Inspect C421 and distinguish the actual evidence artifact from required evidence. |
| 438 | Spec Content Roles | Mapping work: Per source: use Term Spec for shared meaning, exact RMED role paths for rules, or a Selection only for an actual set. |
| 443 | Step/Agentic Execution Context | Mapping work: Map required context to Agentic Step.Context and supplied context to Step Run.Context per occurrence; C426 also requires inspection. |
| 448 | Structural Entity Recursive Containment | Mapping work: map to the agreed CONTAINS relation authority after separating direct and transitive meaning; do not invent a new relation-kind path. |
| 450 | Structural Parent Relation | Mapping work: resolve the existing parent relation kind and its exact qualified path; preserve parentage rather than replacing with containment or a new property. |
| 459 | Subject Relation Kind: DEPENDS_ON | Mapping work: use the canonical qualified DEPENDS_ON relation-kind path consistent with the relation lane; do not reduce it to generic Relation or invent grammar. |
| 467 | Terms Graph Construction Step | Mapping work: relocate CA-O-138 to Project Configuration and encode its named instance applicability under Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step; generic Step alone loses identity. |
| 470 | Tool/Workflow Operations/Atom Lifecycle/Request Parameters | Mapping work: bind the dependency to its actual lifecycle operation and parameter contract; the name alone cannot identify which Action/Workflow owns it. |
| 471 | Translation | Mapping work: inspect M116/E241 with R1274 to distinguish translated Atom content from a derived Projection; no independent Translation Object invented. |
| 473 | Type-Qualified Status Validation | Mapping work: remove Activity-specific clauses, retain applicable owner-qualified Status checks, and split or route cross-owner Status meaning to Terms; do not invent Artifact.Status. |
| 477 | Verification | Mapping work: inspect each use to separate verification criteria, a real assessment execution, and the resulting judgment/record. |
| 482 | Workflow/Step binding ownership | Mapping work: inspect C425's issue to identify its precise binding owner; do not replace with all Workflow definitions. |
| 484 | applicability | Mapping work: target Method.Local Tier for R1669; resolve the old implementation_decision classification for R1670 before selecting its qualified Local Tier. No generic applicability entity. |
| 486 | artifact-model | Mapping work: replace each governing occurrence with its evidenced role/type/Atom target; drop only redundant dependencies. No blanket topic node. |
| 488 | authority | Mapping work: remove redundant dependencies and route source-specific authority rules to their exact owner; shared meaning belongs to Terms. |
| 490 | continuous-improvement | Mapping work: map each source to its actual role, Plan, Concern or Operation target and relocate project-specific policies; no new process root. |
| 491 | development-flow | Mapping work: classify individual source claims as Terms, role-specific governed targets or Journal records; split mixed rules only when needed. |
| 492 | evaluation | Mapping work: map each E/R to its checked or required thing; retain the R1647 concrete Catalog selection rather than all Evaluation Atoms. |
| 493 | extension-model | Mapping work: inspect per-source Extension and binding identity; relocate CAPRMEDIO-specific policies, keeping Settings activation separate. |
| 494 | external-boundary | Mapping work: keep the secret policy in Project Configuration; identify its governed content or Terms scope and inspect R1648 separately. |
| 495 | framework-boundary | Mapping work: relocate to Project Configuration and target the named CAPRMEDIO Project, not every Project or a new Framework Boundary entity. |
| 497 | language | Mapping work: use Atom.Substance for claim-readability rules and precise representation/Terms targets for other sources. |
| 499 | lifecycle-traceability | Mapping work: route individual rules to Relation, Journal.Record or exact governed property; do not invent a cross-owner traceability property. |
| 500 | principles | Mapping work: use the Core Meta-model target adopted by Candidate #6 boundary definitions; do not invent a Principles entity or silently use all Objects. |
| 501 | project-containment graph | Mapping work: retire R834's obsolete partition claim as approved; inspect R836 for remapping before removing its useful constraints. |
| 505 | requirement-topology | Mapping work: inspect R1672 and resolve old Implementation Decision classification; defer genuinely Implementation-related uses rather than deleting valid M policies. |
| 507 | scope-topology | Mapping work: use Scope Unit or its precise property/relation per governing claim and drop redundant topic dependencies. |
| 508 | semantics | Mapping work: route shared meanings to Terms, exact owner-specific constraints to their targets, and remove redundant dependencies. |
| 509 | settings specification | Mapping work: retain Local Tier constraints on concrete configuration specifications, relocate project-specific rules, and avoid inventing ownerless Settings. |

## Checks and limits

- All 511 indices and exact Subject names match the saved inventory, with no duplicates or omissions.
- The three explicitly approved mappings (Confidence, Permissions and Revision) are preserved.
- No mapped target introduces Implementation or Activity, or converts a named Selection into a narrower-kind path.
- Proposed named-Operation mappings retain their instance-specific work rather than silently broadening the rule to every Action or Step.
- Classification files are review data, not an executable migration batch. Removal and mixed-source mappings need occurrence-level dispositions.
- No source Atom, current source graph, Git state or runtime was changed by this recalculation. No full test suite or full source-content audit was run.
