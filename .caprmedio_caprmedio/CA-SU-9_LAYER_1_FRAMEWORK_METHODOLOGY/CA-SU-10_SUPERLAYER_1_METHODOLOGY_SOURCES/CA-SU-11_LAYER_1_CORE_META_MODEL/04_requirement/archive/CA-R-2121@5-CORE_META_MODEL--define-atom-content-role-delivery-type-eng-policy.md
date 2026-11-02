---
atom_id: CA-R-2121@5
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Delivery/Type: Eng Policy'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Delivery'
relations: {}
type: Definition
version: 5
updated_at: 2026-10-25 17:32:27 +0400
tier: 1
---
# Summary

Define Atom/Content Role: Delivery/Type: Eng Policy

## Scope

The Eng Policy value in the qualified Delivery Type domain.

## Claim

Eng Policy **means** a Delivery Type whose rule automatically applies to every child Scope Unit of its Local Scope Unit, subject only to genuine topic or environment conditions.

## Details

A Scope Unit can locally own an Eng Policy only when it has at least one actual, currently declared child. A leaf can inherit ancestor Policies but cannot locally own one. Do not create artificial children or count hypothetical future children to retain a Policy label.

A Policy can select a named technology. Actual-child ownership and automatic application to every child distinguish it from Eng Decision; abstract wording or a technology name alone does not classify it.

If the owner loses its last child, review and relocate or reclassify its local Policies; do not infer an automatic runtime conversion.

This Type does not constrain an Atom to a particular Tier. The PROGRAMMATIC-only allowed-Type restriction belongs to Project Configuration, not this reusable definition.

This definition replaces [CA-R-2113@1](archive/CA-R-2113@1-CORE_META_MODEL-CORE--define-delivery-policy-type.md).
