---
atom_id: CA-R-2122@7
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery/Type: Decision'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery'
relations: {}
type: Definition
version: 7
updated_at: 2026-10-29 07:17:20 +0400
tier: 1
---
# Summary

Define Atom/Content Role: Delivery/Type: Eng Decision

## Scope

The Eng Decision value in the qualified Delivery Type domain.

## Claim

Eng Decision **means** a Delivery Type that records an engineering choice specific to its Local Scope Unit without automatically making that choice a rule for every child.

## Details

An Eng Decision can be reused, but reuse does not make it an automatically inherited Policy. A named technology can occur in either Type; its name alone does not select Eng Decision.

This Type does not constrain an Atom to a particular Tier. The PROGRAMMATIC-only allowed-Type restriction belongs to Project Configuration, not this reusable definition.

This definition replaces [CA-R-2114@1](archive/CA-R-2114@1-CORE_META_MODEL-CORE--define-delivery-engineering-decision-type.md).
