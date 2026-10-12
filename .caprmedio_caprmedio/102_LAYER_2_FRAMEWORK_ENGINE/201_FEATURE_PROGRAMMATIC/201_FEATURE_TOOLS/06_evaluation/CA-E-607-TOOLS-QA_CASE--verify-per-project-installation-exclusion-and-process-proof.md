---
atom_id: CA-E-607
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Concurrency acceptance"
  depends_on: [Tool, Runtime, Project, Process, State]
relations:
  evaluation_for: [CA-R-1912, CA-R-1913, CA-M-364, CA-D-603, CA-D-604]
---
# Summary

Verify per-Project installation exclusion and process proof

## Scope

the competing-publication and PID-insufficiency acceptance cases.

## Claim

the QA case **must** prove the shared lock excludes concurrent selector, wrapper, Skill, projection and state publication for one Project, and **must not** accept a PID-only process record.

## Details

Competing same-Project attempts allow one holder and preserve the other as blocked; two different target contexts proceed independently. Process cases require matching generation, command, package, context and release proof, then change each binding while retaining PID to prove refusal. Stale/uncertain locks never permit automatic takeover.
