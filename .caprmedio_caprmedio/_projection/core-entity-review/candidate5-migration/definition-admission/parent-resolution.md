# Candidate #6 — bounded parent-rule resolution

Reviewed: 2026-10-17. Proposal only. No source or draft edits, new IDs, parent links, or admission were performed.

## Finding

The sources support applicable lower-Global-Tier parents in the same owning Scope Unit and topology-permitted ancestor Scope Units. They do **not** support requiring identical Subjects. CA-R-796's old same-Atom-Scope sentence conflicts with those explicit ancestor permissions and needs a narrow replacement before recording the proposed links.

This resolves the interpretation needed for the 45 reviewed drafts below, using the final 10 Core / 3 General / 32 Standard tier proposals in `metadata-readiness.md`. It does not claim those links are admitted. Same-owner parents require a lower Global Tier; declared ancestor parents may have an equal or lower Global Tier under the existing topology (E117 v10). Structural eligibility does not prove that an arbitrary Atom is a meaningful parent.

## Exact evidence

Path abbreviations below are repository-relative prefixes, not new authority locations:

- `CORE` = `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL`
- `SOURCES` = `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES`
- `PROJECT` = `.caprmedio_caprmedio`

Only the current canonical sources were used, not their copies in `000_CAPRMEDIO_framework`, Applicable Methodology, or archive folders.

| Source and exact location | Current version | Relevant rule |
| --- | --- | --- |
| `CORE/04_requirement/CA-R-796-CORE_META_MODEL-CORE-REQUIREMENT--keep-tier-parent-relations-within-atom-scope.md` | 20 | Every tier-parent relation must connect Atoms with the same Atom Scope. It does not define that expression or mention Subject equality. |
| `CORE/04_requirement/CA-R-920-CORE_META_MODEL-CORE--give-every-atom-one-scope.md` | 20 | Every Atom must have exactly one Scope. Its empty Details do **not** define a composite of owner, target, Subject, and constraints. Treating that composite as R920's explicit text would overstate the source. |
| `PROJECT/04_requirement/CAPRMEDIO-REQU-037-REQUIREMENT--require-parent-coverage-without-claiming-topology-completeness.md` | 16 | Strict-mode active tier-classified PRMEDO requires at least one permitted active parent, unless its Type is orphan-permitted. Permitted cases are Project Goal→Project Principle, an applicable lower-global-tier Atom in the same structural scope, or a topology-permitted Atom in an ancestor scope. Coverage does not establish full topology completeness. |
| `CORE/04_requirement/CA-R-1597-CORE_META_MODEL-CORE-REQUIREMENT--separate-subject-paths-from-scope-coordinates.md` | 6 | Subject paths identify Subject-relation targets; they must not substitute for owning Scope Unit or Claim Target Scope Unit. |
| `CORE/04_requirement/CA-R-718-CORE_META_MODEL-CORE--separate-atom-claim-scope-from-structural-ownership.md` | 25 | Target Scope Unit and textual applicability do not create structural-parent edges or change ownership. |
| `CORE/04_requirement/CA-R-837-CORE_META_MODEL-REQUIREMENT--derive-artifact-scope-inclusion.md` | 21 | Resolve one direct owner and include an Artifact along that owner's ancestor path. This is scope inclusion, not additional ownership or an automatic normative-parent link. Its no-containing-Scope-Unit fallback remains distinct. |
| `CORE/04_requirement/CA-R-1776-CORE_META_MODEL-CORE--separate-graph-dimensions.md` | 21 | Structural ownership, normative authority, Subject classification, and applicability are distinct; one edge does not substitute for another. |
| `CORE/04_requirement/CA-R-879-CORE_META_MODEL-CORE-REQUIREMENT--register-child-of-and-parent-of-relation-pair.md` | 18 | `child_of` is the authored upstream normative-authority relation; `parent_of` is its derived inverse. This is not `contains`, `structural_parent`, or `NARROWER_THAN`. |
| `CORE/04_requirement/CA-R-833-CORE_META_MODEL-CORE-REQUIREMENT--organize-normative-authority-as-an-acyclic-hierarchy.md` | 15 | Normative authority remains explicit, typed, and acyclic. |
| `CORE/04_requirement/CA-R-1390-CORE_META_MODEL-GENERAL--derive-child-core-global-tier-from-parent-standard.md` | 13 | A non-Project Scope Unit's Core is one greater than its direct parent's Standard. |
| `CORE/04_requirement/CA-R-1391-CORE_META_MODEL-GENERAL--derive-non-project-general-and-standard-global-tiers.md` | 11 | Non-Project General = Core + 1; Standard = General + 1. |
| `CORE/04_requirement/CA-R-1392-CORE_META_MODEL-GENERAL--classify-non-project-goals-as-parent-standard.md` | 12 | A non-Project Goal uses its direct parent Scope Unit's Standard tier. |
| `CORE/04_requirement/CA-R-1775-CORE_META_MODEL-CORE-REQUIREMENT--let-parents-own-immediate-child-goals.md` | 17 | The parent Scope Unit owns Goals targeting immediate children; targeting does not transfer ownership. |
| `CORE/04_requirement/CA-R-1573-CORE_META_MODEL-CORE-REQUIREMENT--govern-greater-global-tiers-within-each-scope-unit.md` | 7 | Lower Global Tiers govern greater Global Tiers in each Scope Unit across Content Roles. This does not supply the semantic content of an arbitrary parent link. |
| `CORE/04_requirement/CA-R-1748-CORE_META_MODEL-CORE--bound-descendant-specialization-to-its-structural-scope.md` | 18 | Applicable inherited authority remains effective; specialization must stay inside its permitted boundary. |
| `CORE/04_requirement/CA-R-1375-CORE_META_MODEL-CORE--restrict-methodology-source-expansion-to-core-permission.md` | 15 | Project Configuration/Extensions cannot weaken Core authority. Source-layer authority is not permission to fabricate a sibling normative-parent edge. |

