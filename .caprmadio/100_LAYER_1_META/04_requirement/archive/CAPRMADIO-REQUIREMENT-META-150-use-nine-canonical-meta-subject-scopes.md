---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-150
scope_path: layer:meta
subject_scopes:
  - artifact-model
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-124-use-one-canonical-subject-scope-per-meta-atom
  child_of:
    - CAPRMADIO-REQUIREMENT-META-100-scope-path-does-not-change-semantic-coordinates
---

# Use nine canonical META Subject scopes

Every active META Atom selects its `subject_scopes` from this closed, ordered
vocabulary:

1. `principles` — framework identity and universal constitutional principles;
2. `semantics` — canonical terms, Content-role meanings, semantic distinctions, and role boundaries;
3. `artifact-model` — artifact forms, Types, properties, claims, and relations;
4. `scope-topology` — structural scopes, layers, profiles, inheritance, handoffs, and recursive applicability;
5. `authority` — normative ownership, admission, precedence, and amendment;
6. `assurance` — falsifiability, evidence, verification, uncertainty, and the boundary between authority and observed fact;
7. `lifecycle-traceability` — revisions, dependencies, lineage, replacement, archive, currentness, provenance, Git history, and Journals;
8. `development-flow` — Exploration, candidate promotion, backlog, version, release, and reconciliation; and
9. `framework-boundary` — governed storage, runtime isolation, repository work areas, and bounded self-hosting.

`scope_path` continues to identify structural ownership and Applicability.
`subject_scopes` are layer-local discovery and review classifications and do
not change authority, inheritance, relations, or effective structural scope.

Missing, empty, unknown, duplicate, irrelevant, or fallback Subject scopes fail
META admission and Projection generation. Requirement, Method, Assurance, and
Delivery Atoms select exactly one value; other Content roles may select one or
more. Extending this vocabulary requires the normal MECE and parsimony gates.
