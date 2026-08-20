---
subject_scopes:
  - provenance
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 2
updated_at: 2026-08-20 06:09:50
relations:
  child_of:
    - CAPRMEDIO-META-REQU-165--atoms-have-version-and-updated-at
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Reference exact Atom revisions with version and updated at

An exact identified-Atom Revision reference uses `<ATOM_ID>@<version>,<updated_at>`, where the complete Atom ID and both Revision values exactly match the target governed history. An exact draft Revision reference may use `<CURRENT_DRAFT_FILENAME_STEM>@<version>,<updated_at>` as a provisional locator while no Atom ID exists. Carrier filenames contain neither `version` nor `updated_at`; filename changes never change an assigned Atom ID.
