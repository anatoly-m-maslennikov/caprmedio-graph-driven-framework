---
atom_id: CA-R-1105
ref_id: CA-R-1105@28
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication
tier: 1
status: archived
version: 28
updated_at: '2026-11-12T01:59:14.433341+00:00'
carrier_destination:
  file:
    name: CA-R-1105@28-MCP-RULE--admit-atom-mutations-through-initiative-bound-mcp-operations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement/099_archived
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
---
## Summary

Admit Atom mutations through Initiative-bound MCP operations

## Claim scope

Project MCP requests for the six Atom Lifecycle Tools and separately Initiative-bound Atom Tools.

## Claim

### Prose Claim

A local MCP call to one of the six Atom Lifecycle Tools runs that operation on the bound Project. The call itself is the request. There is no separate apply or authorization step. Create Draft creates a Draft. A successful single-Atom response carries only the operation Status. Before any effect, missing or invalid input returns the fields to correct. The caller may provide only the requested corrections. A failure reports the error and any completed effects. Once an operation has changed a carrier, a failure ends the call. It does not retry, repair, or wait for corrected input. Git integration is deferred for these Tools.

Archive and Promote Draft each also accept an ordered list of exact targets. Each target uses the same one-Atom operation. Stop at the first failed target. Return the actual target results, completed effects, and remaining targets. An independent batch leaves the remaining targets untouched.

Moving a Current Epic from Backlog to Active also sets all recursively contained Current Tasks to Active. A Draft child does not block the change and stays a Draft. Updating only an Epic’s content works when it contains children and preserves their content and Status.

For Initiative-bound Atom Tools, **every** CAPRMEDIO Markdown Atom mutation **must** enter through an authorized project-local MCP operation. MCP **must** identify the selected canonical Atom Tool, preserve the human-origin Initiative input **and** action request, **and** delegate **without** deciding the Atom operation's target set, preconditions, lifecycle meaning, mutation, recovery, **or** success state. The canonical Atom Tool owns those behaviors **and** seals one Initiative **and** stable action identity **before** its effect.

Search **and** read operations remain mutation-free. An Initiative-bound Tool for an atomic or bulk Atom operation **must** validate the current project frontier **and** **must** cause `COMMIT_TRIGGER` **to** receive durable intake acknowledgement **after** a successful mutation **and** **before** MCP reports success. MCP **may** return that Tool outcome but **must not** turn a failed, partial, blocked, **or** unacknowledged outcome into success.

An Atom Action selects exactly one explicit Atom target and binds its expected Revision or source digest before that Action's effect. A Workflow with several Atom targets executes independent admitted Actions, stops at its first failed Action, retains completed Actions and leaves the remainder untouched. MCP **must** preserve those actual per-Action outcomes and **must not** advertise a cross-Atom all-or-nothing effect or overwrite concurrent work. Resume and retry policy for that sequence is deferred; each Action's existing source, permission, preview and storage-effect safeguards remain required.

Multiple MCP service instances **and** sessions **may** operate concurrently. Every mutation of an existing Atom **must** carry its expected Atom Revision **or** carrier digest; a mismatch **must** reject that target rather than overwrite concurrent work. Promotion through an Initiative-bound Tool validates its pre-promotion input and seals a new action. It does not wait for future Git or Journal reconciliation of that action. A direct **or** **otherwise** unowned Atom write outside this gateway is unadmitted **and** cannot be represented as a normal governed MCP mutation.

