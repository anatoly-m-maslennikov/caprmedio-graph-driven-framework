---
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
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-706--make-structural-ownership-immediate-recursive-and-typed
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-GOV-REQU-714--derive-inverse-structural-ownership.md
---
# Derive inverse structural ownership

CAPRMEDIO MUST derive the inverse `structural_children` view from stored `structural_parent` relations and MUST NOT persist that inverse separately.
