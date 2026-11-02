# Invariants, Operations and the Atom version key — 2026-10-31

Processes belong to Operations. RMED states invariants. This pass adds no Workflow Rules, Workflow instances or before/after CFEL language.

## Static version constraints

The existing [Atom Declaration](../../../04_requirement/draft/node-declaration-20261031/primary-expansion/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-atom.md) now states:

```CFEL
Atom;
UNIQUE(Atom//, (.ID, .Version))
```

The tuple is globally unique inside the selected Project across Draft, Current and Archived instances, regardless of containment. Different IDs may reuse a version number; the same ID may have different versions. Distinct instances may not share both values. Repeated Carrier representations of one instance are not additional instances, and equal tuples cannot be used to silently merge distinct instances.

The new [generic tuple-uniqueness Rule](../../../04_requirement/draft/node-declaration-20261031/CA-R-draft-CORE_META_MODEL-CFEL--require-unique-property-tuples.md) requires a complete resolved population and one valid scalar per key component. It validates a constraint; it does not allocate or change values.

The unpublished [Version Declaration](../../../04_requirement/draft/node-declaration-20261031/property-expansion/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-atom-version.md) replaces the former Atom.Version Number spelling. Its one-positive-integer/no-child contract is unchanged. No Current Property was renamed and no alias was introduced.

## Operations behavior retained in the proposal

On promotion, calculate the maximum Version across all logical instances with Atom.ID = X inside the Project, including Draft, Current and Archived instances and the Draft being promoted. Assign that maximum plus one. There is no Current-only filter, preservation of a Draft's proposed number, or search for the smallest unused gap.

```text
$last_version = max(atom.version) where atom.id = X;
$new_version = $last_version + 1;
```

| Before promotion | Selected Draft | Maximum Version | Promoted Current version |
|---|---|---|---|
| Current 5; Drafts 6 and 7 | Draft 7 | 7 | 8 |
| Current 8; remaining Draft 6 | Draft 6 | 8 | 9 |
| Current 7; Drafts 6 and 8 | Draft 6 | 8 | 9 |
| Current 7; Drafts 6 and 12 | Draft 6 | 12 | 13 |

Recheck the same-ID version population when committing promotion. These examples are pseudocode cases, not runtime results. The max(all versions) + 1 rule supersedes the earlier keep-proposed/next-free behavior. The pseudocode belongs to the promotion Workflow and does not extend the invariant CFEL language.

Version-change and Project.Settings input-selection instructions were moved out of Property Declarations and preserved verbatim in the proposal's Deferred Operations notes and [relocation receipts](declaration-expansion/invariant-process-result.json). Timestamp meaning, no-op/archive preservation and identity invariants remain in RMED. Nothing was deleted merely to improve the formal-only count.

## Conditional constraints

Active Subject now uses an IF/THEN required-count conclusion. Essential prose still limits that conditional to complete Atoms; the base optional count preserves incomplete Draft omission. No completeness flag or unbound selector was invented. Semantics classification, Goal ownership and notation admission still need their bindings before full translation.

## Coverage and review

- 100 registered Drafts: 23 Primary and 45 Property Declarations, plus supporting Drafts.
- 43 formal-only Claims across the packet, up from 41 before this pass and 37 before the formalization work. Two newly formal-only Claims result from explicit Operations relocation, not new grammar.
- 25 Claims still contain prose in Node descendants and their Properties: 4 Primary and 21 Property. Including Node itself gives 26.
- All 23 brief Primary Semantics sections are unchanged. There are no Property Semantics sections or Author metadata fields.
- Structural, register-hash and local-link checks pass. The Operator registry, 11 specifically pinned Current sources, all 750 snapshotted Current Core Requirement sources and Current Epic version 37 remain unchanged.
- Independent Terra review passed the process relocation, corrected partial conditional, generic uniqueness Rule, Atom consumer and Project scope. The promotion rule was subsequently changed by the Operator to max(all versions) + 1; the four example results above were checked against that formula.

See [coverage evidence](declaration-expansion/invariant-operations-result.json), [rename mapping](declaration-expansion/version-property-rename.json) and [version-key decision](declaration-expansion/project-version-key-decision.json).

## Limits

This is proposed source. No parser, runtime, allocator or storage migration was changed or tested. The prepared carriers still use unnumbered placeholder markers such as CA-R-draft; allocate unique IDs and rebind references before governed Draft admission. The new Project-wide key constraint is not claimed to pass on those placeholders. Current Author-required carrier rules, exact Subject/reference bindings and Relation-whitelist gates also remain open.
