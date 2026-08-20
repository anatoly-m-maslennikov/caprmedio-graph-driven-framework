---
subject_scopes:
  - work-journal
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 3
updated_at: 2026-08-20 20:11:00
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-338--register-the-project-work-journal
    - CAPRMEDIO-GOV-REQU-339--register-work-journal-events
---
# Append Work Journal events

The framework must provide a deterministic Tool that validates and atomically appends one sealed Work Journal event without rewriting or rereading the complete logical Journal. The Tool must resolve the event author's full GitHub username and calendar date in the configured Artifact timestamp timezone, continue the current `<author>-<YYYY-MM-DD>-part-<N>.ndjson` segment while it contains fewer than 100 accepted events, open the next numbered segment otherwise, and return a receipt binding the event identity, carrier, line position, and before-and-after digests. Reapplying the same sealed event identity must return its existing receipt without appending a duplicate.
