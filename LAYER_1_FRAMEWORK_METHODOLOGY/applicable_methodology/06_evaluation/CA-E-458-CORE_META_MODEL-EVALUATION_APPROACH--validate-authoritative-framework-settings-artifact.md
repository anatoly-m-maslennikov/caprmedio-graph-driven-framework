---
subjects:
  governs: "Framework Instance Settings Validation"
  depends_on:
    ["Entity/Node/Continuant/Project.Framework Settings", "Default Settings", "Entity/Node/Continuant/Project.Framework Settings.Revision Binding"]
version: 20
updated_at: "2026-10-19 15:55:03 +0400"
relations:
  evaluation_for:
    - CA-R-1402
    - CA-R-1430
    - CA-R-1429
    - CA-D-317
    - CA-D-358
    - CA-D-359
    - CA-D-360
    - CA-D-361
    - CA-R-1441
    - CA-M-279
atom_id: "CA-E-458"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-458-CORE_META_MODEL-EVALUATION_APPROACH--validate-authoritative-framework-settings-artifact.md
  source_atom_id: CA-E-458
  source_atom_revision: 20
  source_sha256: 5175cd255c672bc33699862963c871e322ef64f1e8fc3cbd5bc1a32da70b7e1e
  original_relations_sha256: c43710a24ba9609df14ffa1948ef1b7800e193bfc80ab2f310b1715a02cb8616
---
# Summary

Validate Authoritative Framework Settings Artifact

## Scope

Framework Instance Settings.

## Claim

the Evaluation **must** reject Framework Instance Settings **if**

- it is treated as an Atom **or** Projection,
- has an Atom ID **or** Atom Content Role,
- resolves outside the current Project's registered instance directory,
- uses another Project's Settings Carrier,
- has other than **`=1`** authoritative TOML Carrier,
- **contains** Project initialization inputs **or** independently editable Project Structure,
- violates its Core content boundary, applicable General settings specifications, **or** applicable Standard field specifications **after** parameter resolution governed by CA-M-279,
- **or** lacks an exact current Revision, SHA-256 Digest, **and** Work Journal receipt admitted by CA-D-360.

## Details

for recovered baseline registration, the Evaluation **must** check the exact selected Project, Carrier path, lineage-derived logical Revision, **and** Digest binding required by CA-D-360. verify that registration leaves Settings bytes unchanged **and** records the actual observation time **and** evidence-backed observer Run **or** session. reject an absent **or** ambiguous binding, a stale Carrier Digest, a path-based Revision reset **or** guessed allocation, **or** a fabricated Settings write, past mutation, author, **or** history. an admitted baseline receipt **must not** replace any Settings schema **or** ownership check above **or** authorize another operation.
