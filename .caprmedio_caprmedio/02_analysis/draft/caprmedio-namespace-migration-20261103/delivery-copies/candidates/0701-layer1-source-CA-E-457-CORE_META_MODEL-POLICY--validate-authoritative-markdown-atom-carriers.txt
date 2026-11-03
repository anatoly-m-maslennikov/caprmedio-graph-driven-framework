---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/File
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ Carrier/File
  - CAPRMEDIO <+ MODEL <+ Project
version: 34
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-D-463
  - CA-D-479
  - CA-D-356
  - CA-D-470
atom_id: CA-E-457
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Evaluation
form: Eval Policy
---
## Summary

Validate Authoritative Markdown Atom Carriers

## Claim scope

the authoritative Markdown Carrier **and** body structure of an Atom Revision.

## Claim

the Evaluation **must** reject an Atom Revision **if** it has other than **`=1`** authoritative Markdown Atom Carrier on the Project filesystem, its authoritative Carrier does **not** contain YAML Frontmatter followed by the Content-Role-specific structured Main Content under CA-D-479-CORE_META_MODEL-DELIVERY--use-stable-headings-for-atom-body-properties, **or** a TOML, YAML, JSON, database, **or** projected copy is treated as authoritative for that Atom Revision.

## Details

the body-structure checks include:

- exact heading spelling, cardinality, **and** order for the selected Content Role; a universal Claim heading is **not** a substitute for Question, Concern, Objective, **or** Operation.
- RMED requires Scope, Claim, **and** Details **in** that order; the earlier Claim **and** Details layout alone fails. Scope **and** Claim **must** be separately addressable; an empty Details section remains admitted under CA-D-479-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties.
- missing **or** duplicate required sections, unregistered peer sections, ambiguous section boundaries, **and** heading-like fenced examples.
- the nested Plan Definition of Done under CA-D-470-CORE_META_MODEL-DELIVERY--serialize-plan-file-sections; its absence **or** a second carried copy fails validation.

these are Carrier checks. semantic agreement between the primary contribution, its applicability, Details, **and** Summary requires the content Evaluation, **not** heading recognition alone.
