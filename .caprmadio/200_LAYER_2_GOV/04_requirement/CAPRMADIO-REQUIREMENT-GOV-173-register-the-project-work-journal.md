---
subject_scopes:
  - provenance
tier: core
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-GOV-177-keep-governed-journals-in-role-folders
  child_of:
    - CAPRMADIO-REQUIREMENT-META-197-make-journals-canonical-for-governed-provenance
---
# Register the project work journal

GOV must register `.caprmadio/010_journals/` as the canonical home of one project-wide logical Work Journal composed of collision-resistant append-only NDJSON segments. Accepted records and sealed segments must never be edited, reordered, or deleted; segmentation must preserve deterministic total replay order.
