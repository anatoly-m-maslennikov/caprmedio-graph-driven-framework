---
artifact_subtype: defect
subject_scopes:
  - artifact-catalog
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CAPRMEDIO-REQUIREMENT-GOV-029
---

# Defect — Missing artifact classifications are skipped

Validation and health currently continue past governed files that have neither
direct classification metadata nor one applicable registry rule. Procedure
also lacks practical playbook/runbook path coverage.

## Completion condition

Every governed file resolves to exactly one classification or an explicit
registered exclusion. Missing, conflicting, nested, or invalid classification
fails closed, and health reports the complete governed inventory.

## Primary claim

Governed files without direct metadata or a matching path rule can bypass the mandatory exactly-one artifact classification gate.

## Rationale

A MECE catalog is not complete when unclassified carriers silently disappear from validation and health.
