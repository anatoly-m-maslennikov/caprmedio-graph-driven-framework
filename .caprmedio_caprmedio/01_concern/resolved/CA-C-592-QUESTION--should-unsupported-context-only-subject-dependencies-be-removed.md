---
atom_id: CA-C-592
content_role: Concern
type: Question
current_scope_unit: caprmedio
status: Resolved
author: Anatoly Maslennikov
tier: 3
version: 2
updated_at: 2026-10-24 18:16:36 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Subjects
relations: {}
---
# Summary

Should unsupported context-only Subject dependencies be removed?

## Question

Do these old contextual dependencies describe a real reliance boundary of the
owning Atom, or merely its surrounding implementation?

## Scope

CA-M-329, CA-R-1475, CA-R-1891 and CA-R-1895 in the Current Subject migration.
No body, runtime, relation list or classification changes.

## Details

Independent review of increment 71 found four dependencies without sufficient
support in the owning text. Apply the smallest forward correction:

- M329 compiles and reuses a Method Projection, not a Prompt. Remove its
  Prompt dependency; retain Projection and Method-Atom Subjects.
- R1475 specifies reproducible FPF Extension materialization. Its text does
  not select a Skill representation. Remove the Skill dependency; retain its
  existing Extension, candidate and digest context.
- R1891 specifies a Release Host Executor. Its text requires execution
  boundaries and queue isolation, but does not select DBOS. Remove DBOS.
- R1895 describes one frozen Release recovery and recording of its terminal
  outcome. Its text does not require DBOS. Remove DBOS.

These are removals of vague implementation-context links, not new governing
Subjects or a decision to remove any capability. More specific engineering
dependencies can be authored later if their sources actually require them.

The Operator approved removing redundant or vague Subject dependencies and
continuing with a bounded Question below 95% confidence. Preserve the applied
increment-71 history and create ordinary predecessor archives for this forward
correction. Do not roll back unrelated completed effects.

## Resolution

The Operator approved dropping unsupported or redundant contextual links
rather than inventing dependencies. Current M329 no longer depends on Prompt,
R1475 no longer depends on Skill, and R1891/R1895 no longer depend on DBOS.
The four stated forward corrections are present in the actual source fields.
This resolution removes no capability, selects no replacement runtime and
does not reopen deferred Engine design questions. No new source edit is
performed by closing this already-applied correction record.
