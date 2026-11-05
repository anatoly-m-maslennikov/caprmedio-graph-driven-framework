---
atom_id: CA-R-870
ref_id: CA-R-870
container:
  scope_unit: CA-SU-18
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Tier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Version Number
tier: 3
status: Active
version: 28
updated_at: 2026-10-27 20:00:12 +0400
carrier_destination:
  file:
    name: CA-R-870-TOOL_WORKFLOWS-RULE--upgrade-active-atom-authority.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-18_FEATURE_TOOL_WORKFLOWS/04_requirement
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
cce_version: cce_1
cce_form: obligation
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
---
# Summary

Upgrade active Atom authority

## Scope

Independently admitted upgrades of active Atom authority under the applicable Tier and Scope Unit rules.

## Claim

the `ATOM_UPGRADE` Tool is the canonical Doer for upgrading active CAPRMEDIO Markdown Atoms **to** an explicit operator-supplied enabled target Tier of `core` **or** `standard` that is higher than the source Tier. upgrade is neither archive nor promotion: it preserves the stable Atom ID **and** **may** keep the current Scope Unit **or** move the Atom **only** **to** an explicitly named ancestor Scope Unit. the Tool **must** derive the target authority location **and** filename scope segment **when** the Scope Unit changes, advance revision metadata, **and** reject missing, disabled, non-higher, **or** other invalid target Tiers, non-active Atoms, non-ancestor Scope Units, identity **or** destination collisions, **and** partial operations. each Action upgrades **`=1`** explicit Atom target with its expected Revision or digest. A several-Atom Workflow stops at its first failed Action, retains completed upgrades and leaves the remaining targets untouched, while preserving each Action's own preconditions and storage-effect safeguards. it **must** default **to** a mutation-free dry run **and** accept `--apply` **only** through an authorized project-local MCP delegation with a sealed Initiative action envelope.

## Details
