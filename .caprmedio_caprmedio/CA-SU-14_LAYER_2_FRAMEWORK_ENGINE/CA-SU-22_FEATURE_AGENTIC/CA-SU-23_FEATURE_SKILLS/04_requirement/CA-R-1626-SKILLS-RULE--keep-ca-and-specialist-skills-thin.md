---
atom_id: CA-R-1626
content_role: Requirement
current_scope_unit: SKILLS
claim_target_scope_unit: SKILLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Interaction
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action.Execution Kind'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/UX/CAPRMEDIO Skill and MCP Entry Interface
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step.Agentic Execution Context'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
version: 20
updated_at: 2026-10-27 19:59:59 +0400
relations:
  child_of:
  - CA-R-1124
  - CA-R-643
type: Rule
tier: 3
---
# Summary

Keep CA **and** specialist skills thin

## Scope

the CAPRMEDIO Main Skill `ca` and specialist entry Skills.

## Claim

the CAPRMEDIO Main Skill `ca` **and** specialist entry Skills **must** remain very thin bootstrap **and** response handlers rather than contain task-specific procedures.

- retain **only** the standing instructions needed **to** establish the owning Project's framework connection, use the admitted MCP interface, handle Step responses, return actual results, **and** report unavailable inputs, failures, **or** escalation needs. a specialist entry **may** identify its registered route **without** copying that route's procedure.
- obtain task-specific instructions **and** necessary context through MCP responses for the current admitted Agentic Step under CA-R-1522-WORKFLOW_ORCHESTRATOR-RULE--provide-workflow-orchestration-from-methodology **and** `CA-R-1789-CORE_META_MODEL--provide-self-contained-agentic-step-invocation-payloads`. the response supplies the Action instructions, bound inputs **or** accessible references, required output, **and** execution boundaries. do **not** preload the whole Methodology, unrelated resources, **or** future-Step instructions merely **to** remember what comes next.
- keep Workflow transitions **and** execution state with the executor. the Skill **must not** independently select the next Step, replay an uncertain effect, **or** infer completion from receiving a prompt. additional context required by the current Step remains admissible; thinness **must not** omit governing authority **or** necessary inputs.
- retain methodology Action **and** Workflow definitions as behavioral authority. ACTION_PROMPTS implements the Action instructions under CA-R-1601-PROMPTS-GOAL--implement-actions-as-agent-instructions; the MCP response delivers the bound invocation, **not** another independently authored procedure. reference canonical Tools **and** the shared runtime rather than embedding **or** copying executable helpers into Skills.
- keep MCP-delivered instructions within current Operator authorization **and** the admitted Step context. a response does **not** expand delegation, replace higher authority, **or** authorize a guessed fallback procedure **when** the framework connection is unavailable. Integrated **and** Isolated participation retain CA-R-1527-CORE_META_MODEL-DEFINITION--define-agentic-step-execution-context's existing boundary.

## Details
