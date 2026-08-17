---
artifact_type: method
artifact_subtype: technical_decision
artifact_id: CAPRMADIO-DECISION-GOV-035
scope_path: layer:gov
subject_scopes:
  - lifecycle
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: resolution_of
    targets:
      - CAPRMADIO-QUESTION-GOV-010
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-050
---

# Use an archive-based Atomic Artifact lifecycle

CAPRMADIO has no `lifecycle_event` artifact type. An Atomic Artifact has only two
storage states:

- **active:** its carrier is directly in its Content-role folder and participates in
  current authority, planning, assurance, or work views as applicable;
- **archived:** its carrier is in the role-local `archive/` folder and remains
  discoverable by identity as immutable history.

Moving an unchanged carrier into `archive/` is a committed storage transition,
not a mutation of the Atomic Artifact.

## Closing active artifacts

- A successor carrying `replacement_of` replaces an older claim. After the
  successor is committed, the replaced atom moves to `archive/`.
- A resolver carrying `resolution_of` closes a Concern Atom with the `question`
  or `problem` subtype. A resolver carrying `solution_for` closes a relational
  Conflict. After the resolver is committed, the resolved atom moves to
  `archive/`.
- An atom removed from current work without current implementation is moved to
  `archive/`, and any intended future work is represented by a candidate in the
  Development Backlog. That candidate references the archived Atom ID for
  provenance.
- An atom that no longer applies and has no future intent moves to `archive/`
  in a commit whose rationale identifies why no successor is required.

Terms such as `absorbed`, `resolved`, `retired`, and `withdrawn` may describe
the reason for archival in human-facing history, but they are not stored
lifecycle states or artifact types.

## Returning matters

Reopening an archived atom is forbidden. A recurring Concern with the
`question` or `problem` subtype is a new Atom with its own identity, current
claim, provenance, and priority.

The new artifact may point to the archived predecessor with:

```yaml
relations:
  - type: recurrence_of
    targets:
      - CAPRMADIO-PROBLEM-GOV-001
```

`recurrence_of` means the same bounded matter occurred again after the earlier
artifact left the active set. It does not reactivate, replace, resolve, or
invalidate the archived predecessor.

## History and derivation

The successor or resolver owns the typed relation, rationale, and session
provenance. Git records the committed introduction and archival transition.
Derived views infer the current set from active folders and infer historical
connections from typed relations. No separate event carrier duplicates that
information.

## Rationale

Standalone lifecycle-event carriers duplicate typed relations and add a second atomic state model when active/archive placement, successor Atoms, the Development Backlog, Release Records, provenance, and Git already preserve the required history.

## Historical frontmatter metadata

```yaml
promotion:
  affected_children:
    - "governance"
    - "tool"
    - "skill"
    - "implementation"
    - "ops"
  applies_unchanged: false
  local_context_required: true
```
