# Current Core Entities Graph review

Task: CA-P-1905. Observed: 2026-10-10, Asia/Tbilisi.
This is derived review evidence, not source authority, native graph admission or candidate acceptance.

## Result

The saved Step 1 graph reproduces exactly from the current registered Core Meta-model. No source, selection, producer-profile or output drift was found. A complete baseline inventory is saved in [baseline.inventory.json](baseline.inventory.json).

The current graph is a literal Subjects projection. Its roots and links are not yet ontology decisions. No slash classification, Continuant/Occurrent grouping, inheritance, consolidation, deletion or Subject migration was performed.

## Source boundary and pins

- Scope Unit: CORE_META_MODEL by itself; exclude Project Configuration and Extensions.
- Authority: `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL`.
- Project Structure SHA-256: `3783b6f5dad78f5822677577e2f449d17eab6cccdb087ebb96a3d1d0905b335c`.
- Frontier SHA-256: `7792e842cfe6c66320745660e69cd0df5525ec18bb22b5c060a6ddfff5fc97f7`.
- Selection SHA-256: `f72964ad096a671d0c36cc0cf6649cf2cf131110edb57446fb523dc5feedb840`.
- Collection SHA-256: `5ebcf48d24841b65ba46ffdd113e964fe10a53da80a40db32cefedc484ae7d3d`.
- Producer-profile SHA-256: `217ac612cfe4e401dbd7b560d25cf6093c52fcfbb00961a74401a1b7ccd732b1`.
- Step 1 graph fingerprint: `0ea18486fd43ccd546a5d09888e98bc42f56d42d392e5669fecee19fa25f93d1`.
- Step 1 JSON file SHA-256: `57cba13073aa0de34876a734c784a43d124f09ff03584de03252b9d12a89ac0b`.
- Entities DOT file SHA-256: `2754760bde5bce25b9500682d2af71a819b34df342e1da5cf4a91ec2a5cf48dd`.
- Terms DOT file SHA-256: `41dc2e8befbf0a91b40cf5ca90858e4916c8c08e98fac16ff7555d0ce7ee6ebc`.
- Baseline inventory fingerprint: `23394abaf6e9c18a585cf3146aedd0a80df166c9dd82be6e86ed7c3c56780bdc`.

The inventory carries every selected and excluded source pin, all original occurrences, all model nodes/edges, and the complete original relation-segment coordinates. Its digest excludes only its own `inventory_sha256` field.

## Complete baseline counts

| Item | Count |
|---|---:|
| Captured Core source files | 951 |
| Selected exact-Active owned-Core sources | 908 |
| Excluded sources | 43 |
| Subjects occurrences | 4,534 |
| GOVERNS occurrences | 908 |
| DEPENDS_ON occurrences | 3,626 |
| Distinct GOVERNS paths | 561 |
| Full/prefix nodes | 706 |
| Full-target nodes | 673 |
| Supporting-prefix-only nodes | 33 |
| Unclassified unique slash links | 294 |
| Unique colon links | 66 |
| Original slash segment occurrences | 2,275 |
| Original colon segment occurrences | 818 |
| Total original relation-segment occurrences | 3,093 |
| Qualification roots | 346 |
| Roots with qualified descendants | 53 |
| Standalone roots | 293 |
| Repeated literal leaf-label groups | 74 |
| Literal Term components | 534 |
| Term taxonomy edges | 0 |
| Unresolved source extraction | 0 |

“Qualification root” means no parent in the literal prefix chain. Colon chains are counted Property-prefix to value for this display measure, although the stored possible allowed-value edge points value to Property. It is not a count of independent ontology entities. Repeated leaf labels remain separately qualified; none were merged.

## Current graph limitations

1. A slash link is UNCLASSIFIED. For example, `Atom/Content Role: Operations/Type` has 29 source occurrences, including CA-D-457@6. Syntax alone does not decide narrower-than or bearer qualification.
2. Colon syntax is not assignment or proof of native Property/value admission. `Projection/Type: Reconciled Projection` has six supporting occurrences, including CA-O-004@5.
3. Supporting prefixes are generated for navigation. `Applicable Methodology Compilation/Step`, supported by CA-O-153@2, does not become an admitted independent Entity just because a longer path names it.
4. Equal component strings need separate ownership checks. `Type` occurs across 67 qualified paths, `Carrier` across 45 and `Status` across 24. No global field merger follows.
5. Definition labels and run labels coexist. Action, Step and Workflow references must not be conflated with Action Run, Step Run and Workflow Run references. CA-O-161@2 supplies examples of both.
6. DOT and tree views omit some provenance and flags. Use the JSON occurrence IDs and source references for review and migration evidence.
7. Bare names, case variants and helper labels are not automatically independent model entities, aliases, meaningless nodes or drop candidates. Main Content review must decide or leave them explicitly unresolved.

