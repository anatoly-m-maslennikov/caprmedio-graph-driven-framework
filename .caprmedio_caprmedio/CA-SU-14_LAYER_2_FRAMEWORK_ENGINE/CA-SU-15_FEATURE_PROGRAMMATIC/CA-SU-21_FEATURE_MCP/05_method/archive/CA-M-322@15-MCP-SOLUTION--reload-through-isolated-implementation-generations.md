---
atom_id: CA-M-322
ref_id: CA-M-322@15
container:
  scope_unit: CA-SU-21
role: Method
form: Solution
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
    <+ Execution Control
  dependencies:
  - MODEL//CAPRMEDIO <+ Package/Project Package
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution
    Control <+ Recovery
  - MODEL//CAPRMEDIO <+ Actor/Operator
  - MODEL//CAPRMEDIO <+ Project
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Operations)/Workflow
  - MODEL//CAPRMEDIO <+ Atom
tier: 3
status: Archived
version: 15
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-M-322@15-MCP-SOLUTION--reload-through-isolated-implementation-generations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method/archive
current_scope_unit: MCP
author: Anatoly Maslennikov
---

## Summary

Reload through isolated implementation generations

## Claim

### Prose Claim

MCP hot reload is optional and disabled by default. Default startup serves tool implementations in the MCP process, without an implementation child. Apply code changes with a normal server/container restart. Only explicit opt-in enables isolated implementation generations and their existing validated switch behavior.

## Details

### Isolated implementation generations

These rules apply only when hot reload is explicitly enabled. Disabled mode has no generation to replace/drain, preserves Project boundary, transport protections, callable tools, and does not advertise working reload.

1. Keep stdio gateway, protocol session, reload control, and fixed Project binding stable.
2. Load candidate code/dependencies in a separate local implementation process; do not mutate live modules with importlib.reload.
3. Initialize the candidate without Workflows, workers, or source mutation; obtain complete Tool contracts and validate names, schemas, and fixed Project binding.
4. Switch new dispatch only after validation succeeds; preserve the old generation for admitted calls.
5. Drain retired generations after admitted calls finish; expose bounded drain failure rather than silently terminating uncertain effects.
6. On preparation failure discard candidate and keep current generation. If a published generation later fails, report affected calls honestly; never automatically replay a mutating call.
7. Serialize reload requests, suppress duplicate request IDs, and treat an unchanged implementation frontier as a no-op.
