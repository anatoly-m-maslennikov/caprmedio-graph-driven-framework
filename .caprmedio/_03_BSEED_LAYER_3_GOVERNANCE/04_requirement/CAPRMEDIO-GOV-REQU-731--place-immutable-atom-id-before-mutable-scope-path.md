---
subject_scopes:
  - artifact-identity
version: 4
updated_at: 2026-08-20 15:22:24
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

An accepted Atom filename uses `<PREFIX>-<CONTENT_ROLE_LETTER>-<NUMBER>[-<TIER>]-<TYPE_SHORT_NAME>[-<SCOPE_PATH>]--<SUMMARY>.<ext>`, where `<PREFIX>-<CONTENT_ROLE_LETTER>-<NUMBER>` is the immutable Atom ID and the Tier precedes the Type when applicable. A Project Principle therefore uses `CA-<CONTENT_ROLE_LETTER>-<NUMBER>-PRINCIPLE-<TYPE_SHORT_NAME>--<SUMMARY>.md`. A draft filename uses `<PREFIX>-<CONTENT_ROLE_LETTER>--<TYPE_SHORT_NAME>[-<SCOPE_PATH>]--<SUMMARY>.<ext>`: the empty number slot means that no Atom ID has been assigned. The Tier, Type, Scope path, Summary, extension, and complete filename are mutable Carrier facts. After acceptance, every filename Revision preserves the assigned Atom-ID prefix while the remaining filename may change through governed revision.
