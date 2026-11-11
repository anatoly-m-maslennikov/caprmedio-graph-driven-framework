# Property contract evidence

Evidence inventory of selected standard Atom/Project/body properties; not exhaustive Node coverage or adoption. Values listed are type-level contracts, not instance values.

| Property | Direct value Format | Direct value count | Immediate dependent Properties | Evidence |
|---|---|---|---|---|
| Atom.ID | string | 1 | unresolved | CA-R-655, CA-D-657, CA-R-728 |
| Atom.Role | string | 1 | unresolved | CA-R-2357, CA-D-657 |
| Atom.Form | string | 1 | unresolved | CA-R-2361, CA-D-657 |
| Atom.Status | string | 1 | none (0) | CA-R-1989, CA-R-1412 |
| Atom.Updated At | datetime | 1 | none (0) | CA-R-2362, CA-R-1416 |
| Atom.Version Number | int | 1 | unresolved | CA-R-2363, CA-R-1415 |
| Atom.Author | string | 1 | unresolved | CA-R-2356, CA-R-1078 |
| Atom.Local Scope Unit | string | 1 | unresolved | CA-R-920, CA-D-657 |
| Atom.Target Scope Unit | string | 1 | unresolved | CA-R-1596, CA-D-482 |
| Atom.Tier | int | 1 | unresolved | CA-R-2124 |
| Atom.Label | string | 0..1 | unresolved | CA-R-655 |
| Atom.Tier.Label | string | 0..1 | unresolved | CA-R-2274 |
| Atom.Subjects | unresolved | 0 | unresolved | CA-R-1198 |
| Atom.Subjects.Active | string | 1 for complete Current | unresolved | CA-R-1198, CA-R-1363 |
| Atom.Subjects.Passive | string | 0+ | unresolved | CA-R-1198, CA-R-1278 |
| Atom.Relations | unresolved | 0 | unresolved | CA-R-2281, CA-D-657 |
| Atom.Content | unresolved | 0 | unresolved | CA-R-2280, CA-R-1417 |
| Atom.Content.Summary | string | 1 | unresolved | CA-R-655, CA-R-1418, CA-D-479 |
| Atom.Content.Claim | string | 0..1 base; 1 complete RMED | unresolved | CA-R-1269, CA-D-479 |
| Atom.Content.Claim.Formal Claim | string | 0..1 Requirement | unresolved | CA-R-2389, CA-R-1269 |
| Atom.Content.Claim Scope | string | 0..1 | unresolved | CA-R-2160 |
| Atom.Content.Semantics | string | 0..1 | unresolved | CA-R-1946, CA-R-1269 |
| Atom.Content.Details | string | 0..1 | unresolved | CA-R-1269, CA-D-479 |
| Project.Settings.Name | string | 1 | unresolved | CA-R-2458 |
| Project.Settings.Prefix | string | 1 | unresolved | CA-R-2459 |
| Atom.Relations.contained_by | empty domain | 0 | exactly one immediate child from atom, scope_unit | latest Operator clarification |
| Atom.Relations.contained_by.* | unresolved | 1 | none (0) | latest Operator clarification |

## Complete candidate slots

- `atom.status[string]{1}.[]{0}` — No-child constraint comes from latest human clarification.
- `atom.updated_at[datetime]{1}.[]{0}` — No-child constraint comes from latest human clarification.
- `atom.relations.contained_by[]{0}.[in (atom, scope_unit)]{1}` — Each child is separately constrained to one typed target; whether value domain is string/reference or modeled Node remains open. Canonical Relation is IS_CONTAINED_BY with CONTAINS inverse; mapping does not create a second inverse fact.
- `atom.relations.contained_by.*[Node// >| Container = yes]{1}.[]{0}` — Condition in candidate is a target predicate, not proof that underlying value Format or endpoint representation is settled. No Property// construction.

## Conflicts and missing slots

- Current D479/R1269 require direct prose Claim for complete RMED; proposed CFEL-first Declaration policy changes that requirement.
- Current D482 requires explicit target-scope carrier, while proposed omission fallback requires an explicit migration decision.
- Current IS_CONTAINED_BY/CONTAINS naming and proposed Relation representation must use latest human canonical decision; old candidate IS_PART_OF/HAS_PART is superseded.
- No universal scalar child count is assumed.
- No missing value domain or cardinality is treated as unconstrained, empty or zero.
- Exact formal expression and identity of named child-property sets, role-specific restrictions and inherited resolution need review.
- Node/ and instance selector grammar, typed reference endpoint representation, and graph materialization remain unadmitted.

## Highest-impact decision

