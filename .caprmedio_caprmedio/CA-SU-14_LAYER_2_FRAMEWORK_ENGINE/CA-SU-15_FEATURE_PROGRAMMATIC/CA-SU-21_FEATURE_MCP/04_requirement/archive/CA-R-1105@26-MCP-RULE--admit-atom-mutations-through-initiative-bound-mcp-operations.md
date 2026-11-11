---
atom_id: CA-R-1105
ref_id: CA-R-1105@26
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication
tier: 1
status: archived
version: 26
updated_at: 2026-11-11 14:29:18 +0400
carrier_destination:
  file:
    name: CA-R-1105@26-MCP-RULE--admit-atom-mutations-through-initiative-bound-mcp-operations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement/archive
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

Initiative-bound MCP admission and truthful transport of independently admitted Atom Actions.

## Claim

### Prose Claim

A local Project MCP request for one of the six Atom Lifecycle Tools invokes its Workflow on the bound runtime backend. The request names the operation and supplies its inputs. Create Draft creates a Draft. The backend returns only the operation Status after verifying success. On failure, report the error and any completed effects. Git integration is deferred for these six Tools.

For Initiative-bound Atom Tools, **every** CAPRMEDIO Markdown Atom mutation **must** enter through an authorized project-local MCP operation. MCP **must** identify the selected canonical Atom Tool, preserve the human-origin Initiative input **and** action request, **and** delegate **without** deciding the Atom operation's target set, preconditions, lifecycle meaning, mutation, recovery, **or** success state. The canonical Atom Tool owns those behaviors **and** seals one Initiative **and** stable action identity **before** its effect.

Search **and** read operations remain mutation-free. An Initiative-bound Tool for an atomic or bulk Atom operation **must** validate the current project frontier **and** **must** cause `COMMIT_TRIGGER` **to** receive durable intake acknowledgement **after** a successful mutation **and** **before** MCP reports success. MCP **may** return that Tool outcome but **must not** turn a failed, partial, blocked, **or** unacknowledged outcome into success.

An Atom Action selects exactly one explicit Atom target and binds its expected Revision or source digest before that Action's effect. A Workflow with several Atom targets executes independent admitted Actions, stops at its first failed Action, retains completed Actions and leaves the remainder untouched. MCP **must** preserve those actual per-Action outcomes and **must not** advertise a cross-Atom all-or-nothing effect or overwrite concurrent work. Resume and retry policy for that sequence is deferred; each Action's existing source, permission, preview and storage-effect safeguards remain required.

Multiple MCP service instances **and** sessions **may** operate concurrently. Every mutation of an existing Atom **must** carry its expected Atom Revision **or** carrier digest; a mismatch **must** reject that target rather than overwrite concurrent work. Promotion is an ordinary delegated Atom mutation that validates its pre-promotion input **and** seals a new action; it **must not** require the future Git **or** Journal reconciliation of that same new action. A direct **or** **otherwise** unowned Atom write outside this gateway is unadmitted **and** cannot be represented as a normal governed MCP mutation.

