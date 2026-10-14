---
atom_id: CA-O-164
content_role: Operations
type: Workflow
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release selected Framework Version"
  depends_on: [Workflow, Step, Action, Operator, Version, Methodology, Implementation, Skill, Test, Journal]
version: 14
updated_at: "2026-10-12 00:00:51 +0000"
relations:
  relates_to: [CA-O-011, CA-O-165, CA-O-166, CA-O-168, CA-O-169, CA-R-1525]
---
# Summary

Release a selected Framework Version

## Operation

Release selected Framework Version **means** the one Operator-invoked local Workflow that runs intended tool tests, copies active Methodology Sources, compiles them, installs Engine `.install` into the Project runtime package, and verifies the installed Docker/MCP path. It owns the local Engine, package, runtime, `ca`, and Project-MCP work; none is another release Workflow.

## Scope

The Workflow uses the current active Atoms in the Project-owned `METHODOLOGY_SOURCES` Core Meta-Model, installed extensions, and Project Configuration units. `101_FRAMEWORK_METHODOLOGY/` is the derived product; `.caprmedio_caprmedio/000_CAPRMEDIO_framework/` is the installed copy. Settings, `project_structure.toml`, and Project state are protected. Neither derived nor installed bytes become authoring authority.

## Steps

| Step | Action | Bound phase |
| --- | --- | --- |
| CA-O-170 | CA-O-165 | validate current active sources and delivery paths |
| intended tool tests | — | run the intended local-release tests |
| CA-O-172 | CA-O-166 | clear the derived product except protected settings, then copy only the active source units |
| CA-O-173 | CA-O-166 | compile applicable Methodology in that product |
| CA-O-178 | CA-O-169 | clear the installed Framework except protected configuration, copy `101_FRAMEWORK_METHODOLOGY` as-is, install `ca`, restart or reuse Project MCP for smoke, then remove verified superseded Project-owned release images |

## Transitions

| Step result | Next step or outcome |
| --- | --- |
| current active sources and delivery paths are valid | intended tool tests |
| intended tool tests pass | CA-O-172 |
| verified derived source product | CA-O-173 |
| compiled product | CA-O-178 |
| verified installed copy, `ca`, and Project-MCP smoke | complete |
| failed or unsafe result | stop and report it for manual handling |

## Details

This Workflow starts on one Operator command. It runs Git before every listed Step and before intended tool tests, then runs Git again after final completion. It validates the current inputs, runs intended local-release tests, copies active sources into the product, compiles them, installs Engine `.install` into the Project runtime package, and smokes the installed Docker/MCP path. A failed step or test stops and is reported for manual handling. It never starts CA-O-188, pushes, opens a PR, or makes an installed copy authoritative.
