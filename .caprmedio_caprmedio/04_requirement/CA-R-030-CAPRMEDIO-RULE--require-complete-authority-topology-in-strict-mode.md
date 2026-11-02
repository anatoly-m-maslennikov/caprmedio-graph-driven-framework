---
subject_scopes:
- requirement-topology
version: 27
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-1430
  - CA-R-833
cce_version: cce_1
cce_form: obligation
current_scope_unit: caprmedio
status: Active
atom_id: CA-R-030
tier: 2
subjects:
  active: Atom.Relations
role: Requirement
form: Rule
---
## Summary
Require complete authority topology in strict mode

## Claim

a scope **in** strict authority mode **must** maintain a complete, conflict-free active PRMEDO authority topology with these constraints:

- **every** local Tier 0 Atom **and** Core has **`>=1`** permitted active child **unless** the applicable Type authority registers its Type as terminal;
- the normative-authority subgraph is acyclic under CA-R-833;
- **every** edge follows the tier **and** structural-direction rules applicable **to** its graph kind **and** Relation Kind; **and**
- an Active RMED Atom's direct relation **to** an RMED Atom requires an Active target under CAPRMEDIO-GOV-REQU-767. other endpoint classes retain the Status constraints of their own governing Relation authority.

the authority-subgraph acyclicity constraint does **not** impose acyclicity on **every** other graph, including Workflow control flow.
