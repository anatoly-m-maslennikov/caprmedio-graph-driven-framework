---
subject_scopes:
  - work-journal
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 4
updated_at: 2026-08-20 21:22:00
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-338--register-the-project-work-journal
    - CAPRMEDIO-GOV-REQU-339--register-work-journal-events
---
# Append Work Journal events

The framework must provide a deterministic Tool that validates and atomically appends one sealed Work Journal event without rewriting or rereading the complete logical Journal. The Tool must resolve the event author's full GitHub username and calendar date in the configured Artifact timestamp timezone, continue the current `<author>-<YYYY-MM-DD>-part-<N>.ndjson` segment while it contains fewer than 100 accepted events, and open the next numbered segment otherwise. Its receipt binds the event identity, carrier, line position, `previous_carrier_digest`, and `appended_carrier_digest`; these digests describe the Journal carrier append and never duplicate a governed subject's previous and resulting states. Reapplying the same sealed event identity must return its existing receipt without appending a duplicate.
