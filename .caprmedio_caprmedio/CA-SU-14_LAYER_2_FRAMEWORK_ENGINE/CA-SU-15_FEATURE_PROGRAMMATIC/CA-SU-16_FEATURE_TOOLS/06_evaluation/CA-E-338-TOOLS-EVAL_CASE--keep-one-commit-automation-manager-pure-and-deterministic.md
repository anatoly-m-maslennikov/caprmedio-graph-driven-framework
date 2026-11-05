---
cce_version: cce_1
cce_form: evaluation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
version: 19
updated_at: 2026-11-02 19:44:26 +0400
relations:
  evaluation_for:
  - CA-M-182
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-338
ref_id: CA-E-338
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
form: Eval Case
tier: 3
container:
  scope_unit: CA-SU-16
---
# Keep one commit-automation manager pure and deterministic

## Claim checked

the commit-automation manager owns **all** decisions **without** performing I/O.

## Test case

supply equal typed queue, repository, action, result, settings, lease, circuit, **and** clock facts twice while replacing filesystem, subprocess, environment, network, persistence, **and** logging adapters with fail-on-call sentinels.

## Acceptance criteria

both calls return byte-equivalent typed plans **or** commands; no sentinel is called; **every** target, ordering, acceptance, fallback, retry, **and** terminal decision appears **in** the result.

## Failure disposition

reject the manager on the first effect, hidden input, nondeterministic result, **or** unowned decision.
