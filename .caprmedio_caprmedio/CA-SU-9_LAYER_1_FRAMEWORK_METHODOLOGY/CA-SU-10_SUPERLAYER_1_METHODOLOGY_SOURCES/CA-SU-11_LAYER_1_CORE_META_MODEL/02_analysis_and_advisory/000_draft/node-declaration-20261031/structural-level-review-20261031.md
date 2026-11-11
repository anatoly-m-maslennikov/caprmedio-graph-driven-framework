# Structural levels and root kinds — 2026-10-31

Scope Unit.structural_level and Package.structural_level are the number of immediate-parent links to the root. Both values derive solely from IS_CONTAINED_BY links.

| Hierarchy | Root kind | Root level | Other nodes |
|---|---|---|---|
| Scope Unit | Scope Unit/Project | 0 | One immediate Scope Unit parent |
| Package | Package/Implementation | 0 | One immediate Package parent |

For each actual containment link:

```CFEL
IF (Package//$child ((IS_CONTAINED_BY)) Package//$parent)
THEN ($child.structural_level = $parent.structural_level + 1)
```

The same invariant applies to Scope Units. The condition matches actual links, not every possible child/parent pair. Parent reverse counts are explicitly zero or more. The values are required, childless, nonnegative integers in the logical model. Storage and adapter derivation remain future implementation work.

## Kind membership

Implementation is a narrower Package kind. Its instances have no Package parent. The non-root rule uses instance-set membership:

```CFEL
IF (Package//$package not in (Package/Implementation//))
THEN ($package {==1}((IS_CONTAINED_BY)) Package//)
```

The new instance-binding Rule covers narrower-kind instances and same-instance Property access. The numeric Rule adds only binary numeric addition; equality remains a constraint, without assignment.

Each Project has one root Implementation. `Package/Implementation//{:1}` now expresses this with the shared cardinality mechanism. The selected population is the complete current Project; logical instances are counted once.

## Why recursive Relation syntax is unnecessary here

A cycle of k containment links implies L = L + k, with k > 0. Exact integers cannot satisfy that equation. Nonnegative integer levels, zero roots and one parent per non-root also require the chain to reach a root.

The unpublished recursive-path Rule was withdrawn before registration. Its [research snapshot](declaration-expansion/withdrawn-recursive-path-proposal.json) is retained. Existing Property .** and narrower-branch /** syntax is unchanged.

## Review and scope

Independent Terra review passed the root exclusions, polymorphic membership, actual-link binding and integer acyclicity argument. One finding was corrected: both Property Claims now explicitly state the derivation source. Root parent exceptions remain intact. Existing brief Semantics were preserved; Implementation has a brief root meaning.

CA-R-2239 remains unchanged. Its selected root structure is reflected in the target Implementation kind; its realization, direct-editability and nonautomatic-Projection clauses remain explicitly unmigrated. See the [source pin](declaration-expansion/implementation-legacy-source-pin.json).

The latest selected packet contains 105 Drafts: 24 Primary and 47 Property Declarations. The additional Rule applies active-Subject focus across all Roles and Forms. Implementation singleton selection is now formal. Counts and exact residual prose appear in the current inventory. See the [current exact excerpts](remaining-node-claim-prose-20261031.md).

Metadata, registry hashes, local links and bounded Draft structure checks pass. All 750 snapshotted Current Core Requirement sources and the Operator registry are unchanged.

## Epic successor refresh

The older protection snapshot expected Current Epic 37. Current has since advanced to 38 with a content-restoration record. The unpublished successor was refreshed from Draft 38 to Draft 39, carrying that record and all pending model notes. Current 38 was not edited or promoted by this work. An independent Luna audit verified the refresh and navigation. See [refresh evidence](declaration-expansion/epic-successor-refresh.json).

No Current adoption, parser, runtime, allocator or storage migration was performed. Prepared ID markers still require allocation before governed admission; active Author-required carrier rules, exact bindings and whitelist coverage remain migration gates. These Draft checks do not establish live enforcement.