The current `PROJECT/project_structure.toml` declares `CORE_META_MODEL` and `PROJECT_CONFIGURATION` as strict-mode, structural-level-3 siblings under `METHODOLOGY_SOURCES` (level 2). Thus their proposed Core/General/Standard coordinates are 9/10/11; their direct parent's Standard is 8. Sibling local order does not make Core Meta-model an ancestor of Project Configuration.

## Minimum source correction

Replace R796's obsolete equality rule; do not reinterpret equality as “same Subject”, “same Target Scope Unit”, or “identical Substance Scope”. Each interpretation incorrectly excludes valid ancestor governance or confuses graph dimensions.

Keep CA-R-796 and its exact existing Summary: the same contribution remains the boundary on tier-parent applicability. Revise its erroneous equality condition to match the already-declared topology, increment its Version, and preserve the predecessor under the existing update rules. A later rename of its Summary would require a new identity; this packet does not require that rename or allocate an ID.

Proposed Summary:

> Keep tier-parent relations within Atom Scope

Proposed Subjects:

```yaml
subjects:
  governs: "Entity/Continuant/Object/Relation/Type: child_of"
  depends_on:
    - "Entity/Continuant/Object/Atom.Global Tier"
    - "Entity/Continuant/Object/Atom.Owning Scope Unit"
    - "Entity/Continuant/Object/Atom.Target Scope Unit"
    - "Entity/Continuant/Object/Atom.Substance Scope"
```

`child_of` here names the existing normative-authority relation defined by R879, not a new relation family or a change to its graph-qualified identity. Canonical Subject spelling must follow the accepted relation mapping; this packet does not allocate a graph registry entry.

Proposed Scope:

> Tier-parent relations between tier-classified Atoms.

Proposed Claim:

> a tier-parent relation **must** point from a child Atom to an applicable parent Atom permitted by the Global Tier topology. a parent in the child's Owning Scope Unit **must** have a lower Global Tier. a parent in a declared ancestor Scope Unit **may** have an equal or lower Global Tier. the parent's Substance, Target Scope Unit when applicable, and Substance Scope **must** support the authority claimed by that relation.

Proposed Details:

> Structural eligibility alone does not establish parenthood. Different Subjects are allowed when the parent actually governs the child's contribution; equal Subjects do not establish that governance. An ancestor-owned Goal may govern definitions that fulfill its result in the targeted child Scope Unit without changing either Atom's owner. A relational Atom's Target Scope Unit does not replace its Owning Scope Unit in the structural test. Preserve the admitted Project Goal-to-Project Principle case, Type-specific restrictions, orphan permissions, and the acyclic normative-authority boundary. Do not turn a dependency, classification, containment, or source-layer relation into `child_of` merely to fill parent coverage.

