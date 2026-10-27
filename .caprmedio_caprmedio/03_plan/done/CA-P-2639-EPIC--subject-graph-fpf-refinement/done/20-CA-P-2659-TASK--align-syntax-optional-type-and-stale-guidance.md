---
atom_id: CA-P-2659
content_role: Plan
type: Plan
label: Task
work_sequence_number: 20
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Subject
version: 1
updated_at: 2026-10-26 17:56:09 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2639
tier: 4
---
# Summary

Align syntax, optional Type and stale guidance

## Objective

Apply the accepted Subject-path and Type guidance precisely, correct the stale Graph Rule claim location and Carrier role note, and add no unrelated category or inheritance policy.

## Details

- Bound the source proposal to the four reviewed guidance rows in .caprmedio_tmp/subject-alignment-accepted/guidance.json: R1931, R1284, R1996 and R1958. R924 is intentionally excluded because its existing classifications are unchanged by this decision.
- State that x:y is structural notation for variable x and ALLOWED value y, not an instance assignment; retain readable colon-qualified kinds such as Atom/Content Role: Plan, Atom/Content Role: Requirement/Type: Demand and Product: CAPRMEDIO Framework, with // reserved for named instances.
- Keep Type optional for Graph Nodes generally, with finite and expandable allowed-value sets scoped to the governed Property and Applicable Methodology Revision; allow a specific rule to require Atom.Type without choosing inheritance precedence or a local winner.
- Correct R1996 to frontmatter claim.graph_rule_type consistently with R2001/M394/D637. Correct R1958's stale R1342 role wording while preserving the Requirement-versus-Delivery distinction.
- Treat the Framework itself as a reference boundary: no separate examples, trials or mandatory category-admission process. Do not add syntax, Property, Type, relation, Domain or runtime concepts.

### Completion evidence

The accepted source correction is applied. Independent final verification passed.
Evidence: `.caprmedio_tmp/subject-alignment-accepted/verify.final.json`,
`verify.final.md`, both publication receipts, and
`graph-final/graph.subject-views.manifest.json`. The four Current-RMEDO views
contain 2,223 sources (792 Core, 405 Methodology, 1,026 Engine), with zero
unmapped Subjects. This is source/projection verification, not runtime execution.

## Definition of Done

- R1931 distinguishes structural colon qualification from named-instance // syntax without blanket conversion.
- R1284 expresses optional general Graph Node Type and scoped finite/expandable values while leaving specific mandatory Type rules to their own authority.
- R1996 uses frontmatter claim.graph_rule_type, and R1958 no longer carries the stale R1342 role statement.
- The accepted guidance rows preserve existing Summaries and introduce no inheritance precedence, category process, new syntax or new Domain concept.
