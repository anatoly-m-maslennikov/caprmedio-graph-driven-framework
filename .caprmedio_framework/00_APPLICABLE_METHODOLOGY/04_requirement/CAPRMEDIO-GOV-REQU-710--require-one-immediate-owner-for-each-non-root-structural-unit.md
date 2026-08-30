---
subjects:
  governs:
    continuant:
      - scope-topology
  depends_on:
    continuant:
      - authority
cce_version: cce_1
cce_form: cardinality
version: 8
updated_at: 2026-08-29 02:40:41 +0400
relations:
  child_of:
    - CAPRMEDIO-META-REQU-706
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-GOV-REQU-710--require-one-immediate-owner-for-each-non-root-structural-unit.md
---
# Require one parent Scope Unit

**every** Scope Unit except a Scope Unit root **must** have **`=1`** direct parent Scope Unit.
