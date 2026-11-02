---
atom_id: CA-A-1305@6
content_role: Analysis
type: Spec Proposal
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
tier: 3
version: 6
updated_at: 2026-10-29 09:04:03 +0400
subjects:
  governs: Entity
relations: {}
---
### Summary

Track Entity candidate implementation Questions

## Latest candidate

[CA-A-1302 — Entity graph candidate with four root branches](draft/CA-A-1302@1-draft-SPECIFICATION_PROPOSAL--entity-graph-candidate-with-four-root-branches.md), with A1303/A1304 refinements. The Operator’s latest words override older decisions; implementation evidence uses only the last 48 hours. This proposal tracks every Question created while implementing CA-P-2683.

## Questions and chosen continuation

- [CA-C-605 — Where should Term and Selection belong under Entity?](../01_concern/CA-C-605-QUESTION--where-should-term-and-selection-belong-under-entity.md): Keep the existing persistent Term and Selection classifications under Object/Continuant for this migration. This preserves the latest explicit lower-level tree instead of adding a fifth root. The four-root candidate left their exact placement open; this choice is provisional and does not implement the Terms Graph.

- [CA-C-606 — Does a zero-direct-value property need a value Format?](../01_concern/CA-C-606-QUESTION--does-a-zero-direct-value-property-need-a-value-format.md): For a grouping property with cardinality {0}, state that a direct-value Format is not applicable; define the Formats of its children independently. Do not invent void/list/map as Formats. This reconciles the required property coverage with the approved direct-value semantics.

## Boundaries

The six legacy Graph Rule Subject paths are held for source-specific preservation/retirement during the Definition pass. Missing-ID legacy RMED carriers without Subjects are explicitly unchanged in the Subject-only pass. Neither creates a new entity or requires Engine changes. The Current frontier is 1,100 RMED carriers; 17 legacy records have no explicit Atom ID or Subjects. Existing archived/draft carriers and Engine sources are excluded.

- [CA-C-607 — legacy generic Node/Project Model targets](../01_concern/CA-C-607-QUESTION--which-targets-replace-generic-node-and-project-model-subjects.md): use Entity for the old generic Subject/Node, and Object/Continuant for the persistent grouping during the mechanical pass; narrow or retire actual defining sources during coverage.

- [CA-C-608 — duplicate Terms Projection kind](../01_concern/CA-C-608-QUESTION--does-terms-projection-need-a-separate-kind.md): reuse existing Projection/Type: Terms Graph; leave the duplicate Draft unpromoted. Terms Graph implementation remains deferred.

## Stage 3 chosen continuations

- [CA-C-609 — Should all derived reverse views have a name?](../01_concern/CA-C-609-QUESTION--should-all-derived-reverse-views-have-a-name.md): Keep the direct Relation Types and derive their reverse lookup. Preserve already declared inverse names such as CONTAINS, BEARS and IS_CARRIED_BY. Do not invent a second name or stored fact where the Current definition declares no inverse name. This supplies every reverse view without introducing aliases. The open choice is whether those unnamed views need separate names later.

- [CA-C-610 — Which Runtime owns automatic context initialization?](../01_concern/CA-C-610-QUESTION--which-runtime-owns-automatic-context-initialization.md): Preserve legacy REQU-507's automatic session/context initialization commitment as a framework outcome, rather than dropping it for a malformed header. Use the existing Runtime/Session vocabulary and leave its concrete implementation owner to the later Engine Epic. This does not add a Session Engine entity or implement startup code.

- [CA-C-611 — How should installed Extension lifecycle be represented?](../01_concern/CA-C-611-QUESTION--how-should-installed-extension-lifecycle-be-represented.md): Preserve legacy REQU-697's install, uninstall, update and downgrade commitment. Govern the framework capability and refer to the existing installed-Extensions Scope Units; do not introduce another Extension object or application-binding system. Concrete execution belongs to the later Engine work.

- [CA-C-612 — generic Execution Result value Format](../01_concern/CA-C-612-QUESTION--how-should-unconstrained-execution-result-values-be-formatted.md): use the reusable scalar Format and direct-value cardinality; retain producer-specific output constraints.
