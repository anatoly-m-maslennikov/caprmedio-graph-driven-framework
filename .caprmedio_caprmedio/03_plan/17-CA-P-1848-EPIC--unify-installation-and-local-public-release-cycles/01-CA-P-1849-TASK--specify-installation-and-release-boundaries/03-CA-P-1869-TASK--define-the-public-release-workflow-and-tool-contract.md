---
atom_id: CA-P-1869
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-10 18:58:38 +0400"
subjects:
  governs: CAPRMEDIO Framework Instance
  depends_on: [Project, Plan, AI Agent, Operator, Framework Package, Methodology Source, Applicable Methodology, Project Structure, Requirement, Method, Evaluation, Delivery, Workflow, Step, Action, Tool, Journal, Version]
relations:
  is_decomposition_of: [CA-P-1849]
  blocks: [CA-P-1870]
---
# Summary

Define the public-release Workflow **and** Tool contract

## Objective

the AI Agent defines the one reusable Operator-invoked Public release Workflow **and** its governing Tool RMED.

## Details

1. Under CA-R-1799, bind automatic README/documentation preparation, exactly one content prompt, complete public suite, safe commit/push, PR discovery/create/update and actual-URL metadata follow-up into one Public release command.
2. The one prompt returns the complete PR description with “What's new” and “What's fixed” plus concise Version History bullets. No prompt is used for README text or approval retries.
3. Publish only after the complete suite passes; update/reuse a matching `amm/dev`→`main` PR without merge. A URL-only follow-up needs no second suite.
4. Define Public release as the concrete Project Operation in `.caprmedio_caprmedio/09_operations` and its helper Tool RMED in `205_FEATURE_PROJECT_TOOLS`/delivered `PROJECT_TOOLS`, outside the reusable Engine/package and general Methodology. Reusable compiler/installer, shared package/gate models/codecs, detached readers and generic O200 install/bootstrap/restore capability remain in `TOOLS`; register ProjectTools D declarations as excluded delivery-boundary content.
5. Preserve Summary identity, source authority and unrelated edits.

### Definition of Done

the Plan is **not** Done **if** more than one Public command or content prompt is required, Public release/helper placement is outside its Project-owned boundary, reusable generic capability leaves `TOOLS`, ProjectTools D declarations ship in or fault the exporter frontier, a material publishable change bypasses the complete suite, PR/URL behavior is unspecified, or the contract permits merge.
