# Candidate #6 — Recalculated Subject review

Date: 2026-10-16. Status: review only; no source migration.

Eight workers classified all **511** Subjects in the saved inventory. An independent review checked cross-slice consistency; the identified classification inconsistencies were corrected. Representative source Atoms were inspected, not every occurrence.

## Source-occurrence pass — complete

All 48 previously pending source-specific families are reviewed: 546 Subject/source pairs across 441 current Atoms, covering 548 exact governs/depends_on uses. **314 map, 94 redundant-reference removals, 82 content holds, 58 C/A holds.** No new Operator questions. See the [current occurrence report](occurrence-review.md) and its six evidence files.

Mixed-status Atoms remain held as whole Atoms. These are candidate decisions, not an executable migration or source changes. The initial counts below are preserved as the earlier classification snapshot.

## Initial classification results

| Disposition | Subjects | Meaning |
| --- | ---: | --- |
| Mapped | 330 | Candidate target identified; scope and source-specific checks may still be needed |
| Terms | 80 | Shared meaning belongs in Terms, not a new entity node |
| Remove | 20 | Obsolete concept/reference or dedicated rule; not whole-Atom deletion |
| Deferred | 14 | Explicitly outside current model work |
| Unresolved | 67 | At this earlier stage: 48 per-occurrence mappings and 19 later content repairs |
| Total | 511 | Every inventory index appears exactly once |

At the answer-reconciliation stage, 204 entries became 137 resolved candidate dispositions (135 mappings and 2 removals), 48 pending per-occurrence assignments and 19 content deferrals. The occurrence pass above now supersedes the pending assignments; it does not erase their explicit content/C/A holds.

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

The 48 per-occurrence families are now reviewed in the [source-occurrence report](occurrence-review.md), with exact source IDs, roles, evidence and holds. They are no longer uninspected mapping work. No live migration has run. The following 19 families remain in the separately deferred content pass:

| Index | Subject | Work | Remaining action |
| ---: | --- | --- | --- |
| 55 | Artifact/Revision/Status: Archived | Later content pass | Preserve applicable Atom lifecycle constraints; review the broad content before changing its scope. Do not infer Status models for other History/Projection owners. |
| 56 | Artifact/Revision/Version | Later content pass | Split the broad archive naming content from the Atom-specific version mapping during the content pass; no universal Revision.Version field. |
| 77 | Atom Collection | Later content pass | R1381/R1567 contain obsolete non-Atom collection classifications; preserve any valid grouping/tier constraint when replacing that content. |
| 80 | Atom Collection/Type: Ad Hoc | Later content pass | Retire collection-type registration content in R1546; keep its valid prohibition on Plan Labels creating independent types. No source deletion now. |
| 105 | Atom/Content Role: Operations/Type: Actor | Later content pass | Separate permission policies and concrete participant bindings in D457/M314/R1564/R1565; preserve their valid content without inventing a fourth Operations kind. |
| 185 | Consumer Goal | Later content pass | Remove the mandatory accepted-Goal connection: retire R951 and remove the Goal-dependency clause from R933, preserving its single-result constraint and separate Goal-coverage rules. |
| 186 | Container Atom | Later content pass | Retire old Structural Entity/non-Atom collection claims while preserving valid carrier/containment rules. Container instances map to Atom/allowed kind, not to the enablement property itself. |
| 213 | Entity Carrier Binding | Later content pass | D505's universal per-entity Carrier property and M313's matching authoring requirement conflict with the accepted general-D policy and need the later content pass. Do not delete D257's valid inverse relation or all storage rules. |
| 341 | Project Boundary Position | Later content pass | Retire the dedicated R961 coordinate rule and remove only that clause from mixed R1762 during content migration; do not create a replacement boundary entity. |
| 351 | Project Settings/Revision Binding | Later content pass | Remove the obsolete read-admission/baseline requirement in content migration. Preserve genuine historical evidence separately only where needed; do not retain Settings.Revision Binding as a new entity. |
| 359 | Project Structure Maintenance/Step bindings | Later content pass | Keep C/A repair deferred; preserve the exact Step-binding concern and Workflow identity when its Subject is migrated. |
| 412 | Scope Unit Scope | Later content pass | Separate these references and preserve the governed Subject relation; repair old combined Atom Scope and Operator fallback text in content migration. |
| 420 | Selected Operations/Carrier | Later content pass | C/A stays deferred. Preserve selected IDs O007/O008/O017/O019/O021/O024/O089 and the explicitly referenced implementation Steps; do not broaden the issue to every Operation. |
| 421 | Selected Workflow Step/Agentic invocation context binding | Later content pass | Keep C/A deferred; preserve selected Step IDs CA-O-139..144, CA-O-146..151 and CA-O-152..157 and the conditional Agentic execution boundary. |
| 434 | Source Reconciliation Workflow Carrier layout | Later content pass | C/A repair remains deferred; keep both Workflow identities and the format-only concern. |
| 469 | Tool Call | Later content pass | Remove R1528/M304 prescriptions about whether internal calls become substeps. Methodology RMED leaves this unspecified; preserve unrelated valid clauses and do not add the opposite rule or mandatory configuration. |
| 473 | Type-Qualified Status Validation | Later content pass | Content repair must remove Activity clauses and preserve valid type-qualified inherited Status validation; no Artifact.Status or universal Status field. |
| 484 | applicability | Later content pass | Use Type-qualified Local Tier targets. Strict per-Type restrictions are supported in principle; exact allowed tiers are deferred, not inferred from examples. Existing source constraints stay unchanged. |
| 505 | requirement-topology | Later content pass | Use the respective Implementation Decision and Implementation Method Types. Preserve exact parent/child relation applicability; their special permissions were not removed by the Type decision. |

## Checks and limits

- All 511 indices and exact Subject names match the saved inventory, with no duplicates or omissions.
- The three explicitly approved mappings (Confidence, Permissions and Revision) are preserved.
- No mapped target introduces Implementation or Activity, or converts a named Selection into a narrower-kind path.
- Named-Operation candidates retain their specific Atom IDs; generic kind paths are not a substitute for instance identity.
- All 204 reconciliation inputs are covered exactly once. Candidate corrections use `Entity/Continuant/Project`, `Project.Settings` and a consistent Agentic Step.Execution Context name; the actual Invocation Context payload stays distinct.
- General containment/typed parent relations are preserved. Deferring construction-graph implementation does not delete those relations.
- Classification files are review data, not an executable migration batch. Removal and mixed-source mappings need occurrence-level dispositions.
- No source Atom, current source graph, Git state or runtime was changed by this recalculation. No full test suite or full source-content audit was run.
