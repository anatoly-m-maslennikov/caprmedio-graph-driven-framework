# MODEL content, aliases and counterparts

## Operator decisions

The latest Operator input supersedes conflicting earlier model and carrier-layout rules.

1. Separate the Atom into `Atom.Header` for the YAML/frontmatter fields and `Atom.Content` for Markdown content. Both groups and their children are Atom Properties. The Operator chose Header / Content; Metadata and Frontmatter are not the model group names.
2. `Atom.Content.Claim` is a grouping Property with direct-value cardinality `[]{:0}`. Its direct children have string names selected from Formal Claim and Prose Claim, with total occurrence cardinality `{:1..2}`. Names remain unique under the same bearer. Both child values are Markdown; Formal Claim contains a CFEL fence.
3. Remove the declared `Atom.Content.Claim Scope` Property. Preserve relevant existing applicability text according to the selected relocation rule; the destination is Prose Claim.
4. Declare symbolic relation aliases. The proposed formal form is `alias(Relation//CONTAINS) == "<+"`. These are notation aliases, not alternative names for model entities.
5. Record relation counterparts in their declarations. `<-->` is the proposed Subject notation for the counterpart/inverse binding. CONTAINS and IS_CONTAINED_BY remain distinct Relations. Each side has its own Declaration; the direct side carries the shared meaning and binding. The derived side is minimal and carries its own symbolic alias when one exists. A counterpart without an alias, such as the counterpart of `/`, has a minimal Formal Claim containing the reverse view of its counterpart binding. Ordinary Claim child rules apply; no empty-Claim exception is introduced.
6. Markdown headings do not declare Properties. Explicit paths such as `Content.Claim.Prose Claim` identify Properties; wildcard constraints constrain declared Properties and do not introduce arbitrary named model entities. Subheadings inside Prose Claim remain part of its Markdown value when they are not declared child Properties. Wildcard constraints apply only to declared Properties.
7. `Node.**` covers all Properties of Node and its branch through inheritance. Use it for Rules about that whole scope; do not introduce a primary Property kind.

Canonical `IS_CONTAINED_BY`, the MODEL/STRUCTURE split and the distinction between graph Relations and other CFEL operators remain established. Completed Scope Unit/TOML work and its active P2707 verification are preserved.

## Header migration map

The model group names are settled:

- `Atom.<YAML field>` → `Atom.Header.<same field>`.
- Nested fields retain their suffixes, such as `Atom.Relations.IS_CONTAINED_BY` → `Atom.Header.Relations.IS_CONTAINED_BY`.
- Existing `Atom.Content` remains the Markdown group.
- Update property-qualified model references consistently, such as `Atom/(.Role: Method)` → `Atom/(.Header.Role: Method)`.

This map groups model Properties by their declared carrier region. Physical YAML wrapping or other instance-data migration is not inferred from the name choice.

## Claim shape

Operator-approved structure:

```CFEL
Atom.Content.Claim: []{:0};
Atom.Content.Claim.*[string, in (Formal Claim, Prose Claim)]{:1..2}
```

The container has no direct value. One or both named children exist, with no repeated sibling name. This records the chosen structure; both children use Markdown values; the Formal Claim holds a CFEL fence.

## Completed immediate task

P2709 simplified only frontmatter `subjects.active` and `subjects.passive`: `CAPRMEDIO <+ MODEL` → `CAPRMEDIO_MODEL`, `CAPRMEDIO <+ STRUCTURE` → `CAPRMEDIO_STRUCTURE`. Applied and independently verified for 1,178 files / 3,685 values. Other bytes were preserved. See root-subject-migration-20261103 receipts.

## Relation formal syntax

- `Relation//NAME` refers to a declared Relation object.
- `Source {:left}((NAME)){:right} Target` uses a Relation; each bound is optional and retains its endpoint meaning. `Object ((NAME)):{...}` is invalid.
- `Relation//DIRECT ((HAS_INVERSE)) Relation//DERIVED` binds counterparts. The derived Declaration uses the reverse written view of that same binding.
- `alias(Relation//NAME) == "glyph"` binds symbolic notation; `<-->` is the HAS_INVERSE/counterpart Subject notation, not identity equality.
- The `@` reference marker is removed from the new grammar. Atom identity/version tags such as `CA-P-123@1` remain unchanged.

## Ordered execution

### 1. Update/create the Declarations

- Resolve the pending choices one at a time. Create/update the model Property, alias/operator and counterpart Declarations; retire the removed Claim Scope declaration.
- Reconcile the affected R/M/E/D authoring and carrier-layout rules with the new Declarations. Preserve operative constraints when replacing old wording.
- Keep the full direct-relation meaning in its Declaration. Derive counterpart meaning and direction from its declared binding; keep the counterpart's own Declaration minimal.
- Record exact affected Atom IDs, source pins, old-to-new paths and required consumer/profile changes. Use inherited declarations rather than copied child declarations.
- Review the resulting packet for internal conflicts, active-Subject ownership, formats, cardinalities, declaration coverage and latest-Operator alignment.

Acceptance: decisions are settled; the declaration/rule packet and exact migration map are coherent and reviewable. No concrete carrier migration is counted as completed here.

### 2. Commit and push everything to amm/dev

- Coordinate concurrent writers, preserve their work and capture the complete authorized worktree at the checkpoint.
- Commit and push to `amm/dev`; record the local commit and matching remote commit.
- Preserve the Operator's disabled-hook setting.

