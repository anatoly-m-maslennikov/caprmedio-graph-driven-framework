---
atom_id: CA-C-290
ref_id: CA-C-290@1
container:
  scope_unit: CA-SU-11
role: Concern
form: Conflict
relations:
  concern_about:
  - CA-D-470
status: Archived
version: 1
updated_at: 2026-10-04 06:19:35 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: CA-C-290@1-CORE_META_MODEL-CONFLICT--reconcile-supporting-detail-placement-in-plan-carriers.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/01_concern/archive
---
# Summary

Reconcile supporting-detail placement in Plan carriers

## Concern

CA-D-470 version 7 states that Details carries supporting information, then states that any other supporting Details must stay within Objective. These clauses give incompatible placement instructions for supporting Plan content other than Definition of Done.

## Evidences

The active source CA-D-470 Claim item 3 says Details carries supporting information and exactly one nested Definition of Done. Its following paragraph says any other supporting Details must stay within Objective. CA-D-479 version 6 permits lower-level supporting headings but does not resolve this ownership conflict. Independent review of CA-P-1117 identified it.

### Current disposition

Without changing methodology authority in this plan-authoring turn, CA-P-1117 and its descendants take the narrower instruction: supporting subsections in Objective; Details contains only Definition of Done. All requested rules and required headings are preserved. The source conflict remains active for a separate governed resolution; it is not an external-runtime blocker or permission to change other Atoms.

## Blast radius

All Plan carriers governed by CA-D-470 can receive inconsistent placement judgments. CORE_META_MODEL owns the conflict. Current Epic preparation can proceed under the stricter layout; later source resolution must identify affected carriers and checks before applying changes.
