---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Tier
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ Atom.Tier
  - CAPRMEDIO <+ MODEL <+ Carrier
version: 13
updated_at: 2026-11-02 00:18:22 +0400
relations:
  delivery_for:
  - CA-R-2504
atom_id: CA-D-651
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 3
status: Active
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-651-CORE_META_MODEL-DECISION--serialize-numeric-tier-filename-tokens.md
  source_atom_id: CA-D-651
  source_atom_revision: 13
  source_sha256: 48efa7b55876ff816c13f1fef78e32a8d262dacca6cd275470cc4ae9f2f8ad00
  original_relations_sha256: 41bd27c416906d68fc305780f667b40f52b995c33f0af578ab6363d6f7d922d9
---
## Summary

Serialize Numeric Tier Filename Tokens

## Claim scope

Atom filename grammar that represents an Atom's numeric Tier.

## Claim

an Atom filename **must** serialize the Atom's internally carried numeric Tier only through the currently registered filename grammar. For numeric Tier `0`, the Tier segment **must** be the literal `SCOPE_CONTRACT`, exactly once. This token represents `tier: 0`; it does not set the Atom's Type or separate Label property and does not require a second frontmatter flag. Other numeric Tiers keep their registered filename encodings. Numeric Tier tokens are representations only; a higher integer Tier requires an explicitly registered token rule and **must not** be guessed from a retired Local Tier or Global Tier label. Filename interpretation **must** preserve the Atom identity, owner, target, Scope, and sequence grammar, and a filename alone **must not** become the source of the numeric Tier.

The external Project Goal grammar **must** be recognized before applying any ordinary filename default. No Content Role or Type-to-Tier restriction is introduced by this delivery rule.
