---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-126
scope_path: layer:gov
subject_scopes:
  - provenance
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-075
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-125
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-080
      - CAPRMADIO-REQUIREMENT-META-103
---

# Use revision-bound parent and child commit messages

Every governed Git commit uses exactly one line as its complete commit message:

```text
<parents> | <new-children> ; <updated-children>
```

## Parents

Each parent is an exact Atomic Artifact revision:

```text
<artifact-id>/<full-commit-id>
```

The artifact ID identifies the atom. The full Git commit ID identifies the
exact carrier revision on which the commit is based. Multiple parents are
separated by a comma followed by one space.

Parents may belong to different scopes. Every parent must already exist in an
earlier commit; a commit cannot reference its own not-yet-known ID.

## Children

New and updated children are separate comma-space-delimited groups:

- a governed artifact child uses its artifact ID; and
- an implementation, test, evaluation, configuration, documentation, or other
  native project child uses its repository-relative path.

Every child in both groups resolves to exactly one shared `scope_path`.
Project-local governance resolves the scope of native files from their owned
path. A renamed child is updated and uses its destination identity or path;
Git preserves its source history.

`0` represents an empty group and is reserved from use as an artifact ID or
path.

The message contains no parentheses, labels, summary, description, body, or
trailers.

## Examples

Create an initial atom:

```text
0 | PROJ-REQUIREMENT-001 ; 0
```

Refine the atom from committed revision `C1`:

```text
PROJ-REQUIREMENT-001/C1 | 0 ; PROJ-REQUIREMENT-001
```

Create and update implementation children from revision `C2`:

```text
PROJ-REQUIREMENT-001/C2 | docs/feature.md ; src/feature.py, tests/test_feature.py
```

The atom-refinement commit and commits that consume the refined revision are
separate transactions. Existing children remain bound to the parent revision
recorded by their own commit; new or updated children bind to the revision
named in their commit.

Once another commit references an Atomic Artifact revision, the referenced Git
history must not be amended, rebased, squashed, force-rewritten, or otherwise
made unreachable.

Typed relations in artifact carriers continue to define semantic relation
kinds. The commit message defines the exact revision-level provenance edge:

```text
parents | new children ; updated children
```

## Rationale

The format makes each commit a compact, replayable provenance edge. Exact
parent revisions preserve historical meaning, the two child groups expose
creation versus revision, and the one-scope rule keeps each transaction
bounded without preventing cross-scope inputs.
