---
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - feature-boundary
version: 3
updated_at: 2026-09-01 23:47:24 +0400
relations:
  method_for:
    - CA-R-1153
    - CA-R-1154
    - CA-R-1155
    - CA-R-1156
  derived_from:
    - CA-A-058
---
# Register the four generic Tool units

## Applicable when

Use this Method when defining the four generic Tool Scope Units that compose selection, checking, bulk change, and Projection rebuilding.

## Procedure

1. Register TARGET_SET, GRAPH_CHECK, BULK_CHANGE, and PROJECTION_REBUILD as immediate unordered child Scope Units of TOOLS with stable addresses and source paths.
2. Assign TARGET_SET only the read-only sealing of stable target membership, frontier, and digest.
3. Assign GRAPH_CHECK only registered Evaluation execution and attributable issue, evidence, and verdict output over a sealed target set.
4. Assign BULK_CHANGE only approved rollbackable composition of generic carrier changes over an unchanged sealed target set.
5. Assign PROJECTION_REBUILD only affected-Projection derivation, dependency ordering, preview, materialization, and currentness verification.
6. Rebuild the Project Scope Unit Graph and reject duplicated ownership or implicit ordering among the four units.

## Outcome

TOOLS exposes four distinct generic capability boundaries with one owner for selection, checking, mutation composition, and Projection rebuilding.

## Failure or stop

Stop on a missing or duplicate unit, conflicting address, non-immediate ownership edge, or behavior assigned across more than one boundary.
