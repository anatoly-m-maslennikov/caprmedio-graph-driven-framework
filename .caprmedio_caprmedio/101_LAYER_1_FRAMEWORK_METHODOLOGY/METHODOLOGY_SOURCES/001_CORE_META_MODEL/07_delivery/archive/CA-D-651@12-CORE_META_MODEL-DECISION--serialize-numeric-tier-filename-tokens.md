---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Tier
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Governing Objects/Atom.Tier
  - Entity/Carrier
version: 12
updated_at: 2026-10-29 22:26:57 +0400
relations:
  delivery_for:
  - CA-R-2124
atom_id: CA-D-651@12
content_role: Delivery
type: Decision
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 3
status: Archived
author: Anatoly Maslennikov
---
## Summary

Serialize Numeric Tier Filename Tokens

## Claim scope

Atom filename grammar that represents an Atom's numeric Tier.

## Claim

an Atom filename **must** serialize the Atom's internally carried numeric Tier only through the currently registered filename grammar. For numeric Tier `0`, the Tier segment **must** be the literal `SCOPE_CONTRACT`, exactly once. This token represents `tier: 0`; it does not set the Atom's Type or separate Label property and does not require a second frontmatter flag. Other numeric Tiers keep their registered filename encodings. Numeric Tier tokens are representations only; a higher integer Tier requires an explicitly registered token rule and **must not** be guessed from a retired Local Tier or Global Tier label. Filename interpretation **must** preserve the Atom identity, owner, target, Scope, and sequence grammar, and a filename alone **must not** become the source of the numeric Tier.

The external Project Goal grammar **must** be recognized before applying any ordinary filename default. No Content Role or Type-to-Tier restriction is introduced by this delivery rule.
