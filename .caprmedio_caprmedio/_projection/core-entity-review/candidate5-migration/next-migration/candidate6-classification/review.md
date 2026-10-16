# Candidate #6 — Recalculated Subject review

Date: 2026-10-16. Status: review only; no source migration.

Eight workers classified all **511** Subjects in the saved inventory. An independent review checked cross-slice consistency; the identified classification inconsistencies were corrected. Representative source Atoms were inspected, not every occurrence.

## Results

| Disposition | Subjects | Meaning |
| --- | ---: | --- |
| Mapped | 330 | Candidate target identified; scope and source-specific checks may still be needed |
| Terms | 80 | Shared meaning belongs in Terms, not a new entity node |
| Remove | 20 | Obsolete concept/reference or dedicated rule; not whole-Atom deletion |
| Deferred | 14 | Explicitly outside current model work |
| Unresolved | 67 | 48 per-occurrence mappings and 19 later content repairs |
| Total | 511 | Every inventory index appears exactly once |

Your answers were applied to all 204 remaining review entries: **137 candidate dispositions resolved** (135 mappings and 2 removals), **48** still need per-occurrence assignment, and **19** need the later content pass. **No new Operator questions were found.** A resolved candidate is not an executable migration or a live source change.

[Complete review map](review-map.json) includes each Subject, candidate target, reason, evidence, affected source IDs and follow-up, including subsequent Operator decisions and `candidate_resolution` for the 204 reconciled entries. Use `targets` for compound or instance-qualified candidates: each keeps the kind path, specific Atom ID where needed, and source applicability. A null singular `target` does not erase those qualifications. The eight original part files and four `answer-reconciliation-*` files retain worker results; the combined map contains reviewed naming corrections.

## Highest-impact decision families

### Resolved: methodology-source ownership

Core Meta-model, Extensions and Project Configuration are the existing Scope Units. No extra source Object or named Selection is needed. Bind references to the exact Scope Unit; this is mapping work, not another representation question.

This resolves the ownership question for `Extension`, `Methodology Source`, `Methodology Source.Expansion Boundary` and `Project Configuration`, and guides Core source references.

### Resolved: Default Settings

Default Settings belongs in `project_settings.default.toml`, as specified by the Operator. Do not merge it into Framework Settings or infer a file location/rename. Per-source settings-versus-carrier mapping remains work.

### Resolved: Extension installation and metadata

Install the Extension's Atoms under `METHODOLOGY_SOURCES/002_INSTALLED_EXTENSIONS`, then regenerate Applicable Methodology. Metadata remains with the installed Scope Unit; no separate Catalog-entry entity, application-binding Atom or Settings activation/application selection is required. This later answer supersedes the earlier enabled-selection proposal. Align CA-R-1733 and conflicting activation clauses during the content pass; preserve provenance. Exact source mapping remains work.

### Resolved: project and framework names

Framework Instance is resolved: normally Project (`Entity/Continuant/Project`, as supplied by the Operator), or the appropriate Execution for an actual run. No separate Framework Instance entity. Per-source assignment remains mapping work; older Project paths must be reconciled explicitly during migration.

The project is `caprmedio`, named in Project Settings TOML. Its result is the framework `CAPRMEDIO`, named by a project-local Atom in Project Configuration. The framework-name rule is not `Project.Name` and does not belong in universal Core. Its exact project-local Subject remains mapping work; do not reopen the ownership decision.

### Resolved: execution outputs and evidence

Records of what happened during any execution—results, failures and evidence references—belong to History, not necessarily Journal. Authored analysis with rationale/conclusions is an Analysis Atom; compiled views are Projections. No new History subtype is needed now. Per-source assignment remains mapping work.

Subjects: `Evaluation Report`, `Proof Dependency Frontier`.

### Resolved: Consumer goals and producer results

These are old notation. Goals and Demands use Owning Scope Unit and Target Scope Unit; Substance states the result and Substance Scope limits applicability. No separate Consumer Goal / Producer Result entity or mandatory P objective is needed. Per-source field mapping remains work.

