---
atom_id: CA-D-268
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Atom/Direct Relation Serialization
  depends_on:
    continuant:
      - Atom/Relation Owner
version: 2
updated_at: 2026-08-29 01:16:37 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-268-MMODEL-CORE-DELIVERY--serialize-authored-direct-relations-on-their-owning-atoms.md
---
# Serialize Authored Direct Relations on Their Owning Atoms

**every** authored direct semantic relation **must** be serialized once under `relations.<RELATION_KIND>` on the Atom that owns its declared direction as a nonempty list of unique canonical target references.
