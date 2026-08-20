---
subject_scopes:
  - relation-model
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 4
updated_at: 2026-08-20 06:09:50
relations:
  child_of:
    - CAPRMEDIO-META-REQU-122
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Use Atom IDs as stable Artifact references

Every ordinary relation target to an identified Atom must use the target's complete Atom ID `<PREFIX>-<CONTENT_ROLE_LETTER>-<NUMBER>`. Mutable filename components are not part of the reference. A draft has no Atom ID and may be addressed only by its complete current filename stem as a provisional draft locator; every draft rename must update its incoming provisional references in the same governed change.

The resolver must distinguish stable Atom-ID references from provisional draft locators, resolve exactly one current Carrier under `.caprmedio`, and reject an ambiguous, missing, or mismatched reference. Directory location and mutable filename components are not part of an identified Atom's stable reference, so a governed Carrier rename or move preserves incoming Atom-ID relations.
