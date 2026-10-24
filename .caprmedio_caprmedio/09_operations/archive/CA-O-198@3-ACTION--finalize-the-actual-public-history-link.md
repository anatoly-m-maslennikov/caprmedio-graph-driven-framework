---
atom_id: CA-O-198@3
content_role: Operations
type: Action
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Archived
author: "Anatoly Maslennikov"
subjects:
  governs: "Finalize actual public Version History link"
  depends_on: [Version History, Pull Request, Git Commit, Tool Call, Journal]
version: 3
updated_at: "2026-10-12 00:00:00 +0000"
relations:
  relates_to: [CA-O-188, CA-O-197, CA-R-1923, CA-R-1926, CA-R-1928]
---
# Summary

Finalize the actual public history link

## Action

Finalize the actual public history link **means** the mechanical action that either records a no-op for an already present actual PR link or appends a newly created PR’s exact URL to the concise Version History, follows up the commit and push, and refreshes the same PR.

## Details

The actual URL is required. The Action preserves its Tool-call input/result/effect/report references on its parent Action Run. It does not create another PR, guess a URL, merge, or replay an unknown remote outcome.
