---
atom_id: CA-R-1926
content_role: Requirement
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  depends_on:
  - Subject/CAPRMEDIO/Carrier/Pull Request.ID
  - Subject/CAPRMEDIO/Carrier/Git Branch
  - Subject/CAPRMEDIO/Carrier/Git Repository
version: 12
updated_at: 2026-10-27 20:00:05 +0400
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
