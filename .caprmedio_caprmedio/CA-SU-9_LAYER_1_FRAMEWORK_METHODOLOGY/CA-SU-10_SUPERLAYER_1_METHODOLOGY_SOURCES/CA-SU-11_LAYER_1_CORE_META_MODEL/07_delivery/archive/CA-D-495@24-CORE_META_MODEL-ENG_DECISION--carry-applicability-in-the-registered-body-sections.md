---
subjects:
  active: Atom.Content
  passive:
  - Atom.Content
  - Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
  - Carrier/File
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-495@24
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 1
role: Delivery
form: Decision
---
## Summary

Carry applicability in the registered body sections

## Claim scope

applicability restrictions of Claims carried by Markdown Atom Carriers.

## Claim

a Markdown Atom Carrier **must** carry the Claim's applicability **in** the registered body sections, **not** as a duplicate frontmatter value:

- for ordinary RMED layouts, carry applicability **in** Scope, followed by the qualified contribution **in** Claim **and** supporting information **in** Details, using the exact headings registered by CA-D-479.
- for an R Atom with a nested Formal claim, carry that formal expression under Claim using CA-D-479. It complements the same prose Claim and reads within its Claim scope; no operative frontmatter claim is introduced.
- for other Content Roles, retain applicability **in** their registered primary content. this rule does **not** change their body-section layouts.
- an ordinary RMED Claim scope section **must** contain an applicability description, **not** just a copy of `current_scope_unit` **or** `claim_target_scope_unit`. those fields remain the carried structural references under CA-D-482.
- carry the applicability restrictions **=1** time. in the ordinary RMED layout, Claim **and** Details are read within Claim scope; do **not** maintain a second scope declaration **in** either section **or** frontmatter.

## Details

Scope identifies what the Claim applies **to**, including relevant conditions **and** exclusions. it does **not** select another structural target, change ownership, **or** introduce a separate Claim. a reference **to** the carried target is **not** a second authoritative copy of that target.
