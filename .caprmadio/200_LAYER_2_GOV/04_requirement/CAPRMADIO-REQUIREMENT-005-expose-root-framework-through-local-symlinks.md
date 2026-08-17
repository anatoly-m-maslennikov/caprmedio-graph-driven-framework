---
subject_scopes:
  - self-hosting
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-004-keep-local-methodology-installation-empty
  override_of:
    - CAPRMADIO-REQUIREMENT-GOV-052-explicit-methodology-synchronization
---
# Expose root framework through local symlinks

This CAPRMADIO source project must expose its Git-tracked, non-hidden root files
and directories under `.caprmadio/000_caprmadio_framework` using relative
symlinks only. CAPRMADIO project version, release, and changelog entries are
excluded because they describe this project rather than the reusable framework.
The directory contains no copied or independently maintained content; its
deterministic link set is a mechanical root view for recursive discovery and
operator convenience.
