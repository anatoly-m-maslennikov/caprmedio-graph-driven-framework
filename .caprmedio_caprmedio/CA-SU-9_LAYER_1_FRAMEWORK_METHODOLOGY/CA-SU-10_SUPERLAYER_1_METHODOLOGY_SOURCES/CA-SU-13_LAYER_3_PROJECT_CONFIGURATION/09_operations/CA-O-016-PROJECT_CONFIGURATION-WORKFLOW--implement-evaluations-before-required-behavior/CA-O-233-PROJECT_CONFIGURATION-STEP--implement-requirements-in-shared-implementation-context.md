---
atom_id: CA-O-233
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/caprmedio/Step//Requirement Implementation Step
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run.Agentic Step Execution Context
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan/Type: Plan'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
version: 9
updated_at: 2026-10-27 19:59:48 +0400
relations:
  depends_on:
  - CA-R-1527
tier: 3
---
# Summary

Implement requirements in shared implementation context

## Operation

Requirement Implementation Step **means** the Workflow node invoking **=1** Action, CA-O-019, **in** Integrated context under CA-R-1527.

- bind inputs from the selected P/Plan item **and** admitted work from CA-O-231, the same retained participating-session context, direct full `methods` rows **and** R/E/D, prepared tests from CA-O-232, baseline evidence from CA-O-094 **and** CA-O-234 **when** available, **and** the current owned work boundary. An optional legacy `method_projection` may accompany those rows but is not required.
- use the host's native session/subagent, file, **and** command capabilities; this binding has no MCP prerequisite. missing required context **or** capability returns a blocked invocation, **not** silent execution **in** another context.
- retain exact Action/Step Revisions, source bindings, actual effects, **and** returned results. pass the Action's result **to** the Workflow **without** independently copying its behavior.

Retain the participating session and complete source-bound work/evidence across these Integrated invocations. A replacement requires a complete retained handoff and fresh admission; conversational memory alone is not evidence.

- retain shared request/Plan, current source-bound R/M/E/D, exact candidate and actual prior results, findings, and remaining retry/resource state. This explicit Integrated binding does not alter the context of standalone review Steps.

## Details
