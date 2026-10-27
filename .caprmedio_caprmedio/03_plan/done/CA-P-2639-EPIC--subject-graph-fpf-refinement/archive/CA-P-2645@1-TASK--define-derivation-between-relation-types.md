---
atom_id: CA-P-2645@1
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Relation
version: 1
updated_at: 2026-10-26 05:11:58 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2639
tier: 4
---
# Summary

Define derivation between Relation Types

## Objective

Represent the Operator's accepted statement:
CONTAINS is derived relation of IS_CONTAINED_BY.

## Details

Implements D06 and addresses part of I06. Estimated own work: up to 15 minutes.

- Read Current R1368 and the directly relevant Relation Type declaration
  contracts. Check whether an admitted derivation relation already exists;
  reuse it instead of introducing a duplicate name or model.
- Define the source and target as Relation Type instances, not the individual
  Task/Epic or other object links that use those Types.
- Preserve the specific inverse meaning for CONTAINS/IS_CONTAINED_BY:
  each derived CONTAINS link reverses the stored IS_CONTAINED_BY endpoints.
  The generic derivation name alone does not make every derivation an inverse.
- Preserve direct-only source storage and derived inverse views. Do not require
  updating the containing Atom when its children change.
- Keep endpoint restrictions separate from Relation Type meaning, following
  the accepted graph-rule split.
- Do not introduce mandatory derivation-evidence classes, an inference engine
  or guessed behavior for other relation pairs.
- Record actual changed source IDs/versions and normal predecessor archives.
  Preserve existing Drafts, Archives and unrelated source content.
- R1617 retirement or reclassification still needs an explicit disposition.
  Do not silently discard its other categories as part of this Task.

No code, renderer, actual containment-link migration, Terms Graph or runtime
implementation is included.

## Definition of Done

- The accepted derivation statement is defined between Relation Type instances.
- The containment pair retains its explicit reversed-endpoint inverse meaning.
- The type-level relation is distinguished from actual containment links.
- No duplicate authored inverses, new general derivation engine or unapproved
  provenance classification was introduced.
- Changed source definitions and their predecessors are recorded separately
  from this Plan, with any remaining R1617 disposition kept open.