The later Operator answer removes the mandatory accepted-Goal connection for Demands: retire CA-R-951 and remove that clause from CA-R-933 in the content pass, preserving the single-result constraint. Goal and Demand Types and separate Scope Unit Goal-coverage rules remain.

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

Only Workflows, Steps, nested substeps and Actions are needed for operation definitions. Tool operations and prompts returned to the calling session fit that model; actual executions use existing Runs, and records belong to History. Methodology RMED does not decide whether internal tool calls become substeps or remain execution details. Remove that prescription from R1528/M304 in the later content pass without adding the opposite rule or a mandatory setting. A later MCP call by the main session is optional. Do not add an Invocation/Tool Call entity layer or infer a completion protocol.

Subjects: `Step Run/Invocation`, `Tool Call`.

### Resolved: Scope Unit hierarchy names

Use `Scope Unit.Path`, `Scope Unit.Parent` and `Scope Unit.Children`. Map Structural Path to `Entity/Continuant/Object/Scope Unit.Path`: ordered Scope Unit ancestry derived from parentage, not a filesystem path or separate primary entity. Parent and Children identify the corresponding Scope Units in the same hierarchy; do not add duplicate authored ancestry.

Subjects: `Structural Path`.

### Resolved: Method Types

Implementation Method and Implementation Decision are different Method Atom Types, inheriting Method/Atom rules. They are not a separate Implementation entity and are not collapsed into untyped Methods. R1669/R1670 map to the respective Type-qualified Local Tier; R1671/R1672 govern the respective Method Types' parent/child permissions. Types may impose strict Local Tier restrictions, including one allowed tier, but exact Type-to-tier rules are deferred. Method Policy/Core and Implementation Decision/Standard are examples, not adopted constraints. Existing source constraints remain unchanged pending separate review.

## Remaining source work

These are implementation/content tasks under accepted decisions, not unanswered model questions. Mixed source references are not blanket renames. The saved inventory remains the input snapshot; source Atoms are unchanged.

