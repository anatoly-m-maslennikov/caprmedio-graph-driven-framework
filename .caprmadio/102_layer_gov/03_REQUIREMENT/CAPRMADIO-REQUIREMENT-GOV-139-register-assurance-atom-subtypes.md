---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-139
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
tier: standard
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-131
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-093
      - CAPRMADIO-REQUIREMENT-GOV-138
---

# Requirement — Register Assurance Atom subtypes

GOV registers exactly these current direct subtypes of the internal Assurance
Atom Type:

- `qa_case` defines one mechanism-neutral bounded check, including the claim
  checked, applicable conditions, acceptance criteria, and disposition rule;
  and
- `assurance_control` defines one condition or invariant checked during real
  operation, including its signal, healthy boundary, evaluation window,
  ownership, and failure response.

Automated tests, evaluation prompts, executable rubrics, statistical
evaluators, model judges, monitors, alerts, and health checks are
Implementation realizations rather than Assurance subtypes. Their executions
and factual results use the Ops Content role.

One QA Case may have distinct Test and Evaluation implementations. One
implementation may realize several QA Cases only when coverage and results
remain individually attributable. Test and Evaluation chains remain explicit
even when they assure the same Case.

Another Assurance pattern uses the top-level `assurance` Type until GOV admits
a direct subtype for it. Sub-subtypes are forbidden.

## Primary claim

`qa_case` and `assurance_control` are the two currently registered direct
subtypes of the internal Assurance Atom Type.

## Rationale

Mechanism-neutral QA obligations avoid duplicating one assurance claim across
Test and Evaluation implementations, while Assurance Controls keep continuous
production checking distinct from bounded QA.
