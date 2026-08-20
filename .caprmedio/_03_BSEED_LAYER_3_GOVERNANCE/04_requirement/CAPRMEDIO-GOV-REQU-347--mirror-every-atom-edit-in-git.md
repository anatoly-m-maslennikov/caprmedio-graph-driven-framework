---
subject_scopes:
  - provenance
project_settings:
  git:
    commit_each_atom_edit: true
    initialize_if_missing: true
    required: true
version: 7
updated_at: 2026-08-20 20:10:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-158--make-journals-canonical-for-governed-provenance
---
# Mirror every governed file change in Git

Every governed repository-file change must be a separate Git commit for exactly one governed subject file identity and one classified change set: `ADD`, `MOVE`, `UPDATE`, `MOVE+UPDATE`, or `REMOVE`. `MOVE` changes Structural location; `UPDATE` changes content, filename, or other governed carrier state; and `MOVE+UPDATE` records both for the same identity. Before the commit is created, the same action must be appended once to the Project Work Journal with an `action_message` byte-identical to the canonical commit message. The commit must include both the subject change and exactly that one appended Journal record; the Journal carrier is a provenance sidecar of the same action, not a second governed subject or a new Hook trigger. Atom creation, accepted refinement, relocation, archival, and replacement use this same one-action boundary. Git preserves repository snapshots and Implementation changes as a secondary loss-prevention mirror but does not replace the Work Journal as canonical governed provenance.
