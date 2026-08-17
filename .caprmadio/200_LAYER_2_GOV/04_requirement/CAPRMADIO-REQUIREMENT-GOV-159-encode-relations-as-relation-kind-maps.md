---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-159
scope_path: layer:gov
subject_scopes:
  - relation-model
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-144
    - CAPRMADIO-REQUIREMENT-GOV-181
---
# Relation-kind maps

Every Markdown Atom encodes `relations` as a mapping from each registered
relation kind to one non-empty list of unique Artifact references:

```yaml
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-140-apply-dry-across-caprmadio
    - CAPRMADIO-REQUIREMENT-META-193-semantic-irreducibility
```

`relations` is omitted when empty. Each relation kind appears at most once;
relation-kind and target order have no semantic meaning. Unknown relation
kinds, duplicate targets, empty target lists, and the legacy `type` plus
`targets` wrapper are invalid after the governed migration cutover.
