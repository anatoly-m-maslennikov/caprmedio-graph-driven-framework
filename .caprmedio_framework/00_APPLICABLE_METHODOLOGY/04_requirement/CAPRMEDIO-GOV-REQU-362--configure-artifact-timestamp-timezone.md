---
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Framework Instance Settings/Artifact Timestamp Timezone
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 11
updated_at: 2026-09-04 04:05:44 +0400
relations:
  child_of:
    - CA-R-1402
    - CA-R-1054
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-GOV-REQU-362--configure-artifact-timestamp-timezone.md
---
# Configure the Artifact timestamp timezone

the Framework Instance Settings Artifact **may** set `[artifact_timestamps].timezone` to `local`, `UTC`, **or** an IANA timezone name, with `local` as the default; **every** emitted `updated_at` value uses `YYYY-MM-DD HH:MM:SS`, **and** the setting supplies its timezone interpretation.
