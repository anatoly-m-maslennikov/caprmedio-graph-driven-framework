---
atom_id: CA-P-2363@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 7
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Atom
  - Scope Unit
  - Workflow
  - Plan
version: 2
updated_at: 2026-10-24 06:04:19 +0400
relations:
  is_decomposition_of:
  - CA-P-2318
tier: 3
---
# Summary

Preserve local Draft demotion bundles

## Objective

Fix the existing native demotion branch so a nested Workflow/Step Markdown Carrier moves to its local container's Draft placement together with its matching same-stem subtree, without flattening to the Content Role root or leaving descendants behind.

## Details

Own only the smallest demotion local-placement and matching-bundle correction plus focused author tests, under Root-assigned exclusive code ownership. Reproduce the independently observed nested Step-to-Draft failure through the actual native publication path. Apply current D467 v6's local container Status placement and recursive same-stem grouping with D466 v4's lowercase draft directory and existing O128 v6 authorization/publication behavior. Preserve the existing demotion identity and history boundary, not a new identity policy. R1432 v11/R1788 v3 require descendants moved only with their ancestor, without changes to their own bytes, direct ownership or relative placement, to retain their Version and Updated At.

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans/Git and assigns disjoint implementation and independent-test scopes; you are not alone, so preserve others' edits. Draft promotion/identity redesign, cascade orchestration, lifecycle registry activation, general recovery redesign and live migration are excluded. Do not loosen source admission, authorization, collision/currentness checks or existing rollback guarantees. Required source amendments are not inferred from this bug.

### Definition of Done

Actual authorized native nested Step-to-Draft publication puts the Markdown Carrier inside the immediate authenticated container's lowercase draft placement and relocates its optional matching directory to the resulting filename stem. Fixtures with subordinate Steps and older history prove retained nesting, exact descendant bytes/ID/Version/Status/Updated At and unchanged unrelated siblings; no old matching subtree is stranded and nothing is flattened to the role root. Existing demotion identity/history behavior, safe refusal on stale/denied/colliding/unadmitted inputs and affected local-status/bundle regressions remain intact. Pin exact final source/code/test evidence for P2364 independent acceptance; callback-only preparation is insufficient. Parent cascade, promotion identity, registry/runtime activation and live effects remain open.
