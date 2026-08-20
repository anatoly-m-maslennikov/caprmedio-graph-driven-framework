---
subject_scopes:
  - artifact-identity
version: 3
updated_at: 2026-08-20 18:32:49
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
    - CAPRMEDIO-META-REQU-728--separate-immutable-atom-id-from-mutable-scope
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Number Atoms project-wide within each Content role

When operator acceptance identifies a draft, GOV constructs its `atom_id` by taking the next `<NUMBER>` from one project-wide monotonic sequence for the Atom's Content role and combining it with the registered Prefix and Content-role letter. The sequence is shared by every Structural scope, Governance locus, Tier, and Type within that role, and an assigned number is never reused.
