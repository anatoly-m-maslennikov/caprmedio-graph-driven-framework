---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-122
scope_path: layer:gov
subject_scopes:
  - subject-scope
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-167-use-universal-subject-scopes-with-rmad-cardinality
  relates_to:
    - CAPRMADIO-REQUIREMENT-GOV-105-narrowest-common-scope-ownership
---

# Govern Atomic Artifact subject scopes

Every Atom stores `subject_scopes` as a non-empty list of unique, unqualified,
lowercase kebab-case tokens. The allowed vocabulary is registered separately
for each `scope_path`. A token never embeds its Layer, Feature, project,
Artifact Type, or another structural coordinate.

Atomic subject-scope cardinality is:

| Content role | `subject_scopes` |
|---|---|
| Requirement, Method, Assurance, Delivery | exactly one |
| Concern, Analysis, Plan, Implementation, Ops | one or more |

An absent property, empty list, duplicate token, or value outside the owning
scope's vocabulary is invalid. Subject scopes narrow discovery and comparison;
tools must still follow explicit relations before declaring an Atom obsolete,
replaced, resolved, or conflicting.
