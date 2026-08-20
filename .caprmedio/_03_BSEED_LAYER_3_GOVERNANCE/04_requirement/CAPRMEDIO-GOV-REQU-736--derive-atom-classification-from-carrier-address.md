---
subject_scopes:
  - carrier-format
version: 4
updated_at: 2026-08-20 18:36:57
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-740--separate-content-role-from-artifact-type
    - CAPRMEDIO-META-REQU-741--prohibit-artifact-subtypes
    - CAPRMEDIO-GOV-REQU-348--use-canonical-carrier-address-as-authority
---
# Derive Atom classification from carrier address

GOV derives a role-classified Atom's Content role from its canonical role folder and registered filename role letter and derives its Type from the registered Type short name in the filename. It forbids `content_role`, `type`, and `subtype` frontmatter that would duplicate or reintroduce those address facts. It does not derive `atom_id` from the address: for an accepted role-classified Atom it reads the property and validates the filename's identity prefix against it; for a draft it requires both property omission and the empty number slot. Unknown, ambiguous, missing, duplicated, or inconsistent values are invalid.
