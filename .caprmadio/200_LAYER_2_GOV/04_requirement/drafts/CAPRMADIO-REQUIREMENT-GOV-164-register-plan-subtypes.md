---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-164
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-GOV-142-register-development-backlog-projection
    - CAPRMADIO-REQUIREMENT-GOV-150-register-change-plan-subtype
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-149-register-caprmadio-atom-type-surface
    - CAPRMADIO-REQUIREMENT-GOV-152-register-caprmadio-type-prefixes
---

# Register Plan subtypes

GOV must register `development_backlog`, `version_plan`, and `change_plan` as direct subtypes of the internal `plan` Atom Type.

| Subtype | Governed unit |
|---|---|
| `development_backlog` | Accepted unscheduled action points and, before an approved split, target-version sections in the project's default planning carrier. |
| `version_plan` | Action points assigned exclusively to one target version after an approved split. |
| `change_plan` | One bounded execution package that changes governed artifacts or their native realization. |

All three subtypes use the `PLAN` Type prefix and the Plan Type numbering sequence. Subtype names remain explicit in frontmatter and may appear in filenames only when project settings enable subtype-bearing names.
