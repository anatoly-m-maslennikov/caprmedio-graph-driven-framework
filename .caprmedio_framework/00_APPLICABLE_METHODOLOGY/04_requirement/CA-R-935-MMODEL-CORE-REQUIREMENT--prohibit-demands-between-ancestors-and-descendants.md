---
subjects:
  governs:
    continuant:
      - relation-model
  depends_on:
    continuant:
      - scope-topology
      - Atom/Scope
      - Atom/Claim/Scope/Scope Unit Set
atom_id: CA-R-935
cce_version: cce_1
cce_form: prohibition
version: 8
updated_at: 2026-09-04 00:22:20 +0400
relations:
  replacement_of:
    - CA-R-910
    - CA-R-911
  child_of:
    - CA-R-932
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-935-MMODEL-CORE-REQUIREMENT--prohibit-demands-between-ancestors-and-descendants.md
---
# Prohibit Demands between ancestors and descendants

a Demand Atom **must not** target an ancestor **or** descendant of its Consumer Atom Scope Unit **in** its Claim Scope Unit Set.
