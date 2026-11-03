---
atom_id: CA-P-2694
label: Epic
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
tier: 3
version: 52
updated_at: 2026-11-04 00:31:42 +0400
subjects:
  active: CAPRMEDIO_MODEL
relations: {}
role: Plan
form: Plan
carrier_destination:
  file:
    name: CA-P-2694@52-EPIC--entity-graph-refactor-stage-4-polishing.md
    path: .caprmedio_caprmedio/03_plan/archive
---
## Summary

Entity graph refactor stage 4 — polishing

## Objective

Complete declaration-based Scope Unit authority and the latest MODEL/CFEL content, alias and counterpart changes.

## Details

- Remove the five obsolete authority-mode overrides.
- Promote 44 Declaration Atoms and the shared ordering, Project and identity model. Preserve source history; merge existing model Definitions rather than create duplicates.
- Non-root units have stable IDs. The Project root has no Scope Unit ID; it is Unordered and has no order.number.
- Move and rename existing Authority and Delivery folders to the derived names. Derive Authority and Delivery folder names. Only non-root Authority names include the Scope Unit ID; Project Authority remains .caprmedio_<project name>.
- Retire project_structure.toml as a concept, source file and executable dependency: governing Atoms, readers, row writers, file-only bindings, fixtures and documentation.
- Use Declaration Atoms directly. Do not retain a fallback, generated compatibility TOML or second authored registry.
- Keep existing Scope Unit workflow definitions unchanged. Remove their TOML-specific implementation and executable bindings; do not build replacement Scope Unit tools in this Epic.
- Preserve existing business operations through admitted Atom lifecycle behavior. Do not invent new APIs, approval systems, locks or business rules.

## New MODEL follow-up — 2026-11-03

The latest Operator decisions add an explicit YAML/Markdown grouping, an empty Claim container with Formal Claim and Prose Claim children, removal of Claim Scope, symbolic aliases, minimal declared relation counterparts, and declaration-based heading interpretation. `Node.**` covers all Properties of Node and its branch.

Completed next task: [CA-P-2709 — simplify MODEL and STRUCTURE Subject roots](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/13-CA-P-2709-TASK--simplify-model-and-structure-subject-roots.md). Apply `CAPRMEDIO <+ MODEL` → `CAPRMEDIO_MODEL` and `CAPRMEDIO <+ STRUCTURE` → `CAPRMEDIO_STRUCTURE` in `subjects.active` and `subjects.passive` only, with a simple in-place script. Verified 1,178 source files and 3,685 Subject values, with every other source byte preserved. The four follow-up stages below have been executed and checked for the selected frontier.

Execute in this order:

1. Update/create the Declarations and reconcile the affected authoring/layout rules.
2. Commit and push everything at that checkpoint to `amm/dev`.
3. Apply the agreed mechanical migration in place and align its required consumers/projections.
4. Check the migration against the frozen source frontier and adopted Declarations.

The [follow-up plan and pending choices](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-content-alias-followup-20261103.md) define scope, owners and acceptance checks. Ask unresolved choices one at a time. The group names are now `Atom.Header` and `Atom.Content`. Claim/alias grammar choices are resolved. The pre-migration checkpoint db837f08e is pushed and verified; the selected source migration and seven projection rebuilds are complete. The MODEL audit queue remains explicit. Prior completed Tasks remain Done, and P2707 retains its existing verification scope.

## CFEL grouping and variables

- Group Formal Claim expressions with `# model` and `# instances` comments inside the same CFEL block. Model expressions come first. These comments do not create Markdown Properties.
- Use explicit `$x` instance bindings, such as `Atom//$atom` and `Carrier//$carrier`, in place of anonymous instance references. Repeated variables identify the same bound instance within a Claim.
- Use the same `$x` notation for model bindings where needed. Preserve the distinction between model entities and their instances; document the applicable binding scope.
- Preserve explicit named references, inherited constraints, population cardinalities and endpoint-count meanings during migration.
- Update the CFEL rules and authoring guidance, affected readers/checkers/renderers, fixtures and projections. Verify comment handling and model/instance bindings before adoption.

