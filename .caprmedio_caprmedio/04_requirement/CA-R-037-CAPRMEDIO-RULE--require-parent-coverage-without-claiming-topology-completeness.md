---
subject_scopes:
- requirement-topology
version: 28
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-1430
cce_version: cce_1
cce_form: obligation
current_scope_unit: caprmedio
status: Active
atom_id: CA-R-037
tier: 2
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Relations
role: Requirement
form: Rule
---
## Summary
Require parent coverage without claiming topology completeness

## Claim

**in** strict authority mode, **every** active tier-classified PRMEDO Atom **must** have **`>=1`** permitted active parent **unless** the applicable Type authority registers its Type as orphan-permitted.

a permitted parent is:

- the active Project Goal Atom for a Project-owned Tier 0 Atom;
- an applicable lower-global-tier Atom **in** the same structural scope, or a Tier 0 Requirement for a same-Scope Tier 0 Method, Evaluation, Delivery, or Operations Atom when the applicable typed relation admits it; **or**
- an Atom permitted by the global tier topology **in** an ancestor structural scope.

this parent-coverage condition is necessary but insufficient for authority-topology completeness **and** cannot establish Project Scope Contract completeness.
