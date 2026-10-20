---
subjects:
  governs: "DEPENDS_ON"
  depends_on:
    ["Subject", "Entity/Node/Continuant/Atom.Subjects", "Entity", "Entity/Node/Continuant/Atom.Substance", "Entity/Node/Continuant/Atom.Summary"]
version: 19
updated_at: "2026-10-19 15:52:44 +0400"
relations: {}
atom_id: "CA-R-1280"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1280-CORE_META_MODEL-CORE-REQUIREMENT--reference-every-prerequisite-subject-through-depends-on.md
  source_atom_id: CA-R-1280
  source_atom_revision: 19
  source_sha256: 231bab115b3a5c93dc65ef3bc293d173d90104d4d2f1e307eb15c3be387ac22c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Reference Every Prerequisite Subject through DEPENDS_ON

## Scope

coverage of canonical Entity mentions by an Atom's Subjects.

## Claim

**every** Atom's Subject targets **must** be exactly the distinct canonical Entities independently mentioned **in** its Markdown Main Content, **not** an Atom citation label rendered under `CA-M-301-CORE_META_MODEL-METHOD--make-atom-claims-easy-to-understand` as the referenced Atom's complete filename **without** its `.md` extension **or** directory path: **`=1`** GOVERNS target for the Entity governed by its Claim, **and** DEPENDS_ON targets for **every** other mentioned Entity.

## Details

coverage includes Summary **and** **all** other body sections, nested headings, tables, examples, **and** reference labels. an Atom citation label is readable authority evidence, **not** an Entity mention **or** Subject target. this exclusion holds **when** the label occurs **in** the same sentence as Entity language; inventory that Entity **only** **when** the surrounding prose independently uses it. a mention outside Claim is **not** otherwise optional coverage. do **not** repeat GOVERNS **in** DEPENDS_ON **or** include an Entity absent from Main Content. a qualified Subject Path identifies its complete target; its component Terms **and** implicit bearer prefixes are **not** additional Entity mentions **unless** independently referenced. Subjects remain Relations rather than their Entity targets. unresolved Entity mentions require resolution **before** coverage can pass.
