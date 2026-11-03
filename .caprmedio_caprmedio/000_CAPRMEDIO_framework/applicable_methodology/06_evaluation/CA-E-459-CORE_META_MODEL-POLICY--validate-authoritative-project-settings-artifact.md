---
subjects:
  active: Project.Settings
  passive:
  - Project.Settings.Name
  - Project.Settings.Prefix
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - Scope Unit
version: 39
updated_at: 2026-11-02 19:46:47 +0400
relations:
  evaluation_for:
  - CA-R-2532
  - CA-R-1750
  - CA-R-1429
  - CA-D-318
  - CA-D-362
  - CA-D-363
  - CA-D-364
  - CA-D-365
  - CA-D-366
  - CA-D-375
  - CA-D-658
atom_id: CA-E-459
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 8
role: Evaluation
form: Eval Policy
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-459-CORE_META_MODEL-POLICY--validate-authoritative-project-settings-artifact.md
  source_atom_id: CA-E-459
  source_atom_revision: 39
  source_sha256: 58a0dc891fb4a9b37e4852cbcb4a41a254f6055189953956af87943f18c486ac
  original_relations_sha256: 9b8ec930086c35ecbfae2762e780b35b7dbf5b87136c5e657b568946762e7cd7
---
## Summary

Validate Authoritative Project Settings Artifact

## Claim scope

authoritative Project Settings Artifacts.

## Claim

the Evaluation **must** reject Project Settings **if**

- it is treated as an Atom **or** Projection,
- has an Atom ID **or** Atom Content Role,
- is **not** available independently of Project Atoms **and** Implementation,
- violates its registered Project-root placement **or** filename,
- has other than **`=1`** authoritative TOML Carrier,
- **contains** Framework Instance choices **or** independently editable Project Structure,
- violates its foundational content boundary, applicable shared settings specifications, applicable concrete field specifications, **or** the complete closed current field signature under CA-D-366,
- lacks a required CORE_META_MODEL definition **or** storage rule for Project Settings Name **or** Project Settings Prefix,
- lacks an Operator-selected Project Settings Name,
- lacks an Operator-selected Project Settings Prefix,
- treats a Methodology Atom, Framework Instance Settings, **or** a Projection as an independent authoritative source of either selected value,
- **or**, for history-binding evaluation under CA-D-365, lacks an exact current Revision, SHA-256 Digest, **and** admitted Work Journal receipt.

## Details

ordinary Settings Read **must** validate the complete actual Carrier **and** return immutable values with the exact selected Project, physical Carrier path, raw SHA-256 Digest, **and** declared schema marker. it **must not** query the Work Journal **or** determine logical Revision **or** currentness; Journal history is **not** an admission condition for ordinary Read. history-binding evaluation **and** recovered baseline registration under CA-D-365 remain separate operations. neither Read **nor** its refusal authorizes Carrier **or** Journal writes, compatibility fallback, **or** migration.

for recovered baseline registration, the Evaluation **must** check the exact selected Project, Carrier path, lineage-derived logical Revision, **and** Digest binding required by CA-D-365. verify that registration leaves Settings bytes unchanged **and** records the actual observation time **and** evidence-backed observer Run **or** session. reject an absent **or** ambiguous binding, a stale Carrier Digest, a path-based Revision reset **or** guessed allocation, **or** a fabricated Settings write, past mutation, author, **or** history. an admitted baseline receipt **must not** replace any Settings schema **or** ownership check above **or** authorize another operation.

### Project Prefix Decision binding

The replacement Prefix Decision is Current `CA-D-658@2`: [Serialize Project Prefix](../../07_delivery/CA-D-658-CORE_META_MODEL-DECISION--serialize-project-prefix.md). Its observed source SHA-256 is `443848e786be67f06f28a1a753d8e345a794135dad82c09fd09795648537e438`. This Evaluation's `evaluation_for` Relation binds that actual allocated Decision; the historical predecessor is not restored as authority.

### Current source pin

Proposed N+1 successor of `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-459-CORE_META_MODEL-POLICY--validate-authoritative-project-settings-artifact.md`, CA-E-459@36, SHA-256 `0a24497bc8492d7b155f4067ee75c77389decdcbf4cfb13e66eb68acef4de631`. Current bytes remain unchanged; this Draft performs no promotion, evaluation execution, or Journal change.
