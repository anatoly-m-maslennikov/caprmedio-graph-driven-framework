---
subjects:
  governs: "DEPENDS_ON"
  depends_on:
    ["Subject", "Entity/Node/Continuant/Atom.Subjects", "Subject Target", "Entity/Node/Continuant/Atom.Substance", "Entity/Node/Continuant/Atom.Summary"]
version: 20
updated_at: "2026-10-21 01:47:52 +0400"
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
  source_atom_revision: 20
  source_sha256: 47421b2700a1259e79b529b794a9e395f2f1c4832bd367dd35a77abd014ed9a4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Reference Every Prerequisite Subject through DEPENDS_ON

## Scope

coverage of canonical Subject Target mentions by an Atom's Subjects.

## Claim

**every** Atom's Subject targets **must** be exactly the distinct canonical Subject Targets independently mentioned **in** its Markdown Main Content, **not** an Atom citation label rendered under `CA-M-301-CORE_META_MODEL-METHOD--make-atom-claims-easy-to-understand` as the referenced Atom's complete filename **without** its `.md` extension **or** directory path: **`=1`** GOVERNS target for the Subject Target governed by its Claim, **and** DEPENDS_ON targets for **every** other mentioned Subject Target.

## Details

coverage includes Summary **and** **all** other body sections, nested headings, tables, examples, **and** reference labels. an Atom citation label is readable authority evidence, **not** a Subject Target mention **or** Subject target. this exclusion holds **when** the label occurs **in** the same sentence as Subject Target language; inventory that Subject Target **only** **when** the surrounding prose independently uses it. a mention outside Claim is **not** otherwise optional coverage. do **not** repeat GOVERNS **in** DEPENDS_ON **or** include a Subject Target absent from Main Content. a qualified Subject Path identifies its complete target; its component Terms and implicit bearer prefixes are **not** additional Subject Target mentions **unless** independently referenced. Subjects remain Relations rather than their targets. unresolved Subject Target mentions require resolution **before** coverage can pass.
