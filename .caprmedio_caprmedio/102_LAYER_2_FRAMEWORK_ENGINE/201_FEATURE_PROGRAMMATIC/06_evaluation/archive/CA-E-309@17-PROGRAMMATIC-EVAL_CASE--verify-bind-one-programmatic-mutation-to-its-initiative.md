---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: programmatic-mutation
  depends_on:
  - Subject/Graph Node/Engineering/programmatic software
version: 17
updated_at: 2026-10-25 17:32:27 +0400
relations:
  evaluation_for:
  - CA-M-191
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-309@17
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
type: Eval Case
tier: 5
---
# Verify bind one programmatic mutation to its initiative

## Claim checked

one accepted programmatic mutation preserves **=1** sealed Initiative **and**
one stable action identity through asynchronous handoffs **and** retry.

## Applicable conditions

apply **when** one accepted human instruction causes a programmatic mutation that
passes through a queue **or** worker boundary.

## Test case

create one sealed Initiative **and** action identity, dispatch the mutation through
one queue **and** worker, force one retry, **and** observe **every** handoff plus the final
mutation receipt.

## Acceptance criteria

pass **only** **when** **every** handoff **and** the final receipt retain the same Initiative
**and** action identities, while process, queue, worker, **and** retry identities remain
linked execution context **and** never replace them.

## Failure disposition

reject the mutation provenance **and** return the identity propagation boundary **to**
its owner **before** later reliance.

## Sources

- [CA-M-191 — Bind one programmatic mutation to its Initiative](../05_method/CA-M-191-PROGRAMMATIC-ENG_POLICY--bind-one-programmatic-mutation-to-its-initiative.md)
