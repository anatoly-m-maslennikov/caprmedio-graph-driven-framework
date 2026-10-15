---
subjects:
  governs: "Journal/Record"
  depends_on:
    - "Work Journal/Event"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Carrier"
    - "Atom/Content Role: Operations"
    - "Journal"
    - "Atom"
    - "Artifact/Carrier"
    - "Project"
    - "Applicable Methodology"
version: 13
updated_at: "2026-10-13 04:51:40 +0400"
relations:
  evaluation_for:
    - CA-R-1491
    - CA-R-807
atom_id: "CA-E-462"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-462-CORE_META_MODEL-EVALUATION_APPROACH--validate-atom-replacement-event-evidence.md
  source_atom_id: CA-E-462
  source_atom_revision: 13
  source_sha256: 5889044fc5d051f38fb7ff37dbc0839d1589e7a74296d0d343e2990fd334a839
  original_relations_sha256: 08e3ba1b02b72ebd56719baa1c003348b431b4bd58722cfd3ed9eccfe064ba4c
---
# Summary

Validate Atom replacement event evidence

## Scope

Atom replacement event evidence.

## Claim

the Evaluation **must** check whether an Atom replacement satisfies CA-R-807. Journal acceptance is **not** proof that the replacement is correct.

## Details

### Checks

- report a failed replacement Evaluation **if** predecessor **or** successor identities are missing, unresolved, duplicate, self-referencing, **or** mismatched.
- verify that **every** named successor was Active **before** the predecessor was archived, that the archived current predecessor preserves its body, Summary, identity **and** every metadata value except Version, archived Status **and** archive-time Updated At, with Version incremented by exactly **`1`** **and** actual archive-time Updated At. verify retained exact prior Revision bytes, including the prior Version, Status **and** Updated At, **and** that **`=1`** authoritative Journal event records that replacement.
- check event field representation against the selected Delivery authority. a format check alone **must not** be reported as proof of replacement correctness.
- repeated submission of the same event **must not** create another authoritative record.

### Failure disposition

a failed **or** unresolved replacement Evaluation **must not** prevent the Journal from preserving the observed event under CA-R-1491. preserve the supplied identities **and** evidence **without** inventing a conforming replacement **or** claiming that a failed check passed. correction changes the governed source through its authorized Workflow; it does **not** rewrite accepted history.

this Evaluation **must not** require a Git Commit **or** a particular Journal serialization.
