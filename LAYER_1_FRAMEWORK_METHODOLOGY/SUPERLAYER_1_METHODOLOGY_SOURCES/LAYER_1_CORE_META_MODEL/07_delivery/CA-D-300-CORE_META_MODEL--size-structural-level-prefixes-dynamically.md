---
subjects:
  governs: "Entity/Carrier/Directory Carrier.Numeric Prefix"
  depends_on:
    ["Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Scope Unit.Structural Level", "Entity/Node/Continuant/Scope Unit.Navigational Order Number"]
version: 21
updated_at: "2026-10-19 15:55:26 +0400"
relations: {}
atom_id: "CA-D-300"
content_role: "Delivery"
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Size Structural Level Prefixes Dynamically

## Scope

Project-internal numeric Scope Unit Directory Carrier prefixes that use the default Scope Unit directory convention.

## Claim

**when** the default Scope Unit directory convention is used, **every** Project-internal numeric Scope Unit Directory Carrier prefix **must** concatenate these components **without** a separator:

- the Structural Level, using the decimal digit count of the greatest current Project Structural Level as its width.
- the Navigational Order Number, using the decimal rendering governed by CA-D-380-CORE_META_MODEL-DELIVERY--serialize-navigational-order-numbers.

the total prefix width is the sum of those component widths, **not** a fixed limit on the Navigational Order Number. decoding consumes the Structural Level width first **and** treats the remaining digits as the Navigational Order Number. a declared native Carrier binding under CA-D-445-CORE_META_MODEL-GENERAL-DELIVERY--admit-explicit-scope-unit-carrier-bindings **must not** be reinterpreted through this default convention.

## Details
