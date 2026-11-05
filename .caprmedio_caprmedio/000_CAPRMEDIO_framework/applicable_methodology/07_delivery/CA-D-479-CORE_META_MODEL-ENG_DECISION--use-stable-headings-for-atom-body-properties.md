---
atom_id: CA-D-479
ref_id: CA-D-479
container:
  scope_unit: CA-SU-11
role: Delivery
form: Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/File
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Atom.Content.Details
  - CAPRMEDIO_MODEL <+ Term//Property
tier: 3
status: Active
version: 32
updated_at: 2026-11-05 22:47:24 +0400
carrier_destination:
  file:
    name: CA-D-479-CORE_META_MODEL-POLICY--use-stable-headings-for-atom-body-properties.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-479-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties.md
  source_atom_id: CA-D-479
  source_atom_revision: 32
  source_sha256: ff6edfc99f6359c004ed85807d8b6fbdb520cf343e22b888ac93544717939d1c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Use stable headings for Atom body Properties

## Claim

### Prose Claim

Applicability: Structured Main Content of Markdown Atom carriers.

Serialize Content headings in their declared sibling order. Omit absent optional Properties. Other admitted sibling Properties follow the ordered Properties, with no required order among them. For a declared Workflow Claim, Mermaid Scheme precedes Prose Claim, which precedes Formal Claim.

For ordinary RMED, carry one `## Summary` and one `## Claim` as sibling Properties, optionally followed by `## Semantics` and `## Details` in that order. Claim has no direct value and contains one or both `### Formal Claim` and `### Prose Claim`, with unique sibling names. Formal Claim contains a CFEL-labelled code fence; Prose Claim contains ordinary Markdown. Omit absent optional Properties. Do not duplicate Claim in frontmatter.

Map declared headings to their Property paths with a code-fence-aware outline. Only headings admitted as children by an applicable declaration are Properties. Other headings within a Markdown value, including unknown `##` headings within Prose Claim, remain part of that value and do not terminate it. A recognized Property section ends at the next recognized sibling or ancestor heading, or at the end of Main Content. Heading-like text in a fence is content. Direct value counts and dependent Property counts are independent. Retrieving a Property subtree includes its selected heading and its descendants.

Normalize recognized Property heading names to lowercase, replace spaces with underscores, and strip characters other than letters, numbers, underscore and hyphen. Reject an empty normalized key or duplicate normalized key under one parent. A flattened lookup is admissible only when unambiguous; canonical paths retain their parent chain.

Legacy layouts remain readable during migration. The existing C/A/P/O primary-content headings and their own Role-specific content rules remain applicable. A Draft may be incomplete but must satisfy the applicable complete contract before promotion.

