---
subjects:
  governs: "Entity/Node/Continuant/Atom.Substance"
  depends_on:
    ["Entity/Node/Continuant/Atom.Substance", "Entity/Node/Continuant/Atom.Target Scope Unit", "Entity/Carrier/File Carrier", "Entity/Node/Continuant/Atom/Content Role"]
version: 8
updated_at: "2026-10-20 03:02:30 +0400"
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

- for ordinary RMED layouts, carry applicability **in** Scope, followed by the qualified contribution **in** Claim **and** supporting information **in** Details, using the exact headings registered by CA-D-479.
- for an R Atom expressing a formal Graph Rule, carry the operative applicability and restrictions once in the structured YAML under CA-D-637: `applies_to` selects the governed cases and `condition` carries their constraint. There is no Claim or Substance Property or section and no separate prose Scope. Semantics and Details are optional supporting sections under CA-D-637, not another copy of the operative applicability or constraint. Ordinary R/Type: Rule Atoms do not acquire this exception automatically.
- for other Content Roles, retain applicability **in** their registered primary content. this rule does **not** change their body-section layouts.
- an ordinary RMED Scope section **must** contain an applicability description, **not** just a copy of `current_scope_unit` **or** `claim_target_scope_unit`. those fields remain the carried structural references under CA-D-482.
- carry the applicability restrictions **=1** time. in the ordinary RMED layout, Claim **and** Details are read within Scope; do **not** maintain a second scope declaration **in** either section **or** frontmatter.

## Details

Scope identifies what the Claim applies **to**, including relevant conditions **and** exclusions. it does **not** select another structural target, change ownership, **or** introduce a separate Claim. a reference **to** the carried target is **not** a second authoritative copy of that target.
