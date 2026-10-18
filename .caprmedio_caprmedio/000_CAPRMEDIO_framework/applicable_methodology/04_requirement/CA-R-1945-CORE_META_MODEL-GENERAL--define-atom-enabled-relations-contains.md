---
atom_id: CA-R-1945
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
global_tier: 10
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Atom.Enabled Relations.Contains"
relations:
  child_of:
  - CA-R-1174
version: 2
updated_at: "2026-10-18 03:34:01 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1945-CORE_META_MODEL-GENERAL--define-atom-enabled-relations-contains.md
  source_atom_id: CA-R-1945
  source_atom_revision: 2
  source_sha256: 0543f0895a93979b96cf197cb8df0fa2d3516c6d6ee3f3f29aec0fe32b4ae40f
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
# Summary

Define Atom.Enabled Relations.Contains

## Scope

Containment capability of Atom kinds, qualified by Content Role and Type.

## Claim

Atom.Enabled Relations.Contains **means** whether an Atom kind **may** contain other Atoms through `CONTAINS`. Its allowed values **are** (False, True), with default False. The applicable Content Role or Type **may** enable this capability. It belongs to the kind, **not** to a required Boolean field on every Atom instance. True permits containment; it does **not** require children.

## Details

The Operator approved the default-False kind capability and containment for Plan and Workflow kinds. Their particular enabling rules remain separate. Container capability does not replace Owning Scope Unit or Target Scope Unit references, including Goal and Demand targets.

Existing evidence: CA-R-1368 defines `CONTAINS` and its derived inverse `IS_CONTAINED_BY`, but not this capability or its default. CA-R-1378, CA-R-1379 and CA-R-1265 still describe the old non-Atom collection model; their conflicting content needs the later content pass. This draft neither retires those sources nor resumes the deferred construction graph.
