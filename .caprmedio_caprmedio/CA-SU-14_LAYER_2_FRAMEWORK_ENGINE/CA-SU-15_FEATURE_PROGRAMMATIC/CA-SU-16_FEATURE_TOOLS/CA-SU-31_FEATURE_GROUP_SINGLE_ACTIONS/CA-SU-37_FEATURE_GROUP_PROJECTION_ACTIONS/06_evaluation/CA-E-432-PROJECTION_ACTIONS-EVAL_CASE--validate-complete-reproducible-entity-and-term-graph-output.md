---
atom_id: CA-E-432
ref_id: CA-E-432
container:
  scope_unit: CA-SU-37
role: Evaluation
form: Eval Case
topics:
  main_subject: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Entities Graph'
tier: 4
relations:
  evaluation_for:
  - CA-R-1387
  - CA-M-259
status: Active
version: 18
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROJECTION_ACTIONS
claim_target_scope_unit: PROJECTION_ACTIONS
---
# Validate complete reproducible Entity and Term graph output

## Test case

Generate twice from identical fixtures containing declared Terms, one parent chain, direct dependencies with transitive closure, an unresolved reference, a dependency cycle, a cardinality violation, **and** an unparseable Carrier.

## Acceptance criteria

the two semantic outputs are byte-identical **and** stably ordered. They contain **every** declared Term, direct parent, direct edge, closure edge, cycle, violation, unresolved reference, unparseable region, source path **and** digest, frontier identity, settings digest, **and** explicit non-authoritative status.
