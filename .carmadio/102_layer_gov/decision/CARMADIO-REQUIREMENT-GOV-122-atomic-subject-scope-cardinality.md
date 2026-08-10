---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-GOV-122
scope_path: layer:gov
subject_scopes:
  - subject-scope
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-071
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-GOV-105
---

# Requirement — Govern Atomic Artifact subject scopes

Every Atomic Artifact stores `scope_path` as one scalar structural address,
never as a list. The current project is ambient, so the address contains only
the applicable project-relative structural coordinates.

When present, `subject_scopes` is a list of unique, unqualified, lowercase
kebab-case tokens. The allowed vocabulary is registered separately for each
`scope_path`. A token never embeds its layer, feature, project, artifact type,
or another structural coordinate.

Atomic subject-scope cardinality is:

| Atomic Artifact | `subject_scopes` |
|---|---|
| META or GOV Requirement, Concern, or QA Case Atom | exactly one |
| Analysis Atom | one or more |
| Ops Atom, external Evidence Record, or relational Verification Record | zero or more |
| Implementation Atom | zero or more |
| Other Atom | exactly one unless its registered Type policy says otherwise |

An absent optional value is omitted. Empty lists and duplicate tokens are
invalid. Subject scopes narrow discovery and comparison; tools must still
follow explicit relations before declaring an atom obsolete, replaced,
resolved, or conflicting.

## Primary claim

GOV stores one scalar structural scope per atom and governs layer-local subject
scopes through Type-aware cardinality and registered unqualified tokens.

## Rationale

Different atomic jobs need different search breadth. A precise local claim
normally has one subject, analysis may synthesize several subjects, and
evidence or implementation may already be discoverable through relations.
Explicit cardinality preserves those differences without overloading
`scope_path`.
