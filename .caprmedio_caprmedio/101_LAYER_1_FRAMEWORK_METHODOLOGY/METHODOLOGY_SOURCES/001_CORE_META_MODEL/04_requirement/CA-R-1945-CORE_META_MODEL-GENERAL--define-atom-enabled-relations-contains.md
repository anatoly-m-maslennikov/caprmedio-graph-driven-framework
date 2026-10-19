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
  governs: "Entity/Node/Continuant/Atom.Enabled Relations.Contains"
relations:
  child_of:
  - CA-R-1174
version: 4
updated_at: "2026-10-20 00:11:28 +0400"
---
# Summary

Define Atom.Enabled Relations.Contains

## Scope

Containment capability of Atom kinds, qualified by Content Role and Type.

## Claim

Atom.Enabled Relations.Contains **means** whether an Atom kind **may** contain other Atoms through `CONTAINS`. Its allowed values **are** (False, True), with default False. The applicable Content Role or Type **may** enable this capability. It belongs to the kind, **not** to a required Boolean field on every Atom instance. True permits containment; it does **not** require children.

## Details

The Operator approved the default-False kind capability and containment for Plan and Workflow kinds. Their particular enabling rules remain separate. Container capability does not replace Owning Scope Unit or Target Scope Unit references, including Goal and Demand targets.

CA-R-1368 defines direct IS_CONTAINED_BY and its derived inverse CONTAINS; this capability describes which Atom kinds may be the containing endpoint, not another authored inverse. CA-R-1378, CA-R-1379 and CA-R-1265 still describe the old non-Atom collection model; their conflicting content needs the later content pass. This alignment neither retires those sources nor resumes the deferred construction graph.
