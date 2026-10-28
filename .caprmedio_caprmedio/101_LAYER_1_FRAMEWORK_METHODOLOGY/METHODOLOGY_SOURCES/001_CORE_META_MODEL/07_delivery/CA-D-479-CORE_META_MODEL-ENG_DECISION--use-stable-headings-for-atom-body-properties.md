---
subjects:
  governs: Subject/CAPRMEDIO/Carrier/File.Main Content
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Details
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
  - Subject/CAPRMEDIO/Carrier/File
version: 22
updated_at: 2026-10-27 19:59:25 +0400
relations: {}
atom_id: CA-D-479
content_role: Delivery
type: Eng Decision
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
---
# Summary

Use stable headings for Atom body Properties

## Scope

structured Main Content of Markdown Atom Carriers for **all** Content Roles.

## Claim

a Markdown Atom's Main Content **must** carry its body Properties under the following registered layout, **after** **`=1`** literal `# Summary` heading with the Summary value below it. An R Atom expressing a formal Graph Rule carries its fully formal YAML `claim.*` mapping in frontmatter under CA-D-637. Its Main Content has Summary, with optional `## Semantics` and `## Details` sections, and no duplicate prose Claim or Substance Property or section. This exception does not apply automatically to every R/Type: Rule Atom. All other Atoms use these exact headings **in** the listed order:

| Content Role | Required level-two headings, **in** order |
|---|---|
| Requirement, Method, Evaluation, Delivery | `## Scope`, `## Claim`, `## Details` |
| Analysis | `## Question`, `## Scope`, `## Approach`, `## Results`, `## TLDR` |
| Concern | `## Concern`, `## Evidences`, `## Blast radius` |
| Plan | `## Objective`, `## Details` |
| Operations | `## Operation`, `## Details` |

- for the ordinary role layout, carry **`=1`** occurrence of **every** listed heading for the Atom's Content Role. the primary content block is Claim for RMED, Question for Analysis, Concern for Concern, Objective for Plan, **and** Operation for Operations; position alone does **not** identify it; do **not** add a duplicate `## Claim` section **when** another heading is registered for that role.
- in the ordinary RMED layout, Scope carries the Claim's applicability under CA-D-495. it precedes Claim, but is **not** a replacement for Claim **or** the source of Summary by itself.
- carry a Property **only** **in** its registered section, **not** again **in** frontmatter. use CA-D-470 for the Plan Definition of Done inside Details.
- a Property's section ends at the next heading of the same **or** a higher level, **or** at end of Main Content. supporting headings use lower levels; a separately registered nested Property remains independently addressable **without** copying its value.
- heading markers inside fenced code examples are content, **not** Property boundaries.
- do **not** infer a missing, renamed, duplicated, **or** ambiguously nested Property heading from prose, synonyms, **or** position alone.
- a Details section **may** be empty **when** no supporting content **or** required nested Property applies. this does **not** waive the Plan Definition of Done.
- Draft Atoms may omit required body Properties while incomplete; their Atom ID remains mandatory under CA-D-276 and CA-R-2102. Report missing Properties, and require the full role-specific layout before promotion to Current. This does not create another body layout or relax the formal Graph Rule exception above.

## Details
