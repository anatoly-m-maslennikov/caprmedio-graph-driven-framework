---
subject_scopes:
  - self-hosting
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-057-bounded-recursive-self-hosting
    - CAPRMADIO-REQUIREMENT-GOV-052-explicit-methodology-synchronization
---

# Keep local methodology installation empty

This CAPRMADIO source project must keep `.caprmadio/methodology` unmaterialized:
the path may be absent or empty, but it must contain no files or directories.
Only an explicit operator request may populate or synchronize it; ordinary
development, resolution, validation, and self-hosting must use the framework
source in the repository root without creating a mirror.
