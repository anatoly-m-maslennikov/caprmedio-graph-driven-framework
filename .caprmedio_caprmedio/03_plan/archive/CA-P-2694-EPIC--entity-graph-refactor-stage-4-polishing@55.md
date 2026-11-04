---
atom_id: CA-P-2694
label: Epic
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
tier: 3
version: 55
updated_at: 2026-11-04 07:21:10 +0400
subjects:
  active: CAPRMEDIO_MODEL
relations: {}
role: Plan
form: Plan
carrier_destination:
  file:
    name: CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing.md
    path: .caprmedio_caprmedio/03_plan
---
## Summary

Entity graph refactor stage 4 — polishing

## Objective

Complete declaration-based Scope Unit authority and the latest MODEL/CFEL content, alias, counterpart, Property and Projection changes. Verify the affected sources, consumers, projections and P2707 integration gates.

## Scope

- Remove the five obsolete authority-mode overrides.
- Promote 44 Declaration Atoms and the shared ordering, Project and identity model. Preserve source history; merge existing model Definitions rather than create duplicates.
- Non-root units have stable IDs. The Project root has no Scope Unit ID; it is Unordered and has no order.number.
- Move and rename existing Authority and Delivery folders to the derived names. Derive Authority and Delivery folder names. Only non-root Authority names include the Scope Unit ID; Project Authority remains .caprmedio_<project name>.
- Retire project_structure.toml as a concept, source file and executable dependency: governing Atoms, readers, row writers, file-only bindings, fixtures and documentation.
- Use Declaration Atoms directly. Do not retain a fallback, generated compatibility TOML or second authored registry.
- Keep existing Scope Unit workflow definitions unchanged. Remove their TOML-specific implementation and executable bindings; do not build replacement Scope Unit tools in this Epic.
- Preserve existing business operations through admitted Atom lifecycle behavior. Do not invent new APIs, approval systems, locks or business rules.

- Keep MODEL entities distinct from their instances. Use the latest Operator decisions when earlier wording conflicts.
- Keep Atom.Header and Atom.Content, an empty Claim container with one or two Formal Claim / Prose Claim children, declared heading interpretation, explicit counterpart identities, aliases, and the removal of the @ reference operator.
- Keep # model / # instances groups and explicit $x bindings. Inherit declared formats without copying local value counts. A present Property has a value and has schema and bearer links.
- Projection identity is Form + Scope Unit. Named Selection remains source information. Terms Graph is deferred by the latest Operator input; Term Definitions and historical projections remain.

## Completed baseline

- P2695–P2706 and P2709 have recorded completed, bounded results. Preserve their history. P2708 owns the separately deferred O016 desired-behavior item.
- The Scope Unit source cutover, TOML retirement, Header/Claim/alias migration, Subject-root migration and CFEL grouping migration have application and preservation evidence.
- The latest published MODEL projections use 1,151 pinned Current suppliers. The last adopted batch passed 421 graph tests; subsequent reader changes require their own evidence and publication.
- The previous Epic version preserves the detailed checkpoint history. The acceptance matrix retains all 23 requirement groups and their evidence. These baselines do not close the remaining gates.

## Remaining work

1. **Relation permissions.** Adopt explicit outgoing permissions with correct model/instance scope, endpoint bounds and qualifications. Retain separate direct/inverse permissions. Record unary bounds in faithful graph projections.
2. **Property contracts.** Resolve the six conditional cases from applicable Declarations. Keep Relations populated by the containment Relation. Repair the optional Subjects grouping without weakening Current Active-subject requirements.
3. **MODEL coverage.** Disposition every flag in the 64 uncovered / 26 unresolved audit: source correction, declared authority, valid scope, authorized retirement or an Operator decision. Resolve used endpoint kinds and Settings ownership. Preserve operative Claims and exact history.
4. **Projection identity.** Adopt Form + Scope Unit constraints, the required Scope Unit reference and distinct Forms for current views. Align Delivery, readers, identity checks and generated instances. Preserve versioned source references. Defer graph-specific Terms Graph work explicitly.
5. **CFEL and faithful projections.** Repair declared narrowing and namespace binding, supported qualified selectors and bindings. Classify remaining opaque expressions; retain their complete source and diagnostics. Rebuild all seven MODEL-only views from actual Current Declarations. Formats, cardinalities and Formal Claims come only from Declarations.
6. **Current carrier admission.** Align live Delivery authority, source closure, registry and validators. Remove dependencies on retired D274; preserve fail-closed checks. Reconcile Header/Claim, role/form, Author removal and required fields with their Current authority before enabling admission.
7. **P2707.** Verify current Scope Declaration counts and identities, explain source-digest changes, verify absence of TOML dependencies, pass live Project admission, required fresh Docker query/status and lifecycle checks, the complete current-source suite and launcher. Capture one authoritative final result after changes.
8. **Independent closure.** Audit every requirement in the acceptance matrix against live evidence. Verify exact predecessors, metadata/identity rules, actual published projections and the requested remote checkpoint. Mark the Epic Done only after every required item passes or the Operator explicitly changes its scope.

## Decisions and execution

- Ask one question at a time when confidence is below 90%. Record each answer and its affected sources.
- Prepare and review source changes, commit the declaration checkpoint to amm/dev before a dependent mechanical migration, apply the accepted migration in place, then check it. Preserve disabled hooks and concurrent work.
- Root owns canonical source integration and Git. Workers own the separate evidence and preview lanes in the completion packet. No release or external publication is required by this plan. Required local integration tests remain in scope.

## Definition of Done

1. Every acceptance-matrix requirement has current authoritative evidence. Required MODEL decisions and migration defects are closed.
2. Current Declarations, Relations, Property contracts, Projection identity and affected R/M/E/D are coherent with the latest Operator decisions. Each retained model entity has its applicable defining authority. History is preserved.
3. No live project_structure.toml or production read/write dependency remains. No retired binding or compatibility registry replaces Declaration authority. The 44 Scope Declarations and their current identities are verified.
4. Required source, reader, validator, script, Docker and launcher checks pass on the final candidate. P2707 is Done; the separately owned P2708 disposition is explicit. Focused tests alone do not satisfy this gate.
5. All seven published MODEL views match the final source frontier and their governing Declarations. Unsupported expressions remain complete and explicitly classified.
6. The declaration checkpoint and checked final changes are committed and pushed to amm/dev, with matching local/remote evidence.

## Evidence

- [Full acceptance matrix](../02_analysis/draft/epic-completion-20261104/acceptance/matrix.json).
- [Completion lanes and current findings](../02_analysis/draft/epic-completion-20261104/README.md).
- [P2707 verification task](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/12-CA-P-2707-TASK--verify-declaration-source-cutover.md).
- [Adopted Property and inherited-format batch](../02_analysis/draft/property-instances-20261104/REPORT.md).
- [Earlier Header/Claim/alias stages](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/model-content-alias-followup-20261103.md).

## Status

Active. Plan review found stale checkpoint wording, retired carrier authority and incomplete MODEL and integration gates. The remaining-work list retains the complete scope and gives each gap a concrete closure check.
