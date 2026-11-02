---
atom_id: CA-R-1802@6
content_role: Requirement
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 00:51:05 +0400
subjects:
  governs: Subject/Domain/Node/Occurrent/Execution/Workflow Run
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Evaluation
  - Prompt
  - Subject/Domain/Node/Continuant/Term//Property
  - Subject/Engineering/Outcome Evidence
relations:
  relates_to:
  - CA-O-104
  - CA-O-111
  - CA-R-1801
tier: 3
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
