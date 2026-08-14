---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-155
scope_path: layer:meta
subject_scopes:
  - semantics
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-116-preserve-strict-semantic-distinctions
    - CAPRMADIO-REQUIREMENT-META-138-use-nouns-for-content-role-names
    - CAPRMADIO-REQUIREMENT-META-140-apply-dry-across-caprmadio
    - CAPRMADIO-REQUIREMENT-META-150-use-nine-canonical-meta-subject-scopes
---

# Canonical scoped vocabulary

Each canonical CAPRMADIO term has one active Atom that owns one precise meaning
for one declared scope. A registered alias resolves to that canonical term and
owns no independent meaning.

Framework vocabulary applies to all adopting projects. Project vocabulary
applies only within its project. Reusing the same name across scopes does not
merge their meanings.
