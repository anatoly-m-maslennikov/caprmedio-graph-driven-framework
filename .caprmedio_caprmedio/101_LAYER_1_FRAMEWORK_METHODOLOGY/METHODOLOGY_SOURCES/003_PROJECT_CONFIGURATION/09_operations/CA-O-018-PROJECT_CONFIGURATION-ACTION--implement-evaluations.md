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
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Atom/Content Role: Plan/Type: Plan", "Entity/Continuant/Object/Atom/Content Role: Evaluation", "Entity/Continuant/Object/Atom/Content Role: Method", "Entity/Continuant/Object/Atom/Content Role: Delivery", "Entity/Continuant/Object/Atom/Content Role: Requirement", "Implementation"]
version: 9
updated_at: "2026-10-18 16:21:26 +0400"
relations:
  relates_to:
    - CA-O-017
    - CA-O-020
global_tier: 11
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