The retained legacy Summary's phrase “Atom Scope” refers here to the explicit applicability boundary above. It does not declare a fourth Scope field, resurrect a composite Subject Entity, or require identical coordinates. The operative text names the three accepted coordinates separately.

REQU-037 already owns this Project's strict-mode active-parent requirement. No change to its count, active-status condition, orphan exception, or casual-mode policy is necessary. R796's replacement does not create a new global coverage gate.

R920 does not need a speculative new composite-Scope definition for this correction. Its generic “one Scope” wording belongs to the accepted Owning/Target/Substance Scope content alignment. Existing R837 already supports the direct-owner fact for contained Atoms; R718 and R1597 keep the coordinates separate. Do not rewrite R920 as “every Atom has one owner” without preserving the existing external/no-containing-Scope-Unit cases. This packet introduces no new Scope cardinality rule.

## Concrete, bounded parent candidates

These are proposed links after R796 alignment and after each draft's Local Tier is accepted, not links already written or verified as admitted.

| Proposed child contribution | Parent candidate and evidence | Why the relation is meaningful |
| --- | --- | --- |
| `Define Entity/Continuant` and `Define Entity/Occurrent`, proposed CORE_META_MODEL Core/9 | CA-R-1174 v13, `SOURCES/04_requirement/CA-R-1174-METHODOLOGY_SOURCES-DEFINES_GOAL_FOR-CORE_META_MODEL--provide-the-minimal-self-applicable-canonical-methodology-model.md`; Active Goal, owner METHODOLOGY_SOURCES, target CORE_META_MODEL, Standard/8 | Its actual Claim requires the minimal self-applicable canonical model needed to represent/govern/validate/compile Methodology authority. These definitions establish that accepted model's fundamental persistent-thing/actual-occurrence distinction. Direct-parent Goal placement and 8→9 follow R1390/R1392/R1775. The parent Subject is `CORE_META_MODEL/Goal`, not either child entity Subject. |
| `Define Entity/Continuant/History`, proposed CORE_META_MODEL Core/9 | The same CA-R-1174 | Defining the accepted history-vs-current/event boundary supplies the canonical model required by that Goal. This is a specific contribution to its result, not an inference that every unrelated Atom can cite the Goal. Do not substitute same-owner R1371 Core/9 as a lower-tier parent: 9 is not lower than 9. |
| `Define Project.Framework Settings.Confidence`, proposed PROJECT_CONFIGURATION Standard/11 | CA-R-1176 v15, `SOURCES/04_requirement/CA-R-1176-METHODOLOGY_SOURCES-DEFINES_GOAL_FOR-PROJECT_CONFIGURATION--select-core-meta-model-and-project-configuration-for-compilation.md`; Active Goal, owner METHODOLOGY_SOURCES, target PROJECT_CONFIGURATION, Standard/8 | Its Claim requires Project-owned Customizations and composition decisions in Project Configuration. This definition contributes the accepted CAPRMEDIO-specific defaults grouping to that source, without inventing thresholds or overriding generic Core authority. The governing result is local customization, not a Claim that R1176 supplies numeric Confidence defaults. |
| A Project Configuration rule choosing this project's default Settings values or declaring its framework-specific settings grouping | CA-R-1222 v10, `SOURCES/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1222-PROJECT_CONFIGURATION-GENERAL-REQUIREMENT--defer-caprmedio-specific-extension-packaging.md`; same owner, General/10 | Its Claim keeps this Project's methodology customizations in PROJECT_CONFIGURATION until separate Extension packaging is accepted. It can supply the explicit source-placement boundary for such a Standard/11 customization. It does not prescribe the default value or replace the source defining that field. Use only when the complete child contribution is genuinely a Project customization. |

The concrete defaults group remains distinct from choosing a runtime Settings value. Its draft defines a grouping only. Neither parent candidate authorizes adding threshold values, precedence, runtime behavior, or new Settings fields to the Claim.

No same-owner Core/9 definition can parent another Core/9 definition through a lower-tier edge. No CORE_META_MODEL/9 rule becomes a structural parent for PROJECT_CONFIGURATION/11 merely because 9 < 11: those owners are siblings. R1375's Core-authority boundary still applies independently of whether a normative parent link is present.

## Remaining decision and implementation boundary

The Operator authorized the bounded ancestor-parent fix. There is no uncovered need to invent a new notion of Atom Scope or require matching Subjects. R796's contradictory equality sentence still needs the source update stated above. The implementation preserves E117's equal-tier ancestor case; it does not impose a new lower-only rule on ancestors.

