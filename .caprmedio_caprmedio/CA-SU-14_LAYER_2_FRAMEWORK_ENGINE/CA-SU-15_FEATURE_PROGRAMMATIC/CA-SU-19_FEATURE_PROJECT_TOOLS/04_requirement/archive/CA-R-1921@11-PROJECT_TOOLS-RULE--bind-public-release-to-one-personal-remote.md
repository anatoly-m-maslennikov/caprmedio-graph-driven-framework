---
atom_id: CA-R-1921@11
content_role: Requirement
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Delivery
  depends_on:
  - Subject/Graph Node/Engineering/Git/Remote
  - Subject/Graph Node/Engineering/Git/Branch
  - Subject/Graph Node/Engineering/Pull Request
version: 11
updated_at: 2026-10-26 00:46:35 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Bind public release to one personal remote

## Scope

the selected remote boundary of one public release.

## Claim

**the Operator** **must** bind one public-release invocation to an explicit personal remote identity and the exact `amm/dev` to `main` branch direction.

## Details

The binding contains no credential or secret. A different remote, owner, head, base, or branch direction is out of scope and stops the invocation.
