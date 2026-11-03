---
subjects:
  active: Atom.Updated At
  passive:
  - Atom/(.Role := Evaluation)
  - Atom
  - Entity/Object/Continuant/Governing Objects/Atom.Version Number
  - Carrier
  - Atom.Status
  - Atom.Content.Summary
  - Atom.ID
  - Entity
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-D-270
  - CA-R-1432
  - CA-R-1788
  - CA-O-051
atom_id: CA-E-521
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/06_evaluation/CA-E-521-PROJECT_CONFIGURATION-EVAL_CASE--verify-updated-at-refresh-and-semantic-versioning.md
  source_atom_id: CA-E-521
  source_atom_revision: 22
  source_sha256: e7a0428876f74b34fac644f8799ac651fd4ec5745869268a825668d883b296a9
  original_relations_sha256: c623ba9a228b435f122f3a3bbfe731c3c55aa738665beb67f9045b3edfca684f
---
## Summary

Verify Updated At refresh and semantic Versioning

## Claim scope

accepted Markdown Atom Carrier edits classified by governed meaning.

## Claim

the Evaluation **must** accept **only** an actual same-ID edit that refreshes `updated_at` **and** increments Version by exactly **`1`**, regardless of semantic change class. an exact no-op retains Version **and** Updated At; required predecessor history retains its exact prior bytes.

## Details

### Test case

- apply a formatting-only edit, a lossless Entity-name edit, **and** an equivalent refinement; verify an actual refreshed timestamp **and** Version incremented by exactly **`1`** for **every** edit.
- apply a semantic revision; verify an actual refreshed timestamp **and** the next Version.
- archive a current predecessor; verify `status: Archived`, the predecessor's unchanged Version and Updated At, **and** preservation of body, Summary, identity, **and** **all** other metadata. the resulting Archive Carrier uses the predecessor's version-qualified identity; archival alone does not increment Version or refresh Updated At. verify that its prior Revision is retained as exact bytes, including its prior Version, Status **and** Updated At.
- apply an exact no-op; verify unchanged bytes, Version **and** Updated At.

### Acceptance criteria

- reject an actual accepted edit whose `updated_at` does **not** identify its actual Project-time edit instant **or** whose Version increment is other than exactly **`1`**.
- reject a no-op that changes Version **or** Updated At.
- reject retained predecessor history whose bytes, Version, Status **or** Updated At differ from its exact prior Revision.

the checked rules are `CA-D-270-CORE_META_MODEL-DELIVERY--serialize-atom-revision-metadata-in-frontmatter`, `CA-R-1432-CORE_META_MODEL-GENERAL-REQUIREMENT--classify-admitted-atom-changes-by-semantic-effect`, `CA-R-1788-CORE_META_MODEL-RULE--refresh-updated-at-whenever-an-atom-changes`, and `CA-O-051-PROJECT_CONFIGURATION-ACTION--persist-atom-replacement-through-ordered-carrier-transitions`. CA-R-1433 is retained only as retired historical evidence, not a current Version exception.