The local validator fix in `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/check_graph_extended.py` resolves the declared ancestor chain and applies the tier distinction above. Fifteen new synthetic regressions and sixty existing graph/structure tests passed. Deployment, source alignment and admission are separate results; this package does not claim those effects.

Not included: full-project parent repair, new Type-to-tier constraints, filling legacy headers, activating definitions, or checking full topology completeness.

## Complete bounded map for the 45 reviewed drafts

Each key identifies `../empty-r-drafts/CA-R--CORE_META_MODEL--define-<key>.md`. The historical filename does not override the owner below. Each row supplies one proposed parent, not a list of required graph edges. Source contradictions in the Status, containment, Revision and Carrier alignment packets remain prerequisites; a parent proposal cannot repair a conflicting Claim.

Parent evidence used by this map:

- **R1174**: CA-R-1174 v13, exact path and active metadata above. The accepted minimal canonical model Goal targets CORE_META_MODEL; its Standard/8 coordinate is below all proposed child tiers 9/10/11. The child is included in the parent's ancestor scope under R837; R1573 establishes greater-tier governance there. R1390/R1392/R1775 establish the direct-parent Goal placement. A parent edge need not traverse every intermediate tier: REQU-037 says lower tier, not exactly one tier lower. The distinct contribution in each row is the semantic applicability witness.
- **R1176**: CA-R-1176 v15, exact path and active metadata above. Its Project-owned customization result targets PROJECT_CONFIGURATION. All seven local framework setting definitions are Standard/11; Goal/8 is a permitted ancestor candidate under the same topology. It does not prescribe specific default values. These definitions are accepted project-owned customization content, not universal Core concepts.
- **R1746**: CA-R-1746 v22, `CORE/04_requirement/CA-R-1746-CORE_META_MODEL-CORE--define-projection-artifact-form.md`, Active, CORE_META_MODEL Core/9. Its Claim defines a non-authoritative generated view, declared source selection and source traceability. It supplies actual same-owner higher authority for the Semantics projection-authority boundary and Direct Relation Registry specialization; it is not selected merely because the Subject mentions Projection.

