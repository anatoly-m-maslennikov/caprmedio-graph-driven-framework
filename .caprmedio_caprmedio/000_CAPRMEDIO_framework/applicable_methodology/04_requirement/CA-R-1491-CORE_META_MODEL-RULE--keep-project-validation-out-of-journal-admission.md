---
subjects:
  active: Journal
  passive:
  - Entity/Object/Continuant/History/Journal > Event Record
  - Carrier
  - Atom
  - Project
  - 'Entity/Object/Continuant/Projection/Type: Applicable Methodology'
  - Atom/(.Role := Evaluation)
version: 29
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2448
atom_id: CA-R-1491
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1491-CORE_META_MODEL-RULE--keep-project-validation-out-of-journal-admission.md
  source_atom_id: CA-R-1491
  source_atom_revision: 29
  source_sha256: b8a3b5cf96971ae59f6c19877c75241cf82ecd2004bd985c9b6310d4b95cc6a2
  original_relations_sha256: 1c8dbdb6ec99acae043d53724c2c907d16b11cbb375710999addae41b4be44c8
---
## Summary

Keep Project validation out of Journal admission

## Claim scope

Plain append/read of observable Project events.

## Claim

the Journal **must** preserve observable Project events independently of whether the recorded Project state conforms **to** Applicable Methodology.

- append **and** read supplied observations **without** a Journal validation layer, required historical chain, canonical receipt, digest check, deduplication, retry **or** recovery gate. prior records are **not** prerequisites for a new entry.
- Atom-ID grammar, filenames, placement, Properties, Relations **and** lifecycle conformance belong **to** separate Evaluations **and** their Tools; none is a Journal append/read gate.
- preserve supplied observed values **without** silently repairing them **or** inventing an earlier event, baseline, Actor, session, time **or** result. log entries do **not** prove Project conformance **or** correct execution.
- later Project changes **must not** prevent recording historical observations **or** rebind them **to** current state.
- each explicit append records its supplied data, including repeated data; do **not** suppress it as a duplicate **or** overwrite existing entries.
- retain ordinary authorized Project/filesystem access **and** truthful I/O failure. the Journal grants no permission **to** mutate a source, perform a Git effect **or** bypass access controls. existing records remain readable as recorded **without** migration.
