---
atom_id: CA-R-1926@8
content_role: Requirement
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Public Release/Pull Request Identity
  depends_on:
  - Subject/Engineering/Public Release/Pull Request Identity
  - Subject/Engineering/Git/Branch
  - Subject/Engineering/Git/Remote
version: 8
updated_at: 2026-10-24 20:11:44 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Maintain one matching open `main` PR

## Scope

one public release Pull Request boundary.

## Claim

**the Operator** **must** discover, create, or update exactly one actual open PR from the selected `amm/dev` head to `main` on the selected personal remote.

## Details

Zero matches permits create after the actual initial push. More than one match, a changed existing identity, or an unsafe/nonmatching URL blocks the Workflow.
