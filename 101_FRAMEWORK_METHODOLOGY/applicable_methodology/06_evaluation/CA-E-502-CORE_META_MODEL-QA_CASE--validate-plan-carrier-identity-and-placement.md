---
subjects:
  governs: "Entity/Carrier"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Plan", "Entity/Carrier/File Carrier", "Entity/Carrier/Directory Carrier", "Entity/Continuant/Node/Atom.ID", "Entity/Continuant/Node/Atom.Summary", "Entity/Continuant/Node/Atom/Content Role: Plan.Work Sequence Number", "Entity/Continuant/Node/Atom/Content Role: Plan.Label", "Entity/Continuant/Node/Atom/Content Role: Plan.Status", "Entity/Continuant/Node/Atom/Content Role: Plan.Definition of Done"]
version: 10
updated_at: "2026-10-18 03:34:30 +0400"
relations: {"evaluation_for": ["CA-D-460", "CA-D-461", "CA-D-469", "CA-D-470", "CA-D-472", "CA-D-475", "CA-R-1534", "CA-R-1599", "CA-R-997"]}
atom_id: "CA-E-502"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-502-CORE_META_MODEL-QA_CASE--validate-plan-carrier-identity-and-placement.md
  source_atom_id: CA-E-502
  source_atom_revision: 10
  source_sha256: f6ef3136a69d09e411a105ba6e91615ccd5599b24a448acf0fd692e10ebe1c58
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary
Validate Plan Carrier identity **and** placement

## Scope
Plan Carrier identity **and** placement.

## Claim
the Plan Carrier Evaluation **must** reject Carrier facts that create duplicate identity **or** contradict the shared Plan model.

- accept a mandatory Markdown file **with** **or** **without** a matching optional Hub directory under `CA-D-460-CORE_META_MODEL-CORE-DELIVERY--serialize-plan-atom-carrier-bundles`; reject a directory **without** that file.
- count a matching pair once; reject two IDs, divergent stems, conflicting Status, a separate Epic identity, **or** an Objective file that claims **to** be another Atom for the same Hub.
- require DoD **in** **every** supplied Plan file, even **when** it carries a pure Hub **or** explicit overrides.
- validate leading navigation numbers **before** Atom IDs, their local uniqueness, mutable Label tokens, **and** canonical Summary slugs. changing a number **or** Label **must not** change identity **or** scheduling.
- read Plan Status from its own file **and** check its local placement; reject read-time inference from a containing Hub **or** path.
- change a parent Plan's Status to Active, Backlog, Done, Canceled **or** Archived as admitted by its model: require the same requested Status through independent single-Atom Actions for **all** recursively contained descendants' latest Revisions under CA-R-1521. check each Atom's own model; reject an invented target value **or** a multi-target Action.
- retain each descendant inside its parent Carrier tree with the local Status mapping under CA-D-461; for a Done parent at `03_plan/done/<parent>.md`, accept its Done child at `03_plan/done/<parent>/done/<child>.md` using canonical matching stems. apply CA-D-289's Version suffixes for Archived placement **without** extracting descendants from the parent.
- leave referenced Plans outside the tree **and** older archived Revision bytes, Version **and** Status unchanged; reject older Revisions as cascade targets. no migration of noncanonical legacy `archive/` trees is implied.
- accept root Backlog Plans **in** `03_plan/001_backlog`; reject `031_backlog` as the canonical new encoding **and** reject a `version-<VERSION>` directory substituted for a Version-labeled Plan identity.
- retain one identity **when** decomposed work is added, removed, **or** reordered; a changed Summary follows Atom replacement authority rather than independent filename editing.

report the invalid Carrier Bundle, source fact, **and** violated Delivery rule.

## Details
