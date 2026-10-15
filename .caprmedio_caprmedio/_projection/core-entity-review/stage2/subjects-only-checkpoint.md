# Subjects-only migration checkpoint — 2026-10-12

Derived progress record, not methodology authority or migration approval.

## Scope

CA-P-1959 migrates Subjects only. CA-P-1970 is the separate deferred content
Epic. Summary, Substance, Scope, Details, Semantics, identity/filename adoption
and Terms-compiler content work are not authorized by this migration.

Prepare candidates only in `.caprmedio_tmp`; do not publish them to original
Core, history or Journal. The staged-preview contract permits only Subject
changes plus required illustrative Version/time metadata. Live publication is
still deferred.

## Verified progress

- Starting work was pushed to `amm/dev` at
  `757c02701a90ec452633ce334ad593f100237d59`.
- Fresh registered Core inventory: 907 non-archived RMEDO original Atoms,
  4,534 Subject occurrences. All happen to be Active; eligibility is not an
  Active-only filter.
- Independent inventory verification passed, including four negative controls.
- The BEFORE literal Subject tree covers all 4,534 occurrences. It is a
  construction-only projection, not a completed native entity graph.
- The historical first seven mapping packets and independent reviews cover 140 Atoms and 760
  occurrences: 662 prospectively supported rows, 31 withheld proposals and 67
  existing unresolved rows. R001 has packet acceptance; the other packets need
  corrections under that earlier model. No partial result admits a whole-source migration. Exact report
  pins are in [the review index](subjects-only-review-index.json).
- All 12,124 captured Core and historical Markdown files matched the inventory
  at the earlier checkpoint. The 907 selected original files were reopened and
  checked against their captured hashes and byte snapshots again after the
  five-branch candidate update; all remain unchanged. No Core Subject or content
  migration has occurred.
- Validator locator correction `e1e3d2d91` changes only 20 paths, preserving
  the exact 18 authority source versions and hashes.
- Plan separation `7d8fba7ac` independently passed: 13 current Plans, eight
  preserved predecessors and 201 resolving links.
- Installed-copy identity fix `1fc85bf12` passed 87 UPDATE tests, 13 independent
  checks and a real no-op preview. Installed copies are not original
  competitors; selecting an installed copy and genuine duplicate originals
  still fail. See [the acceptance record](tools-first/installed-copy-identity-acceptance.md).
- Tool/inventory leaf closure was committed as `177b337d3`; the parent Epics
  remain Active. The CA-P-2193 group was created with 48 Active review Tasks covering
  all 907 sources / 4,534 occurrences. Independent partition, input-pin,
  history and link checks passed; this is not semantic acceptance.
- Six further frozen reports (R004–R008 and O002) cover 120 additional Atoms
  and 542 occurrences. Independent reviews have found corrections and pending
  choices; these reports do not grant staging permission. Other review and
  correction lanes may still be running. Frozen earlier reports are preserved.
- Before the five-branch continuation, frozen proposals covered 760 distinct
  Atoms and 3,687 occurrences: all R, M and E packets, D001–D003 and O001–O002
  (R010 as two halves). Their model pins remain historical.
- The remaining D004–D008 and O003–O006 producer packets are now frozen against
  the five-branch candidate: 147 Atoms / 847 occurrences. Root reconciled all
  48 inventory packets against 49 selected producer files, including R010's
  two halves: exactly 907 distinct owners and 4,534 distinct occurrences, no
  missing or duplicate coverage. All 907 source hashes and byte snapshots
  remain unchanged. This is complete first-pass proposal coverage, not current
  semantic acceptance of the older 760 owners or completion of the migration.
- The R010 split is committed as `8189c1d33`. Confirmed whole-Atom conflict
  boundaries and the full-review gate are committed as `be92fece8`; all parent
  Plans remain Active. Independent Plan checks covered 228 current links and
  exact predecessor archives, not migration semantics.

## Gates still open

1. Complete and independently verify the whole fresh mapping ledger.
   CA-P-2188/2189 are prerequisites for CA-P-2190; a few accepted owners do not
   satisfy that gate. The Operator now permits explicit whole-Atom exclusions
   for confirmed content conflicts, with those unchanged Atoms assigned to the
   separate content Epic. A later explicit answer also permits unchanged whole
   owners with unresolved meanings, recorded separately from content conflicts.
   Every source and every such disposition still requires review.
