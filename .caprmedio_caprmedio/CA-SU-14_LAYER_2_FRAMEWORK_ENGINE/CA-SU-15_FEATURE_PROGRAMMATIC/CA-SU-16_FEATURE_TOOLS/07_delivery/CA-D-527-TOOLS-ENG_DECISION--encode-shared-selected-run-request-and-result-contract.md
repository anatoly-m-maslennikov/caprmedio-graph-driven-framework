---
atom_id: CA-D-527
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 16
updated_at: 2026-10-27 19:59:26 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
relations:
  delivery_for:
  - CA-R-1821
  - CA-R-1822
  - CA-R-1823
type: Eng Decision
tier: 4
---
# Summary

Encode shared selected Run request and result contract

## Scope

The small caller-facing contract shared by selected capability, MCP, and
adapter implementations. It is a service interface, not a new Workflow.

## Claim

RUN_SUPPORT **must** expose `run_selected_operation(request) -> result` with
the following exact bounded request and result representations.

## Details

- `request.mode` is the closed enum `preview | execute`, defaults to `preview`,
  and only literal `execute` starts work; `apply` and all other aliases are
  invalid. Every request contains the non-empty caller-supplied stable
  `request_id`, one `operation_route`, typed non-secret `parameters`, and
  `parameters_digest`; `target_frontier` (ordered safe refs plus
  `target_frontier_digest`); requested `effects` (typed route-owned effect
  descriptors plus `effects_digest`); and `definition_manifest`
  (`manifest_ref`, `manifest_digest`). The shared contract validates these
  shapes/digests but does not enumerate manifest members or decide route domain
  semantics.
- `source_freshness` is required and contains
  `selected_source_registry_ref`, `selected_source_registry_version`,
  `selected_source_registry_digest`, `selected_binding_ref`,
  and `selected_binding_digest`. It is evaluated against the one canonical
  outer `definition_manifest` reference/digest above; shadow or duplicate
  manifest fields inside `source_freshness` are unknown fields and are rejected
  before any Run or effect. Optional
  `expected_definition_revisions` contains ordered Atom ID, kind, Version,
  safe source path, and digest entries and must match that outer canonical
  manifest. The complete per-route manifest and its source construction remain
  owned by the reviewed selected-source/MCP delivery; this contract consumes
  only its exact reference and digest.
- `initiative` contains sealed identity, human-instruction summary, and safe
  reference. Optional `lineage` contains only actual known lineage. A preview
  returns a sealed read-only `proposal_receipt` and `proposal_receipt_digest`
  that bind `request_id`, route, Initiative reference, source-freshness
  declaration/currentness observation, and every parameters/target-frontier/
  effects/definition-manifest digest. It may report preview currentness or a
  non-start blocker, but never has Run IDs or Event IDs/receipts.
- An `execute` request additionally contains that exact `proposal_receipt` and
  digest, `assigned_action_id`, requested Run identity/identities, and sealed
  `operator_authorization`. Authorization contains its reference/freshness
  evidence and binds the same request ID, route, proposal-receipt digest,
  parameters digest, target-frontier digest, effects digest,
  definition-manifest reference/digest, and source-freshness declaration. The
  service rechecks all declared sources/currentness before dispatch. Unknown
  fields, implicit source selection, ambient authorization, secret inputs,
  missing/stale preview/authorization, or reuse of a `request_id` with changed
  canonical bytes are rejected before effect or Run creation.
- `result` always contains `request_id`, `disposition` (`preview`, `declined`,
  `blocked`, `started`, or `terminal`), the proposal receipt for preview, and
  the `source_freshness` comparison/currentness result. Only a started/terminal
  result contains actual Run IDs and admitted definition bindings; a terminal
  result additionally contains truthful operation outcome/result/effect/report
  refs. Preview and every unstarted disposition have no Run/Event identity.
  Plain Journal append/read records supplied observations independently:
  canonical Event IDs/receipts, prior history and successful logging are not
  dispatch or completion prerequisites. An append failure is reported through
  existing diagnostics without changing the independently observed operation
  outcome. No recording-pending or Journal retry/recovery disposition is
  required; any existing replay disposition describes actual dispatch/effect
  state, never permission to repeat an uncertain effect.
- The service neither decides route-specific domain semantics nor creates a
  second workflow executor. Callers supply their selected route implementation;
  MCP and other adapters reuse this contract and default mutations to preview.
