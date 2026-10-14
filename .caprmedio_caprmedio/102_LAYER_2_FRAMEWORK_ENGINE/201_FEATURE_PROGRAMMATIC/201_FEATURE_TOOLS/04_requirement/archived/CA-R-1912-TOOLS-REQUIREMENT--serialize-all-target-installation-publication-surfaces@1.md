---
atom_id: CA-R-1912
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Publication exclusion"
  depends_on: [Tool, Runtime, Skill, Projection, State, Project]
relations:
  relates_to: [CA-D-603, CA-E-607]
---
# Summary

Serialize all target installation publication surfaces

## Scope

the mutual exclusion boundary for target runtime effects.

## Claim

the INSTALL_TOOLS facade **must** use the same per-Project lock for selector, wrappers, Skill, projection and state publication, and **must not** let a competing installation publish any subset.

## Details

The lock names target context, owner run, operation, command digest and lock generation; every publication reopens it and revalidates inputs. The lock is project-specific, so separate selected Projects do not serialize each other. Candidate construction and image proof cannot bypass it.