Acceptance: the declaration checkpoint is on `amm/dev` remotely before step 3 starts. This checkpoint is distinct from the later migrated working state.

### 3. Mechanical migration in place

- Freeze the exact source/consumer frontier and before hashes from the accepted map. Preserve historical snapshots.
- Apply the mechanical path, Claim-layout, notation and reference changes in place as requested. Preserve the underlying Claims and relation facts.
- Apply only the affected reader, checker, renderer, fixture and authority-pin changes required by the adopted contracts. Historical semantic profiles keep their historical pins unless explicitly advanced.
- Rebuild the affected Subject/MODEL projections from their actual selected source Declarations. Preserve unsupported expressions as diagnostics.
- Hold unresolved semantic transformations instead of treating them as mechanical substitutions.

Acceptance: every selected item has an applied or explicit held disposition; identity/history and Claim text have verified preservation; affected consumers use the chosen contract. No migration beyond the agreed frontier is inferred.

### 4. Check the migration

- Read back all selected source changes and declared Property paths. Check preserved fields/text and removed Claim Scope paths.
- Test the new Claim container and chosen child counts/formats. Verify Formal Claim extraction and that undeclared headings inside prose remain Markdown.
- Verify alias resolution, `<-->` counterpart bindings, distinct identities on both sides, minimal derived declarations and unchanged one-fact inverse semantics.
- Check inherited formats/cardinalities, exact Declaration provenance and actual-source projections.
- Run focused consumer/profile tests with both valid and invalid examples. Record failures and held items; a generated graph alone is not completion.

Acceptance: the source, consumer and projection checks pass for the exact frontier. Existing unrelated P2707/Engine blockers remain separately tracked. Step 2 records the pre-migration remote checkpoint; step 4 records the checked migrated state.

## Pending choices, asked one at a time

| ID | Choice | State |
| --- | --- | --- |
| Q1 | YAML group name | Resolved: Header / Content |
| Q2 | Formal Claim / Prose Claim child presence | Resolved: 1..2 children; names Formal Claim or Prose Claim; Claim has zero direct values |
| Q2b | Formal Claim / Prose Claim value formats | Resolved: retain Markdown values; Formal Claim contains a CFEL fence |
| Q3 | Destination of existing Claim Scope applicability text | Preserve in Prose Claim during the mechanical move |
| Q4 | Minimum valid derived Declaration when no symbolic alias exists | Resolved: Formal Claim states counterpart binding; no exception |
| Q5 | Whether wildcard constraints declare new Properties | Resolved: constrain declared Properties only; titles alone are not Properties |

The counterpart notation is an inverse/counterpart binding, not equality of Subject identities. The exact alias and counterpart grammar is specified in step 1 under the latest decision, not inferred from old syntax.

## Source and consumer inventory

Candidate model sources: R2508; R2488–R2507; R2545/R2546; R2692–R2695. Core content targets are R2498–R2503. Retain R2499/R2502/R2503 meanings while reviewing their placement and open-child contracts.

Conflicting layout/authoring sources include D479, D495, D482, D478, D664, R1417, R2102, R718, R796, R2471, M228, M264 and E240. This is a candidate inventory; step 1 pins the actual accepted set.

Counterpart/alias sources include R2478, R2617, R2485, R2170, R2486, R2588, R2247, R2487 and R2609. Review other inverse Declarations for duplicated endpoint, derivation and meaning text.

Required consumer review covers VALIDATE_ATOMS section/schema checks, its authority-bound registry and fixtures, and GENERATE_ENTITY_GRAPH Claim parsing/rendering and semantic-profile pins. Implement only changes required by this migration; no new Tool, MCP, runtime or release feature is introduced.

## Lane table

| Deliverable | Owner | Exclusive edit scope | Dependencies | Acceptance | State |
| --- | --- | --- | --- | --- | --- |
| Atom/Claim model inventory | issues_property_contracts | Read-only | Current sources | Exact targets, conflicts and choices | Done |
| Alias/counterpart model inventory | relation_declaration_packet | Packet only | Latest counterpart interpretation | Exact bindings and minimal-derived claims | Done |
| Markdown consumer inventory | issues_projection_accuracy | Read-only | Current readers and authority pins | Bounded migration/check impact | Done |
| Source/Epic boundary inventory | graph_source_coverage | Read-only | Current plans and model sources | Preserve completed work; correct phase order | Done |
| Epic and decision integration | root | P2694, its new archive and this follow-up | Lane returns and Operator choices | Correct sequence and honest status | Running |

## Current status

Header / Content and the Claim child-presence rule are decided. Claim has zero direct values and one or two named children. Current decisions cover the value formats, Claim Scope relocation, counterpart binding and declared-Property rule. Packet reviews and exact consumer alignment continue before declaration adoption. The new commit/push checkpoint and migration have not started. Existing completed work is retained, and P2694 remains Active.

## Applied Declaration checkpoint

87 Current outputs were applied manually with 86 exact-byte predecessor archives. 23 Header identity replacements and four new Declarations use CA-R-2696–CA-R-2722. R2501, R2595 and D482 were retired. M228 and E240 now follow the current grammar and active-Subject scope resolution. The D479 Current layout adapter pin was refreshed. This is manual source application, without a native workflow admission or Journal append. The bulk migration remains pending until the remote checkpoint is verified.
