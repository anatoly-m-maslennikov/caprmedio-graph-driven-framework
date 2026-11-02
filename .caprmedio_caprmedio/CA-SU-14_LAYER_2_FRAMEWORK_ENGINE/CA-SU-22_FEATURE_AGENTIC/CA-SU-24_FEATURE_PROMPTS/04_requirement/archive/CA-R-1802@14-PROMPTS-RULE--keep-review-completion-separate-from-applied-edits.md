---
atom_id: CA-R-1802@14
content_role: Requirement
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Archived
author: Anatoly Maslennikov
version: 14
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: Subject/Graph Node/Documentation/Traceability
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
  - Subject/Graph Node/Engineering/Prompt
  - Subject/Graph Node/Domain/Continuant/Term//Property
  - Subject/Graph Node/Engineering/Outcome Evidence
relations: {}
tier: 3
type: Rule
---
# Summary

Keep review completion separate from applied edits

## Scope

completion results produced by the RMED review prompt Implementation for a selected Atom **or** selection.

## Claim

the Implementation **must** report completion **only** from complete initial check coverage **and** resolved findings, rather than from the existence of a report **or** an applied edit.

## Details

- an initial failed check is a completed check with a finding; a blocked **or** unperformed check is incomplete coverage.
- confirmed findings are resolved by an authorized correction **or** a recorded rejection supported by the supplied rules. partial correction does **not** resolve remaining findings **or** coverage.
- **every** finding retains its own disposition. a nonempty correction list **or** an empty unresolved list alone does **not** establish that **all** findings were handled. a correction-permission blocker does **not** turn a concluded initial check into an unperformed check.
- a completed selection requires completion evidence for **every** selected Atom. independent completed Atoms remain distinguishable from the unfinished selection.
- completion after fixes records completion of the admitted one-pass work, **not** a claim that saved output passed another Evaluation. this specification adds no recheck Step.
