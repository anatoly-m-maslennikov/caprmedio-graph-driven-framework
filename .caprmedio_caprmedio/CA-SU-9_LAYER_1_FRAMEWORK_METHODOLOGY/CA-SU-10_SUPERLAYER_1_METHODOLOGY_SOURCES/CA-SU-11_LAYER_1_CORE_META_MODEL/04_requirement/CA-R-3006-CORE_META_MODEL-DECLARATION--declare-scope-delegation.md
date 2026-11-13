---
atom_id: CA-R-3006
ref_id: CA-R-3006
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Form := Scope Delegation)
tier: 3
status: active
version: 12
updated_at: '2026-11-12T19:22:19.544711+00:00'
carrier_destination:
  file:
    name: CA-R-3006-CORE_META_MODEL-DECLARATION--declare-scope-delegation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Scope Delegation

## Claim

### Prose Claim

Scope Delegation is one generic Form for an external Atom whose Role is in RMEDO. Its active Subject identifies exactly one receiving non-Project Scope Unit within the Project. Its Container is that unit’s one direct structural Parent. Project may contain delegations for its children but is never their receiver. The direct Parent authors the structural declaration and assigns a contribution to the receiving unit; it retains its broader scope and accountability.

The Scope Unit Declaration states the structural facts for FORMAL_MODEL_ENGINE.

During the Python migration, each Scope Unit listed below may have one separate Scope Unit Declaration alongside its existing Scope Delegation. The Declaration states the unit's Name, stable ID, ordering state, order number when ordered, direct containing Scope Unit, and structural level. Label remains optional. The existing Delegation retains its responsibilities and local admissions. While both Claims state a structural fact, their values agree.

- AGENTIC (CA-SU-22)
- APPS (CA-SU-20)
- CODEX_EXTENSION (CA-SU-48)
- CODEX_HOOK (CA-SU-49)
- CONNECTOR_TOOLS (CA-SU-17)
- CORE_META_MODEL (CA-SU-11)
- FRAMEWORK_DELIVERY (CA-SU-27)
- FRAMEWORK_ENGINE (CA-SU-14)
- FRAMEWORK_METHODOLOGY (CA-SU-9)
- MCP (CA-SU-21)
- PROGRAMMATIC (CA-SU-15)
- PROJECT_TOOLS (CA-SU-19)
- PROMPTS (CA-SU-24)
- SKILLS (CA-SU-23)
- TOOLS (CA-SU-16)
- TOOL_WORKFLOWS (CA-SU-18)
- WORKBENCH (CA-SU-43)
- WORKBENCH_BACKEND (CA-SU-45)
- WORKBENCH_FRONTEND (CA-SU-46)

For each other Scope Unit that uses a combined Scope Delegation, that Delegation remains its structural declaration and states the same structural facts except structural level.

Each concrete Scope Delegation Claim lists admitted local Role/Form pairs and typed HAS_ACTIVE_SUBJECT target selections. Plan / Work Report is admitted as a supporting Atom for an already admitted Task. It has that Task’s Container and remains within the applicable Subject selections. Its Role/Form pair needs no separate local listing.

For other local Atoms, admission requires the Header.Container-derived IS_CONTAINED_BY target to be the receiving Scope Unit, the HAS_ACTIVE_SUBJECT target to be in a listed selection, and the Role/Form pair to be listed. Solution, Direct Policy and Approach Policy are RMEDO Forms and require explicit inclusion in the local whitelist. Decision is a MEDO Form.

### Formal Claim

```CFEL
# model
Atom.Header.Context.Form :: Scope Delegation;

# instances
FOR EACH $a[<Atom>, (.Header.Context.Form = Scope Delegation)]:
(
    $a.Header.Context.Role:: [in (Requirement, Method, Evaluation, Delivery, Operations)]{::1};
)
```
