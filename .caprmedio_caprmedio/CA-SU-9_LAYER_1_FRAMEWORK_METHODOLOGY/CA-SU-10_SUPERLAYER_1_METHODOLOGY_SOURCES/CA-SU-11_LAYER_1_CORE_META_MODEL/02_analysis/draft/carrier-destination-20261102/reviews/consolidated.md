# Carrier destination proposal review

Both findings are now fixed and independently re-reviewed. [Final validation](../fixes/yaml-encoding-and-adoption-20261102/verification/final-readback.json). The review below records the pre-fix snapshot; [preserved predecessors](../fixes/yaml-encoding-and-adoption-20261102/predecessors/index.json) retain the original evidence.

Four subagents reviewed the six unchanged Drafts. Result: **two P2 gaps**. No internal contradiction or direct conflict with operative Active Claims was established.

| Review area | Result |
| --- | --- |
| Internal consistency | Container, leaf and Delivery constraints agree. |
| Active authority | The new fields still need explicit registered YAML encoding. |
| Gaps | The proposal needs an explicit population/validation gate before promotion. |
| Ambiguity | Exact serialization remains unspecified. The semantic and storage choices are already settled. |

1. **[P2] Specify the exact YAML encoding.** The generic frontmatter mapping identifies a region, but does not register concrete keys or nesting. A nested map and flat keys can therefore produce incompatible carriers. Add explicit Delivery mappings for the agreed `carrier_destination.file.name` and `carrier_destination.file.path` keys. This records the user's existing decision; it requires no new choice about mandatory values, storage or Carrier meaning.

   Evidence: [CA-D-478@31](../../../../07_delivery/CA-D-478-CORE_META_MODEL-ENG_DECISION--store-every-atom-property-in-one-internal-location.md) (Claim, lines 31–40), [D664 Draft](../../../../07_delivery/draft/CA-D-664@3-draft-CORE_META_MODEL-ENG_DECISION--deliver-atoms-to-markdown-files.md) (lines 32–39), [CA-D-657@2](../../../../07_delivery/CA-D-657-CORE_META_MODEL-DECISION--yaml-frontmatter-encodes-atom-properties-with-minimal-syntax.md) (Claim, lines 29–38; Details, lines 44–52). The stronger admission-invalidity language is in Details, so this review reports an encoding gap rather than a proven Claim-level rejection.

2. **[P2] State the adoption gate.** The Properties are mandatory, but the Adoption paragraph leaves population and migration as separate work without stating what must be complete before promotion. Existing Current Atoms lack the new fields. Require the agreed encoding and population/validation of affected carriers, or an explicitly governed transition boundary, before activation. Detailed migration mechanics remain Workflow/Engine work.

   Evidence: [Name Declaration Draft](../../../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination-file-name.md) (lines 21–26), [Specification Proposal](../../CA-A-draft-CORE_META_MODEL-SPECIFICATION_PROPOSAL--declare-stored-atom-carrier-destinations.md) (lines 45–47), [CA-R-2508@2](../../../../04_requirement/CA-R-2508-CORE_META_MODEL-DECLARATION--declare-atom.md) (existing frontmatter, lines 1–20). This is an adoption-readiness gap, not a defect in saving Drafts.

The review preserves the settled design: Name includes the extension; Path is the repository-relative containing directory; both are calculated, mandatory single strings stored in frontmatter. Existing Carrier meanings, filename rules and placement rules remain applicable.

Observed-first address adoption was rejected as contrary to the user decision and CA-D-480. Calculation timing belongs to later operational work. No separate current ambiguity was established for future root-level layouts, repeated CARRIES facts, Property/Carrier conflation or Draft markers.

All six Draft hashes and all 1,128 selected Current source hashes remained unchanged. No fixes, promotion, migration or runtime tests were performed. The creation-time Engine preflight block was not retested and is separate from these two findings.

Detailed lane evidence: [internal](internal.json), [Active authority](active-conflicts.json), [gaps](gaps.json), [ambiguity](ambiguity.json). Machine-readable consolidation: [consolidated.json](consolidated.json).
