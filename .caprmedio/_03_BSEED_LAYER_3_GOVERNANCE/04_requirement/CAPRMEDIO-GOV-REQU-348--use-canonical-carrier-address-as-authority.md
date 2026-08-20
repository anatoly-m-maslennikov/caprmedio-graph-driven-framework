---
subject_scopes:
  - carrier-format
version: 4
updated_at: 2026-08-20 18:36:57
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
  replacement_of:
    - CAPRMEDIO-META-REQU-273--use-canonical-carrier-address-as-authority
---
# Use canonical carrier address as authority

When the active GOV grammar derives a governed fact completely and unambiguously from a carrier's canonical project-relative directory, filename, or extension, that address is the fact's sole authority and the carrier must not repeat it as embedded metadata. `atom_id` is the explicit exception for a role-classified Atom: its encoded Atom property is authoritative, while an accepted Carrier filename only renders the same value and must match it exactly.

The resolver derives only registered address facts, including structural scope, Content role, lifecycle placement, Tier, Type, Summary, and format. It reads `atom_id` from the accepted role-classified Atom's governed property encoding, validates any filename rendering against that value, and fails closed for an unknown, ambiguous, malformed, missing, duplicated, or inconsistent fact. A move or rename that changes a derived address fact is a governed operation but does not change `atom_id`.
