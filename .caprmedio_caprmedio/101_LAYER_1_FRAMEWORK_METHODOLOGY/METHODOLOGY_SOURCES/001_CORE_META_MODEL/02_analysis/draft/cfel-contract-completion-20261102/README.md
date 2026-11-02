# Model and CFEL migration — completed

The authorized Epic work is applied and checked against Current carriers. [CA-P-2694@40 is Done](../../../../../../03_plan/done/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing.md).

- 257 Draft promotions; 209 preserved predecessors; 10 obsolete Current Atoms retired.
- 267 source Journal events record the accepted changes.
- All 31 starting narrowing-tree diagnostics resolved.
- 41 canonical and derived Relations have Requirement / Declaration owners, Semantics, signatures and formal metadata.
- The Current frontier contains 1,137 unique RMED sources.
- The narrowing tree contains 54 nodes and 46 NARROWER_THAN links.
- Contract display has zero binding gaps, duplicate Declaration owners, missing Relation Semantics or inheritance diagnostics.
- The graph tool suite passes all 358 tests. Source-profile path updates preserve drift checks; the historical 90-Declaration snapshot remains a historical fixture.

## Views

- [CA-PROJ-018 — narrowing tree](../../../../../../_projection/CA-PROJ-018-CAPRMEDIO--Entities-Graph--Current-Subject-Narrowing-Tree.md)
- [CA-PROJ-019 — full formal contracts](../../../../../../_projection/CA-PROJ-019-CAPRMEDIO--MODEL-Formal-Contracts.md)

CA-PROJ-014–017 are also refreshed. Projection Form is Map; sources use `Source.Named Selection` and versioned `Source.Atoms`. The unchanged CA-PROJ-017 follows its initial receipt; the other five follow the later receipt.

## Evidence

- [Bulk lifecycle receipt](integration/publication-receipt.json)
- [Three CFEL editorial follow-ups](integration/source-cleanup-receipt.json)
- [Current source frontier](integration/current-source-frontier.json)
- [Current contract register](integration/current-contract-register.json)
- [Projection follow-up receipt](integration/projection-followup-receipt.json)
- [Current lifecycle readback](verification/final-current-lifecycle-readback.json)
- [CFEL readback](verification/final-cfel-readback.json)
- [Projection readback](verification/final-projection-readback.json)
- [Test evidence](verification/final-tests.json)

Exact inspected bytes are retained in `integration/frozen-sources`; archives preserve predecessor Version, Updated At and content. The selected Drafts are consumed. Independent source and scope reviews remain alongside their packet manifests.

## Remaining boundary

The view preserves 137 formal clauses outside the bounded extractor. Complete display coverage establishes that source content is present; it does not establish full CFEL evaluation. All 367 selected sources outside the declared model remain explicit evidence.

Actual Workflow-instance migration and general runtime admission remain separate Engine work. Twelve nonblocking Questions retain the bounded choices made under the Operator’s latest fallback instruction:

CA-C-618; CA-C-619; CA-C-620; CA-C-621; CA-C-622; CA-C-623; CA-C-624; CA-C-625; CA-C-626; CA-C-627; CA-C-628; CA-C-629.

## Follow-up — Property selectors

The Operator confirmed recursive aggregation and direct-child selection. CA-R-2472@8 adds selector composition; CA-C-624@3 is Resolved. [Follow-up evidence](../property-selectors-20261102/README.md). Current source vectors and contract views are repinned by [the selector receipt](integration/projection-selectors-receipt.json).

C618 is Resolved: rollback information belongs to its Release. The obsolete block is removed from Framework Settings and its source template; existing release evidence is retained.
