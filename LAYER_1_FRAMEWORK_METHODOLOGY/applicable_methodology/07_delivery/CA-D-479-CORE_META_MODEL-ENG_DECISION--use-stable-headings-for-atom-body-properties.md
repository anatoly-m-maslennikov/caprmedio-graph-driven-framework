---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/File.Main Content
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom.Content.Summary
  - CAPRMEDIO <+ MODEL <+ Atom.Content
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Content Role
  - CAPRMEDIO <+ MODEL <+ Atom.Content.Details
  - CAPRMEDIO <+ MODEL <+ Term//Property
  - CAPRMEDIO <+ MODEL <+ Carrier/File
version: 27
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-479
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Policy
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-479-CORE_META_MODEL-ENG_DECISION--use-stable-headings-for-atom-body-properties.md
  source_atom_id: CA-D-479
  source_atom_revision: 27
  source_sha256: 83c781939d44f0263101159c083b187c88f3535c526dfff1533b560fdfd7ea29
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Use stable headings for Atom body Properties

## Claim scope

Structured Main Content of Markdown Atom carriers.

## Claim

For RMED, carry one `## Summary` and one `## Claim` as sibling Properties, optionally preceded by `## Claim scope` before Claim and followed by `## Semantics` and `## Details` in that order. The Claim's direct Markdown value may consist of a fenced CFEL expression without prose. Do not create a `Formal claim` child, a separate Prose claim section, or a duplicate frontmatter Claim. Omit absent optional sections.

Map headings to Property paths with a code-fence-aware outline. A section ends at the next real heading of the same or higher level, or at the end of Main Content. Lower-level real headings nest under their parent; equal-level headings are siblings, and skipped levels create no empty Properties. Heading-like text in a fence is content. Direct value counts and dependent Property counts are independent. Retrieving a section subtree includes its selected heading and its descendants.

Normalize real heading names to lowercase, replace spaces with underscores, and strip characters other than letters, numbers, underscore and hyphen. Reject an empty normalized key or duplicate normalized key under one parent. A flattened lookup is admissible only when unambiguous; canonical paths retain their parent chain.

Legacy layouts remain readable during migration. The existing C/A/P/O primary-content headings and their own Type-specific content rules remain applicable. A Draft may be incomplete but must satisfy the applicable complete contract before promotion.
