---
atom_id: CA-E-295
ref_id: CA-E-295
container:
  scope_unit: CA-SU-37
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  dependencies:
  - Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
tier: 3
relations:
  evaluation_for:
  - CA-M-149
  derived_from:
  - CA-A-057
status: Active
version: 20
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROJECTION_ACTIONS
claim_target_scope_unit: PROJECTION_ACTIONS
---
# Rebuild one project graph state from configuration

## Claim checked

the graph-state Tool derives one current non-authoritative Projection from the inputs admitted by CA-M-149: authoritative Project Structure, separate Settings authority, **and** the selected Atom, directory-observation **and** Journal evidence frontier.

## Test case

rebuild graph state twice from unchanged source Revisions **and** observations. include accepted declarations whose folder materialization **or** Goal coverage is missing, **and** observed directories that do **not** match an accepted declaration.

## Acceptance criteria

- both Projections agree semantically **and** identify their selected sources.
- accepted Scope Unit declarations **and** concrete bindings come **only** from Project Structure. Project Settings **and** Framework Instance Settings retain their separate selected-value authority.
- declarations, Atom Claims, directory observations **and** Journal evidence remain distinct. missing coverage **and** mismatches stay visible **without** creating **or** rewriting accepted declarations.
- no direct output edit becomes authority, **and** **all** source Carriers remain unchanged.
- missing, invalid **or** incompletely read required authority is reported as incomplete coverage, **not** a complete accepted Project Structure.

## Failure disposition

reject the Projection as stale, nondeterministic, source-altering **or** authority-creating **when** **any** corresponding condition fails.
