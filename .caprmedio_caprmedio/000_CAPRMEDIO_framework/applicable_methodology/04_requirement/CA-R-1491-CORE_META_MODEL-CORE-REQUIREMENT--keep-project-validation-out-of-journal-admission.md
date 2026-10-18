---
subjects:
  governs: "Entity/Continuant/Node/History/Journal"
  depends_on:
    ["Entity/Continuant/Node/History/Journal.Record", "Entity/Carrier", "Entity/Continuant/Node/Atom", "Entity/Continuant/Node/Project", "Entity/Continuant/Node/Projection/Type: Applicable Methodology", "Entity/Continuant/Node/Atom/Content Role: Evaluation"]
version: 11
updated_at: "2026-10-18 03:33:35 +0400"
relations:
  child_of:
    - CA-R-1490
  relates_to:
    - CA-R-1745
atom_id: "CA-R-1491"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1491-CORE_META_MODEL-CORE-REQUIREMENT--keep-project-validation-out-of-journal-admission.md
  source_atom_id: CA-R-1491
  source_atom_revision: 11
  source_sha256: 6fa1acc14e8b953f2a4ce85a1ab3f500698f63b96921fc03d2060aa80b85c9e1
  original_relations_sha256: 9924b6ff7c6932dfffb0d4989dcbbd73519db955518463bb61a9ef1a4be43d59
---
# Summary

Keep Project validation out of Journal admission

## Scope

Plain append/read of observable Project events.

## Claim

the Journal **must** preserve observable Project events independently of whether the recorded Project state conforms **to** Applicable Methodology.

- append **and** read supplied observations **without** a Journal validation layer, required historical chain, canonical receipt, digest check, deduplication, retry **or** recovery gate. prior records are **not** prerequisites for a new entry.
- Atom-ID grammar, filenames, placement, Properties, Relations **and** lifecycle conformance belong **to** separate Evaluations **and** their Tools; none is a Journal append/read gate.
- preserve supplied observed values **without** silently repairing them **or** inventing an earlier event, baseline, Actor, session, time **or** result. log entries do **not** prove Project conformance **or** correct execution.
- later Project changes **must not** prevent recording historical observations **or** rebind them **to** current state.
- each explicit append records its supplied data, including repeated data; do **not** suppress it as a duplicate **or** overwrite existing entries.
- retain ordinary authorized Project/filesystem access **and** truthful I/O failure. the Journal grants no permission **to** mutate a source, perform a Git effect **or** bypass access controls. existing records remain readable as recorded **without** migration.

## Details
