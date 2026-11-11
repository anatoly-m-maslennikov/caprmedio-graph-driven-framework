---
atom_id: CA-R-024
ref_id: CA-R-024@30-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Concern)
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
  - CAPRMEDIO_MODEL <+ Atom
tier: 2
status: Draft
version: 30
updated_at: "2026-11-11 18:12:55 +0400"
carrier_destination:
  file:
    name: CA-R-024@30-draft-CORE_META_MODEL-RULE--govern-requirement-conflicts-by-tier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
cce_version: cce_1
cce_form: obligation
current_scope_unit: CORE_META_MODEL
---
## Summary
Govern Requirement conflicts by tier

## Claim

### Prose Claim


CAPRMEDIO **must** resolve conflicts among active Requirements other than Requirements expressing Project-wide foundational invariants through explicit rules determined by their applicability tiers rather than presentation order, Concern priority, **or** implicit interpretation.

## Details

Draft review: Before promotion, reconcile the role of tier with CA-R-2149: numeric tier alone does not select a conflict winner. Retain the Operator's decision authority.
