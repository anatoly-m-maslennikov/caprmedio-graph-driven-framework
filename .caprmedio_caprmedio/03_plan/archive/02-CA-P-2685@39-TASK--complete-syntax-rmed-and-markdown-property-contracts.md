---
atom_id: CA-P-2685@39
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity
version: 39
updated_at: 2026-10-29 05:35:13 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2683
tier: 4
---
# Summary

Complete syntax RMED and Markdown property contracts

## Objective

Prepare the reviewed plain syntax and Markdown-layout Drafts for adoption with their corrected Subjects.

## Details

Stage 2 support, after the mechanical Subject pass. Reconcile the existing prepared packet against the latest Current predecessors and their migrated Subjects. Use A1301's reviewed repairs; do not reopen the completed design review or invent a new syntax language.

The root is Entity, with Object, Aspect, Graph Syntax and Carrier branches. Continuant/Occurrent specialize Object; Carrier is separate. Graph Syntax includes Relation and value Format. Retain /, //, ., :, ::, >, existing-kind @ references and ((RELATION_TYPE)). Property counts are {n}, {n+}, {n..m}; omitted counts are undefined, explicit {0} forbids direct values without forbidding declared children. Formats describe values, not YAML list/map containers or ref semantics.

RMED top-level sections are sibling ## Summary, optional ## Claim scope, ## Claim, optional ## Semantics and ## Details. R alone may include ### Formal claim below Claim. One direct prose Claim remains required; the formal child's independent optional count cannot satisfy it. Put operative meaning in Claim. YAML null/empty strings count as values; formats and prose conditions govern admissibility.

Confirm each adoption candidate's governs/dependencies against the new paths. Keep advanced formulas, conditions in [], materialization and function proposals outside the packet. Unrelated Drafts and Current sources are not changed by this preparation check.

## Definition of Done

The selected syntax/layout replacements have correct Subjects and a clear adopt/reuse/hold disposition for P2688. Earlier review evidence is linked; no missing-definition/catalog work is disguised as a completed adoption.

## Progress

Prepared packet review and ten repairs are recorded in A1301. Current-source reconciliation and adoption remain pending.
