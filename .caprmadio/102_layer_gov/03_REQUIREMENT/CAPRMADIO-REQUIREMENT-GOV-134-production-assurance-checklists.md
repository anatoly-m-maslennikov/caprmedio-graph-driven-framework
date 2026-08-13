---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-134
scope_path: layer:gov
subject_scopes:
  - assurance
tier: standard
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-093
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-124
      - CAPRMADIO-REQUIREMENT-GOV-138
      - CAPRMADIO-REQUIREMENT-GOV-139
      - CAPRMADIO-REQUIREMENT-GOV-133
---

# Requirement — Require production assurance checklists

Every production-relevant component or governed scope must define a Production
Assurance Checklist before it can pass a production-readiness gate. The
checklist states how operators will know that the realized system remains
healthy, correct, supportable, and within its accepted operating boundaries
during real work.

Each operational condition or invariant is owned by one `assurance_control`
Atom. The control identifies:

- the Requirement, Contract, Constraint, Method, or other governed claim being
  assured;
- the production signal and authoritative data source;
- the healthy condition, expected range, threshold, or failure predicate;
- the evaluation window, cadence, and permitted detection delay;
- the component, entity, lifecycle state, or workflow boundary to which it
  applies;
- the accountable owner and escalation destination;
- the alert, incident, investigation, degradation, rollback, or recovery action
  triggered by failure;
- the diagnostic context required to investigate the condition;
- the required Ops record and evidence-retention boundary; and
- known blind spots, sampling limits, unavailable signals, and other assurance
  limitations.

A Production Assurance Checklist is an Assurance-role Catalog Projection over
the applicable `assurance_control` Atoms. It organizes and navigates those
controls without absorbing, paraphrasing, or replacing their claims.

Each control distinguishes its governed meaning from its realization and
results:

- the Assurance Control defines the production assurance condition;
- monitors, dashboards, alerts, health checks, and operational automation are
  Implementation;
- metrics, logs, traces, alerts, incidents, and recorded check outcomes are
  Ops; and
- a Concern Atom with the `problem` subtype records a material discrepancy
  requiring disposition.

A Production Assurance Checklist governs real production operation. It is not
a QA Case, and passing pre-release Test or Evaluation implementations does not
by itself satisfy the production-assurance obligation.

## Primary claim

Every production-relevant scope defines independently replaceable Assurance
Controls and an actionable Production Assurance Checklist Projection that
connects them to live signals, ownership, response, retention, and known
limitations.

## Rationale

Pre-release QA demonstrates behavior under bounded conditions, while production
assurance must detect degradation, incorrect state, and supportability failures
during actual operation. Atomic controls preserve independent lifecycle and
replacement, while the checklist provides a navigable scope view without
conflating definitions, implementations, and observations.
