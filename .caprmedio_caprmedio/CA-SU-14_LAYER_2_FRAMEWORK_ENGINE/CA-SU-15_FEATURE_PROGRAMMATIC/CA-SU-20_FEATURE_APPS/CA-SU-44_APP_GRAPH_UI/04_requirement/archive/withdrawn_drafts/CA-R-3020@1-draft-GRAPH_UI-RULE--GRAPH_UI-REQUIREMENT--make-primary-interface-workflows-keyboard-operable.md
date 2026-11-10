---
identity:
  atom_id: CA-R-3020
  ref_id: CA-R-3020@1-draft
context:
  container:
    scope_unit: CA-SU-44
  role: Requirement
  form: Rule
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Interaction/Accessibility
    dependencies:
    - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
    - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
    - Workflow
  tier: 3
state:
  status: Draft
  version: 1
  updated_at: 2026-11-10 12:02:33 +0400
destination:
  file:
    name: CA-R-3020@1-draft-GRAPH_UI-RULE--GRAPH_UI-REQUIREMENT--make-primary-interface-workflows-keyboard-operable.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-44_APP_GRAPH_UI/04_requirement/draft
author: Anatoly Maslennikov
relations:
  child_of:
  - CA-R-1076
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
---
## Summary
Make primary interface workflows keyboard-operable

## Claim

### Prose Claim

GRAPH_UI **must** make **every** primary Operator workflow usable by keyboard **without** requiring a pointer-only interaction.

the supported interaction boundary includes visible focus, understandable control names **and** roles, predictable traversal, perceivable status changes, **and** reachable error recovery. this Requirement governs the optional GRAPH_UI; it does **not** make that interface a prerequisite for WORKBENCH, Tools, **or** MCP.
