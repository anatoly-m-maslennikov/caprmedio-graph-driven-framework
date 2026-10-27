---
atom_id: CA-C-591
content_role: Concern
type: Question
current_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
tier: 3
version: 1
updated_at: 2026-10-24 06:45:25 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Subjects
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Subject/Engineering/Methodology
relations: {}
---
# Summary

Which existing topics best describe legacy Plan Subject tags?

## Question

Do the existing topics preserve the meaning of the old untyped tags in these
completed Plans without introducing new Domain entities or properties?

## Scope

The Subjects-only migration of CA-P-064–068, CA-P-070–075 and CA-P-080–082.
Bodies, statuses, identities, ownership and relations remain unchanged.

## Details

Use these bounded choices and retain this Question for the later content review:

- CA-P-066: Atom is the mutation target. Tool, Runtime and Journal are
  dependencies. Its separate concurrency, provenance and Git-gate work remains
  explicit in the body; the broad Subject does not combine those requirements.
- CA-P-068: the old artifact-identity tag means the existing Atom.ID property
  in this task about Requirement carriers. Do not restore an Artifact branch.
- CA-P-070–075 and CA-P-081: use Engineering/Methodology for the work on
  Method/Evaluation/Delivery authority and coverage. Keep body-specific Scope
  Unit, Atom, Tool, Journal and graph dependencies. Content Roles remain
  independent from Subjects; these choices do not make every Method or
  Evaluation an Engineering/Methodology Subject.

The packet changes only the typed Subject classification of fourteen Current
Plans. It does not re-execute completed tasks, endorse obsolete body rules or
change any implementation. Existing Drafts and Archives remain excluded.

Candidate #7, the migration plan, latest Operator decisions and active
principles govern the choice. The Operator authorized recording a small-blast
Question, making the best bounded choice and continuing. This Question adds no
approval gate and is not evidence of full migration completion.
