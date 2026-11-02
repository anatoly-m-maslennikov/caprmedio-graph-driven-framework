---
atom_id: CA-A-1305@8
content_role: Analysis
type: Spec Proposal
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
tier: 3
version: 8
updated_at: 2026-10-29 10:36:14 +0400
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

## Property and Relation completion choices

- [CA-C-613 — Confirm minimal shared Property value schemas](../01_concern/CA-C-613-QUESTION--confirm-minimal-shared-property-value-schemas.md): The implementation uses string for identifiers/names/locators, integers for counts, optional explicit Scope Unit Label, and one or more string values for an ordered Scope Unit Path. Settings/registry/configuration groups have zero direct scalar values; their children keep independent counts. Producer- or invocation-specific properties read within their defining Claim scope. These choices complete the existing model without new stored fields or advanced conditions; change them only if a concrete source requires a different shape.

- [CA-C-614 — Does a concrete Relation connection need a separate kind?](../01_concern/CA-C-614-QUESTION--does-a-concrete-relation-connection-need-a-separate-kind.md): For now an actual directed connection remains the tuple (source, Relation Type, target), without a new Connection entity or separate ID. R2247 preserves source/target reference meanings; R1986 and R1987 were retired because those are not reusable Type metadata. Existing direct facts and derived inverses stay governed. A separate endpoint-record kind can be reconsidered only if a concrete operation needs it.

## Actual readback reference disposition

- [CA-C-615](../01_concern/CA-C-615-QUESTION--should-legacy-concern-resolution-links-be-restored-as-history.md): Remove the three unresolvable legacy resolution_of links from Current R1646, R1647 and R1648. Their Current Claims remain unchanged; the exact former links remain in the newly preserved predecessors and Journal history. Do not invent canonical Concern IDs or migrate C/A. If those old Concern records are recovered, consider source-traceable historical references rather than guessing a Current native target.
