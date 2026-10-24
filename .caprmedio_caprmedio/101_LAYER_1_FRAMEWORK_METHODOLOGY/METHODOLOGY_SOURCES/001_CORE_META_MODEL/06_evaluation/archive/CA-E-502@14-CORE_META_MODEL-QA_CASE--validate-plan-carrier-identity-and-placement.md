---
subjects:
  governs: "Entity/Carrier"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Plan", "Entity/Carrier/File Carrier", "Entity/Carrier/Directory Carrier", "Entity/Node/Continuant/Atom.ID", "Entity/Node/Continuant/Atom.Summary", "Entity/Node/Continuant/Atom/Content Role: Plan.Work Sequence Number", "Entity/Node/Continuant/Atom/Content Role: Plan.Label", "Entity/Node/Continuant/Atom/Content Role: Plan.Status", "Entity/Node/Continuant/Atom/Content Role: Plan.Definition of Done"]
version: 14
updated_at: "2026-10-20T20:50:42.246Z"
relations: {"evaluation_for": ["CA-D-460", "CA-D-461", "CA-D-469", "CA-D-470", "CA-D-472", "CA-D-475", "CA-R-1534", "CA-R-1599", "CA-R-997"]}
atom_id: CA-E-502@14
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: Archived
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
---
# Summary
Validate Plan Carrier identity **and** placement

## Scope
Plan Carrier identity **and** placement.

## Claim
the Plan Carrier Evaluation **must** reject Carrier facts that create duplicate identity **or** contradict the shared Plan model.

- accept a mandatory Markdown file **with** **or** **without** a matching optional Hub directory under `CA-D-460-CORE_META_MODEL-CORE-DELIVERY--serialize-plan-atom-carrier-bundles`; reject a directory **without** that file.
- count a matching pair once; reject two IDs, divergent stems, conflicting Status, a separate Epic identity, **or** an Objective file that claims **to** be another Atom for the same Hub.
- require DoD **in** **every** supplied Plan file, even **when** it carries a pure Hub **or** explicit overrides.
- validate leading navigation numbers **before** Atom IDs, their local uniqueness, mutable Label tokens, **and** canonical Summary slugs. changing a number **or** Label **must not** change identity **or** scheduling.
- read Plan Status from its own file **and** check its local placement; reject read-time inference from a containing Hub **or** path.
- change a parent Plan's Status to Active, Backlog, Done, Canceled **or** Archived as admitted by its model: require independent single-Atom Actions for the selected latest descendants under CA-R-1521, without an optional descendant mode. For target Done, contained latest Plans already Done remain unchanged with no Revision churn, and every other contained latest Plan is requested as Canceled. For target Archived, every contained latest Atom is requested as Archived, including Done Plans. Other admitted targets retain the same-Status cascade. Check each Atom's own model; reject an invented target value **or** a multi-target Action.
- retain each Current descendant inside its parent Carrier tree with the local Status mapping under CA-D-461; for a contained Current Plan, validate its Status placement relative to its immediate containing Plan's Directory Carrier. For example, a Done child is in `<parent-directory>/done/<child>.md`, using its canonical matching stem. Validate Draft carriers in the owning Scope Unit's shared `03_plan/draft` area. Validate each Archived Plan Markdown Carrier directly in the shared `03_plan/archived` area, without parent/child Plan directory nesting, and with CA-D-289's Version suffixes.
- leave referenced Plans outside the tree **and** older archived Revision bytes, Version **and** Status unchanged; reject older Revisions as cascade targets. Allow retained-history subtrees and non-Atom assets to accompany the matching Directory Carrier byte-for-byte unchanged, without inferring Status effects. No independent migration of noncanonical legacy `archive/` trees is implied.
- accept root Backlog Plans **in** `03_plan/001_backlog`; reject `031_backlog` as the canonical new encoding **and** reject a `version-<VERSION>` directory substituted for a Version-labeled Plan identity.
- retain one identity **when** decomposed work is added, removed, **or** reordered; a changed Summary follows Atom replacement authority rather than independent filename editing.

report the invalid Carrier Bundle, source fact, **and** violated Delivery rule.

## Details