The governing follow-up is adopted in 89 Current revisions, with 19 retired sources and 108 exact predecessor archives. The notation migration and seven MODEL-only projection rebuilds are verified. The earlier completed migration remains completed history. The [decision record](../02_analysis/draft/model-completeness-audit-20261103/decisions.md) holds the latest Operator wording.

## Current tasks

- CFEL grouping and `$x` notation — applied and verified; 1,148 selected sources, 263 changed, zero held; seven MODEL-only projections rebuilt.
- [CA-P-2709](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/13-CA-P-2709-TASK--simplify-model-and-structure-subject-roots.md) — Done; Subject-root migration independently verified.
- [CA-P-2704](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/done/09-CA-P-2704-TASK--remove-obsolete-scope-authority-mode-overrides.md) — Done.
- [CA-P-2705](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/done/10-CA-P-2705-TASK--adopt-formal-scope-unit-declarations.md) — Done.
- [CA-P-2706](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/done/11-CA-P-2706-TASK--retire-project-structure-toml-entirely.md) — Done.
- [CA-P-2707](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/12-CA-P-2707-TASK--verify-declaration-source-cutover.md) — Active.

## Definition of Done

Current Declarations and shared model are coherent and history is preserved. The new MODEL follow-up has completed its declaration, remote checkpoint, in-place migration and migration-check stages; unresolved choices and migration defects are closed. The live project_structure.toml file is absent. Production execution no longer requires or writes it. Retired bindings are not exposed. Affected runtime/script tests pass, including required integration checks for release. Remaining source or implementation gaps are explicit rather than hidden by legacy fallback. The pending CFEL grouping and variable follow-up is adopted in its governing rules and affected sources; model/instance binding, comment handling and projection checks pass.

## Previous completed stage

The earlier CFEL/model migration remains completed history. Its eight completed child Tasks are not reopened by this follow-up. The previous Epic content is preserved in its version-40 archive.

## Verification checkpoint

The Scope Unit cutover is complete through P2706; P2709 is Done. The Header/Claim/alias follow-up applied 87 Current outputs with 86 exact-byte predecessor archives, pushed the pre-migration checkpoint db837f08e to amm/dev, migrated 1,158 selected files in place (1,071 changed), repaired five remaining consumers and rebuilt seven faithful MODEL projections from 1,154 Current sources. Independent preservation checks and 160 focused tests pass. Twelve model-binding gaps remain in the audit queue. P2707 retains its existing Engine verification blockers; the Epic remains Active. This update records manual source application and focused checks, without native workflow or release completion.

[Migration report and remaining queue](../02_analysis/draft/model-header-content-migration-20261103/report.md).

The CFEL grouping and variable rules are adopted. The mechanical notation migration and seven MODEL-only projections are verified. The Epic remains Active for this follow-up and P2707.

## Carrier boundary

- Operate on Objects read from whole Carriers.
- Keep Carrier kinds in the MODEL.
- Delivery templates and adapters own Carrier internals and physical layout.
- Keep Atom.Header.Carrier Destination.File.Name and Path as mandatory string values.
- Retire the internal Carrier Property sources, their internal-region Rule, and Git Index.

The reviewed packet applies 89 revisions and 19 retirements. The declaring Relation is IS_DECLARED_BY, registered by CA-R-2732; its qualified derivation remains intact. The selected frontier contains 1,148 Current sources after retirement.

## Latest verification

- CFEL migration: 1,148 Current sources, 263 changed, zero held; 45 marker corrections retain business expressions.
- All 44 Scope Declarations use instance markers and remain readable.
- Seven MODEL-only projections are rebuilt from the final source pins.
- Role values are admitted through their individual Declarations. The duplicate list in R1283 is removed; the wider allowed-value audit found no other equivalent duplication.
- Independent preservation checks pass. All 412 graph tests pass; guard and migration checks pass.
- The projection audit retains 74 uncovered Subject expressions and 51 unresolved expressions for review. P2707 keeps its existing Engine verification scope.

[Continuation report](../02_analysis/draft/model-completeness-audit-20261103/implementation/report.md). The Epic remains Active; this does not claim a release or complete semantic evaluation.
