---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    occurrent:
      - lifecycle
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 5
updated_at: 2026-08-23 15:00:38
relations:
  child_of:
    - CAPRMEDIO-META-REQU-170--govern-ops-factual-admission-lifecycle
    - CA-R-1054
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-GOV-REQU-368--place-ops-records-by-factual-admission.md
---
# Place Ops records by factual admission

Within each `09_ops/` directory, the optional `drafts/` directory holds governed Ops Atoms whose asserted facts are not yet admitted, the role root holds admitted factual records, and `archive/` holds invalidated, duplicated, or replaced records. This placement model is exhaustive; handling is represented separately and does not create a `handled/` lifecycle directory.
