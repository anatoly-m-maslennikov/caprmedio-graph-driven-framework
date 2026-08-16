---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-116
subject_scopes:
  - principles
tier: principle
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
---

# Preserve strict semantic distinctions

CAPRMADIO keeps independently governed meanings distinct even when ordinary
language, one carrier, one workflow, or one implementation change presents
them together. An entity is not its description or carrier; a Requirement is
not its Method; a Method is not its Implementation; an Assurance criterion is
not its execution result; provenance is not evidence; and an observed fact is
not authority for the desired state.

When wording could resolve to more than one governed meaning, the writer or
tool must recover the intended meaning and its owning Type before the Claim is
admitted. Co-location, readable presentation, automation, or a relation between
meanings never merges their identities or transfers their semantic force.
CAPRMADIO-REQUIREMENT-114 separately requires every canonical decomposition to remain MECE.
