---
artifact_type: requirement
artifact_id: DSET-REQUIREMENT-GOV-134
scope_path: layer:gov
subject_scopes:
  - assurance
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - DSET-REQUIREMENT-META-081
  - type: relates_to
    targets:
      - DSET-REQUIREMENT-GOV-124
      - DSET-REQUIREMENT-GOV-131
---

# Requirement — Require production assurance checklists

Every production-relevant component or governed scope must define a Production
Assurance Checklist before it can pass a production-readiness gate. The
checklist states how operators will know that the realized system remains
healthy, correct, supportable, and within its accepted operating boundaries
during real work.

Each checklist item owns one operational condition or invariant and identifies:

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
- the required observation and evidence-retention boundary; and
- known blind spots, sampling limits, unavailable signals, and other assurance
  limitations.

The checklist distinguishes its governed meaning from its realization and
results:

- the checklist defines the production assurance obligation;
- monitors, dashboards, alerts, health checks, and operational automation are
  Implementation;
- metrics, logs, traces, alerts, incidents, and recorded check outcomes are
  Observation; and
- a Problem or Concern records a material discrepancy requiring disposition.

A Production Assurance Checklist governs real production operation. It is not
a Test Case or Eval Case, and passing pre-release tests or evaluations does not
by itself satisfy the production-assurance obligation.

## Primary claim

Every production-relevant scope defines an actionable Production Assurance
Checklist that connects governed claims to live signals, ownership, response,
retention, and known limitations.

## Rationale

Pre-release QA demonstrates behavior under bounded conditions, while production
assurance must detect degradation, incorrect state, and supportability failures
during actual operation. A checklist makes that continuing obligation explicit
without conflating its definition, implementation, and observations.
