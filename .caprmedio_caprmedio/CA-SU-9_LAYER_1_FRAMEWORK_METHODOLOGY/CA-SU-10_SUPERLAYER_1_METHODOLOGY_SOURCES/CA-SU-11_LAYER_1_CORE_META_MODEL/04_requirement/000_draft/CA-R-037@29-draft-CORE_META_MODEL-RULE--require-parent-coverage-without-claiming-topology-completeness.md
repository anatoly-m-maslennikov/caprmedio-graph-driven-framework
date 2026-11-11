---
atom_id: CA-R-037
ref_id: CA-R-037@29-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Relations
tier: 2
relations:
  child_of:
  - CA-R-1430
status: Draft
version: 29
updated_at: "2026-11-11 18:12:55 +0400"
carrier_destination:
  file:
    name: CA-R-037@29-draft-CORE_META_MODEL-RULE--require-parent-coverage-without-claiming-topology-completeness.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
subject_scopes:
- requirement-topology
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
cce_version: cce_1
cce_form: obligation
current_scope_unit: CORE_META_MODEL
---
## Summary
Require parent coverage without claiming topology completeness

## Claim

### Prose Claim


**in** strict authority mode, **every** active tier-classified PRMEDO Atom **must** have **`>=1`** permitted active parent **unless** it is a Project Axiom **or** the applicable Type authority registers its Type as orphan-permitted. A Project Axiom is independent of the Project Goal **and** **must not** name it as a parent.

a permitted parent is:

- an applicable lower-global-tier Atom **in** the same structural scope, or a Tier 0 Requirement for a same-Scope Tier 0 Method, Evaluation, Delivery, or Operations Atom when the applicable typed relation admits it; **or**
- an Atom permitted by the global tier topology **in** an ancestor structural scope.

this parent-coverage condition is necessary but insufficient for authority-topology completeness **and** cannot establish Project Scope Contract completeness.
