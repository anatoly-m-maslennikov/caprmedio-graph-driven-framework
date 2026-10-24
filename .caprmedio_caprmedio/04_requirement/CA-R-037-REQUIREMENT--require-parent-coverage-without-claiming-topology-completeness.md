---
subject_scopes:
- requirement-topology
version: 20
updated_at: 2026-10-24 04:48:21 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-029
cce_version: cce_1
cce_form: obligation
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: caprmedio
status: Active
atom_id: CA-R-037
type: Rule
tier: 2
subjects:
  governs: Subject/Graph/Rule
  depends_on: []
---
# Require parent coverage without claiming topology completeness

**in** strict authority mode, **every** active tier-classified PRMEDO Atom **must** have **`>=1`** permitted active parent **unless** the applicable Type authority registers its Type as orphan-permitted.

a permitted parent is:

- the active Project Goal Atom for a Project Principle;
- an applicable lower-global-tier Atom **in** the same structural scope; **or**
- an Atom permitted by the global tier topology **in** an ancestor structural scope.

this parent-coverage condition is necessary but insufficient for authority-topology completeness **and** cannot establish Principle-set completeness.
