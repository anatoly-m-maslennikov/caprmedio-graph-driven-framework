---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-052
scope_path: layer:gov
subject_scopes:
  - methodology
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-057
---

# Synchronize installed methodology only on command

CAPRMADIO maintainers edit the reusable methodology only in its repository-root
source. An ordinary source edit never rewrites
`.caprmadio/000_caprmadio_framework/` and no workflow copies installed files back into
the root source.

An explicit operator synchronization command performs the one-way
root-to-installed refresh. Until that command runs, the installed methodology
remains the last accepted snapshot and may intentionally differ from the
working source.

## Rationale

Separating authoring from installation keeps ordinary edits bounded, preserves a reviewable installed snapshot, and prevents accidental bidirectional drift.
