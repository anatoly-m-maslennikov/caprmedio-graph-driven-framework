---
atom_id: CA-P-1807
ref_id: CA-P-1807
container:
  atom: CA-P-1794
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/MCP
  dependencies:
  - Subject/Graph Node/Engineering/Continuant/Tool
  - Subject/Graph Node/Engineering/Workflow
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Engineering/Manifest
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1794
  relates_to:
  - CA-C-512
  - CA-R-1804
  - CA-R-1805
  - CA-R-1806
  - CA-D-514
  - CA-P-1800
status: Done
version: 8
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 7-CA-P-1807-TASK--return-current-selected-route-execution-context.md
    path: .caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/34-CA-P-1794-TASK--repair-confirmed-final-review-gaps/done
work_sequence_number: 7
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
---
# Summary

Return current selected route execution context

## Objective

repair the discovery implementation so current admitted selected routes and their exact Operations definitions return truthful bounded context under existing authority.

## Details

- use the validated canonical manifest and actual exposed names; a source definition alone does not establish an executable binding.
- keep route-specific request schemas and disclose all matching bindings for a shared Action without choosing or executing one.
- preserve currentness, ambiguity, context-budget and explicit-gap behavior; do not add a new route, request protocol or permission grant.
- root owns source integration, actual MCP reload and rediscovery before freezing N13.

## Definition of Done

focused service/MCP regressions and independent review accept the bounded implementation; live route-name, Workflow-ID and shared Action-ID context requests return their current exact source bindings and truthful schemas without effects.

## Result

the discovery suite passes 16 cases and the isolated MCP suite passes 4 cases; independent review accepts the manifest-validated exposed-route catalog and schema behavior. after an explicit hot reload, all sixteen route-name contexts, Workflow CA-O-136 and shared Action CA-O-128 return complete current bindings. O128 discloses all four lifecycle routes with no arbitrarily selected input schema. no Action or Workflow was executed by these read-only checks.
