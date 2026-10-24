---
atom_id: CA-O-198@5
content_role: Operations
type: Action
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Finalize actual public Version History link
  depends_on:
  - Subject/Engineering/Release/Version History
  - Pull Request
  - Git Commit
  - Subject/Domain/Node/Occurrent/Execution
  - Journal
version: 5
updated_at: 2026-10-24 00:38:25 +0400
relations:
  relates_to:
  - CA-O-188
  - CA-O-197
  - CA-R-1923
  - CA-R-1926
  - CA-R-1928
tier: 3
---
# Summary

Finalize the actual public history link

## Action

Finalize the actual public history link **means** the mechanical action that either records a no-op for an already present actual PR link or appends a newly created PR’s exact URL to the concise Version History, follows up the commit and push, and refreshes the same PR.

## Details

The actual URL is required. The Action preserves its Tool-call input/result/effect/report references on its parent Action Run. It does not create another PR, guess a URL, merge, or replay an unknown remote outcome.
