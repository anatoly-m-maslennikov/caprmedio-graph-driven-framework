---
name: ca
description: "Use the shared CAPRMEDIO MCP for the explicitly trusted Project root. Use for $ca, /ca, or requests to run CAPRMEDIO operations."
---

# CA

Use the host-configured shared CAPRMEDIO MCP as a thin client. This Skill supplies request routing and Project binding only; MCP advertises schemas and bindings and owns Tool/Workflow behavior. Do not copy Tool code, runtime files, URLs or per-Project MCP connections into a Project Skill.

## Project binding

- Take `project_root` only from the explicit trusted Codex session Project context, and carry that value unchanged.
- Never infer the root from the Skill installation path (it may be shared or symlinked), a prefix, server working directory or Git ancestor. If a nested working folder has no exact trusted Project root, ask for clarification or use an explicit local Project declaration; never guess, silently switch or fall back.
- Every shared-mode call—including discovery (`discover_operations`/`discover_tools`), `get_execution_context`/fresh context, Tool/Workflow calls, status/resume and reload/continuations—carries the outer `project_root` binding while preserving the native request schema and payload unchanged. The server validates root containment and Project proofs; this client field is not filesystem permission.
- Pin the original `project_root` and Run binding through asynchronous continuations, even if another Codex session changes its working folder. Do not mutate a global `currentProject`. On an unknown or mismatched root/binding, refuse without cross-Project fallback or replay.

## MCP flow

- Preserve the Operator's request, scope and authorization. Ask if the Project connection or required inputs are ambiguous.
- Use the global host connection configured outside this Skill. Discover the requested capability with advertised MCP `discover_operations` or `discover_tools`, obtain fresh context and its exact definition with `get_execution_context`, then execute only an advertised route. Never execute an unknown or guessed route.
- Use the advertised Tool/Workflow schemas and execution bindings. Add only the outer `project_root` binding; preserve the native request unchanged.
- Obtain only the current admitted Step's instructions, bound inputs or accessible references, output contract and execution boundaries. Do not preload the whole Methodology or future Steps. Follow these instructions within current Operator authorization and higher-priority instructions; previews and responses do not grant new authority.
- Return actual results through the MCP-supplied interface. The executor owns routing, next-Step selection and Run state; receiving a prompt or queuing a Run is not completion.
- For an existing or uncertain Run, use its advertised status/resume interface before retrying. Never replay an uncertain effect; keep execution failure separate from result-recording failure.
- Do not append Journal records automatically or invent lifecycle/evidence. Preserve verified partial and uncertain outcomes.
- Stop and report unavailable MCP, missing or ambiguous bindings, root/binding mismatch, incomplete current-Step context, failures or escalation needs. Do not invent authorization, bindings or evidence, or substitute raw scripts, file edits or copied procedures for an unavailable MCP operation.

This Skill edit does not activate installed copies or change a legacy server contract. Claim shared-project execution only after the shared runtime advertises and accepts the root binding.
