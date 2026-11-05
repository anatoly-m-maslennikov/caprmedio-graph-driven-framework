---
topics:
  main_subject: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Scope Unit
    Graph'
  dependencies:
  - Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
version: 23
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  evaluation_for:
  - CA-R-1070
atom_id: CA-E-164
ref_id: CA-E-164
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: PROJECTION_ACTIONS
form: Eval Case
tier: 2
claim_target_scope_unit: PROJECTION_ACTIONS
container:
  scope_unit: CA-SU-37
---
# Rebuild the Scope Unit Graph and Sources Projection from Configuration Authority

## Test case

use an isolated Project fixture with valid authoritative Project Structure, Project Settings, Framework Instance Settings, Project Atoms, **and** observed Scope Unit folders. include:

- a declared Scope Unit **without** an active Goal;
- a declared Scope Unit whose folder is absent;
- an observed folder **without** an accepted declaration;
- an observed path that conflicts with its accepted declaration.

remove previous generated Graph **and** Sources outputs. run the generator. **in** separate fixtures, remove **or** invalidate Project Structure.

## Acceptance criteria

- valid authoritative inputs produce deterministic views of the accepted declarations **and** their exact source revisions **without** reading previous generated views.
- Goal **and** materialization gaps remain visible. undeclared **or** mismatched folders remain observations **and** **must not** become accepted Scope Units **or** redefine bindings.
- missing **or** invalid Project Structure yields an explicit unresolved-authority diagnostic **without** claiming a complete accepted Project Structure.
- Project Structure **and** Settings remain byte-identical.

## Failure disposition

reject the generator **if** it promotes observations **or** generated outputs into authority, silently drops declared units, **or** modifies an authoritative input.
