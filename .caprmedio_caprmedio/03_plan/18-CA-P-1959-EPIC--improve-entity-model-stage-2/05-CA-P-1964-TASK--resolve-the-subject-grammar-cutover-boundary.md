---
atom_id: CA-P-1964
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Term, Property, Carrier, Revision, Scope Unit, Projection, Plan, Tool, Journal, Operator]
version: 2
updated_at: "2026-10-10 23:24:00 +0400"
relations:
  is_decomposition_of: [CA-P-1959]
  blocks: [CA-P-1965, CA-P-1967, CA-P-1968]
---
# Summary

Resolve the Subject grammar cutover boundary

## Objective

Resolve the minimum grammar exception needed before any live Subject migration.

## Details

Own work: none. Required prerequisite: CA-P-1960. CA-P-1976 prepares the exact question/contract candidate; CA-P-1977 records an actual answer before this group can complete. Operator waiting time is not assigned executable work.

Reopen the current Subject grammar authorities and their pins. The audit found / currently means IS_BORNE_BY, : means IS_ALLOWED_VALUE_OF, and . is ordinary text. The selected candidate instead uses / for broader-to-narrower and . for bearer qualification. Recheck this conflict rather than treating the captured review as live authority.

Prepare the smallest exact grammar-contract revision candidate, with relation direction, escaping/reserved characters and proposed parser/validator behavior. : remains allowed-value notation, not assignment. @ remains carrier display notation; dependent-instance pseudocode is not silently admitted as native Subject syntax.

Ask the Operator whether Step 1 may include these necessary governing body revisions. All other Summary/Substance/Scope/Details updates remain Step 2. Record the actual answer and exact authorized boundary; if it is refused or uncertain, retain a blocked cutover rather than rewriting Subjects under the old meaning.

No governing grammar Atom is changed by this Task. Proposed syntax may be evaluated only in isolated, clearly labelled previews.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

### Decomposing Plans

- [CA-P-1976 — Prepare the Subject grammar decision packet](05-CA-P-1964-TASK--resolve-the-subject-grammar-cutover-boundary/01-CA-P-1976-TASK--prepare-the-subject-grammar-decision-packet.md)
- [CA-P-1977 — Record the Subject grammar cutover decision](05-CA-P-1964-TASK--resolve-the-subject-grammar-cutover-boundary/02-CA-P-1977-TASK--record-the-subject-grammar-cutover-decision.md)

### Definition of Done

The Plan is **not** Done if the live grammar conflict is ignored, the exception has no actual Operator decision, the proposed grammar is ambiguous, or authoritative grammar/body changes occur; any direct decomposing Plan is not Done; or own work exceeds 15 minutes without decomposition.
