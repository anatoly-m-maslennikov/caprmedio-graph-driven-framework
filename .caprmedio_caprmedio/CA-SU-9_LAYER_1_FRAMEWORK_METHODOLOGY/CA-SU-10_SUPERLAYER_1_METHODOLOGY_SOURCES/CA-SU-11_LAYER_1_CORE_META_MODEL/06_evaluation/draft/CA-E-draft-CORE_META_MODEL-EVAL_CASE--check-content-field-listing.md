---
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
topics:
  main_subject: Model::CAPRMEDIO::Continuant/Governing Objects/Atom.content
version: 1
updated_at: 2026-10-29 00:04:17 +0400
tier: 4
atom_id: CA-E-draft
role: Evaluation
form: Eval Case
container:
  scope_unit: CA-SU-11
---
# Summary

Check Content Field Listing

## Claim

The proposed `content.get_list()` contract must distinguish allowed registered Markdown Content headings for a kind from headings actually present in a selected instance. It must return heading names, not heading values, logical-key aliases, unrelated metadata keys, or function names.

The registered headings are `# Summary`, optional `## Claim scope`, `## Claim`, optional `## Semantics`, and optional `## Details`. Formal and natural claims both use `atom.content.claim`; version identity remains `atom.version_number` in YAML. `atom.content.details` returns the text/value under the registered Details heading.

## Details

Use a declared qualified Requirement fixture whose allowed headings include `# Summary`, `## Claim scope`, `## Claim`, and `## Details`, while the selected instance contains only `# Summary`, `## Claim`, and `## Details`. The kind-level result must report all allowed headings, including optional headings; the instance-level result must report only headings actually present. Preserve heading spelling and order. Do not include `atom.property`, colon/property-text layers, unrelated metadata, or `get_list` itself. This remains a proposal, not an executable test or implementation.

## Proposal status

This is a proposed candidate only, tracked by CA-A-1237. Its normative wording is not adopted methodology and must not be promoted as part of relation-notation changes.
