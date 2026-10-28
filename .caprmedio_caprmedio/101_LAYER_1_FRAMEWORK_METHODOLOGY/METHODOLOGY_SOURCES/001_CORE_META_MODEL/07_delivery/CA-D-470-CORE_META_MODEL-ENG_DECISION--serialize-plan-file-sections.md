---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Definition of Done'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Details'
  - Subject/CAPRMEDIO/Carrier/File
version: 25
updated_at: 2026-10-27 19:59:25 +0400
relations: {}
atom_id: CA-D-470
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize Plan file sections

## Scope

Plan Markdown File Carriers and their body-section layout.

## Claim

**every** Plan Markdown File Carrier **must** contain YAML Frontmatter followed by the Plan layout registered **in** CA-D-479-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties:

1. `# Summary` carries the Summary value.
2. `## Objective` carries the intended work **or** outcome Claim, including its applicability restrictions.
3. `## Details` carries supporting information **and** **`=1`** nested `### Definition of Done` section with the Plan's falsifying Condition Expression.

the Definition of Done is the Plan's existing Property, **not** a second completion Claim **or** an optional detail. carry its value **only** **in** that nested section. **any** other supporting Details **must** stay within the Objective. use CA-D-479-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties for section boundaries; do **not** duplicate these Properties **in** frontmatter **or** add a separate Scope section duplicating restrictions **in** the Objective. a Hub uses this same mandatory file, **not** an additional Objective Atom.

## Details
