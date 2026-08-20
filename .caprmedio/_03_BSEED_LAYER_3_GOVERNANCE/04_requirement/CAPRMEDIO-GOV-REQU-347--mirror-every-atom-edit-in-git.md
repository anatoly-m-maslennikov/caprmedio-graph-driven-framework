---
subject_scopes:
  - provenance
project_settings:
  git:
    commit_each_atom_edit: true
    initialize_if_missing: true
    required: true
version: 6
updated_at: 2026-08-20 19:36:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-158--make-journals-canonical-for-governed-provenance
---
# Mirror every governed file change in Git

Every governed repository-file change must be a separate Git commit that changes exactly one file identity and is classified as `ADD`, `MOVE`, `UPDATE`, `MOVE+UPDATE`, or `REMOVE`. `MOVE` changes Structural location; `UPDATE` changes content, filename, or other governed carrier state; and `MOVE+UPDATE` records both for the same identity. The commit message must be generated from the affected file's direct typed upstream relations, change set, filename, and version under the canonical commit-message rule. Atom creation, accepted refinement, relocation, archival, and replacement use the same one-file boundary. Git preserves repository snapshots and Implementation changes as a secondary loss-prevention mirror but does not replace the Work Journal as canonical governed provenance.
