---
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
topics:
  main_subject: Model::CAPRMEDIO::Continuant/Governing Objects/Atom.content
version: 1
updated_at: 2026-10-29 00:04:17 +0400
tier: 3
atom_id: CA-R-draft
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-11
---
# Summary

List Logical Content Fields

## Claim

The proposed read-only `content.get_list()` function, applied to an Atom kind, qualified kind, or selected Atom instance, returns registered Markdown Content headings. For a kind it returns allowed registered headings, including applicable inherited and optional headings. For a selected instance it returns only headings actually present.

The registered headings are `# Summary`, optional `## Claim scope`, `## Claim`, optional `## Semantics`, and optional `## Details`. The function returns heading names, not heading values, logical-key aliases, function names, or unrelated metadata. `atom.content.details` returns the text/value under the registered Details heading. Formal and natural claims both use `atom.content.claim`; version identity remains `atom.version_number` in YAML.

This proposal does not add `atom.property`, colon/property-text layers, or any other API. `atom.get_properties()` is a separate proposal for the full property set, including Content, with exact return shape unresolved. Existing Summary content remains unchanged.

## Details

The proposal distinguishes allowed headings for a kind from actual headings present in a selected instance. It remains separate from Formal Claim syntax and does not authorize parser, Tool, runtime, Current-source, or projection changes.

## Proposal status

This is a proposed candidate only, tracked by CA-A-1237. Its normative wording is not adopted methodology and must not be promoted as part of relation-notation changes.
