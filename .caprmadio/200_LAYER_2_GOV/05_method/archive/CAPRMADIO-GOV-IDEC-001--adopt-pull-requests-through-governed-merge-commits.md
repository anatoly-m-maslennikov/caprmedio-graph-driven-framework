---
artifact_type: integration_decision
artifact_id: CAPRMADIO-GOV-IDEC-001
scope_path: layer:gov
subject_scopes:
  - provenance
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: resolution_of
    targets:
      - CAPRMADIO-QUESTION-GOV-018
  - type: override_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-126
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-076
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-121
---

# Integration Decision — Adopt pull requests through governed merge commits

A pull request is adopted into the protected target branch by a true merge
commit. The merge preserves every reviewed source commit and uses this distinct
governed integration-commit message:

```text
<pull-request-id>/<reviewed-source-head> | 0 ; <target-ref>
```

The fields mean:

- `<pull-request-id>` is the stable provider-qualified identity of the pull
  request;
- `<reviewed-source-head>` is the full Git commit ID reviewed and approved in
  that pull request; and
- `<target-ref>` is the full protected branch reference updated by the merge.

For GitHub, the pull-request identity is:

```text
github:<owner>:<repository>:<number>
```

Example:

```text
github:example:project:42/0123456789abcdef0123456789abcdef01234567 | 0 ; refs/heads/main
```

The merge commit must have the pre-merge target head as its first parent and
the reviewed source head as another parent. The pull request's declared target
must equal `<target-ref>`, and the target ref must point to the merge commit
after integration.

Squash merge, rebase merge, force rewriting, or any integration that replaces
the reviewed commit identities is forbidden. If the reviewed source head
changes, the pull request must pass its required review and assurance gates
again before integration.

This integration profile overrides the Atomic-Artifact parent and
repository-child field meanings of CAPRMADIO-REQUIREMENT-GOV-126 only for a
pull-request merge commit. It retains the same one-line, parent-to-child
transaction shape: the reviewed pull request is the parent, no new carrier is
created, and the protected target ref is the maintained child updated by the
adoption transaction.

The pull request remains a maintained relational Implementation carrier. The
merge commit records adoption, not a new implementation claim; the preserved
source commits retain their own governed parent-to-child provenance.

## Primary claim

A pull request enters a protected branch through a lineage-preserving merge
commit whose governed message binds the pull-request identity and reviewed
source head to the updated target ref.

## Rationale

The repository must preserve the exact governed commits that were reviewed.
Treating the merge as a pull-request adoption transaction keeps integration
inside the same compact commit system without inventing meaningless children
or replacing the implementation history through squash or rebase.
