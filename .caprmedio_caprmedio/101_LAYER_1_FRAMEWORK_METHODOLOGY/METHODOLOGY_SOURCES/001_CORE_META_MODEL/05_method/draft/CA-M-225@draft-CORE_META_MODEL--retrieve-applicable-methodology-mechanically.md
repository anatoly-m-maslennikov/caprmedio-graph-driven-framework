---
subjects:
  governs: "Entity/Continuant/Node/Projection/Type: Applicable Methodology"
  depends_on:
    ["Entity/Continuant/Node/Projection/Type: Applicable Methodology", "Entity/Continuant/Node/Atom.Subjects"]
version: 19
updated_at: "2026-10-17 23:26:54 +0000"
relations: {}
atom_id: "CA-M-225@draft"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Retrieve Applicable Methodology Mechanically

## Scope

Applicable Methodology retrieval for one Subject **or** Workflow query.

## Claim

**to** retrieve Applicable Methodology for one Subject **or** Workflow query, the Retriever **must** derive GOVERNS **and** DEPENDS_ON indexes on demand from projected Atom Subjects, select matching GOVERNS paths, add DEPENDS_ON authority **only** through transitive prerequisite closure, retain Applicable Methodology membership order, make no inference, **and** return no Atom **if** no matching GOVERNS path exists.

## Details
