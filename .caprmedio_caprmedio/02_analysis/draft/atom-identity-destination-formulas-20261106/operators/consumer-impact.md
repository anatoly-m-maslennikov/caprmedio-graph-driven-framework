# Pure `?==` consumer impact

Basis: the refreshed 4,677-carrier native Current/Draft snapshot, read from live paths, plus new Drafts CA-R-2995@1, CA-R-2996@1 and CA-R-2997@1. Archives, projections, generated material and analysis-packet copies were excluded.

The approved global meaning is pure: `x ?== y` returns `y` when `x` is `null`, `""`, or undefined (including omission); otherwise it returns `x`. It gives neither operand a Model value.

## Result

- 30 literal occurrences on 27 lines in 16 native sources.
- 12 sources retain assignment/default semantics or clauses and need reconciliation before coordinated adoption.
- 4 sources are already pure or only support a read-only fallback expression.
- CA-D-485 has no literal use but assumes a default selects and carries a required Atom value.

## Assignment-reliant consumers

| ID | Path | Impact |
| --- | --- | --- |
| CA-P-2694 | `03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing.md` | Current narrative says `?==` gives a missing effective Property value and puts defaults on Property Declarations. |
| CA-A-1318@1-draft | `.../02_analysis/draft/CA-A-1318@1-draft-CORE_META_MODEL-SPECIFICATION_PROPOSAL--consolidate-cfel-syntax-and-precise-relations.md` | Defines an effective default. |
| CA-A-1320@1-draft | `.../02_analysis/draft/CA-A-1320@1-draft-CORE_META_MODEL-SPECIFICATION_PROPOSAL--declare-setting-defaults-on-project-settings-properties.md` | Places Project.Settings defaults on Properties with `?==`. |
| CA-R-2487 | `.../04_requirement/CA-R-2487-CORE_META_MODEL-ENTITY_DEFINITION--define-cfel.md` | Refers to the ordered-assignment Rule. |
| CA-R-2564 | `.../04_requirement/CA-R-2564-CORE_META_MODEL-DECLARATION--declare-project-settings-ai-agent-confidence-threshold.md` | `?== 90` depends on supplying the required Project setting. |
| CA-R-2705 | `.../04_requirement/CA-R-2705-CORE_META_MODEL-DECLARATION--declare-atom-header-label.md` | `$atom.Header.Label ?== $atom.Header.Form` currently supplies Form to an absent Label. |
| CA-R-2711 | `.../04_requirement/CA-R-2711-CORE_META_MODEL-DECLARATION--declare-atom-header-role-plan-header-ai-agent-confidence-threshold.md` | Its LOOKUP/Project-setting chain currently supplies an absent Plan override. |
| CA-R-2768 | `.../04_requirement/CA-R-2768-CORE_META_MODEL-RULE--assign-a-default-when-an-object-property-is-absent.md` | Current conditional-assignment Rule; superseded semantics. |
| CA-R-2769 | `.../04_requirement/CA-R-2769-CORE_META_MODEL-DECLARATION--declare-cfel-operator.md` | Current operator declaration says `?==` conditionally assigns. |
| CA-R-2487@14-draft | `.../04_requirement/draft/CA-R-2487@14-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-cfel.md` | Retains ordered-default semantics. |
| CA-R-2768@3-draft | `.../04_requirement/draft/CA-R-2768@3-draft-CORE_META_MODEL-RULE--assign-a-default-when-an-object-property-is-absent.md` | Retains conditional assignment, chain and missing-final behavior. |
| CA-R-2818@1-draft | `.../04_requirement/draft/CA-R-2818@1-draft-CORE_META_MODEL-RULE--define-conditional-default-assignment-with.md` | Defines `p ?== e` as Model assignment. |

## Non-assigning sources

- CA-A-1321@1-draft and CA-R-2487@15-draft already state the pure result-only meaning and require consumer reconciliation.
- CA-R-2997@1-draft is the pure fallback operator Declaration. It defines left-to-right chain evaluation and no Model or Carrier write.
- Current CA-R-2770 allows `LOOKUP` inside a `?==` fallback expression but does not itself store a value.
- CA-R-2552@5-draft, CA-R-2778@1-draft, CA-R-2957@1-draft, CA-R-2995@1-draft and CA-R-2996@1-draft contain no literal `?==`.

## Indirect policy impact

Current CA-D-485 requires a required Atom value selected by a default to be carried at its internal location. Pure `?==` does not select or store that value, so the policy needs a separate default/value authority before applying.

## Mandatory Form consequence

Current CA-R-2703 requires exactly one string Form. The live Form audit reports 159 Current and 26 Draft carriers without Form. Pure `?==` leaves CA-R-2705's Label absent; a missing Form also leaves no fallback result. This report does not infer a Label/Form/Role chain.

CA-R-2997@1 defines left-to-right `?==` chain evaluation. No Label/Form/Role chain operands or order, source change, runtime change, or workflow change is inferred by this audit. The complete machine-readable paths and line numbers are in `consumer-impact.json`.
