---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - settings
version: 7
updated_at: 2026-08-23 15:00:38
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-035--identify-necessary-information-by-confidence
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-GOV-REQU-375--configure-necessary-information-confidence-threshold.md
---
# Configure necessary-information confidence threshold

The Project Configuration Atom MUST expose `confidence.necessary_information_threshold_percent` as an integer percentage from 0 through 100 with an initial value of 95.
