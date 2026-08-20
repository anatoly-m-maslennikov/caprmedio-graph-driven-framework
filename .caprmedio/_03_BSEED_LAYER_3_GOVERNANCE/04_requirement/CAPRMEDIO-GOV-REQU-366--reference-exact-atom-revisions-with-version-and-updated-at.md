---
subject_scopes:
  - provenance
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 4
updated_at: 2026-08-20 18:36:57
relations:
  child_of:
    - CAPRMEDIO-META-REQU-165--atoms-have-version-and-updated-at
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Reference exact Atom revisions with version and updated at

An exact identified role-classified Atom Revision reference uses `<atom_id>@<version>,<updated_at>`, where the `atom_id` property value and both Revision-property values exactly match the target governed history. An exact Intent Revision reference uses `CA-INTENT@<version>,<updated_at>`. An exact draft Revision reference may use `<CURRENT_DRAFT_FILENAME_STEM>@<version>,<updated_at>` as a provisional locator while `atom_id` is absent. Carrier filenames contain neither `version` nor `updated_at`; filename changes never change an assigned `atom_id`.
