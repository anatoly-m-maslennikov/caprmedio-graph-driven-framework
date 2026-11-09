---
atom_id: CA-E-336
ref_id: CA-E-336
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source Retrieval"
tier: 4
relations:
  evaluation_for:
  - CA-M-218
status: Active
version: 22
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Verify resolve GitHub Extension source

## Claim checked

CA-M-218 resolves the declared GitHub repository **and** package-root boundary for one Extension **without** choosing an installed state.

## Applicable when

apply whenever GitHub Extension source-boundary resolution changes.

## Test case

resolve one Extension whose package root is a declared repository subdirectory, **then** resolve another whose package root is the complete repository. repeat with an undeclared subdirectory.

## Acceptance criteria

**every** valid case reports the declared GitHub repository **and** its exact complete-repository **or** declared-directory package root. the undeclared-subdirectory case produces an explicit failure **and** no alternative source boundary.

## Failure disposition

reject the realization **and** preserve source declarations, resolved boundaries, undeclared-subdirectory finding, **and** proof that installed Extension state was unchanged.
