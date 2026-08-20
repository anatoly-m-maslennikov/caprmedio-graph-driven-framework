---
subject_scopes:
  - lifecycle
tier: core
version: 3
updated_at: 2026-08-19 22:22:41
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  resolution_of:
    - CAPRMEDIO-GOV-CONC-047--should-lifecycle-event-artifacts-be-removed
  replacement_of:
    - CAPRMEDIO-GOV-REQU-408--atomized-transactional-state
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---

# Use an archive-based Atomic Artifact lifecycle

CAPRMEDIO has no `lifecycle_event` artifact type. An Atomic Artifact has only two
storage states:

- **active:** its carrier is directly in its Content-role folder and participates in
  current authority, planning, evaluation, or work views as applicable;
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
      - CAPRMEDIO-GOV-CONC-029--active-deltas-and-accepted-truth-reuse-ids-inconsistently
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
