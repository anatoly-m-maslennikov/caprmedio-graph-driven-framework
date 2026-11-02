---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Project.Settings
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/Project.Settings.Project Name
  - Subject/Graph Node/Domain/Continuant/Project.Settings.Atom Prefix
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Domain/Continuant/Scope Unit
version: 32
updated_at: 2026-10-25 17:32:27 +0400
relations:
  evaluation_for:
  - CA-R-1738
  - CA-R-1750
  - CA-R-1429
  - CA-D-318
  - CA-D-362
  - CA-D-363
  - CA-D-364
  - CA-D-365
  - CA-D-366
  - CA-D-375
  - CA-D-376
atom_id: CA-E-459@32
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Policy
tier: 8
---
# Summary

Validate Authoritative Project Settings Artifact

## Scope

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
- lacks a required CORE_META_MODEL definition **or** storage rule for Project Name **or** Project Atom prefix,
- lacks an Operator-selected Project Name,
- lacks an Operator-selected Project Atom prefix,
- treats a Methodology Atom, Framework Instance Settings, **or** a Projection as an independent authoritative source of either selected value,
- **or**, for history-binding evaluation under CA-D-365, lacks an exact current Revision, SHA-256 Digest, **and** admitted Work Journal receipt.

## Details

ordinary Settings Read **must** validate the complete actual Carrier **and** return immutable values with the exact selected Project, physical Carrier path, raw SHA-256 Digest, **and** declared schema marker. it **must not** query the Work Journal **or** determine logical Revision **or** currentness; Journal history is **not** an admission condition for ordinary Read. history-binding evaluation **and** recovered baseline registration under CA-D-365 remain separate operations. neither Read **nor** its refusal authorizes Carrier **or** Journal writes, compatibility fallback, **or** migration.

for recovered baseline registration, the Evaluation **must** check the exact selected Project, Carrier path, lineage-derived logical Revision, **and** Digest binding required by CA-D-365. verify that registration leaves Settings bytes unchanged **and** records the actual observation time **and** evidence-backed observer Run **or** session. reject an absent **or** ambiguous binding, a stale Carrier Digest, a path-based Revision reset **or** guessed allocation, **or** a fabricated Settings write, past mutation, author, **or** history. an admitted baseline receipt **must not** replace any Settings schema **or** ownership check above **or** authorize another operation.
