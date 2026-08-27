---
atom_id: CA-R-1008
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Task/Carrier
  depends_on:
    continuant:
      - Task/Job
      - Task/Scope
      - Task/Definition of Done
      - Task/Details
version: 4
updated_at: 2026-08-27 00:50:08 +0400
relations:
  child_of:
    - CA-R-989
    - CA-R-1000
    - CA-R-1211
    - CA-R-1212
    - CA-R-1214
    - CA-R-1215
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1008-GOVERN-CORE-REQUIREMENT--encode-task-atom-sections.md
---
# Encode Task Atom sections

every Markdown Task Atom Carrier **must** contain, in order, one H1 Task Summary, one CCE Task Job, one `Scope` section containing one Scope Expression, one `Definition of Done` section containing one Definition of Done, and at most one `Details` section.
