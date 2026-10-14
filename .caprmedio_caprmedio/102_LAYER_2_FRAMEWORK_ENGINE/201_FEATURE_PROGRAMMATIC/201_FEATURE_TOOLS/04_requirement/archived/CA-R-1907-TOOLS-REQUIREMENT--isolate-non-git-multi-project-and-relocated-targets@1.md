---
atom_id: CA-R-1907
content_role: Requirement
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-09 16:24:06 +0400"
subjects:
  governs: "Framework Installation contribution/Target topology isolation"
  depends_on: [Tool, Project, Runtime, Registry]
relations:
  relates_to: [CA-D-600, CA-E-603]
---
# Summary

Isolate non-git, multi-project and relocated targets

## Scope

the supported target topology variations for one installation contribution.

## Claim

the INSTALL_TOOLS facade **must** distinguish a non-git Project, two Projects in one repository and relocation by separate target contexts, and **must not** use repository root or absolute checkout path as the sole Project identity.

## Details

A non-git context records no repository identity; sibling Projects in one repository require distinct Project identities and control children. Relocation makes a new context with an explicit predecessor and verifies the declared Project identity and controls again. Each target owns separate lock, selector and state; ambiguous topology refuses.
