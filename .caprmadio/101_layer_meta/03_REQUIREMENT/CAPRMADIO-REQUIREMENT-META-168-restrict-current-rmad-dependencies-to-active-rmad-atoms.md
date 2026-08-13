---
subject_scopes:
  - lifecycle-traceability
tier: standard
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-053-separate-active-authority-from-preserved-history
    - CAPRMADIO-REQUIREMENT-META-145-let-the-dependent-atom-own-the-relation
    - CAPRMADIO-REQUIREMENT-META-159-define-atom-admission-and-lifecycle
---

# Restrict current RMAD dependencies to active RMAD Atoms

Every current semantic dependency owned by an active Requirement, Method,
Assurance, or Delivery Atom must target either an active RMAD Atom or a
Concern, Analysis, Plan, Implementation, or Ops Atom. CAP/IO targets remain
eligible until their role-specific lifecycle establishes a narrower rule.

Historical lineage relations, including `replacement_of`, are not current
semantic dependencies and may target archived RMAD Atoms.
