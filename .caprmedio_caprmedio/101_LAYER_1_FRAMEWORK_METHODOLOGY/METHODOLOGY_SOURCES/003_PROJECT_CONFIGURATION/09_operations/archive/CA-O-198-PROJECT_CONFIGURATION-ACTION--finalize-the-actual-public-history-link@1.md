---
atom_id: "CA-O-198"
content_role: Operations
type: Action
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Finalize actual public Version History link"
  depends_on: [Version History, Pull Request, Full Gate, Git Commit, Tool Call, Journal]
version: 1
updated_at: "2026-10-09 12:45:00 +0000"
relations:
  relates_to: [CA-O-188, CA-O-197, CA-R-1922, CA-R-1923, CA-R-1924, CA-R-1925, CA-R-1926, CA-R-1928, CA-R-1929]
---
# Summary

Finalize the actual public history link

## Action

Finalize the actual public history link **means** the native action that either records a no-op for an already gated actual PR link or binds a newly created PR’s actual URL into the concise Version History, renews the exact Full Gate, follows up the push, and refreshes the same PR.

## Details

The actual URL and changed candidate snapshot are both required before the renewed gate. The action preserves its Tool-call input/result/effect/report references on its parent Action Run. It does not create another PR, guess a URL, merge, or replay an unknown remote outcome.
