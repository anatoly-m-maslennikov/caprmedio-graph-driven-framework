---
subjects:
  governs: "Entity/Node/Continuant/Project.Framework Settings.Interaction.Reporting Mode.Mandatory Information"
  depends_on:
    ["Entity/Node/Continuant/Project.Framework Settings.Interaction.Reporting Mode", "Entity/Node/Continuant/Actor/Type: Operator"]
version: 11
updated_at: "2026-10-19 15:53:05 +0400"
relations:
  child_of:
    - "CA-R-1402"
  relates_to:
    - "CA-R-1420"
atom_id: "CA-R-1440"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1440-CORE_META_MODEL-GENERAL--preserve-mandatory-information-in-every-reporting-mode.md
  source_atom_id: CA-R-1440
  source_atom_revision: 11
  source_sha256: 7461c1d1d83125ce9cebcb8cbc064a668ba19f0acc28540119713570640b1044
  original_relations_sha256: 0340864db7abe404688a97498db8cf00b4ab1863cf1571a0cc596bb09548562e
---
# Summary

Preserve mandatory information in every reporting mode

## Scope

mandatory information reported by **every** interaction reporting mode.

## Claim

**every** interaction reporting mode **must** report the following mandatory information:

- blockers **and** failed operations;
- ambiguity that requires Operator input;
- permission **or** approval requests;
- safety-critical information;
- material deviations from the requested outcome.

## Details
