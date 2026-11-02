---
atom_id: CA-P-2693@2
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Formal Model
version: 2
updated_at: 2026-10-28 20:04:15 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2683
tier: 4
---
# Summary

Rebuild the actual Formal Model views and close the migration

## Objective

Rebuild the actual Formal Model views and close the migration.

## Details

After CA-P-2692.

Rebuild the primary and flat property-bearing views from the actual selected Current Methodology/project-local RMED sources. Show the full declared source selection and exact versions; the six base branches; correct specialization, grouping, parts and named relations; no false inheritance from Project Model grouping; defining R IDs; and properties with accurate inherited marks. Do not copy the candidate tree and label it Current.

Check the selected Current source shapes, normalized paths, one-Claim layout, applicable formal syntax, direct/derived directions, counts, references and conversion/retirement coverage. These are bounded migration checks, not a new repository-wide Atom-validation release gate or a runtime test-suite change. Report unsupported formal parsing as unsupported rather than a semantic pass.

Keep prepared, reviewed, applied and rebuilt outcomes distinct. Close only when the selected migration and required corrections are actually done. Expose Engine deferral, unresolved cases or partial coverage explicitly; do not claim the full project/runtime was migrated.

## Definition of Done

Current source readback and rebuilt primary/property views agree with the latest model and Claim structure; selected-source coverage is complete or precisely bounded; required unresolved work prevents an unqualified Done claim.

## Progress

Not started. Prior analysis and Drafts are inputs, not completion evidence.

## R-only scope

Only R enters operative formal Claim conversion. M/E/D may describe syntax, Formats and Relations in prose and undergo the shared body/path migration, but have no operative content.claim.formal_claim field in this iteration. A1244 records the latest scope.
