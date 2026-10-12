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
