# Node Declaration Expansion Census

Status: evidence-only; Current unchanged; no mapping or declaration generated.

Authority: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL`

## Scope and counts

- 750 active direct Core R carriers indexed: {'Rule': 378, 'Relation Definition': 36, 'Entity Definition': 334, 'Term Definition': 1, 'Demand': 1}.
- The prior Entity Definition inventory has 333 rows: 232 Object, 57 Aspect, 1 Property, and 43 Syntax/Carrier/Term boundary rows.
- 259 active sources govern Atom or an Atom branch; 57 Atom Property expressions and 120 formal Property expressions across all active Core R sources have active code-form claim evidence.
- The census carries metadata for all 750 active sources. The full source lists, exact hashes and paths are in `census.json`, including formal Property expressions found across all 750 active sources.

No Current source changed. A matching Entity path or a source Definition does not by itself authorize Node identity.

## Atom base property evidence

CA-R-655@42 is the structural Atom form. CA-R-2102@13 refines completeness, role/type-specific content and ordinary Atom exceptions. Separate current evidence defines these base properties:

- `CA-R-655@42` — Current Atom artifact form; full formal base-property structure. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-655-CORE_META_MODEL-ENTITY-DEFINITION--define-atom-artifact-form.md]
- `CA-R-2102@13` — Current Atom completeness rule; names required properties and role/type conditions; refines base counts and explicit exceptions. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2102-CORE_META_MODEL-RULE--require-the-base-properties-of-every-current-atom.md]
- `CA-R-2357@2` — Content Role format/cardinality. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2357-CORE_META_MODEL-ENTITY_DEFINITION--define-atom-content-role.md]
- `CA-R-2361@1` — Type format/cardinality. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2361-CORE_META_MODEL-ENTITY_DEFINITION--define-atom-type.md]
- `CA-R-728@35` — Atom ID identity meaning; formal cardinality inherited from R655. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-728-CORE_META_MODEL-DEFINITION--define-project-atom-id.md]
- `CA-R-1989@16` — Status formal cardinality/domain; see also R1412. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1989-CORE_META_MODEL-DEFINITION--define-atom-status.md]
- `CA-R-2362@1` — Updated At format/cardinality. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2362-CORE_META_MODEL-ENTITY_DEFINITION--define-atom-updated-at.md]
- `CA-R-2363@1` — Version Number format/cardinality. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2363-CORE_META_MODEL-ENTITY_DEFINITION--define-atom-version-number.md]
- `CA-R-2356@1` — Author format/cardinality. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2356-CORE_META_MODEL-ENTITY_DEFINITION--define-atom-author.md]
- `CA-R-2124@14` — Tier is numeric Atom Property; see tier Rules. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2124-CORE_META_MODEL-ENTITY-DEFINITION--define-numeric-tier-as-an-atom-property.md]
- `CA-R-1594@18` — Label is optional explicit text; effective fallback from Type is derived, not another stored value. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1594-CORE_META_MODEL-DEFINITION--define-label.md]
- `CA-R-1465@26` — Summary is one navigation Property with role-specific source. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1465-CORE_META_MODEL--define-summary-as-an-atom-property.md]
- `CA-R-2359@1` — Local Scope Unit; R2102 supplies ordinary Atom exact-one rule/Project Goal exception. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2359-CORE_META_MODEL-ENTITY_DEFINITION--define-atom-local-scope-unit.md]
- `CA-R-1595@21` — Target Scope Unit; R2102 gives optionality and Goal-specific requirement. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1595-CORE_META_MODEL-DEFINITION--define-claim-target-scope-unit.md]
- `CA-R-1198@29` — Subjects grouping; defines Governs and Depends On child properties. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1198-CORE_META_MODEL-DEFINITION--define-atom-subjects.md]
- `CA-R-2280@1` — Content grouping; R2102 supplies Role/Type-specific required content contract. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2280-CORE_META_MODEL-ENTITY_DEFINITION--define-atom-content.md]
- `CA-R-1945@13` — Enabled Relations property; relation group-specific semantics. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1945-CORE_META_MODEL--define-atom-enabled-relations-contains.md]
- `CA-R-1269@33` — Claim, formal Claim, Claim Scope, Semantics and Details property contract. [.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1269-CORE_META_MODEL-DEFINITION--define-claim.md]

R655 groups Content, Subjects and Relations with zero direct values; child properties remain governed individually. R2102 supplies required children and contextual cardinalities. Effective Label can be derived from Type when no explicit Label is stored. Do not flatten these into one generic cardinality.

## Structural kind families and classification

- R1248@24 names the root branches: Object, Aspect, Graph Syntax, Carrier, Term and Property. It says Entity is broader than Object and does not assert an exhaustive or disjoint partition.
- R2226@2, R1967@10 and R1972@11 establish Object, Continuant and Occurrent structure.
- R2210@4 defines Aspect as a topic addressed by an Atom.
- R1193@23 and related R1251/R1247/R2003/R1351 sources establish dependent Property and bearer constraints; they do not settle the proposed Independence classifier or HAS_VALUE endpoints.
- Role, Type/Form and Status values are classifications or allowed values. CFEL operators and syntax definitions do not create Nodes. Carrier and Term remain separate branches.

## Existing candidate set and open bindings

- The 290-row prior census remains a candidate review set, not a mapping. The full metadata rows are included under `primary_kind_candidates.source_inventory_rows` for 289 Object/Aspect candidates and the property-kind source is listed separately.
- All active Core R sources, including Rules and their formal/property claims, are indexed. The atom property expression table includes source bindings rather than filtering to Entity Definitions.
- There are many repeated governed subjects across active Definition and Rule sources. They generally represent constraints that must be composed; they are not automatically competing identity claims. R1531/R1549 is a notable Content Role source collision.
- Workflow, Step, Substep and Action declarations describe kinds/forms; actual instances remain deferred.

## Draft packet

The current register contains 31 Draft carriers; metadata paths, IDs, governs values and hashes are included in `draft_register_sources` in JSON.
