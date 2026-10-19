---
subjects:
  governs: "Entity/Continuant/Node/Atom.Updated At"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Evaluation", "Entity/Continuant/Node/Atom", "Entity/Continuant/Node/History/Revision/Type: Atom", "Entity/Carrier", "Entity/Continuant/Node/Atom.Version Number", "Entity/Continuant/Node/Atom.Status", "Entity/Continuant/Node/Atom.Summary", "Entity/Continuant/Node/Atom.ID", "Entity"]
version: 6
updated_at: "2026-10-18 03:34:31 +0400"
relations:
  evaluation_for:
    - CA-D-270
    - CA-R-1432
    - CA-R-1788
    - CA-O-051
atom_id: "CA-E-521"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
---
# Summary

Verify Updated At refresh and semantic Versioning

## Scope

accepted Markdown Atom Carrier edits classified by governed meaning.

## Claim

the Evaluation **must** accept **only** an actual same-ID edit that refreshes `updated_at` **and** increments Version by exactly **`1`**, regardless of semantic change class. an exact no-op retains Version **and** Updated At; required predecessor history retains its exact prior bytes.

## Details

### Test case

- apply a formatting-only edit, a lossless Entity-name edit, **and** an equivalent refinement; verify an actual refreshed timestamp **and** Version incremented by exactly **`1`** for **every** edit.
- apply a semantic revision; verify an actual refreshed timestamp **and** the next Version.
- archive a current predecessor; verify `status: Archived`, archive-time `updated_at`, Version incremented by exactly **`1`**, **and** preservation of body, Summary, identity, **and** **all** other metadata. verify that its prior Revision is retained as exact bytes, including its prior Version, Status **and** Updated At.
- apply an exact no-op; verify unchanged bytes, Version **and** Updated At.

### Acceptance criteria

- reject an actual accepted edit whose `updated_at` does **not** identify its actual Project-time edit instant **or** whose Version increment is other than exactly **`1`**.
- reject a no-op that changes Version **or** Updated At.
- reject retained predecessor history whose bytes, Version, Status **or** Updated At differ from its exact prior Revision.

the checked rules are `CA-D-270-CORE_META_MODEL-DELIVERY--serialize-atom-revision-metadata-in-frontmatter`, `CA-R-1432-CORE_META_MODEL-GENERAL-REQUIREMENT--classify-admitted-atom-changes-by-semantic-effect`, `CA-R-1788-CORE_META_MODEL--refresh-updated-at-whenever-an-atom-changes`, and `CA-O-051-CORE_META_MODEL-ACTION--persist-atom-replacement-through-ordered-carrier-transitions`. CA-R-1433 is retained only as retired historical evidence, not a current Version exception.
