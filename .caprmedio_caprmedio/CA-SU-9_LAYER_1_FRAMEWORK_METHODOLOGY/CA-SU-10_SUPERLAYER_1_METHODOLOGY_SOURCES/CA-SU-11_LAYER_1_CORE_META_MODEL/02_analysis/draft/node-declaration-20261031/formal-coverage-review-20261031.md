# Formal Claim coverage — 2026-10-31

Latest checkpoint: [Author deferral and omission fallback](author-deferral-fallback-review-20261031.md) records 41 formal-only Claims, Author removal and the resolved fallback decision. The 40-Claim results below describe the previous iteration.

Formal-only Claims increased from 37 to 40. The packet now contains 99 Drafts: the original 98 plus one reusable numeric-comparison Rule. All 23 Primary Node Semantics sections are preserved unchanged. Properties have no Semantics sections.

## Translated constraints

- INSTANCE_OF: its endpoint signature, inverse and zero Property instances now express the Claim without prose.
- Atom.Relations: the existing value/dependent-name rules already express the removed repetition.
- Atom.Tier.Label: five guarded IF/THEN expressions preserve optional presence and the mappings for Tiers 0–4. Other tiers retain no fixed Label.
- Numeric bounds: Version Number is at least 1, Tier is at least -1, and a supplied Work Sequence Number is greater than 0. Remaining monotonicity, ownership and scoped uniqueness rules remain prose.
- YAML field placement: five formal delivery mappings replace repeated field-mapping prose. Required/optional presence, Node Declaration scope and matching containment reference kind remain explicit.

## New reusable syntax

[Compare numeric values in CFEL](../../../04_requirement/draft/node-declaration-20261031/CA-R-draft-CORE_META_MODEL-CFEL--compare-numeric-values.md) defines `>`, `>=`, `<` and `<=` for single numeric values. It forbids string coercion, requires guards for optional operands and leaves Relation operators distinct. This is proposed methodology syntax, not an implemented parser feature.

## Remaining repeated patterns

| Pattern | Real cases | Missing decision |
|---|---|---|
| Default resolution | Label, Author, confidence threshold, retry limit | Stored versus effective values; admission-time writes and precedence |
| Scoped uniqueness | Work Sequence Number, Passive Subjects | Exact group selector and equality key |
| Revision constraints | ID, Version Number, Updated At, Summary, Projection ID | Predecessor/successor or rebuild pairing and event context |
| Reference domains | Author, Projection Sources, Source Of Truth | ID/name/link representation and resolution time |
| Dynamic admitted values | Atom.Form, Projection.Form, relation notation | Governing registry and admission binding |

The [Property pattern report](declaration-expansion/formal-property-patterns.json) and [model pattern report](declaration-expansion/formal-model-patterns.json) retain the source cases and candidate alternatives. Numeric facet sketches in research are superseded by the reviewed comparison Rule. Other candidate sketches are not adopted syntax. The stored/effective-value question is pending.

## Preservation review

An independent Terra reviewer checked the changed Claims against their original text. Four concerns were corrected: carrier scope/presence, matching typed containment targets, an overbroad synonym prohibition and accidental tightening of the prose fallback method. The final review passed the existing-notation conversions and numeric extension with its three consumers.

- 40 Claims are entirely formal; this count excludes language-definition prose.
- All 99 registered Drafts pass the bounded structure, register and local-link checks.
- All 69 Declaration Subjects remain distinct: 23 Primary and 46 Property.
- All 23 Primary Semantics sections are byte-for-byte unchanged.
- All 750 snapshotted Current Core Requirement sources and Current Epic version 37 remain unchanged.
- Transition commentary was moved to the proposal; normative constraints were retained in their Claims.

See [coverage evidence](declaration-expansion/formal-coverage-result.json) for changed paths and [bounded checks](draft-checks.json) for structural results.

No parser/schema/runtime implementation, actual-instance migration or promotion was performed. Existing whitelist and reference-mapping gates remain open.
