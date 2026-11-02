---
atom_id: CA-O-230@5
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Archived
version: 5
updated_at: 2026-10-23 03:14:50 +0400
global_tier: 11
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Agentic Step Execution Context
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Occurrent/Execution/Step Run
relations:
  relates_to:
  - CA-O-016
  - CA-O-225
  - CA-R-1527
  - CA-R-1525
---
# Summary

Review code in shared implementation context

## Operation

Shared Implementation Review Step means the CA-O-016 node invoking exactly one Action, CA-O-225, in explicit Integrated context under CA-R-1527.

- require explicit review_phase preliminary or final from CA-O-231; do not derive the phase from absent evidence or use the standalone default.
- bind selected Project, bounded request and P/Plan, owned candidate and changed paths, direct full `requirements`, `methods`, `evaluations`, and `delivery` rows with applicable Project-Principle sources, substantive obligation/coverage map, actual check and diagnosis evidence with pending/stale outcomes, relevant inputs, permissions, retained findings, and remaining retry/resource state. An optional legacy `method_projection` may accompany direct rows but is not required.
- retain the participating session without replacing complete source-bound inputs with conversational memory. Revalidate source/candidate/test/input bindings before assessment and preserve actual partial findings.
- pass preliminary_clear, passed, findings, partial, or unresolved directly to CA-O-016. Read-only review never edits code, changes authority, grants a retry, or launches release; repairs remain in the enclosing implementation Workflow.
- preserve exact Action/Step revisions, candidate and evidence bindings, actual effects, and returned results. Standalone CA-O-229 retains its own Isolated binding.

## Details
