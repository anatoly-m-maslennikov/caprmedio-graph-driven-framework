---
atom_id: CA-R-1300
cce_version: cce_1
cce_form: restriction
subjects:
  governs:
    continuant:
      - Epic/Membership
  depends_on:
    continuant:
      - Containment Relation Pair
      - Delivery
version: 4
updated_at: 2026-09-02 04:15:00 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1300-MMODEL-CORE-REQUIREMENT--use-only-delivery-derived-containment-for-epic-membership.md
---
# Use Only Delivery-Derived Containment for Epic Membership

Epic membership **must** use **only** `CONTAINS` **and** `IS_CONTAINED_BY` relation pairs derived by Delivery authority.
