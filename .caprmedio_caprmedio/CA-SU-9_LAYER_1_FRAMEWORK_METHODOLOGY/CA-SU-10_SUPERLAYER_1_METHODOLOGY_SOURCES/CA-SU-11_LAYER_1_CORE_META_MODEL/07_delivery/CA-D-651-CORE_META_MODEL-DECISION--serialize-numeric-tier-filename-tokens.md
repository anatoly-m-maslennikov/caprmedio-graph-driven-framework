---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Tier
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
  - CAPRMEDIO_MODEL <+ Carrier
version: 13
updated_at: 2026-11-02 00:18:22 +0400
relations:
  delivery_for:
  - CA-R-2706
atom_id: CA-D-651
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 3
status: Active
role: Delivery
form: Decision
---
## Summary

Serialize Numeric Tier Filename Tokens

## Claim

### Prose Claim


Atom filename grammar that represents an Atom's numeric Tier.


an Atom filename **must** serialize the Atom's internally carried numeric Tier only through the currently registered filename grammar. For numeric Tier `0`, the Tier segment **must** be the literal `SCOPE_CONTRACT`, exactly once. This token represents `tier: 0`; it does not set the Atom's Type or separate Label property and does not require a second frontmatter flag. Other numeric Tiers keep their registered filename encodings. Numeric Tier tokens are representations only; a higher integer Tier requires an explicitly registered token rule and **must not** be guessed from a retired Local Tier or Global Tier label. Filename interpretation **must** preserve the Atom identity, owner, target, Scope, and sequence grammar, and a filename alone **must not** become the source of the numeric Tier.

The external Project Goal grammar **must** be recognized before applying any ordinary filename default. No Content Role or Type-to-Tier restriction is introduced by this delivery rule.
