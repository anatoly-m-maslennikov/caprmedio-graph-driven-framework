---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-GOV-052
scope_path: layer:gov
subject_scopes:
  - methodology
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-057
---

# Requirement — Synchronize installed methodology only on command

CARMADIO maintainers edit the reusable methodology only in its repository-root
source. An ordinary source edit never rewrites
`.carmadio/000_CARMADIO_METHODOLOGY/` and no workflow copies installed files back into
the root source.

An explicit operator synchronization command performs the one-way
root-to-installed refresh. Until that command runs, the installed methodology
remains the last accepted snapshot and may intentionally differ from the
working source.

## Primary claim

Reusable methodology is authored only in the repository-root source and is copied unidirectionally into the installed .carmadio methodology only after an explicit operator synchronization command.

## Rationale

Separating authoring from installation keeps ordinary edits bounded, preserves a reviewable installed snapshot, and prevents accidental bidirectional drift.
