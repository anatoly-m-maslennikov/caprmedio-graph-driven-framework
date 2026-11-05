---
atom_id: CA-R-025
ref_id: CA-R-025
container:
  scope_unit: CA-SU-00
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Tier
tier: 3
relations:
  child_of:
  - CA-R-024
status: Active
version: 16
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-025-CAPRMEDIO-RULE--preserve-higher-tier-authority-in-cross-tier-conflicts.md
    path: .caprmedio_caprmedio/04_requirement
subject_scopes:
- authority
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: caprmedio
---
## Summary
Preserve higher-tier authority in cross-tier conflicts

## Claim

### Prose Claim


a conflict between active Requirements at different global tiers **must** preserve the lower-numbered claim **and** reconcile the higher-numbered claim **without** changing the lower-numbered meaning.
