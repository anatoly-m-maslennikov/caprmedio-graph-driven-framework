---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
  - CAPRMEDIO_MODEL <+ Atom.Header.Status
  - CAPRMEDIO_MODEL <+ CFEL > Relation
  - CAPRMEDIO_MODEL <+ Carrier/File
version: 28
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-R-1598
  - CA-R-1599
  - CA-D-478
  - CA-D-479
  - CA-D-480
  - CA-R-2102
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
---
## Summary

Validate self-sufficient Atom Carriers

## Claim

### Prose Claim


self-sufficiency **and** representation consistency of Markdown Atom Carriers.


the Evaluation **must** accept **only** Atom Carriers that preserve self-sufficiency, **`=1`** internal value source, **and** consistent outward representations.

## Details

### Test case

- construct a valid Atom with its required Properties inside its Markdown Carrier, using the applicable registered fields **and** body sections. include a required defaulted value, an optional absent Property, **and** an inapplicable Property that is correctly absent.
- extract Summary **and** the Role-specific primary contribution under CA-D-479-CORE_META_MODEL-DELIVERY--use-stable-headings-for-atom-body-properties **without** reading the filename **or** containing directories. include fenced code containing example headings; those examples **must not** create Property boundaries.
- for RMED, include exactly one Claim container with one or both of Formal Claim and Prose Claim; Details is optional. Extract only declared headings and include narrower **and** composite applicability in Prose Claim without changing the target resolved from the active Subject.
- compare the carried values against filename **and** placement representations using the applicable encoding. include a Summary whose slug differs from its readable text.
- include active Subjects that resolve to the current Scope Unit and to a permitted different target; derive current Scope Unit from containment.
- include a Plan with its mandatory Markdown file **and** DoD nested inside Details, with **and** **without** a matching directory; include a child-owned `IS_CONTAINED_BY` edge with its derived `CONTAINS` view.
- include an unselected inherited confidence setting **and** a selected override currently equal **to** inheritance; change the upstream setting **and** check that **only** the inherited selection follows it.
- include invalid RMED fixtures with a missing or duplicated Claim container, no Formal Claim or Prose Claim, duplicated Claim children, an undeclared heading treated as a Property, **or** a second applicability copy **in** frontmatter.
- create invalid fixtures by removing a required internal value, supplying that value **only** through an address, duplicating it **in** frontmatter **and** body, repeating a declared Property heading **or** YAML key, renaming a required heading, introducing an ambiguous boundary, conflicting with the address, omitting a Plan's file **or** DoD, **or** storing an inverse Atom Relation independently.

### Acceptance criteria

- **every** valid fixture yields the expected Property values **and** Relations.
- **every** invalid fixture fails with the exact Property, location, Relation, **or** address conflict identified.
- address **and** inverse checks **must not** silently rewrite the source **or** treat derived representations as separate authority.
