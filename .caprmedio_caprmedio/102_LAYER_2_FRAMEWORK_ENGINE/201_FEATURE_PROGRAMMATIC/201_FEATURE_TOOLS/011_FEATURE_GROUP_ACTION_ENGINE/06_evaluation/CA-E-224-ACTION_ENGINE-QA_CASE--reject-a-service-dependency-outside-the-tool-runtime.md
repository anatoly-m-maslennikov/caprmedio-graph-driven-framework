---
subjects:
  governs: Background Service/Implementation Dependency
  depends_on: []
version: 16
updated_at: 2026-10-24 03:32:22 +0400
relations:
  evaluation_for:
  - CA-R-2154
  - CA-M-104
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-224
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: ACTION_ENGINE
type: Eval Case
tier: 3
claim_target_scope_unit: ACTION_ENGINE
---
# Reject a service dependency outside the Tool runtime

## Claim checked

A registered background service cannot load Framework implementation from the canonical source, a non-Tool runtime descendant, temporary state, **or** another Project path.

## Test case

Install a service registry whose Python command addresses a script **in** the repository outside `.caprmedio_runtime/tools`; invoke dry-run.

## Acceptance criteria

the Tool returns one stable dependency-boundary diagnostic **before** starting a process **or** creating service runtime state. Git, governed source, registry, runtime, temporary state, **and** the external script remain byte-identical.

## Failure disposition

Reject delivery **if** the external script is accepted, read as framework dependency, copied implicitly, **or** started; **or** **if** rejection mutates project state.
