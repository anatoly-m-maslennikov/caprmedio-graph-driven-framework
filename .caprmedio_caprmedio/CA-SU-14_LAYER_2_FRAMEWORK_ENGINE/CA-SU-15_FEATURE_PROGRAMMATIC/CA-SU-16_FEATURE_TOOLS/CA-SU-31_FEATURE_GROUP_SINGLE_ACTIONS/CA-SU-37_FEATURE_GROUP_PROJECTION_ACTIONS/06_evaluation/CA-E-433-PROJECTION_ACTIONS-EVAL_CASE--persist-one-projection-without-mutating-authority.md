---
atom_id: CA-E-433
ref_id: CA-E-433
container:
  scope_unit: CA-SU-37
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Output Publication
tier: 4
relations:
  evaluation_for:
  - CA-R-1387
  - CA-M-259
  - CA-R-1076
status: Active
version: 21
updated_at: 2026-11-04 15:23:33 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROJECTION_ACTIONS
claim_target_scope_unit: PROJECTION_ACTIONS
---
# Persist one Projection without mutating authority

## Test case

Run description **and** ordinary generation **without** a destination; persist **to** one explicit valid Projection destination; repeat through one registered destination; **then** attempt an ambiguous destination, path traversal, symlink escape, **and** destinations inside Atom **and** Journal authority. Optionally let `GRAPH_UI` present the valid result.

## Acceptance criteria

**only** the explicit **or** unambiguous registered persistence replaces exactly one Projection Carrier atomically. Every authority **and** Journal byte remains unchanged. Invalid destinations fail **without** partial output. Optional `GRAPH_UI` presentation preserves the Projection’s source lineage **and** non-authoritative status; it cannot use the Projection as authority **or** mutate it.
