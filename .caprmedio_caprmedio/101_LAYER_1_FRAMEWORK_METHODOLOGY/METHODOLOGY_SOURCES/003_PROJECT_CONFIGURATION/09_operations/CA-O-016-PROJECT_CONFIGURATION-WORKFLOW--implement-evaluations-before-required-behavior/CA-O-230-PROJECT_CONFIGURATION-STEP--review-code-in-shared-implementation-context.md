---
atom_id: CA-O-230
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
version: 10
updated_at: 2026-10-27 19:59:48 +0400
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run.Agentic Step Execution Context
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
relations:
  depends_on:
  - CA-R-1527
tier: 3
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
