---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Projection/Type: Applicable Methodology'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Projection/Type: Applicable Methodology'
  - Subject/Domain/Node/Continuant/Atom.Subjects
version: 22
updated_at: 2026-10-23 03:06:32 +0400
relations: {}
atom_id: CA-M-225@22
content_role: Method
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
status: Archived
author: Anatoly Maslennikov
global_tier: 11
---
# Summary

Retrieve Applicable Methodology Mechanically

## Scope

Applicable Methodology retrieval for one Subject **or** Workflow query.

## Claim

**to** retrieve Applicable Methodology for one Subject **or** Workflow query, the Retriever **must** derive GOVERNS **and** DEPENDS_ON indexes on demand from projected Atom Subjects, select matching GOVERNS paths, add DEPENDS_ON authority **only** through transitive prerequisite closure, retain Applicable Methodology membership order, make no inference, **and** return no Atom **if** no matching GOVERNS path exists.

## Details
