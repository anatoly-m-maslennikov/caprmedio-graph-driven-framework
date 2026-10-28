---
subjects:
  governs: Subject/Graph Node/Engineering/Verification
  depends_on: []
version: 35
updated_at: 2026-10-27 06:04:45 +0400
relations:
  depends_on:
  - CA-R-1503
  - CA-R-1504
  - CA-R-1505
atom_id: CA-R-1635@35
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Require production evaluation checklists

## Scope

production-relevant components and governed scopes.

## Claim

**every** production-relevant component **or** governed scope **must** define a Production Evaluation Checklist **before** it can pass a production-readiness gate. the checklist states how operators will know that the realized system remains healthy, correct, supportable, **and** within its accepted operating boundaries during real work.

**every** operational condition **or** invariant is owned by one `evaluation_control` Atom. the control identifies:

- the Requirement, Demand For, Constraint, Method, **or** other governed claim being assured;
- the production signal **and** authoritative data source;
- the healthy condition, expected range, threshold, **or** failure predicate;
- the evaluation window, cadence, **and** permitted detection delay;
- the component, entity, lifecycle state, **or** workflow boundary **to** which it applies;
- the accountable owner **and** escalation destination;
- the alert, incident, investigation, degradation, rollback, **or** recovery action triggered by failure;
- the diagnostic context required **to** investigate the condition;
- the required factual execution record **and** evidence-retention boundary; **and**
- known blind spots, sampling limits, unavailable signals, **and** other evaluation limitations.

a Production Evaluation Checklist is a Catalog Projection over the applicable `evaluation_control` Atoms. it organizes **and** navigates those controls **without** absorbing, paraphrasing, **or** replacing their Claims. the Catalog Projection does **not** acquire the Content Role of its source Atoms.

**every** control distinguishes its governed meaning from its realization **and** results:

- the Evaluation Control defines the production evaluation condition;
- monitors, dashboards, alerts, health checks, **and** operational automation are Implementation;
- recorded metrics, logs, traces, alerts, incidents, **and** check outcomes are factual execution records, **not** reusable Operations definitions; **and**
- a Concern Atom of Type `problem` records a material discrepancy requiring disposition.

a Production Evaluation Checklist presents the applicable controls for real production operation **without** becoming their authority. it is **not** a QA Case, **and** passing pre-release Test **or** Evaluation implementations does **not** by itself satisfy the production-evaluation obligation.

## Details

pre-release QA demonstrates behavior under bounded conditions, while production evaluation **must** detect degradation, incorrect state, **and** supportability failures during actual operation. atomic controls preserve independent lifecycle **and** replacement, while the checklist provides a navigable scope view **without** conflating definitions, implementations, **and** observations.
