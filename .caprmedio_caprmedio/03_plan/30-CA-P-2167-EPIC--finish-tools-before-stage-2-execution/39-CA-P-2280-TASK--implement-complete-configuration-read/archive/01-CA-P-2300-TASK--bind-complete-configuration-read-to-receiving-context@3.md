---
atom_id: CA-P-2300
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Workflow, Configuration, Plan]
version: 3
updated_at: "2026-10-13 22:24:17 +0400"
relations:
  is_decomposition_of: [CA-P-2280]
---
# Summary

Bind complete configuration Read to receiving context

## Objective

Bind complete Project Structure and Project Settings Read to actual schema/source/permission context. Prove complete source text, structured data and state with no effects. Resolve or explicitly report typed TOML representation gaps; do not silently stringify or claim partial Read as complete.

For remaining Project Settings work, the accepted boundary is a standalone inspection Read of a complete schema-valid document whose history may be unknown. Such a Read does not admit the document for operations requiring verified history. Existing Settings documents, existing callers, Journal and runtime remain unchanged by this work.

## Details

### Current continuation checkpoint — 2026-10-13 22:24:17 +0400

The current Project Structure branch has a private O218 receiver using a genuine recorded Action, exact schema/selection pins, complete supplied Settings validation and native full text/document/state results. Ten author checks, independent receiving tests and all 264 connector tests passed. Evidence is selected-read-receivers-checkpoint.md under the tools-first projection. The remaining new Settings inspection branch is decomposed into three Active Tasks in this Task's matching Directory Carrier: CA-P-2354 aligns its narrowly scoped schema/source authority; CA-P-2355 implements the standalone no-legacy inspection reader returning a typed immutable Settings snapshot and provenance; CA-P-2356 independently verifies that bounded outcome. The latest Operator choice permits schema-valid Read with unknown history and does not confer admission for verified-history operations. These children do not require a generic native TOML text/document result API. Broader complete Project Settings Configuration Read remains open after their acceptance. Historical views, existing-caller migration and runtime activation remain separate. Keep this Task Active and accept the children only against their narrow snapshot/provenance definitions of done.

Each child has an own-work bound of up to 15 minutes; split any larger responsibility before exceeding that bound. CA-P-2355 uses CA-P-2354's accepted schema/source result; CA-P-2356 verifies the connected implementation after those inputs are ready. Inherit the parent Task's accepted contracts, current-source checks and authority boundaries. Internal helpers are not newly admitted Tools. Keep parsing, reading, writing and CLI responsibilities separate. The integration owner controls Plans and Git; parallel implementation owns disjoint files only.

### Definition of Done

The Plan is not Done until exact implementation/source pins, focused positive/refusal/no-op checks and an independent review establish this child's bounded outcome. Preparation alone, invented public bindings, source-policy changes, deferred publication or live Core migration do not satisfy it. Parent-wide and runtime completion remain separate.
