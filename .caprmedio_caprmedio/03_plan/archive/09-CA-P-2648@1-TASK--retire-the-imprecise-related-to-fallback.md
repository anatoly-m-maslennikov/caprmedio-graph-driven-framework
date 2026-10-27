---
atom_id: CA-P-2648@1
content_role: Plan
type: Plan
label: Task
work_sequence_number: 9
current_scope_unit: caprmedio
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
version: 1
updated_at: 2026-10-26 05:17:30 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2639
tier: 4
---
# Summary

Retire the imprecise related_to fallback

## Objective

Apply the Operator's already-established precise typed-relation policy to
R1653 and its affected Current source uses.

## Details

Addresses the remaining part of I06. Run after the overlapping P2646 work.
Estimated own work: up to 15 minutes per bounded batch.

- Read Current R1653 and locate direct consumers and uses of the imprecise
  related_to/relates_to fallback in the affected reviewed source set.
- Retire the fallback definition; do not replace it with another vague kind.
- Keep only source-supported precise links. A contextual or redundant link
  may be dropped; never rename every vague link to depends_on or invent a
  dependency, evaluation or derivation that the Claim does not support.
- Preserve relevant explanatory source text and existing historical carriers.
  Current source edits receive normal predecessor archives.
- Keep child_of/parent_of replacement in its separate Epic. Do not expand
  into unrelated relation migrations or code registry changes.
- Record the actual batch, dispositions and concrete ambiguous obligations.
  Split wider consumer cleanup into further Tasks if needed.

## Definition of Done

- R1653 has its approved retirement disposition.
- The completed source batch has no imprecise fallback links; retained typed
  links have an evidenced meaning and redundant links are not reintroduced.
- No unsupported dependency or broad relation rewrite was invented.
- Remaining uses outside the completed batch are explicit.
