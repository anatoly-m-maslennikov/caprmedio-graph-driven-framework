---
atom_id: CA-P-2694
label: Epic
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
tier: 3
version: 43
updated_at: 2026-11-02 20:24:36 +0400
subjects:
  active: Scope Unit
relations: {}
role: Plan
form: Plan
---
## Summary

Entity graph refactor stage 4 — polishing

## Objective

Adopt formal Scope Unit Declarations as the sole structural source and retire project_structure.toml completely.

## Details

- Remove the five obsolete authority-mode overrides.
- Promote 44 Declaration Atoms and the shared ordering, Project and identity model. Preserve source history; merge existing model Definitions rather than create duplicates.
- Non-root units have stable IDs. The Project root has no Scope Unit ID; it is Unordered and has no order.number.
- Move and rename existing Authority and Delivery folders to the derived names. Derive Authority and Delivery folder names. Only non-root Authority names include the Scope Unit ID; Project Authority remains .caprmedio_<project name>.
- Retire project_structure.toml as a concept, source file and executable dependency: governing Atoms, readers, row writers, file-only bindings, fixtures and documentation.
- Use Declaration Atoms directly. Do not retain a fallback, generated compatibility TOML or second authored registry.
- Keep existing Scope Unit workflow definitions unchanged. Remove their TOML-specific implementation and executable bindings; do not build replacement Scope Unit tools in this Epic.
- Preserve existing business operations through admitted Atom lifecycle behavior. Do not invent new APIs, approval systems, locks or business rules.

## Current tasks

- [CA-P-2704](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/done/09-CA-P-2704-TASK--remove-obsolete-scope-authority-mode-overrides.md) — Done.
- [CA-P-2705](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/done/10-CA-P-2705-TASK--adopt-formal-scope-unit-declarations.md) — Done.
- [CA-P-2706](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/11-CA-P-2706-TASK--retire-project-structure-toml-entirely.md) — Active.
- [CA-P-2707](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/12-CA-P-2707-TASK--verify-declaration-source-cutover.md) — Active.

## Definition of Done

Current Declarations and shared model are coherent and history is preserved. The live project_structure.toml file is absent. Production execution no longer requires or writes it. Retired bindings are not exposed. Affected runtime/script tests pass, including required integration checks for release. Remaining source or implementation gaps are explicit rather than hidden by legacy fallback.

## Previous completed stage

The earlier CFEL/model migration remains completed history. Its eight completed child Tasks are not reopened by this follow-up. The previous Epic content is preserved in its version-40 archive.
