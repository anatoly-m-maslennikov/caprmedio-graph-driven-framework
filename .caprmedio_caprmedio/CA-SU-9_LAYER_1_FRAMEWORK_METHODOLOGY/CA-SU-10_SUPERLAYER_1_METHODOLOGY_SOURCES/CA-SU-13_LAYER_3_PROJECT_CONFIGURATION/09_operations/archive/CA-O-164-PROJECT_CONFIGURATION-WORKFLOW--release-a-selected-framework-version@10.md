---
atom_id: CA-O-164
content_role: Operations
type: Workflow
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Release selected Framework Version"
  depends_on: [Workflow, Step, Action, Operator, Version, Methodology, Implementation, Skill, Test, Journal]
version: 10
updated_at: "2026-10-10 18:44:09 +0400"
relations:
  relates_to: [CA-O-011, CA-O-165, CA-O-166, CA-O-168, CA-O-169, CA-R-1525]
---
# Summary

Release a selected Framework Version

## Operation

Release selected Framework Version **means** the one Operator-invoked, programmatic local Workflow that builds and installs a selected Version from its frozen active Methodology Sources. It owns the local Engine, package, runtime, `ca`, and Project-MCP work; none is another release Workflow.

## Scope

The boundary pins the Version, `version.toml`, selected active Atom identities and digests, Project Structure, settings, compiler, tests, lock, permissions, and Journal inputs. Source membership is limited to active Atoms in the Project-owned `METHODOLOGY_SOURCES` Core Meta-Model, installed extensions, and Project Configuration units. `101_FRAMEWORK_METHODOLOGY/` is the derived product; `.caprmedio_caprmedio/000_CAPRMEDIO_framework/` is the installed copy. Settings, `project_structure.toml`, and Project state are protected. Neither derived nor installed bytes become authoring authority.

## Steps

| Step | Action | Bound phase |
| --- | --- | --- |
| CA-O-170 | CA-O-165 | freeze and validate the exact local boundary |
| CA-O-175 | CA-O-167 | prepare a private active-source copy, compiled package, runtime, and `ca` payload |
| CA-O-176 | CA-O-168 | build the exact candidate image from that staged package |
| CA-O-186 | CA-O-168 | canary that exact package and image |
| CA-O-185 | CA-O-168 | run the complete local test suite before any clear operation |
| CA-O-172 | CA-O-166 | clear the derived product except protected settings, then copy only the active source units |
| CA-O-173 | CA-O-166 | compile applicable Methodology in that product and verify tested-output identity |
| CA-O-178 | CA-O-169 | clear the installed Framework except protected configuration, copy `101_FRAMEWORK_METHODOLOGY` as-is, install `ca`, and restart or reuse Project MCP for smoke |

## Transitions

| Step result | Next step or outcome |
| --- | --- |
| frozen, complete active-source boundary | CA-O-185 |
| frozen, complete active-source boundary | CA-O-175 |
| verified private package, runtime, and `ca` payload | CA-O-176 |
| verified exact candidate image | CA-O-186 |
| verified exact image canary | CA-O-185 |
| complete local tests pass | CA-O-172 |
| verified derived source product | CA-O-173 |
| byte-identical compiled product | CA-O-178 |
| verified installed copy, `ca`, and Project-MCP smoke | complete |
| missing, stale, unauthorized, failed, partial, or unsafe result | stop with actual evidence; do not clear, copy, retry, or recurse implicitly |

## Details

This Workflow starts only on one Operator command. Preparation, admission, and pin checks are internal to that command; an available receipt is a prerequisite, not another release command. A private active-source copy, compiled package/runtime/`ca`, and image are prepared and proved before the complete suite. The full suite then runs before either destructive clear operation. The later product copy and compilation must be byte-identical to the tested preparation; installation reuses the same passed package/image and does not rebuild them. Each successful state-changing step has one Git commit; a read-only preflight has recorded evidence rather than an empty commit. It never starts CA-O-188, pushes, opens a PR, or makes an installed copy authoritative.
