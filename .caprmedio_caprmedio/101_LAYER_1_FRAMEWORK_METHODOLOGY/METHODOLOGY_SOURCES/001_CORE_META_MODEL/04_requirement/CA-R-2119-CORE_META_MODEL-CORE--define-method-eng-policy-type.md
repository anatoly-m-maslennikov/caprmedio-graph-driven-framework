---
atom_id: CA-R-2119
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Method/Type: Eng Policy'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
relations: {}
type: Definition
version: 2
updated_at: 2026-10-24 00:38:25 +0400
tier: 1
---
# Summary

Define Atom/Content Role: Method/Type: Eng Policy

## Scope

The Eng Policy value in the qualified Method Type domain.

## Claim

Eng Policy **means** a Method Type whose rule automatically applies to every child Scope Unit of its Local Scope Unit, subject only to genuine topic or environment conditions.

## Details

A Scope Unit can locally own an Eng Policy only when it has at least one actual, currently declared child. A leaf can inherit ancestor Policies but cannot locally own one. Do not create artificial children or count hypothetical future children to retain a Policy label.

A Policy can select a named technology. Actual-child ownership and automatic application to every child distinguish it from Eng Decision; abstract wording or a technology name alone does not classify it.

If the owner loses its last child, review and relocate or reclassify its local Policies; do not infer an automatic runtime conversion.

This Type does not constrain an Atom to a particular Tier. The PROGRAMMATIC-only allowed-Type restriction belongs to Project Configuration, not this reusable definition.

This definition replaces [CA-R-2111@1](archive/CA-R-2111@1-CORE_META_MODEL-CORE--define-method-policy-type.md).
