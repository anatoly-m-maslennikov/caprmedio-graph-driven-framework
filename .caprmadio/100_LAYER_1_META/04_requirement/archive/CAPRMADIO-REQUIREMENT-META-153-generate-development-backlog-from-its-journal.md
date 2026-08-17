---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-153
scope_path: layer:meta
subject_scope: development-flow
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-105
  child_of:
    - CAPRMADIO-REQUIREMENT-META-135-preserve-content-role-boundaries-through-caprmadio-loop
    - CAPRMADIO-REQUIREMENT-META-154-three-artifact-forms-with-generated-projections
---
# Requirement — Generate Development Backlog from its Journal

The project has one append-only Development Backlog Journal with the Concern
Content role. Its records add, revise, allocate, move, remove, or promote
one-line work candidates that may anticipate work in any CAPRMADIO Content role.

CAPRMADIO automatically generates the current Development Backlog Projection
from the Journal without operator-authored Projection content. The Projection
groups unresolved candidates into unscheduled work, the current target version,
and future target versions. Candidates express Concerns requiring disposition;
they are neither Plans nor specification authority. A target-version allocation
is not a frozen version or release claim.

## Primary claim

CAPRMADIO derives one current Development Backlog Concern Projection from an
append-only Journal of candidate-planning events.
