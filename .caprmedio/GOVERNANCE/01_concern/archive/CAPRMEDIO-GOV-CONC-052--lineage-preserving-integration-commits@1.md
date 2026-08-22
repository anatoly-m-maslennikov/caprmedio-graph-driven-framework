---
artifact_subtype: question
subject_scopes:
  - provenance
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMEDIO-META-REQU-245--git-as-canonical-history-engine
  - type: relates_to
    targets:
      - CAPRMEDIO-GOV-REQU-309--revision-bound-parent-child-commit-messages
---

# Question — How should lineage-preserving integration commits be represented?

DSET's base delivery flow develops locally, pushes commits to the remote
integration branch, and opens a pull request to the protected branch.
Revision-bound provenance requires every referenced commit ID to remain
reachable and unchanged.

Squash or rebase integration would replace the governed commit IDs. A
host-created merge commit preserves them, but the merge commit normally
transports existing governed transactions rather than creating or updating a
governed child and therefore does not naturally fit:

```text
<parents> | <new-children> ; <updated-children>
```

Which rule should govern integration commits?

- exempt a pure transport merge commit from the governed child-transaction
  grammar while requiring PR and parent-commit provenance;
- require a distinct governed integration-commit grammar;
- require fast-forward integration only; or
- adopt another lineage-preserving mechanism.

## Resolution criteria

The answer must preserve referenced commit IDs, work with protected GitHub pull
requests, distinguish integration from implementation, remain reconstructable
from Git, and avoid a meaningless `0 | 0 ; 0` commit.
