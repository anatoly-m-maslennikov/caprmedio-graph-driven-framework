---
atom_id: CA-P-2694@46
label: Epic
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
tier: 3
version: 46
updated_at: 2026-11-03 17:30:20 +0400
subjects:
  active: CAPRMEDIO <+ MODEL
relations: {}
role: Plan
form: Plan
author: Anatoly Maslennikov
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

Execute in this order:

1. Update/create the Declarations and reconcile the affected authoring/layout rules.
2. Commit and push everything at that checkpoint to `amm/dev`.
3. Apply the agreed mechanical migration in place and align its required consumers/projections.
4. Check the migration against the frozen source frontier and adopted Declarations.

The [follow-up plan and pending choices](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-content-alias-followup-20261103.md) define scope, owners and acceptance checks. Ask unresolved choices one at a time. The group names are now `Atom.Header` and `Atom.Content`. Remaining Claim/alias grammar choices are tracked in the follow-up; the new Git checkpoint and migration have not started. Prior completed Tasks remain Done, and P2707 retains its existing verification scope.

## Current tasks

- [CA-P-2704](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/done/09-CA-P-2704-TASK--remove-obsolete-scope-authority-mode-overrides.md) — Done.
- [CA-P-2705](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/done/10-CA-P-2705-TASK--adopt-formal-scope-unit-declarations.md) — Done.
- [CA-P-2706](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/done/11-CA-P-2706-TASK--retire-project-structure-toml-entirely.md) — Done.
- [CA-P-2707](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/12-CA-P-2707-TASK--verify-declaration-source-cutover.md) — Active.

## Definition of Done

Current Declarations and shared model are coherent and history is preserved. The new MODEL follow-up has completed its declaration, remote checkpoint, in-place migration and migration-check stages; unresolved choices and migration defects are closed. The live project_structure.toml file is absent. Production execution no longer requires or writes it. Retired bindings are not exposed. Affected runtime/script tests pass, including required integration checks for release. Remaining source or implementation gaps are explicit rather than hidden by legacy fallback.

## Previous completed stage

The earlier CFEL/model migration remains completed history. Its eight completed child Tasks are not reopened by this follow-up. The previous Epic content is preserved in its version-40 archive.

## Verification checkpoint

The earlier Scope Unit cutover is complete through P2706. P2707 remains Active for its recorded Engine verification blockers. The new MODEL follow-up is at planning/decision resolution and keeps the Epic Active independently. No new release, live MCP replacement, commit or push is claimed by this plan update.