| Index | Subject | Work | Remaining action |
| ---: | --- | --- | --- |
| 8 | Agentic Step Execution Context | Per-occurrence mapping | Assign the 35 occurrences from their definition/run meaning; mixed sources may require both Subjects. Content repair remains separate. |
| 30 | Artifact | Per-occurrence mapping | Resolve each of the 68 occurrences without narrowing valid claims or replacing all Artifact uses with Object. This is source assignment under an approved policy. |
| 53 | Artifact/Revision | Per-occurrence mapping | Assign historical/current meaning per occurrence; preserve version references and do not rewrite Concern history. |
| 55 | Artifact/Revision/Status: Archived | Later content pass | Preserve applicable Atom lifecycle constraints; review the broad content before changing its scope. Do not infer Status models for other History/Projection owners. |
| 56 | Artifact/Revision/Version | Later content pass | Split the broad archive naming content from the Atom-specific version mapping during the content pass; no universal Revision.Version field. |
| 72 | Atom Change Classification | Per-occurrence mapping | Assign the RMED and Action occurrences separately, preserving the approved changed-Summary/new-ID rule. |
| 77 | Atom Collection | Later content pass | R1381/R1567 contain obsolete non-Atom collection classifications; preserve any valid grouping/tier constraint when replacing that content. |
| 80 | Atom Collection/Type: Ad Hoc | Later content pass | Retire collection-type registration content in R1546; keep its valid prohibition on Plan Labels creating independent types. No source deletion now. |
| 86 | Atom Scope | Per-occurrence mapping | Classify 31 source occurrences; remove redundant references and keep exact applicability when multiple properties are required. |
| 89 | Atom Tier Validation.Concrete Cases | Per-occurrence mapping | Retain the explicitly tested relation/settings/selection targets from its complete source; separate CAPRMEDIO-specific fixtures from reusable constraints during relocation. No new policy decision. |
| 105 | Atom/Content Role: Operations/Type: Actor | Later content pass | Separate permission policies and concrete participant bindings in D457/M314/R1564/R1565; preserve their valid content without inventing a fourth Operations kind. |
| 138 | CAPRMEDIO Framework Identity | Per-occurrence mapping | Retain R1778's framework-name applicability while encoding its concrete project-local Subject; the ownership decision is resolved. Do not fabricate a Product/Implementation root or map the requirement to the name of its own Atom. |
| 139 | CAPRMEDIO Framework Instance | Per-occurrence mapping | Assign Project or actual Run per source across ten uses, preserving context. Reconcile older Object/Project spelling explicitly. |
| 141 | CAPRMEDIO Graph | Per-occurrence mapping | Assign the 16 occurrences and preserve projection type/source selection; remove obsolete General Artifact Graph assumptions only with their disposition recorded. |
| 142 | CAPRMEDIO Graph.Connectivity | Per-occurrence mapping | R1472's typed cross-graph relations map to Relation; R1410's obsolete General Artifact Graph requirement needs later content disposition. |
| 149 | CCE Method | Per-occurrence mapping | Encode the existing CCE Method selection from Subject/scope/source identity, not a new CCE Method entity or universal Method dependency. |
| 185 | Consumer Goal | Later content pass | Remove the mandatory accepted-Goal connection: retire R951 and remove the Goal-dependency clause from R933, preserving its single-result constraint and separate Goal-coverage rules. |
| 186 | Container Atom | Later content pass | Retire old Structural Entity/non-Atom collection claims while preserving valid carrier/containment rules. Container instances map to Atom/allowed kind, not to the enablement property itself. |
| 195 | DEPENDS_ON | Per-occurrence mapping | Partition each occurrence by relation domain; preserve the Subject relation defined by CA-R-1200 and dependency ordering in CA-M-239/CA-E-404 separately. No new Object root or untyped relation. |
| 197 | Default Settings | Per-occurrence mapping | Bind the configuration and carrier to the named default file per occurrence. Do not merge into Framework Settings or invent its directory/field migration; preserve default-versus-override meaning. |
| 213 | Entity Carrier Binding | Later content pass | D505's universal per-entity Carrier property and M313's matching authoring requirement conflict with the accepted general-D policy and need the later content pass. Do not delete D257's valid inverse relation or all storage rules. |
| 229 | Extension | Per-occurrence mapping | Bind individual source references to existing extension Scope Unit identities and distinguish Term usages. Do not turn each restricted extension reference into every Scope Unit. |
| 253 | Hub Atom | Per-occurrence mapping | Classify each occurrence among container Plan, unsupported Hub-chain rule and actual navigation Projection. Preserve explicit retry-policy content for separate review; the confidence answer alone does not silently rewrite unrelated retry semantics. |
| 254 | Hub Carrier.Navigation Entry | Per-occurrence mapping | Bind the actual carrier/Projection in the exact scope before selecting its migration Subject. Plan projection admission is deferred; retain the stable-folder navigation restriction, not a new navigation entity. |
| 275 | Implementation Workflow | Per-occurrence mapping | Assign each RMED occurrence precisely and preserve CA-O-016-specific applicability. The permission rule also depends on Author and confidence, but is not another implementation entity. |
| 291 | Markdown Atom Carrier.Main Content | Per-occurrence mapping | Keep the body-after-frontmatter restriction on the Markdown Atom file carrier and exact property-specific rules on their properties. Use general D policy rather than creating another body-property hierarchy; exact list/source replacement remains occurrence work. |
| 294 | Markdown Atom Carrier.YAML Frontmatter | Per-occurrence mapping | Retain the Markdown/frontmatter applicability of general D policy, and resolve specific property references individually. D478 covers applicable Atom properties as a policy, not a requirement to register a Carrier binding for each. |
| 303 | Methodology Source | Per-occurrence mapping | Bind each occurrence to the existing source Scope Unit identity and preserve the relevant layer/extension scope. General source terminology belongs to Terms, not an unrestricted replacement with all Scope Units. |
| 305 | Methodology Source.Expansion Boundary | Per-occurrence mapping | Bind concrete source units and exact governing rule targets per occurrence; preserve permitted expansion constraints in source applicability. Relocate CAPRMEDIO-specific compilation rules to Project Configuration. |
| 306 | Methodology Source.Expansion Mapping | Per-occurrence mapping | Identify each described mapping's actual authored source carrier/Atom and retain source/target bindings. Existing content does not identify one universal mapping Object or Atom role; do not invent one merely to finish the executable map. |
| 341 | Project Boundary Position | Later content pass | Retire the dedicated R961 coordinate rule and remove only that clause from mixed R1762 during content migration; do not create a replacement boundary entity. |
| 342 | Project Configuration | Per-occurrence mapping | Bind each occurrence to the existing 003_PROJECT_CONFIGURATION Scope Unit identity; retain generic definitional meaning as Term usage when appropriate. Broad Scope Unit alone must not erase this instance restriction. |
| 343 | Project Lexicographic Selection | Per-occurrence mapping | Preserve the named admissible-alternatives selection and the O023 run restriction; comparison semantics remain in Method content/Terms. No new selector grammar. |
| 347 | Project Priority Model Application | Per-occurrence mapping | Keep affected scope/stage and Operator-selected model restrictions per occurrence; do not invent a Priority Model Application entity. Concrete CAPRMEDIO rules move to Project Configuration. |
| 351 | Project Settings/Revision Binding | Later content pass | Remove the obsolete read-admission/baseline requirement in content migration. Preserve genuine historical evidence separately only where needed; do not retain Settings.Revision Binding as a new entity. |
| 359 | Project Structure Maintenance/Step bindings | Later content pass | Keep C/A repair deferred; preserve the exact Step-binding concern and Workflow identity when its Subject is migrated. |
| 390 | Relation Kind Metadata | Per-occurrence mapping | Resolve field-specific occurrences and graph-qualified kind applicability. Keep M120's registry output identity without inventing a new Projection type or a cross-owner Metadata entity. |
| 405 | Runtime State | Per-occurrence mapping | Resolve each dependency to the storage carrier, historical record or view actually meant; remove redundant Runtime State topic links. Journal views outside current RMED projection scope remain deferred, not new roots. |
| 412 | Scope Unit Scope | Later content pass | Separate these references and preserve the governed Subject relation; repair old combined Atom Scope and Operator fallback text in content migration. |
| 420 | Selected Operations/Carrier | Later content pass | C/A stays deferred. Preserve selected IDs O007/O008/O017/O019/O021/O024/O089 and the explicitly referenced implementation Steps; do not broaden the issue to every Operation. |
| 421 | Selected Workflow Step/Agentic invocation context binding | Later content pass | Keep C/A deferred; preserve selected Step IDs CA-O-139..144, CA-O-146..151 and CA-O-152..157 and the conditional Agentic execution boundary. |
| 434 | Source Reconciliation Workflow Carrier layout | Later content pass | C/A repair remains deferred; keep both Workflow identities and the format-only concern. |
| 438 | Spec Content Roles | Per-occurrence mapping | Assign each occurrence to its existing governed RMED role/property; remove redundant Spec-topic dependencies. Do not mechanically replace all uses with all four roles. |
| 443 | Step/Agentic Execution Context | Per-occurrence mapping | Bind C426 to its O139-O144/O146-O157 Step identities and exact context property; use Step Run context only for actually supplied context. No extra Invocation kind. |
| 448 | Structural Entity Recursive Containment | Per-occurrence mapping | Bind the existing qualified CONTAINS kind and distinguish authored direct edges from their transitive closure. This does not resume construction-graph implementation. |
| 459 | Subject Relation Kind: DEPENDS_ON | Per-occurrence mapping | Use the existing canonical qualified relation-kind path during occurrence mapping; Plan Graph implementation remains deferred. |
| 469 | Tool Call | Later content pass | Remove R1528/M304 prescriptions about whether internal calls become substeps. Methodology RMED leaves this unspecified; preserve unrelated valid clauses and do not add the opposite rule or mandatory configuration. |
| 471 | Translation | Per-occurrence mapping | Map each occurrence to source content or derived output as appropriate; do not add a Translation root/type merely to retain the old name. |
| 473 | Type-Qualified Status Validation | Later content pass | Content repair must remove Activity clauses and preserve valid type-qualified inherited Status validation; no Artifact.Status or universal Status field. |
| 477 | Verification | Per-occurrence mapping | Assign per source. Keep Implementation Overview uses deferred rather than admitting that projection through this mapping; retain recorded evidence without promoting it to authority. |
| 482 | Workflow/Step binding ownership | Per-occurrence mapping | Identify referenced canonical Steps per occurrence, retain their identities, and relocate named project procedures to Project Configuration. |
| 484 | applicability | Later content pass | Use Type-qualified Local Tier targets. Strict per-Type restrictions are supported in principle; exact allowed tiers are deferred, not inferred from examples. Existing source constraints stay unchanged. |
| 486 | artifact-model | Per-occurrence mapping | Complete per-source routing; preserve each claim's applicability rather than blanket-mapping every occurrence to Atom. |
| 488 | authority | Per-occurrence mapping | Map each governing use to its actual owner and remove only redundant topic dependencies. Preserve existing permissions and source-authority distinctions. |
| 490 | continuous-improvement | Per-occurrence mapping | Resolve per-source role/operation target and relocate CAPRMEDIO-specific process policies. No new improvement entity. |
| 491 | development-flow | Per-occurrence mapping | Separate occurrence meanings using each source claim; preserve records and remove redundant topic dependencies. Mixed content repair stays separate. |
| 492 | evaluation | Per-occurrence mapping | Map per source to checked owner or concrete projection selection. Do not create a new Evaluation entity or silently widen a named catalog to all Projections. |
| 493 | extension-model | Per-occurrence mapping | Apply install → regenerate. Remove the mandatory application-binding Atom and extra activation/application selection requirements in the content pass; preserve governing constraints and provenance. |
| 494 | external-boundary | Per-occurrence mapping | Keep R1627 project-specific with its full applicability and permitted-storage constraints; map R1648's exact admitted Analysis Type where available. |
| 495 | framework-boundary | Per-occurrence mapping | Bind the named caprmedio Project instance from Project Settings; do not widen it to every Project or conflate the CAPRMEDIO framework name. |
| 497 | language | Per-occurrence mapping | Map other sources to their actual content/representation targets and remove redundant dependencies; do not blindly map all language uses to Substance. |
| 499 | lifecycle-traceability | Per-occurrence mapping | Resolve each existing relation or historical record target and drop redundant topic references; retain valid traceability claims for later content review. |
| 500 | principles | Per-occurrence mapping | Bind the exact Core Meta-model Scope Unit identity from Project Structure and preserve its implementation-neutral applicability. |
| 505 | requirement-topology | Later content pass | Use the respective Implementation Decision and Implementation Method Types. Preserve exact parent/child relation applicability; their special permissions were not removed by the Type decision. |
| 507 | scope-topology | Per-occurrence mapping | Assign remaining sources by actual claim; keep Owning/Target Scope Unit references distinct from Scope Unit hierarchy and filesystem carriers. |
| 508 | semantics | Per-occurrence mapping | Route by source and drop redundant alias/topic links; keep old content conflicts explicit instead of inventing a shared entity. |
| 509 | settings specification | Per-occurrence mapping | Assign exact settings-governing Atom selections/owners during migration; relocate project-specific rules, do not turn default Settings into Project.Framework Settings. |

## Checks and limits

- All 511 indices and exact Subject names match the saved inventory, with no duplicates or omissions.
- The three explicitly approved mappings (Confidence, Permissions and Revision) are preserved.
- No mapped target introduces Implementation or Activity, or converts a named Selection into a narrower-kind path.
- Named-Operation candidates retain their specific Atom IDs; generic kind paths are not a substitute for instance identity.
- All 204 reconciliation inputs are covered exactly once. Candidate corrections use `Entity/Continuant/Project`, `Project.Settings` and a consistent Agentic Step.Execution Context name; the actual Invocation Context payload stays distinct.
- General containment/typed parent relations are preserved. Deferring construction-graph implementation does not delete those relations.
- Classification files are review data, not an executable migration batch. Removal and mixed-source mappings need occurrence-level dispositions.
- No source Atom, current source graph, Git state or runtime was changed by this recalculation. No full test suite or full source-content audit was run.
