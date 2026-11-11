---
atom_id: CA-R-030
ref_id: CA-R-030@28-draft
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
  - CA-R-833
status: Draft
version: 28
updated_at: "2026-11-11 18:12:55 +0400"
carrier_destination:
  file:
    name: CA-R-030@28-draft-CORE_META_MODEL-RULE--require-complete-authority-topology-in-strict-mode.md
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
Require complete authority topology in strict mode

## Claim

### Prose Claim


a scope **in** strict authority mode **must** maintain a complete, conflict-free active PRMEDO authority topology with these constraints:

- **every** local Tier 0 Atom **and** Core other than a Project Axiom has **`>=1`** permitted active child **unless** the applicable Type authority registers its Type as terminal;
- the normative-authority subgraph is acyclic under CA-R-833;
- **every** edge follows the tier **and** structural-direction rules applicable **to** its graph kind **and** Relation Kind; **and**
- an Active RMED Atom's direct relation **to** an RMED Atom requires an Active target under CAPRMEDIO-GOV-REQU-767. other endpoint classes retain the Status constraints of their own governing Relation authority.

the authority-subgraph acyclicity constraint does **not** impose acyclicity on **every** other graph, including Workflow control flow.

A Project Axiom **may** have no applicable Method or other active child. Absence of a child alone **must not** fail strict topology for that Axiom.
