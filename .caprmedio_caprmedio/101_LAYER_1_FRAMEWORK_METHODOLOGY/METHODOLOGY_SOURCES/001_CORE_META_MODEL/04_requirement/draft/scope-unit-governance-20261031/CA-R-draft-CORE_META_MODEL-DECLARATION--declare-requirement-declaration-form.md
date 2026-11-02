---
atom_id: CA-R-draft
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
tier: 3
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement'
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit
version: 1
updated_at: 2026-10-31 18:14:08 +0400
relations: {}
form: Declaration
---
## Summary

Declare the Requirement Declaration form

## Claim

By default, one Atom has one coherent Claim. Its Summary faithfully condenses the whole Atom and is normally a statement for RMED. Semantics and Details remain optional.

An explicit Requirement Form: Declaration may contain multiple statements expressed in prose, GFEL formal expressions, or both, provided that they form one coherent declaration about one topic. Its template may allow a topic Summary such as “Define Run”.

Scope Unit Declaration is a Requirement Form using the Declaration template, including its permission for multiple prose/GFEL statements and a topic Summary. It is not a new Atom Role.

A topic-only Summary is allowed when its explicit Form template permits it; it is not an automatic global rule. Requirements without an explicit override continue to use the default coherent-Claim and faithful-Summary expectations.

This Draft uses the proposed `form: Declaration` field without retaining a duplicate `type` field. Existing schemas and readers are not claimed migrated. It introduces no GFEL syntax or functions; any later technical syntax must be separately admitted.
