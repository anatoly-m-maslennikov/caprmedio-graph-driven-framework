---
atom_id: CA-O-231
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step//Implementation Preparation Step'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run.Agentic Step Execution Context
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
version: 8
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
tier: 3
---
# Summary

Prepare shared-context implementation work

## Operation

Implementation Preparation Step **means** the Workflow node invoking **=1** Action, CA-O-017, **in** Integrated context under CA-R-1527.

- bind inputs from the Workflow inputs, bounded request **and** current P/Plan **when** supplied, admitted direct RMED authority rows **and** declared input universe, optional legacy `method_projection` when supplied, selected R/D implementation targets, separate Evaluation authority, permissions, selected mode, complete runtime inputs, retained work/evidence, retained participating-session references, remaining retry state, **and** latest returned results.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

- retain shared request/Plan, current source-bound R/M/E/D, exact candidate and actual prior results, findings, and remaining retry/resource state. This explicit Integrated binding does not alter the context of standalone review Steps.

## Details
