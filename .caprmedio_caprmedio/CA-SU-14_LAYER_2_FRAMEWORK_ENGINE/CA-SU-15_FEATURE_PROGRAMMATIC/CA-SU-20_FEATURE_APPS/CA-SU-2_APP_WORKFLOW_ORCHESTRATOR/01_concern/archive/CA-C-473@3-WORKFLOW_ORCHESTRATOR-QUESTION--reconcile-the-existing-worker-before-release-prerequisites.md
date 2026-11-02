---
atom_id: CA-C-473@3
content_role: Concern
type: Question
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: 2026-10-23 03:06:32 +0400
subjects:
  governs: Release prerequisite worker compatibility
  depends_on:
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Runtime
  - Workflow Run
  - Implementation
  - Journal
relations:
  concern_about: [CA-P-1714, CA-P-1624]
---
# Summary

Reconcile the existing worker before Release prerequisites

## Concern

How should the existing host Worker be reconciled with the current Implementation while preserving its older queued Workflow Run?

## Evidences

The Operator confirmed the old Worker was killed. The current foreground host Worker started as PID 87864 and emitted structured readiness for application version base-revise-v5-selected-v1-docker-project-mount with runtime fingerprint 07757655bd5d586d709ea8880b17541c89cc881c911a883963f042b83ce877ca. The older base-revise-replacements-20261004-0305 Run remains ENQUEUED for base-revise-v3-replacements, unchanged.

## Blast radius

Current host Worker readiness and preservation of the older queued intent. A separate selected compiler Run was admitted through the configured Docker transport; host readiness is not proof that its compilation completed.

## Decision

The Worker-startup uncertainty is resolved. Preserve the older queued Run without cancellation, replay or version migration. The actual selected compiler Run release-methodology-reconcile-20261005-1805 reached its first Action but ended interrupted_pending without effects because its host-root parameter was not translated to the Docker execution root. CA-C-474 records that distinct code defect.
