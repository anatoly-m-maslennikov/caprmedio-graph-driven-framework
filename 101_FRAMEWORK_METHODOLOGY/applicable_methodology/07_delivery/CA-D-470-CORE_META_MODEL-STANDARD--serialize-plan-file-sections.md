---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Plan"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Plan", "Entity/Continuant/Node/Atom.Summary", "Entity/Continuant/Node/Atom.Substance", "Entity/Continuant/Node/Atom/Content Role: Plan.Definition of Done", "Entity/Continuant/Node/Atom/Content Role: Plan.Details", "Entity/Carrier/File Carrier"]
version: 11
updated_at: "2026-10-18 03:34:50 +0400"
relations: {"relates_to": ["CA-R-1599", "CA-R-1586", "CA-D-482", "CA-D-460"]}
atom_id: "CA-D-470"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-470-CORE_META_MODEL-STANDARD--serialize-plan-file-sections.md
  source_atom_id: CA-D-470
  source_atom_revision: 11
  source_sha256: a7ebe17cc4ffde117070ccdfd4b93195036fdaefeae63f702499677e3528a825
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize Plan file sections

## Scope

Plan Markdown File Carriers and their body-section layout.

## Claim

**every** Plan Markdown File Carrier **must** contain YAML Frontmatter followed by the Plan layout registered **in** CA-D-479-CORE_META_MODEL-DELIVERY--use-stable-headings-for-atom-body-properties:

1. `# Summary` carries the Summary value.
2. `## Objective` carries the intended work **or** outcome Claim, including its applicability restrictions.
3. `## Details` carries supporting information **and** **`=1`** nested `### Definition of Done` section with the Plan's falsifying Condition Expression.

the Definition of Done is the Plan's existing Property, **not** a second completion Claim **or** an optional detail. carry its value **only** **in** that nested section. **any** other supporting Details **must** stay within the Objective. use CA-D-479-CORE_META_MODEL-DELIVERY--use-stable-headings-for-atom-body-properties for section boundaries; do **not** duplicate these Properties **in** frontmatter **or** add a separate Scope section duplicating restrictions **in** the Objective. a Hub uses this same mandatory file, **not** an additional Objective Atom.

## Details
