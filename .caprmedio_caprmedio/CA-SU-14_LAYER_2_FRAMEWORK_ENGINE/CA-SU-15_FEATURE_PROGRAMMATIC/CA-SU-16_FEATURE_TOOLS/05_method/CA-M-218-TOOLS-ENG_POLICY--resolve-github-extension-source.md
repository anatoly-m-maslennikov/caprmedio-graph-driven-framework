---
atom_id: CA-M-218
ref_id: CA-M-218
container:
  scope_unit: CA-SU-16
role: Method
form: Eng Policy
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source Retrieval"
tier: 3
relations:
  method_for:
  - CA-R-1151
  derived_from:
  - CA-A-058
status: Active
version: 20
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Resolve GitHub Extension source

## Applicable when

use this Method **when** determining the declared GitHub source boundary for one Extension package.

## Procedure

1. resolve the declared GitHub repository for one Extension **and** determine whether its package root is the complete repository **or** one declared directory.
2. normalize the repository identity **and** optional declared directory **without** inventing an implicit subdirectory **or** alternate source provider.
3. retrieve the source boundary **and** report the declared repository **and** package-root path as attributable source metadata.
4. reject a missing repository, undeclared subdirectory, **or** source boundary that cannot be mapped **to** the Extension package.
5. return source-resolution facts **only**; do **not** choose an installed version **or** change installed Extension state.

## Outcome

one Extension has an exact attributable GitHub repository source boundary **and** either its complete repository **or** one declared package-root directory.

## Failure or stop

stop on an ambiguous repository, undeclared package root, missing source boundary, **or** an attempt **to** manage installed state.
