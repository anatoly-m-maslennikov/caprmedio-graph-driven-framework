---
identity:
  id: CA-P-2737
  ref_id: CA-P-2737@2
context:
  container:
    atom: CA-P-2715
  role: Plan
  form: Plan
  label: Task
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Aspect/Engineering/Traceability
  tier: 4
relations:
  IS_BLOCKED_BY:
  - CA-P-2727
state:
  status: Archived
  version: 2
  updated_at: 2026-11-08 19:15:36 +0400
destination:
  file:
    name: 21-CA-P-2737@2-TASK--map-adopted-atoms-to-implementation-modules.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/archived
author: Anatoly Maslennikov
---

## Summary

Map adopted Atoms to implementation modules

## Objective

Try to map the accepted in-scope Atom IDs and versions to the modules that implement them. Record gaps honestly instead of assigning a module by name alone.

## Subtasks

- [ ] Review the selected scope-local Atom batch through query_run and identify implementation evidence. (ETA: 15–20 min per batch.)
- [ ] Build a thin Atom ID@Version | Module | Status map; allow one Atom to map to several modules and one module to implement several Atoms. Distinguish implemented behavior from imports, calls and test coverage. (ETA: 15–20 min per batch.)
- [ ] Compare the mapping with module comments, I / Code Synopsis and the spec/code difference review; record unimplemented Atoms, unbound code and stale pins. (ETA: 15–20 min per batch.)
- [ ] Update the map after accepted code/spec corrections and verify the claims against code and tests. (ETA: 15–20 min per batch.)

## Working procedure

Review and fix the next work unit first. If confidence is below 90%, re-read Operator input; if still uncertain, ask. One Scope Unit per worker. Main judgments use GPT-6.1 Sol High. Keep the Task's small P / Work Report under the adopted model.

## Acceptance

Every attempted mapping has evidence or an explicit unmapped/uncertain status. The result does not claim that a call, imported dependency or test implements an Atom. Module comments use only implemented Atom IDs with versions, such as CA-R-123@2. The map is thin execution evidence, not a second specification.
