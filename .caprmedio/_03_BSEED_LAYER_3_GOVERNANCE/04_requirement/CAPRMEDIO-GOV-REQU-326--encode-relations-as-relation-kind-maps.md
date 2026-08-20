---
subject_scopes:
  - relation-model
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-117--store-each-semantic-relation-once
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Relation-kind maps

Every Markdown Atom encodes `relations` as a mapping from each registered
relation kind to one non-empty list of unique Artifact references:

```yaml
relations:
  child_of:
    - CAPRMEDIO-REQU-003--apply-dry-across-caprmedio
    - CAPRMEDIO-META-REQU-154--semantic-irreducibility
```

`relations` is omitted when empty. Each relation kind appears at most once;
relation-kind and target order have no semantic meaning. Unknown relation
kinds, duplicate targets, empty target lists, and the legacy `type` plus
`targets` wrapper are invalid after the governed migration cutover.
