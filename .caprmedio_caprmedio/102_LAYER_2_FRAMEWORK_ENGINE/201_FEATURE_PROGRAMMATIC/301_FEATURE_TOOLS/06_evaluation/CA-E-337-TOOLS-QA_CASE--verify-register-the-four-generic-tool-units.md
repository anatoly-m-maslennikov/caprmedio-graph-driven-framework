---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - feature-boundary
    occurrent:
      - evaluation
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  evaluation_for:
    - CA-M-219
---
# Verify register the four generic tool units

## Claim checked

CA-M-219 gives TOOLS four immediate unordered generic capability owners with mutually distinct selection, checking, change, and Projection responsibilities.

## Applicable when

Apply whenever TARGET_SET, GRAPH_CHECK, BULK_CHANGE, PROJECTION_REBUILD, or their parent decomposition changes.

## Test case

Build the Project Scope Unit Graph and inventory the governed behavior of all four units. Trace one sample workflow from target sealing through checking, approved bulk change, and affected-Projection rebuilding.

## Acceptance criteria

TOOLS has exactly four immediate units with unique addresses and no sibling ordering; each sample step is owned once by its named unit; Finder and Checker steps do not mutate; change and rebuild require their declared approval and verification boundaries.

## Failure disposition

Reject the decomposition and preserve graph nodes and edges, behavior inventory, sample trace, duplicate or missing ownership, and any boundary-crossing mutation.
