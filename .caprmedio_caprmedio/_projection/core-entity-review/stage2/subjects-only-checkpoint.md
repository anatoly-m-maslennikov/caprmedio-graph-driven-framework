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
- Seven mapping packets and independent reviews cover 140 Atoms and 760
  occurrences: 662 prospectively supported rows, 31 withheld proposals and 67
  existing unresolved rows. R001 has packet acceptance; the other packets need
  corrections. No partial result admits a whole-source migration. Exact report
  pins are in [the review index](subjects-only-review-index.json).
- All 12,124 canonical Core and historical Markdown files still match the fresh
  inventory hashes. No Core Subject or content migration has occurred.
- Validator locator correction `e1e3d2d91` changes only 20 paths, preserving
  the exact 18 authority source versions and hashes.
- Plan separation `7d8fba7ac` independently passed: 13 current Plans, eight
  preserved predecessors and 201 resolving links.
- Installed-copy identity fix `1fc85bf12` passed 87 UPDATE tests, 13 independent
  checks and a real no-op preview. Installed copies are not original
  competitors; selecting an installed copy and genuine duplicate originals
  still fail. See [the acceptance record](tools-first/installed-copy-identity-acceptance.md).
- Tool/inventory leaf closure was committed as `177b337d3`; the parent Epics
  remain Active. The new CA-P-2193 group has 48 Active review Tasks covering
  all 907 sources / 4,534 occurrences. Independent partition, input-pin,
  history and link checks passed; this is not semantic acceptance.
- Six further frozen reports (R004–R008 and O002) cover 120 additional Atoms
  and 542 occurrences. Independent reviews have found corrections and pending
  choices; these reports do not grant staging permission. Other review and
  correction lanes may still be running. Frozen earlier reports are preserved.

## Gates still open

1. Complete and independently verify the whole fresh mapping ledger.
   CA-P-2188/2189 are prerequisites for CA-P-2190; a few accepted owners do not
   satisfy that gate.
2. Resolve concrete ambiguous mappings with the Operator. Do not substitute
   an actual Actor or a collection of Atoms with its classification Property.
   Implementation does not create Implementation Atoms.
3. Only then export the authorized Subject candidates, verify exact byte-span
   changes, and build the AFTER graph from those actual staged bytes.

No staged candidate export or AFTER graph is claimed at this checkpoint.

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

One representation question is pending: use `Atom.Owning Scope Unit`,
`Atom.Target Scope Unit`, and `Atom.Substance Scope`, with the first two naming
Atom references, or retain the first two as the actual addressed units? The
three meanings are approved; the reference-versus-referent distinction is not
yet settled. Affected rows remain withheld. No storage/content change follows
from either answer during this Epic.

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
