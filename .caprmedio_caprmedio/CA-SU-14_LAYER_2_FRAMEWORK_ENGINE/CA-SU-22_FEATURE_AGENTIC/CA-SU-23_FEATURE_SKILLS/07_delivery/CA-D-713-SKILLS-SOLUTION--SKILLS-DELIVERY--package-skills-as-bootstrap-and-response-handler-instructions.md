---
identity:
  atom_id: CA-D-713
  ref_id: CA-D-713
context:
  container:
    scope_unit: CA-SU-23
  role: Delivery
  form: Solution
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Carrier
    dependencies:
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Operations)/Action
    - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Entry
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Role in RMED)
    - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Interaction
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Operations)/Step
    - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
      <+ Communication <+ API
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Operations)/Workflow
  tier: 4
state:
  status: Active
  version: 1
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-D-713-SKILLS-SOLUTION--SKILLS-DELIVERY--package-skills-as-bootstrap-and-response-handler-instructions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-23_FEATURE_SKILLS/07_delivery
author: Anatoly Maslennikov
relations:
  delivery_for:
  - CA-R-1626
cce_version: cce_1
cce_form: serialization
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
---
## Summary
Package Skills as bootstrap and response-handler instructions

## Claim

### Prose Claim

a delivered Skill package **must** carry its discovery metadata **and** very thin bootstrap/response-handler body separately from task-specific Action instructions supplied through MCP.

- place canonical Skill packages at the SKILLS Delivery binding. identify the entry purpose **and** **any** registered direct-route reference **in** the host-admitted metadata representation.
- carry the standing instruction body **and** **only** references, templates, **or** assets necessary for bootstrap **and** generic response handling. references identify the canonical shared runtime **and** capabilities rather than copy executable contents.
- do **not** bundle deterministic scripts, executable helpers, copies of the MODEL//CAPRMEDIO <+ Atom/(.Header.Role in RMED), independent Workflow transitions, **or** a task-prompt library as Skill-owned procedure. Prompt Implementation remains separately owned; the current Step invocation remains delivered through MCP.
- keep discovery metadata, standing body, **and** optional bootstrap resources distinguishable so the host can load the applicable part. portable content is shared; host-specific encoding follows its declared host boundary rather than assuming **every** host has identical fields **or** loading behavior.

this Delivery specifies the package Carrier, **not** a new Workflow, permission policy, response schema, installer, Hook, host-support promise, **or** PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ API implementation.
