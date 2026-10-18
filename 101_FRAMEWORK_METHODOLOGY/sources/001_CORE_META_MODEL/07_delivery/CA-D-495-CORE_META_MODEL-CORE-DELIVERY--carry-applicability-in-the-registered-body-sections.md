---
subjects:
  governs: "Entity/Continuant/Node/Atom.Substance"
  depends_on:
    ["Entity/Continuant/Node/Atom.Substance", "Entity/Continuant/Node/Atom.Target Scope Unit", "Entity/Carrier/File Carrier", "Entity/Continuant/Node/Atom/Content Role"]
version: 5
updated_at: "2026-10-18 03:34:53 +0400"
relations: {"relates_to": ["CA-D-479", "CA-D-482", "CA-R-1271"]}
atom_id: "CA-D-495"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Carry applicability in the registered body sections

## Scope

applicability restrictions of Claims carried by Markdown Atom Carriers.

## Claim

a Markdown Atom Carrier **must** carry the Claim's applicability **in** the registered body sections, **not** as a duplicate frontmatter value:

- for RMED, carry applicability **in** Scope, followed by the qualified contribution **in** Claim **and** supporting information **in** Details, using the exact headings registered by CA-D-479.
- for other Content Roles, retain applicability **in** their registered primary content. this rule does **not** change their body-section layouts.
- the RMED Scope section **must** contain an applicability description, **not** just a copy of `current_scope_unit` **or** `claim_target_scope_unit`. those fields remain the carried structural references under CA-D-482.
- carry the applicability restrictions **=1** time. Claim **and** Details are read within Scope; do **not** maintain a second scope declaration **in** either section **or** frontmatter.

## Details

Scope identifies what the Claim applies **to**, including relevant conditions **and** exclusions. it does **not** select another structural target, change ownership, **or** introduce a separate Claim. a reference **to** the carried target is **not** a second authoritative copy of that target.
