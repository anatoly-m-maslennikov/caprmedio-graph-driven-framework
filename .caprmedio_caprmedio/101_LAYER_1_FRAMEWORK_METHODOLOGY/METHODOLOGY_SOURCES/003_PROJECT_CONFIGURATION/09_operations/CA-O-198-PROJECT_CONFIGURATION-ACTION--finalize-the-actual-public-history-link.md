---
atom_id: CA-O-198
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/caprmedio/Action//Finalize actual public Version History link
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History
  - Subject/CAPRMEDIO/Carrier/Pull Request
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery/Git Commits
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 13
updated_at: 2026-10-27 19:59:48 +0400
relations: {}
tier: 3
---
# Summary

Finalize the actual public history link

## Action

Finalize the actual public history link **means** the mechanical action that either records a no-op for an already present actual PR link or appends a newly created PR’s exact URL to the concise Version History, follows up the commit and push, and refreshes the same PR.

## Details

The actual URL is required. The Action preserves its Tool-call input/result/effect/report references on its parent Action Run. It does not create another PR, guess a URL, merge, or replay an unknown remote outcome.
