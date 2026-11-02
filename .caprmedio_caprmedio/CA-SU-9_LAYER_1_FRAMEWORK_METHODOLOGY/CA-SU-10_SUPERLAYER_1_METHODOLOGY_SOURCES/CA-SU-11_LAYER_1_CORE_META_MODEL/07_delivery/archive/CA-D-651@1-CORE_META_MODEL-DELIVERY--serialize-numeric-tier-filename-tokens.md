---
subjects:
  governs: Subject/Engineering/Carrier/Filename/Atom.Tier
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Tier
  - 'Subject/Domain/Node/Continuant/Atom.Tier: 0 / Principle'
  - 'Subject/Domain/Node/Continuant/Atom.Tier: 1 / Core'
  - 'Subject/Domain/Node/Continuant/Atom.Tier: 2 / General'
  - 'Subject/Domain/Node/Continuant/Atom.Tier: 3 / Standard'
  - Subject/Engineering/Carrier
version: 1
updated_at: 2026-10-23 23:33:48 +0400
relations:
  delivery_for:
    - CA-R-2124
atom_id: "CA-D-651@1"
content_role: "Delivery"
type: "Definition"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
tier: 3
status: "Archived"
author: "Anatoly Maslennikov"
---
# Summary

Serialize Numeric Tier Filename Tokens

## Scope

Atom filename grammar that represents an Atom's numeric Tier.

## Claim

an Atom filename **must** serialize the Atom's internally carried numeric Tier only through the currently registered filename grammar. The initial display names remain the registered tokens for Tier `0` Principle, Tier `1` Core, Tier `2` General, and Tier `3` Standard where that grammar admits named tokens; a higher integer Tier requires an explicitly registered token rule and **must not** be guessed from a retired Local Tier or Global Tier label. Filename interpretation **must** preserve the Atom identity, owner, target, Scope, and sequence grammar, and a filename alone **must not** become the source of the numeric Tier.

The external Project Goal grammar **must** be recognized before applying any ordinary filename default. No Content Role or Type-to-Tier restriction is introduced by this delivery rule.

## Details

