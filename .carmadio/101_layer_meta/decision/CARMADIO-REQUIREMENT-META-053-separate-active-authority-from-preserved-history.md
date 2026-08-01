---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-053
scope_path: layer:meta
subject_scopes:
  - governance-surface
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-META-032
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-058
---

# Requirement — Separate active authority from preserved history

## Primary claim

CARMADIO's durable control plane distinguishes accepted current project
authority, applicable current Projections, and operative governance. Archives
preserve accepted historical Atoms without making them active authority.
Future intentions remain outside active authority in governed future-planning
surfaces, and unaccepted exploration remains outside governed state.

## Rationale

The corrected boundary distinguishes current authority from preserved history
without excluding archives from durable history or admitting future intent and
session speculation into active authority. Secret handling, provider
portability, and runtime acquisition remain downstream requirements because
they are implementation mechanisms rather than META invariants.
