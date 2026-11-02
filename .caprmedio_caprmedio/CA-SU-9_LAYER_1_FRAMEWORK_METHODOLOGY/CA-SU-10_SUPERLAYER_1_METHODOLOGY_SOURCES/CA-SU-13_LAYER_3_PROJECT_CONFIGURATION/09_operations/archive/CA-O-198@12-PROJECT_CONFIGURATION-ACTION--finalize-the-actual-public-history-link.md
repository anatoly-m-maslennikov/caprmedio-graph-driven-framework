---
atom_id: CA-O-198@12
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action//Finalize actual public Version History link'
  depends_on:
  - Subject/Graph Node/Domain/Continuant/History
  - Subject/Graph Node/Carrier/Pull Request
  - Subject/Graph Node/Engineering/Delivery/Git Commits
  - Subject/Graph Node/Domain/Occurrent/Execution
  - Subject/Graph Node/Domain/Continuant/History/Journal
version: 12
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
tier: 3
---
# Summary

Finalize the actual public history link

## Action

Finalize the actual public history link **means** the mechanical action that either records a no-op for an already present actual PR link or appends a newly created PR’s exact URL to the concise Version History, follows up the commit and push, and refreshes the same PR.

## Details

The actual URL is required. The Action preserves its Tool-call input/result/effect/report references on its parent Action Run. It does not create another PR, guess a URL, merge, or replay an unknown remote outcome.
