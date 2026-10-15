# Candidate #5 — missing R definitions

Status: supported Subjects-only migration completed: 750 Atoms. R definition gaps remain open; empty drafts do not close them. See [execution outcome](execution/outcome.md).

Updated: 2026-10-15 21:48:31 +0400.

## Boundary

- Subject migration only. Existing Summary, Substance, Scope and Details stay unchanged.
- Every primary kind, dependent property and allowed value needs defining R evidence; a mention or depends_on reference alone is insufficient.
- One R can define several related values. Inherited properties reuse their declaring R; no duplicate R is required for every descendant.
- A named instance of an admitted kind does not automatically require another type-definition R.
- Empty drafts are work items, not definitions and not proof that coverage is complete.
- These 54 unassigned draft files are staged in this review folder, not admitted into the source Atom set. Their Claims are empty, no Atom IDs or lineage are invented, and each now has its full rooted governs path. Their empty Claims still provide no definition.
- Term expansion remains excluded. Existing unplaced names are not silently migrated or deleted.

## Coverage

Primary kinds: 69 checked against 524 current Core R files. 35 covered, 9 alias mappings, 7 conflicting definitions, 18 missing or uncertain.

Own property/value declarations: 101 checked; 59 covered, 34 missing, 6 uncertain, 2 conflicting. Inherited copies are excluded. Three base Status values share one draft; the Contains Boolean property and its values share one draft.

Evidence: [primary coverage](primary-r-coverage.json), [property/value coverage](property-r-coverage.json). Covered means defining meaning is present; it does not prove new parentage or every candidate rule is already adopted.

## Missing or uncertain definitions

| Target | Finding | Empty draft |
| --- | --- | --- |
| Entity/Occurrent | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-occurrent.md) |
| Entity/Occurrent/Event | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-occurrent-event.md) |
| Entity/Occurrent/Execution | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-occurrent-execution.md) |
| Entity/Occurrent/Execution/Action Run | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-occurrent-execution-action-run.md) |
| Entity/Occurrent/Session | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-occurrent-session.md) |
| Entity/Continuant | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant.md) |
| Entity/Continuant/Object | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant-object.md) |
| Entity/Continuant/Object/Governing Configuration | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant-object-governing-configuration.md) |
| Entity/Continuant/Object/Relation | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant-object-relation.md) |
| Entity/Continuant/Actor/Type: AI Agent | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant-actor-type-ai-agent.md) |
| Entity/Continuant/History | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant-history.md) |
| Entity/Continuant/History/Revision/Type: Atom | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant-history-revision-type-atom.md) |
| Entity/Continuant/Projection/Type: Direct Relation Registry | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant-projection-type-direct-relation-registry.md) |
| Entity/Continuant/Selection | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-continuant-selection.md) |
| Entity/Carrier | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-carrier.md) |
| Entity/Carrier/File Carrier | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-carrier-file-carrier.md) |
| Entity/Carrier/Directory Carrier | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-carrier-directory-carrier.md) |
| Entity/Carrier/Database Carrier | missing_or_uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-entity-carrier-database-carrier.md) |
| Entity/Occurrent/Execution.Execution ID | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-execution-execution-id.md) |
| Entity/Continuant/Object/Atom.Enabled Relations.Contains | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-atom-enabled-relations-contains.md) |
| Entity/Continuant/Object/Atom.Governance Locus | uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-atom-governance-locus.md) |
| Entity/Continuant/Object/Atom.Property | uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-atom-property.md) |
| Entity/Continuant/Object/Atom.Semantics | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-atom-semantics.md) |
| Entity/Continuant/Object/Atom.Status | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-atom-status-allowed-values.md) |
| Entity/Continuant/Object/Project.Framework Settings.Artifact Timestamp Timezone | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-artifact-timestamp-timezone.md) |
| Entity/Continuant/Object/Project.Framework Settings.Code-Root Locators | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-code-root-locators.md) |
| Entity/Continuant/Object/Project.Framework Settings.Confidence | uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-confidence.md) |
| Entity/Continuant/Object/Project.Framework Settings.Extension Selections | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-extension-selections.md) |
| Entity/Continuant/Object/Project.Framework Settings.Framework Control-Root Locator | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-framework-control-root-locator.md) |
| Entity/Continuant/Object/Project.Framework Settings.Identifier | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-identifier.md) |
| Entity/Continuant/Object/Project.Framework Settings.Interaction | uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-interaction.md) |
| Entity/Continuant/Object/Project.Framework Settings.Parameter Resolution | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-parameter-resolution.md) |
| Entity/Continuant/Object/Project.Framework Settings.Parameter Resolution Validation | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-parameter-resolution-validation.md) |
| Entity/Continuant/Object/Project.Framework Settings.Revision Binding | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-revision-binding.md) |
| Entity/Continuant/Object/Project.Framework Settings.Tool Selections | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-project-framework-settings-tool-selections.md) |
| Entity/Continuant/Object/Project.Operator Registry | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-project-operator-registry.md) |
| Entity/Continuant/Object/Project.Settings.Identifier | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-project-settings-identifier.md) |
| Entity/Continuant/Object/Project.Settings.Revision Binding | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-project-settings-revision-binding.md) |
| Entity/Continuant/Object/Scope Unit.ID | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-scope-unit-id.md) |
| Entity/Continuant/Object/Relation.Source Reference | uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-relation-source-reference.md) |
| Entity/Continuant/Object/Relation.Target Reference | uncertain | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-relation-target-reference.md) |
| Entity/Continuant/Actor.Name | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-actor-name.md) |
| Entity/Carrier.Canonical Address | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-carrier-canonical-address.md) |
| Entity/Carrier.Canonical Address.Segment | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-carrier-canonical-address-segment.md) |
| Entity/Carrier.Format | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-carrier-format.md) |
| Entity/Carrier.ID | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-carrier-id.md) |
| Entity/Carrier.Ownership Class | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-carrier-ownership-class.md) |
| Entity/Carrier.Storage Boundary | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-carrier-storage-boundary.md) |
| Entity/Carrier/File Carrier.Extension | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-file-carrier-extension.md) |
| Entity/Carrier/File Carrier.Filename | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-file-carrier-filename.md) |
| Entity/Carrier/File Carrier.Path | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-file-carrier-path.md) |
| Entity/Carrier/Directory Carrier.Name | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-directory-carrier-name.md) |
| Entity/Carrier/Directory Carrier.Numeric Prefix | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-directory-carrier-numeric-prefix.md) |
| Entity/Carrier/Directory Carrier.Path | missing | [draft](empty-r-drafts/CA-R--CORE_META_MODEL--define-directory-carrier-path.md) |

