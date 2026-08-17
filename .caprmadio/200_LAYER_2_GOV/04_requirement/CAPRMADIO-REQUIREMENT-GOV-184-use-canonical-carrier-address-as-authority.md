---
subject_scopes:
  - carrier-format
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-181-represent-accepted-meaning-faithfully
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-139-use-canonical-carrier-address-as-authority
---
# Use canonical carrier address as authority

When the active GOV grammar derives a governed fact completely and unambiguously from a carrier's canonical project-relative directory, filename, or extension, that address is the fact's sole authority and the carrier must not repeat it as embedded metadata.

The resolver derives only registered address facts, including structural scope, Content role, lifecycle placement, Type, optional subtype, sequence, summary, and format, and fails closed for unknown, ambiguous, malformed, or inconsistent addresses. A move or rename that changes a derived fact is a governed operation.