For a Property whose Current authority fixes its value Format and count but says nothing about direct dependent Properties, should the new Declaration require zero dependent Properties, or leave that slot unresolved until reviewed individually?

Leave the slot unresolved and review per Property; Tier and Claim already demonstrate legitimate children, so a blanket default could reject valid structures.

## Source pins

- CA-R-655@42: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-655-CORE_META_MODEL-ENTITY-DEFINITION--define-atom-artifact-form.md`
- CA-R-728@35: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-728-CORE_META_MODEL-DEFINITION--define-project-atom-id.md`
- CA-R-1412@23: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1412-CORE_META_MODEL--give-every-atom-revision-one-status.md`
- CA-R-1989@16: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1989-CORE_META_MODEL-DEFINITION--define-atom-status.md`
- CA-R-1415@25: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1415-CORE_META_MODEL--give-every-atom-revision-one-version.md`
- CA-R-2363@1: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2363-CORE_META_MODEL-ENTITY_DEFINITION--define-atom-version-number.md`
- CA-R-1416@25: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1416-CORE_META_MODEL--give-every-atom-revision-one-updated-at.md`
- CA-R-2362@1: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2362-CORE_META_MODEL-ENTITY_DEFINITION--define-atom-updated-at.md`
- CA-R-1417@29: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1417-CORE_META_MODEL-RULE--give-every-atom-revision-one-content.md`
- CA-R-1418@27: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1418-CORE_META_MODEL--give-every-atom-one-summary.md`
- CA-R-1078@31: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1078-CORE_META_MODEL-RULE--give-every-atom-revision-one-author.md`
- CA-R-2356@1: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2356-CORE_META_MODEL-ENTITY_DEFINITION--define-atom-author.md`
- CA-R-2357@2: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2357-CORE_META_MODEL-ENTITY_DEFINITION--define-atom-content-role.md`
- CA-R-2361@1: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2361-CORE_META_MODEL-ENTITY_DEFINITION--define-atom-type.md`
- CA-R-1198@29: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1198-CORE_META_MODEL-DEFINITION--define-atom-subjects.md`
- CA-R-1363@29: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1363-CORE_META_MODEL--define-atom-governed-subject.md`
- CA-R-1278@22: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1278-CORE_META_MODEL--allow-zero-or-more-dependency-subjects.md`
- CA-R-2280@1: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2280-CORE_META_MODEL-ENTITY_DEFINITION--define-atom-content.md`
- CA-R-2281@1: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2281-CORE_META_MODEL-ENTITY_DEFINITION--define-atom-relations.md`
- CA-R-2124@14: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2124-CORE_META_MODEL-ENTITY-DEFINITION--define-numeric-tier-as-an-atom-property.md`
- CA-R-2274@2: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2274-CORE_META_MODEL-ENTITY-DEFINITION--define-atom-tier-label.md`
- CA-R-1269@33: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1269-CORE_META_MODEL-DEFINITION--define-claim.md`
- CA-R-2160@8: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2160-CORE_META_MODEL-DEFINITION--define-atom-content-scope.md`
- CA-R-1946@14: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1946-CORE_META_MODEL--define-atom-semantics.md`
- CA-R-2389@1: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2389-CORE_META_MODEL-ENTITY_DEFINITION--define-requirement-content-formal-claim.md`
- CA-R-1596@21: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1596-CORE_META_MODEL--give-every-claim-one-target-scope-unit.md`
- CA-R-920@32: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-920-CORE_META_MODEL--give-every-atom-one-scope.md`
- CA-R-2458@2: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2458-CORE_META_MODEL-ENTITY_DEFINITION--define-project-settings-name.md`
- CA-R-2459@2: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2459-CORE_META_MODEL-ENTITY_DEFINITION--define-project-settings-prefix.md`
- CA-R-2243@3: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2243-CORE_META_MODEL-ENTITY_DEFINITION--define-cardinality-notation.md`
- CA-R-2248@1: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2248-CORE_META_MODEL-ENTITY_DEFINITION--define-value-format.md`
- CA-D-479@26: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/CA-D-479-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties.md`
- CA-D-478@29: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/CA-D-478-CORE_META_MODEL-ENG_DECISION--store-every-atom-property-in-one-internal-location.md`
- CA-D-482@26: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/CA-D-482-CORE_META_MODEL-ENG_DECISION--carry-the-resolved-claim-target-scope-unit.md`
- CA-D-657@1: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/07_delivery/CA-D-657-CORE_META_MODEL-DECISION--yaml-frontmatter-encodes-atom-properties-with-minimal-syntax.md`
