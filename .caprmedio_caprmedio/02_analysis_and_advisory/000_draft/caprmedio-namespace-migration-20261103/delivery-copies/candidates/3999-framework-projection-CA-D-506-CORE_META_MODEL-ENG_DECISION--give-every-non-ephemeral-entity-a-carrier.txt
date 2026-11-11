---
atom_id: CA-D-506
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 18
updated_at: 2026-11-02 00:18:22 +0400
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity
  passive:
  - CAPRMEDIO <+ MODEL <+ Carrier
  - CAPRMEDIO <+ MODEL <+ Term//Property
relations: {}
tier: 1
role: Delivery
form: Policy
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-506-CORE_META_MODEL-ENG_DECISION--give-every-non-ephemeral-entity-a-carrier.md
  source_atom_id: CA-D-506
  source_atom_revision: 18
  source_sha256: 6e10bd4a73a08f4b9e6057d5fa898829089f4cf80efcff08063aab165d221965
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Give every non-ephemeral Entity a Carrier

## Claim scope

non-ephemeral Entities.

## Claim

Every represented non-ephemeral Entity has at least one declared Carrier or a location within a shared Carrier. Reusable D Policies may define that binding for an entire Object kind and its dependent properties; individual D Decisions govern bounded exceptions. The governed Subject names the represented entity, not an extra representation node.

## Details

a binding **may** use a shared Carrier **or** a location within it. A carried Property does not require a separate file or authored CARRIES edge. Its representation follows the applicable owner/property Policy. A derived property can be represented in a Projection without making the Projection authoritative for its source. Occurrents themselves are excluded; retained information about them follows CA-D-654.
