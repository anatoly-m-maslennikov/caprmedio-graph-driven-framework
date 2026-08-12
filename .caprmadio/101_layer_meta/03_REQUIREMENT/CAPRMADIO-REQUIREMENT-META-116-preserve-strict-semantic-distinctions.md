---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-116
scope_path: layer:meta
subject_scope: principles
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-086
      - CAPRMADIO-REQUIREMENT-META-091
      - CAPRMADIO-REQUIREMENT-META-098
      - CAPRMADIO-REQUIREMENT-META-114
---

# Requirement — Preserve strict semantic distinctions

CAPRMADIO keeps independently governed meanings distinct even when ordinary
language, one carrier, one workflow, or one implementation change presents
them together. An entity is not its description or carrier; a Requirement is
not its Method; a Method is not its Implementation; an Assurance criterion is
not its execution result; provenance is not evidence; and an observed fact is
not authority for the desired state.

When wording could resolve to more than one governed meaning, the writer or
tool must recover the intended meaning and its owning Type before the claim is
admitted. Co-location, readable presentation, automation, or a relation between
meanings never merges their identities or transfers their semantic force.
META-114 separately requires every canonical decomposition to remain MECE.

## Primary claim

CAPRMADIO preserves independently governed meanings as distinct identities and
forbids wording, carriers, workflows, or relations from collapsing them.

## Rationale

This adapts FPF Strict Distinction while keeping MECE as its own independently
replaceable CAPRMADIO invariant.
