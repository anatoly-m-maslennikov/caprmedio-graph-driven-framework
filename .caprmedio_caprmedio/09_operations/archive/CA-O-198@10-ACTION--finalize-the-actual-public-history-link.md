---
atom_id: CA-O-198@10
content_role: Operations
type: Action
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action//Finalize actual public Version History link'
  depends_on:
  - Subject/Graph Node/Engineering/Release/Version History
  - Subject/Graph Node/Engineering/Pull Request
  - Subject/Graph Node/Engineering/Git/Commit
  - Subject/Graph Node/Domain/Occurrent/Execution
  - Subject/Graph Node/Domain/Continuant/History/Journal
version: 10
updated_at: 2026-10-25 17:32:27 +0400
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
