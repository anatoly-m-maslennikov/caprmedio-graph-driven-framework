---
subjects:
  governs: Background Service/Implementation Dependency
  depends_on: []
version: 13
updated_at: 2026-10-24 00:51:05 +0400
relations:
  evaluation_for:
  - CA-R-857
  - CA-M-104
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-224@13
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
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