2. Keep uncertain whole owners outside the payload, with exact source pins,
   affected occurrences, reasons and questions. Do not substitute an actual
   Actor or a collection of Atoms with its classification Property.
   Implementation does not create Implementation Atoms. Fully supported other
   whole owners may be staged only after the complete ledger is accepted.
3. Only then export the authorized Subject candidates, verify exact byte-span
   changes, and build the AFTER graph from those actual staged bytes.

No staged candidate export or AFTER graph is claimed at this checkpoint.

## Current candidate: five branches

The Operator requested applying the agreed model to
[Candidate #3](../presentation/operator.model.candidate-3.md) and continuing.
The candidate now has five sibling branches: Object, History, Projection,
Selection and Actor. The change is committed as `ea756f83c`; its SHA-256 is
`b0ad3f0d803112bf5e2d16c3f882cd0b01032273474c41cf6045db9ee86e40b7`.

- Object includes source Atoms, non-Atom governing configurations and live
  ephemeral Executions. Only Object divides into Continuant and Occurrent.
- History contains preserved Revisions and Journals. A Journal Record is a
  stored History record **about** what happened, not the Execution itself.
- Projection is derived, separate from Object; Terms Graph is a Projection type.
- Selection chooses existing items. Actor means who performs work.
- Terms remain source meanings and derived vocabulary, not a sixth root or a
  new authoritative definition layer. Review metadata may use `Term` without
  creating a graph node. The invariants framing remains withdrawn.

The additive decision is `model/root-branches-decision.md`, SHA-256
`fd265d787544d4c16f395c920cf6a634ec32285431ee28dad4d52083fee85ba7`.
New reviews bind both final pins. Older reports and receipts retain their exact
earlier pins: neither changing a hash nor relabeling a category grants current
semantic acceptance. This candidate update does not adopt native taxonomy,
change grammar, or authorize original migration.

The independent impact report is `reviews/root-branches-impact.md`, SHA-256
`636f5db11e4c366af8d1909def15bdb6feb30dc17768f609ee133d6a19f44430`.
It confirms reuse of existing syntax/patch/staging transport and identifies
affected source meanings, category-only annotations and older review defects.
It does not accept mappings. Current Plan guidance binds the new candidate
without overwriting older reports or automatically completing descendant Tasks.
The eight necessary current Plans and eight exact predecessor archives passed
independent checks and were committed as `fbe924614`. Their IDs, Summaries and
Statuses were preserved, versions increased once, and all 250 local links
resolved. Receipt: `plan-review/five-branch-plan-acceptance.json`, SHA-256
`7b73da2ab25d85f7e2801e0119d953858a9632aaf4360219426051388804bc15`.

The mixed-profile graph audit found that one global notation profile cannot
silently preserve both old held-owner meanings and approved Subject meanings.
Its proposed existing-tool route uses disjoint owner captures and reconciles
raw Subject incidence with explicit profile provenance. The current tree helper
rejects dot paths. Neither the audit nor syntax-only construction establishes
native semantic acceptance; see scratch `reviews/mixed-profile-graph-boundary.md`.

## Earlier decision retained: Actors are who; Objects are what

[Candidate #3](../presentation/operator.model.candidate-3.md) previously had four
Entity branches: Object, Actor, Term and Selection. Only Object divided into
Occurrent and Continuant. Actor is not an Object subtype or a display-only
exception. The candidate change is committed as `08ff76660`.

Actor Type and optional Name retain their meanings and the existing identity
convention. These Properties remain dependent Objects with an Actor bearer;
actual performers are Actors, allowed-value names are Terms, and expressions
choosing Actors are Selections. No Actor selector or storage schema was added.

That historical candidate SHA-256 is
`3a8a91eea5da3dc05716647d21c39e03e6c3d3d26760349b291f369ef3753765`.
The additive scratch decision `model/actor-branch-decision.md` has SHA-256
`8fc22d8c5ca231ac4caecd19888ec28488b644a92a223fa1448f58a131d1fcd1`.
Earlier candidate pins stay historical; changing a hash alone is not a fresh
semantic review. Current reviews bind the five-branch model above and retain
the who/what distinction from this earlier decision.

A bounded code audit found no runtime parser, graph constructor or patch/staging
schema change required by this separation. New scratch review guards must admit
Actor and distinguish performers from values and Properties. Exact unchanged
Subject strings do not need a carrier edit or Version increment. Focused
in-memory checks passed; native admission and staged acceptance remain unproved.

The Operator subsequently approved leaving genuinely ambiguous whole Atoms
unchanged and listing them separately as unresolved. The additive decision is
`model/unresolved-owner-decision.md`, SHA-256
`d325383d4d4b049347bc77381e3f17616d3a473d93fce587c6b23a11e0ad9912`.
It does not raise mapping confidence, call uncertainty a content conflict, or
permit skipped sources. All 907 owners still require review before supported
changes enter staging; unresolved owners retain their original graph coverage.

R013 received independent acceptance under the earlier four-branch model for
all 20 owners /98 occurrences, with
no holds or conflict exemptions. CA-P-2206 is Done in `1b5e6b17d`, backed by the
producer and separate receipt. This is one completed review Task, not a staged
migration, current five-branch acceptance, or acceptance of other packets.

## Latest Operator decision: named Selections

The Operator approved distinct named Selections when existing selector syntax
does not express the subset. A named Selection is not an Object. Preserve its
actual source-grounded predicate instead of collapsing it to a generic target.

Owned Atoms selects by owning Scope Unit. Targeting Atoms selects by target
Scope Unit. The same permission covers other supported named subsets, such as
Atom Properties or Applicable Methodology Sources; it does not automatically
turn plain Terms, records or performers into Selections. No selector grammar or
Atom content change is implied. The recorded first-pass counts predate this
answer; affected mappings still need explicit revision and independent checks.

The Operator also approved keeping the old contextual Atom Scope as a named
Selection, distinct from Substance Scope. Whether that old concept remains
needed belongs to the later content Epic; it is not a same-meaning alias here.

The latest clarification distinguishes three concepts:

- Owning Scope Unit: where the Atom belongs.
- Target Scope Unit: the Scope Unit addressed by a relational Atom, such as
  a Demand or Goal.
- Substance Scope: the exact boundary of what the Atom governs.

The old combined lookup context is a Selection, not a fourth scope. These
meanings guide Subject review; content fields and storage keys remain unchanged.

The old literal `Atom/Scope` is overloaded. CA-R-1287 refers to the breadth of
Claim Scope (Substance Scope); CA-R-1294 refers to the Consumer's owning Scope
Unit. Neither is the combined lookup Selection used by CA-R-1014. Each mapping
must follow its own source content, not a global string replacement.

The Operator approved `Atom.Owning Scope Unit`, `Atom.Target Scope Unit`, and
`Atom.Substance Scope`. The first two name Atom references, not new Scope Unit
kinds; the third names the applicability boundary. Storage fields and content
remain unchanged. Affected reports require revised mappings and fresh separate
acceptance, not automatic promotion of their old proposals.

The additive decision is recorded in scratch at
`model/scope-reference-decision.md`. It supplements the unchanged base decision
pin used by CA-P-2193's Tasks; frozen review evidence remains intact.

The Operator also approved keeping Atoms with confirmed conflicting content
unchanged and staging the other fully supported Subject changes. Record whole
Atom exclusions and their exact evidence for CA-P-1970; do not omit them from
coverage. For example, CA-R-1343 still defines Implementation Atoms, which the
new model excludes. The additive decision is at
`model/content-conflict-decision.md`. This does not authorize content edits or
unreviewed/uncertain changes.

## Local evidence

Scratch outputs are under `.caprmedio_tmp/stage2-migration-20261012/` and are
not committed source carriers:

- `inventory/current-subjects.inventory.json`, SHA-256
  `0b2f217e8ebf541cc84322d18be81073bfdbb54342f248cbf9928583678455c7`.
- `inventory/current-source-frontier.json`, SHA-256
  `da810174e1b1fbbb930959b929a6e830e2dae5b4a0a7b0758bbc3d221bd192a9`.
- `inventory-independent-check.json`.
- `graph-prep/before-literal-subjects/before-literal-subjects.tree.txt` and
  `before-summary.json`.
- `reviews/review-{r-001,r-002,r-003,m-001,e-001,d-001,o-001}.json` and
  their separate independent acceptance reports when complete.
- `plan-review/subjects-only-plan-packet-acceptance.json`, SHA-256
  `508b74848cdd4ea081b7f1d3e0aaafb9b9fcacca6432d52501d4a45edb22152c`.

These results must be rebound to current source hashes before later use.
