---
atom_id: CA-R-2203@5
content_role: Requirement
type: Entity Definition
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Entity/Carrier/Git Repository
version: 5
updated_at: 2026-10-29 11:35:34 +0400
relations: {}
tier: 1
---
## Summary

Define Git Repository Carrier

## Claim

A Git Repository **means** a Carrier of versioned content and Git references.

### Formal claim

```text
Git Repository > @(Git Branch)
```

## Semantics

A remote repository or branch on GitHub is another Carrier. Git Repository > Git Branch denotes whole/part containment. Local connection names and URLs describe how the repository is selected.