| Draft key | Owner | Local / Global Tier | Proposed `child_of` | Actual contribution governed by that parent |
| --- | --- | --- | --- | --- |
| actor-name | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines the accepted model's optional Actor naming field; creates no extra identity or permission. |
| atom-enabled-relations-contains | CORE_META_MODEL | General / 10 | CA-R-1174 | Supplies the accepted generic kind-level containment capability/default needed to govern container Atoms; concrete enablement remains separate. |
| atom-semantics | CORE_META_MODEL | General / 10 | CA-R-1746 | Defines source meaning content while expressly preserving the governing non-authority of derived Terms definitions. The parent governs that source/projection boundary; it does not invent the property. |
| atom-status-allowed-values | CORE_META_MODEL | General / 10 | CA-R-1174 | Supplies the common lifecycle domain and additive kind inheritance needed by the canonical Atom model, subject to the separate Status alignment. |
| carrier-canonical-address-segment | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines address components used to identify model representations without inventing a storage format. |
| carrier-canonical-address | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines locator meaning while keeping it distinct from represented identity. |
| carrier-format | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines how the accepted Carrier model identifies encoding/interpretation rules. |
| carrier-id | CORE_META_MODEL | Core / 9 | CA-R-1174 | Establishes Carrier identity independent of mutable locators, a canonical model boundary. |
| directory-carrier-name | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines the name/path distinction for the accepted directory representation kind. |
| directory-carrier-numeric-prefix | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines a conditional naming component, not an additional entity identity or mandatory numbering rule. |
| directory-carrier-path | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines the directory locator and preserves separation from structural ownership. |
| entity-carrier-database-carrier | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Supplies the accepted database representation kind without identifying the database with its represented Entity. |
| entity-carrier-directory-carrier | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Supplies the directory representation kind and distinguishes mere file grouping from representation. |
| entity-carrier-file-carrier | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Supplies the file representation kind in the canonical model. |
| entity-carrier | CORE_META_MODEL | Core / 9 | CA-R-1174 | Establishes representation versus represented thing/occurrence. |
| entity-continuant-actor-type-ai-agent | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines the accepted Actor kind performing delegated model-based work without creating new permission rules. |
| entity-continuant-history-revision-type-atom | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines archived Atom state within the accepted historical-state model, subject to Revision alignment. |
| entity-continuant-history | CORE_META_MODEL | Core / 9 | CA-R-1174 | Establishes preserved state/record versus actual event separation. |
| entity-continuant-object-governing-configuration | CORE_META_MODEL | Core / 9 | CA-R-1174 | Establishes authoritative non-Atom configuration versus generated Projection. |
| entity-continuant-object-relation | CORE_META_MODEL | Core / 9 | CA-R-1174 | Establishes typed directional connection meaning in the canonical graph model. |
| entity-continuant-object | CORE_META_MODEL | Core / 9 | CA-R-1174 | Establishes what-is-governed versus who-acts separation. |
| entity-continuant-projection-type-direct-relation-registry | CORE_META_MODEL | Standard / 11 | CA-R-1746 | Specializes a generated, source-traceable, non-authoritative Projection of Relation Kinds. |
| entity-continuant-selection | CORE_META_MODEL | Core / 9 | CA-R-1174 | Establishes selection criteria versus selected members/copies. |
| entity-continuant | CORE_META_MODEL | Core / 9 | CA-R-1174 | Establishes identifiable persistent thing versus actual occurrence. |
| entity-occurrent-event | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines an actual Event distinct from its record within the accepted occurrence branch. |
| entity-occurrent-execution-action-run | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines one actual Action execution, not its reusable definition or record. |
| entity-occurrent-execution | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines work performed distinctly from definition/history under the accepted Occurrent boundary. |
| entity-occurrent-session | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines actual interaction distinctly from logs and stored envelopes. |
| entity-occurrent | CORE_META_MODEL | Core / 9 | CA-R-1174 | Establishes actual occurrence versus record. |
| execution-execution-id | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines the accepted Execution identifying field without inventing its syntax. |
| file-carrier-extension | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines filename suffix/format indication without conflating carried Entity identity. |
| file-carrier-filename | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines file name separately from its containing path. |
| file-carrier-path | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines file location separately from Carrier identity. |
| project-framework-settings-artifact-timestamp-timezone | PROJECT_CONFIGURATION | Standard / 11 | CA-R-1176 | Defines this framework's timestamp interpretation setting, not a universal timezone choice. |
| project-framework-settings-code-root-locators | PROJECT_CONFIGURATION | Standard / 11 | CA-R-1176 | Defines this framework's code-root configuration references, not generic Project identity. |
| project-framework-settings-confidence | PROJECT_CONFIGURATION | Standard / 11 | CA-R-1176 | Defines this framework's existing Confidence-default grouping without choosing new thresholds. |
| project-framework-settings-framework-control-root-locator | PROJECT_CONFIGURATION | Standard / 11 | CA-R-1176 | Defines this framework's control-directory configuration reference. |
| project-framework-settings-identifier | PROJECT_CONFIGURATION | Standard / 11 | CA-R-1176 | Defines the identifier of this framework's selected governing configuration, not another Atom ID. |
| project-framework-settings-interaction | PROJECT_CONFIGURATION | Standard / 11 | CA-R-1176 | Defines this framework's Operator-presentation choices group. |
| project-framework-settings-parameter-resolution | PROJECT_CONFIGURATION | Standard / 11 | CA-R-1176 | Defines how this framework names effective-parameter selection under existing governing rules; adds no override precedence. |
| project-operator-registry | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines authoritative identifying information without treating registration as permission. |
| project-settings-identifier | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines the generic authoritative Settings configuration's identifier, not an Atom. |
| relation-source-reference | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines the start endpoint slot of an admitted directional relation, without admitting new endpoints. |
| relation-target-reference | CORE_META_MODEL | Standard / 11 | CA-R-1174 | Defines the end endpoint slot of an admitted directional relation, without admitting new endpoints. |
| scope-unit-id | CORE_META_MODEL | Core / 9 | CA-R-1174 | Establishes structural identity distinct from mutable Name, Label and Path. |

This map uses only three current parent identities: R1174 for 36 distinct model contributions, R1746 for two projection-related contributions, and R1176 for seven local framework configuration contributions. It is not a new general rule that these Goals must parent every future Atom. Applicability and admitted Type/tier restrictions must still be checked for future contributions individually. No missing/archived/draft parent or unresolved successor identity is used.
