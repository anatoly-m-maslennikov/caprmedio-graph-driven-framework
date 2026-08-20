---
subject_scopes:
  - provenance
project_settings:
  artifacts:
    enabled_types:
      - work_journal
  paths:
    journal_root: .caprmedio/work_journal
version: 4
updated_at: 2026-08-20 04:03:30
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-158--make-journals-canonical-for-governed-provenance
  replacement_of:
    - CAPRMEDIO-GOV-REQU-484--keep-governed-journals-in-role-folders
---
# Register the Project Work Journal

GOV must register `.caprmedio/work_journal/` as the canonical home of one project-wide logical Work Journal composed of collision-resistant append-only NDJSON segments. Accepted records and sealed segments must never be edited, reordered, or deleted; segmentation must preserve deterministic total replay order.
