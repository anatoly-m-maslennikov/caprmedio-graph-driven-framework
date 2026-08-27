---
atom_id: CA-R-838
subjects:
  declared:
    continuant:
      - relation-model
  prerequisite:
    continuant:
      - atom-boundary
cce_version: cce_1
cce_form: obligation
version: 6
updated_at: 2026-08-23 15:24:07
relations:
  child_of:
    - CA-R-833-REQUIREMENT--organize-normative-authority-as-an-acyclic-hierarchy
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-838-REQUIREMENT-BSEED_GOVERNANCE--validate-normative-authority-hierarchy.md
---
# Validate the normative-authority hierarchy

GOVERNANCE validators MUST construct the active normative-authority subgraph from registered authority-bearing direct relations and MUST reject the subgraph when any authority edge lacks registered typing or the directed subgraph contains a cycle.
