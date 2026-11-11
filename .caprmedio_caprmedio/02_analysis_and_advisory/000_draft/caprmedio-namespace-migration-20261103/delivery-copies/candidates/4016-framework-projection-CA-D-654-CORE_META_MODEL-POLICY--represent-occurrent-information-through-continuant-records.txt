---
atom_id: CA-D-654
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Node/Occurrent
  passive:
  - CAPRMEDIO <+ MODEL <+ Carrier
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/History/Journal > Event Record
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation//CARRIES
version: 3
relations: {}
tier: 1
updated_at: 2026-11-02 00:18:22 +0400
role: Delivery
form: Policy
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-654-CORE_META_MODEL-POLICY--represent-occurrent-information-through-continuant-records.md
  source_atom_id: CA-D-654
  source_atom_revision: 3
  source_sha256: 806b9143fff18465c8340f46ea75c74da75012949925434270e2ad7391175c9d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Represent Occurrent information through Continuant records

## Claim scope

representation of an Occurrent's recorded information.

## Claim

An Occurrent is not carried or stored as the occurrence itself. When
information about an Occurrent is retained, a Continuant record represents
that information; the Carrier binds the Continuant record, not the Occurrent.
An Event Record in a Journal is one such record.

This reusable Policy governs Occurrent representation. It creates no new
Carrier, per-occurrence binding, Journal record, or relation type.

## Semantics

The Event remains the actual occurrence. Its Event Record is a distinct
Continuant that may have a Carrier. CARRIES and its derived IS_CARRIED_BY view
therefore apply to the represented non-ephemeral record rather than directly
to the Occurrent.

## Details

This Policy reuses CA-R-1958, CA-R-1968@12, CA-R-2590, and CA-R-1993. It fills
the missing reusable D Policy boundary without changing their definitions or
introducing a direct Occurrent-to-Carrier fact.