## Definition evidence available for the next Task

This is a bounded evidence register, not a claim that every node has an admitted definition.

| Concept | Current Core source | What is available |
|---|---|---|
| Atom | CA-R-655@23, Claim line 26 | Definition as the smallest independently governed Artifact |
| Artifact | CA-R-1268@12, Claim line 29 | Persistent governed identity across Artifact Revisions |
| Scope Unit | CA-R-1757@17, Claim line 29 | Ownership boundary for Atoms and child Scope Units |
| Property | CA-R-1193@11, Claim line 28 | Dependent Entity characteristic of a bearer |
| Carrier | CA-D-414@14, Claim line 28 | Explicit classification as a Primary Entity; do not merge with qualified Carrier bindings |
| Applicable Methodology | CA-R-1213@17, Claim line 36 | Non-authoritative Reconciled Projection constraints |
| Workflow Run | CA-R-1510@4, Claim line 30 | Specific run definition |
| Step Run | CA-R-1511@5, Claim line 32 | Specific run definition |
| Step Run/Invocation | CA-R-1789@1, Claim line 36 | Invocation payload constraint; no automatic relation classification |
| Artifact/Revision | CA-R-1371@10, Claim line 27 | Artifact Revision definition; other qualified Revision labels remain distinct |
| Terms Graph | CA-R-1335@13, Claim line 32 | Specific graph definition |
| IS_BORNE_BY | CA-R-1260@13, Claim line 31 | Specific relation definition |

Resolve each ID/revision through `source_atoms` in the inventory for its exact current Carrier path and SHA-256. Literal names such as Run, Invocation, Graph and Relation do not establish a generic definition or supertype by themselves.

## Operator inputs and precedence

Edited draft:
`/Users/am/.codex/attachments/cf8361d3-bff7-4048-a21f-e8f74e14c668/Pasted text.txt`
SHA-256 `b3ba990ebb0d5f570f6aac2a42bf067ce855bb3810304e29b523e59fd29fbf68`; 14,340 bytes; 1,081 lines.

Valid literal tree:
`.caprmedio_caprmedio/_projection/core-subject-notation/step1.entities.indented.txt`
SHA-256 `05c915b23f3679b44f3c69ecdd96abaf0d663d229c9c503b9e7ba7f2ea390e89`; 14,110 bytes; 1,056 lines.

The draft is edited modelling input, not the unchanged projection or source authority. Its Continuant/Occurrent groups, Actor/Artifact nesting and question marks are design intentions only. The dirty `step1.entities.tree.txt` was not edited or used.

Latest Operator decisions override older draft text:

- Group the candidate by Continuant and Occurrent.
- Inherit common constraints, not another Entity's concrete Carrier.
- Minimize genuine roots without forcing invented relationships.
- Review every entity for duplicates, redundancy, empty/no distinct meaning and generalization.
- Mark Revision as a candidate for consolidation with Version Number and Updated At; preserve history.
- Evaluate Applicable Methodology as a general Projection/single-document candidate, not a source Atom set. This is concept review, not full methodology compilation.
- Use `/` for broader to narrower, `.` for general bearer qualification, `:` for allowed values, and `@` for IS_CARRIED_BY display.
- Use concept names Version Number, Updated At and Status. Do not rename YAML keys.

Later input for CA-P-1906: consider content-role and Internal/External/Relational views or node types, including method-related roots for M and carriers in D. This is an additional design question; no view, entity partition or new root was adopted in this baseline review.

## Verification and handoff

Fresh read-only regeneration matched the complete saved Step 1 JSON and both DOT serializations. The inventory producer checked all 951 source hashes, Project Structure and producer components before and after generation. It retained all 706 nodes, 360 syntax edges and 4,534 original occurrences, and expanded all 3,093 relation segments with exact Subject property/item coordinates.

No extraction defect was found within the mechanical contract. Semantic gaps above are handed to CA-P-1906; no uncertain interpretation was selected. CA-P-1906 must supply source-backed proposals or explicit unresolved/not-native rows with reasons and questions. Candidate design and later approval/migration gates remain pending.

This local evidence has no MCP Run, Journal or native-admission receipt.
