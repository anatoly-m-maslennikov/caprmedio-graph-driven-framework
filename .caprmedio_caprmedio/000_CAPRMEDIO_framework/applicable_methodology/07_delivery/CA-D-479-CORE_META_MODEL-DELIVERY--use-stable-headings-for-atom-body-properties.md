---
subjects:
  governs: "Markdown Atom Carrier.Main Content"
  depends_on:
    ["Entity/Node/Continuant/Atom.Summary", "Entity/Node/Continuant/Atom.Substance", "Atom/Content Role", "Entity/Node/Continuant/Atom.Details", "Property", "Markdown Atom Carrier"]
version: 11
updated_at: "2026-10-20 03:01:57 +0400"
relations: {"relates_to": ["CA-D-356", "CA-D-478"]}
atom_id: "CA-D-479"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-479-CORE_META_MODEL-DELIVERY--use-stable-headings-for-atom-body-properties.md
  source_atom_id: CA-D-479
  source_atom_revision: 11
  source_sha256: 76025c01f0f9d7599a2dfdfa0bd3664bb6afaff9eeb95f889ccede9d31cd1b8d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Use stable headings for Atom body Properties

## Scope

structured Main Content of Markdown Atom Carriers for **all** Content Roles.

## Claim

a Markdown Atom's Main Content **must** carry its body Properties under the following registered layout, **after** **`=1`** literal `# Summary` heading with the Summary value below it. An R Atom expressing a formal Graph Rule uses Summary followed by one operative YAML block under CA-D-637. It has no Claim or Substance Property or section and no separate prose Scope. Optional `## Semantics` and `## Details` sections may follow the operative block, each at most once and in either order; neither is required. This exception does not apply automatically to every R/Type: Rule Atom. All other Atoms use these exact headings **in** the listed order:

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

## Details
