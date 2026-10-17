---
atom_id: CA-O-018
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Evaluation Implementation"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Atom/Content Role: Plan/Type: Plan", "Entity/Continuant/Object/Atom/Content Role: Evaluation", "Entity/Continuant/Object/Atom/Content Role: Method", "Entity/Continuant/Object/Atom/Content Role: Delivery", "Entity/Continuant/Object/Atom/Content Role: Requirement", "Implementation"]
version: 8
updated_at: "2026-10-15 18:52:51 +0000"
relations:
  relates_to:
    - CA-O-017
    - CA-O-020
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-018-CORE_META_MODEL-ACTION--implement-evaluations.md
  source_atom_id: CA-O-018
  source_atom_revision: 8
  source_sha256: 34e7155f05d54d79d47e1651e9660d4172cbe867c9d516ac54f2be2607174557
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
