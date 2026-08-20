---
subject_scopes:
  - artifact-identity
version: 7
updated_at: 2026-08-20 18:40:52
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-REQU-304--expandable-scope-path-identities
  child_of:
    - CAPRMEDIO-META-REQU-728--separate-immutable-atom-id-from-mutable-scope
    - CAPRMEDIO-META-REQU-730--preserve-atom-id-across-scope-change
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
    - CAPRMEDIO-GOV-REQU-764--register-content-role-identity-letters
---
# Place immutable Atom ID before mutable scope path

Every accepted role-classified Markdown Atom encodes the required `atom_id` property in YAML frontmatter; a registered native Atom whose executable format excludes governance metadata encodes it in the governed external Atom binding. Its value is `<PREFIX>-<CONTENT_ROLE_LETTER>-<NUMBER>`. Every accepted role-classified Carrier filename begins with that exact property value and continues as `<ATOM_ID>[-<TIER>]-<TYPE_SHORT_NAME>[-<SCOPE_PATH>]--<SUMMARY>.<ext>`, with Tier before Type when applicable. A Project Principle therefore uses `CA-<CONTENT_ROLE_LETTER>-<NUMBER>-PRINCIPLE-<TYPE_SHORT_NAME>--<SUMMARY>.md`.

A draft omits `atom_id` and uses
`<PREFIX>-<CONTENT_ROLE_LETTER>--<TYPE_SHORT_NAME>[-<SCOPE_PATH>]--<SUMMARY>.<ext>`;
the empty number slot is a visible absence marker, not an identity. Tier, Scope
path, Summary, extension, and the complete filename are Carrier facts. Once
accepted, every filename Revision of the same Atom must preserve and render the
assigned `atom_id`; a change to an identity-bearing Type creates a successor
Atom with a new `atom_id` rather than renaming the existing Atom.
