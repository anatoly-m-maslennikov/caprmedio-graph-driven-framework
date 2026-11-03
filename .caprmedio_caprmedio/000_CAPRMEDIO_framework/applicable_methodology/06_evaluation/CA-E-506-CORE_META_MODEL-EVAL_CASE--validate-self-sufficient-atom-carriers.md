---
subjects:
  active: Carrier/File
  passive:
  - Atom
  - Atom.Content
  - Atom.Content.Summary
  - Atom.Status
  - CFEL > Relation
  - Carrier/File
version: 28
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-R-1598
  - CA-R-1599
  - CA-D-478
  - CA-D-479
  - CA-D-480
  - CA-D-482
  - CA-D-483
  - CA-D-485
  - CA-D-460
  - CA-D-470
atom_id: CA-E-506
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-506-CORE_META_MODEL-EVAL_CASE--validate-self-sufficient-atom-carriers.md
  source_atom_id: CA-E-506
  source_atom_revision: 28
  source_sha256: 60a12bff52e8f379bfbed24821e230fea11019101e42ae528c996d9ffdeafaa4
  original_relations_sha256: b7937a6522e063dad89bd26e9d55b22b49fb5c546df59d24663e53414b5f1e77
---
## Summary

Validate self-sufficient Atom Carriers

## Claim scope

self-sufficiency **and** representation consistency of Markdown Atom Carriers.

## Claim

the Evaluation **must** accept **only** Atom Carriers that preserve self-sufficiency, **`=1`** internal value source, **and** consistent outward representations.

## Details

### Test case

- construct a valid Atom with its required Properties inside its Markdown Carrier, using the applicable registered fields **and** body sections. include a required defaulted value, an optional absent Property, **and** an inapplicable Property that is correctly absent.
- extract Summary **and** the Content-Role-specific primary contribution under CA-D-479-CORE_META_MODEL-DELIVERY--use-stable-headings-for-atom-body-properties **without** reading the filename **or** containing directories. include fenced code containing example headings; those examples **must not** create Property boundaries.
- for RMED, include **`=1`** Scope, **`=1`** Claim, **and** **`=1`** Details section **in** that order. extract Scope **and** Claim independently; an empty Details section is valid **when** no required nested Property applies. include narrower **and** composite applicability **without** changing the carried target Scope Unit.
- compare the carried values against filename **and** placement representations using the applicable encoding. include a Summary whose slug differs from its readable text.
- include a Current-scope target explicitly equal **to** its owner; it remains Current-scope. include a permitted different target **and** an external Project Goal with its Author fallback.
- include a Plan with its mandatory Markdown file **and** DoD nested inside Details, with **and** **without** a matching directory; include a child-owned `IS_CONTAINED_BY` edge with its derived `CONTAINS` view.
- include an unselected inherited confidence setting **and** a selected override currently equal **to** inheritance; change the upstream setting **and** check that **only** the inherited selection follows it.
- include invalid RMED fixtures with missing Scope, duplicated Scope, Scope **after** Claim, a Scope section used instead of Claim, **or** a second applicability copy **in** frontmatter.
- create invalid fixtures by removing a required internal value, supplying that value **only** through an address, duplicating it **in** frontmatter **and** body, repeating a heading **or** YAML key, renaming a required heading, introducing an ambiguous boundary, conflicting with the address, omitting a Plan's file **or** DoD, **or** storing an inverse Atom Relation independently.

### Acceptance criteria

- **every** valid fixture yields the expected Property values **and** Relations.
- **every** invalid fixture fails with the exact Property, location, Relation, **or** address conflict identified.
- address **and** inverse checks **must not** silently rewrite the source **or** treat derived representations as separate authority.
