---
atom_id: CA-P-2691@1
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Formal Model
version: 1
updated_at: 2026-10-28 20:00:14 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2683
tier: 4
---
# Summary

Formalize in-scope Claims in bounded batches

## Objective

Formalize in-scope Claims in bounded batches.

## Details

After CA-P-2690.

Review all in-scope Current Methodology and direct project-local RMED Claims for supported full or partial formalization. Start with model Definitions, syntax, Formats and Relation contracts. Formalize structure, cardinality, allowed values, identity/uniqueness and other constraints when the approved syntax expresses the exact meaning.

Use the Claim unit appropriate to its Role/Type. A Definition may combine formal structure and complementary prose in the same Atom; do not create two Atoms solely for formal/prose representations or split every property condition into its own Atom. Keep prose when it carries meaning the syntax cannot yet state, and put explanatory meaning in optional Semantics. Do not invent business logic, constraints, entities, precedence or a new formal primitive to force conversion.

Create leaf Subtasks/batches estimated at no more than 15 minutes before a large stage is executed. Maintain a compact coverage record of Fully formalized, Partially formalized, Prose retained with reason, and Unresolved. Stop and ask one concrete question when solution confidence is below 95%. Preserve one coherent contribution, not merely one Markdown heading.

## Definition of Done

Every selected Current Claim has an evidenced conversion disposition; formal/prose parts agree; retained prose is explained; no source meaning is silently lost, strengthened or weakened.

## Progress

Not started. Prior analysis and Drafts are inputs, not completion evidence.
