---
atom_id: CA-R-2203
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/Git Repository
version: 6
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
---
## Summary

Define Git Repository Carrier

## Claim

### Prose Claim


A Git Repository **means** a Carrier of versioned content and Git references.


```text
Git Repository > @(Git Branch)
```

## Semantics

A remote repository or branch on GitHub is another Carrier. Git Repository > Git Branch denotes whole/part containment. Local connection names and URLs describe how the repository is selected.