## Existing content conflicts — not fixed by Subject migration

- CA-R-1765@20: Artifact Type admission through NARROWER_THAN is explicitly prohibited; candidate narrower type trees need alignment or clarified classification semantics.
- CA-R-1531@5: Content Role is defined as Atom Property, while candidate uses role-qualified subtype branches.
- CA-R-1342@12: Carrier definitions and classification explicitly D-only; conflicts with requested defining-R coverage for every primary entity.
- Entity/Continuant/Object/Atom/Content Role: Delivery: Defines Delivery but explicitly assigns Carrier definitions/classification to D even abstractly; conflicts with demand for defining R for every Carrier entity.
- Entity/Continuant/Object/Atom/Content Role: Plan: Plan role is defined, but common Plan R1574 still requires redundant Type Plan; candidate removed this subtype.
- Entity/Continuant/Object/Project: R1759 governs Project but prescribes a Project Scope Unit, not a definition of new sibling Object/Project. Must clarify/adopt separation.
- Entity/Continuant/History/Revision: Old Artifact/Revision means immutable governed-meaning state while Status/Updated At may change without semantic Revision. Candidate means archived Atom/history and every update versions.
- Entity/Continuant/Projection/Type: Canonical Scope Signature: Defines derived comparison value for Scope expression, not an independent Projection Artifact Type; do not silently equate value and report carrying it.
- Entity/Continuant/Projection/Type: Canonical Signature: Defines derived comparison value for Claim expression, not an independent Projection Artifact Type; do not silently equate value and report carrying it.
- Entity/Continuant/Selection/Applicable Methodology Membership Selection: Defines active RMEDO membership restriction, not general selection kind; candidate requires current eligible versions and local active/archived placement. Subject rename alone does not resolve this.
- CA-R-1412: Current base Status rule requires one Status but declares no universal allowed set. Role-specific lists cannot be broadened to Atom merely by changing Subjects.
- CA-R-1539: Exact source domain excludes inherited Draft. Existing role additions Backlog/Canceled/Done are covered separately.
- CA-R-1875: Exact source domain excludes inherited Active; Done itself is covered.
- CA-R-1608: Exact source domain uses lowercase draft/active/resolved/canceled and excludes inherited Archived.
- CA-R-1308, CA-R-1313: Current qualified domain rules prohibit a global override and qualify extensions. Candidate universal additive inheritance requires content alignment.
- CA-R-1378, CA-R-1379, CA-R-1265: Container-related R text still describes non-Atom collections despite Container Atom Subjects; no current R declares proposed Boolean capability/default. Subject-only rename cannot make non-Atoms into Atoms.
- CA-R-1577: R1576 covers Labels, but R1577 still defines separate Plan authoring Subtypes although its Subject is Label. Later content pass must resolve; no duplicate Label definition needed.
- CA-R-1342: R1342 currently places Carrier definitions/classification in D even without concrete format/location. New demand for R for every entity conflicts with that rule; report missing R without reclassifying D by Subject rename.

## Recorded Operator decisions

1. Use full rooted Subjects, for example `Entity/Continuant/Object/Atom.Status`.
2. The earlier prepare-only gate was superseded by “run the migration + drafts”. Execute supported Subject mappings while retaining the missing-definition list and empty drafts.
3. Existing Atom content migration remains separate. Empty placeholders cannot satisfy the definition gate.

## Prepared Subject map

[Subject map](subject-map.json) records the current inventory and exact candidate-backed mappings. [Candidate path index](candidate-paths.json) expands readable names to full paths.

- 983 current Core Atoms inspected; 660 distinct Subject names.
- 155 names have explicit changed mappings; 2 are unchanged.
- 503 names have no explicit candidate placement and are held unchanged.
- One current Atom, CA-C-290, has no Subjects mapping and remains separately diagnosed.

This map is preparation data, **not an executable packet**. The fresh [execution packet](execution/prepared-targets.json) pins 750 selected Atoms to their Git checkpoint. [Exclusions](execution/exclusions.json) retain 228 unchanged Atoms and five explicit holds. Execution results must establish staging and promotion; preparation alone does not.

Only exact candidate names, declared aliases and the explicitly adopted Settings/Plan bearer relocations are mapped. No arbitrary suffix or unsupported old concept is guessed into the new tree.

## Existing migration route

The existing instructed Subjects-only batch route is available in local code; no new migration engine is proposed. Preserve selected original files in a Git checkpoint, create and commit source-pinned edit drafts, archive/promote each independent Atom, stop on failure, and rebuild the graph after completion. Unrelated dirty files do not require a global clean tree.

These empty new-definition drafts are not the source-pinned edit drafts used for promotion. They must never be passed to the Subject-promotion packet.
