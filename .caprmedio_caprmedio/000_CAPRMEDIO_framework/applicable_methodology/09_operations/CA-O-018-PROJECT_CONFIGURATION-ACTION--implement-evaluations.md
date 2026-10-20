---
atom_id: CA-O-018
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Evaluation Implementation"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Atom/Content Role: Plan/Type: Plan", "Entity/Node/Continuant/Atom/Content Role: Evaluation", "Entity/Node/Continuant/Atom/Content Role: Method", "Entity/Node/Continuant/Atom/Content Role: Delivery", "Entity/Node/Continuant/Atom/Content Role: Requirement", "Implementation"]
version: 10
updated_at: "2026-10-19 15:56:41 +0400"
relations:
  relates_to:
    - CA-O-017
    - CA-O-020
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-018-PROJECT_CONFIGURATION-ACTION--implement-evaluations.md
  source_atom_id: CA-O-018
  source_atom_revision: 10
  source_sha256: 2d87a0e8a5524d010f90991be5cf291d7ad7b7806e2362f55808952d4785b1e7
  original_relations_sha256: 95f6c99d1efc99d7004ab8a8f29dde5c29b2e88c3e0dc4ba5902eff79acf5b23
---
# Summary

Implement Evaluations

## Operation

Evaluation Implementation **means** the Agentic Action that prepares **or** reuses the tests for selected implementation work **before** its required behavior is implemented.

- inputs: the selected P/Plan item, active Method Projection, applicable R/E/D authority, current candidate, existing tests, complete test inputs, **and** owned work boundary.
- derive expected behavior from the governing R/E/D, **not** from the current code. apply **all** governing Methods within Delivery boundaries; reuse sufficient existing tests **when** the selected mode permits.
- write positive, negative, boundary, **and** relevant regression cases. preserve the selected test requirements, including real-command end-to-end execution with mock input Atoms **when** required; do **not** mock the implementation being checked.
- make tests runnable **when** prerequisites permit **and** return the exact tests, commands, expected outcomes, authority bindings, **and** any execution blocker. actual execution belongs **to** Implementation Evaluation.
- return `prepared` **or** `blocked`. preparing tests is **not** a passing test result; missing behavior **may** cause an expected initial failure, which still requires diagnosis before feature implementation.

- honor the selection procedure established by applicable Methods **and** the acceptance, priority, **and** disposition rules established by applicable Evaluation authority. prepare the complete admitted portfolio at its selected observable boundaries; no test scope has default priority. preserve issue-driven targeted checks as complementary evidence **without** creating Method Atoms.

## Details
