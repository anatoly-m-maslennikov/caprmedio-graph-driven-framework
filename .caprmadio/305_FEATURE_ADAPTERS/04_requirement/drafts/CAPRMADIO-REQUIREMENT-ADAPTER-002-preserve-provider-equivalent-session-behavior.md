---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-ADAPTER-002
scope_path: feature:adapters
subject_scopes:
  - portability
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-001-llm-provider-agnostic-framework
---

# Preserve provider-equivalent session behavior

Supported agent-host adapters must preserve equivalent CAPRMADIO routing, authority, persistence, and reconciliation behavior despite provider-specific session and compaction mechanisms.
