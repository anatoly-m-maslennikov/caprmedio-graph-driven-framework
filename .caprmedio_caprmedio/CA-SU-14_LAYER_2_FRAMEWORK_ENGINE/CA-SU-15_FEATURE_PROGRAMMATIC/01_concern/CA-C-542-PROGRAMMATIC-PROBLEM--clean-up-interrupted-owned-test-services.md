---
atom_id: CA-C-542
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: high
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2451]
version: 2
updated_at: 2026-10-23 03:06:32 +0400
---
# Summary

Clean up interrupted owned test services safely

## Concern

Four detached test-worker/agent services remain after the interrupted full-suite attempt. They are owned by image `bfb07ac...` and full-attempt UUID `5d368da683e04a2b8922a934a36214cd`.

## Evidences

The root validated the exact four containers and is stopping only those owned services; no production service is being stopped. The automatic interruption-cleanup gap remains unimplemented. Manual teardown must not be treated as closing that broader cleanup Concern.

## Scope

This Concern remains Active pending bounded ownership verification and safe manual cleanup. Retain the associated data, images, and stopped containers; make no production-state, validation, or generic cleanup change.
