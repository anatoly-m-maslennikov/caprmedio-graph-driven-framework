---
atom_id: CA-R-1011
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Task/Dependency
  depends_on:
    continuant:
      - Task/Job
      - Task/Carrier
version: 4
updated_at: 2026-08-27 00:50:08 +0400
relations:
  child_of:
    - CA-R-992
    - CA-R-1007
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1011-GOVERN-CORE-REQUIREMENT--encode-task-dependencies.md
---
# Encode Task dependencies

every Task Dependency **must** be stated in the dependent Task Job as an explicit `**when** <TASK_ATOM_ID> is Done` condition.
