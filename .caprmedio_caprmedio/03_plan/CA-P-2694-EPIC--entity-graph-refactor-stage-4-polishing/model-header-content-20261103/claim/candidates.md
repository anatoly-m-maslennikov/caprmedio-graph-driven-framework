# Claim and declared headings: candidate changes

These are proposed replacement passages, not Current authority. Inventory and migration instructions are separate. Retain each source's other content and metadata except the explicitly identified replacements and Subject changes. Use the new Subject roots `CAPRMEDIO_MODEL` and `CAPRMEDIO_STRUCTURE` when the integrated subject-path migration defines their exact paths; do not allocate IDs here. The derived named-relation counterpart has a minimal binding Claim; it has no special exception.

## CA-R-2498, Claim replacement

```CFEL
Atom.Content{:1}: []{:0};
Atom.Content.*[string]{:0+};
Atom.Content.**[string]{:0+}: [markdown]{:0..1}
```

Retain the Current formal content unchanged. A grouping Property has zero direct values; its descendant values, where present, are Markdown. A heading is a Property only when its applicable declaration admits it. This does not prohibit ordinary Markdown headings within a value.

## CA-R-2499, CA-R-2502, CA-R-2503

Retain the Current Claims and cardinalities. Summary is required, Semantics and Details are optional for RMED; Details' declared dependents remain allowed. Their property headings are recognized through applicable declarations, not merely through heading depth. Other Roles retain their own applicable declarations.

## CA-R-2500, Claim replacement

```CFEL
Atom/(.Header.Role in RMED).Content.Claim{:1}: []{:0};
Atom/(.Header.Role in RMED).Content.Claim.*[string, in (Formal Claim, Prose Claim)]{:1..2};
Atom/(.Header.Role in RMED).Content.Claim.Formal Claim{:0..1}: [markdown]{:1};
Atom/(.Header.Role in RMED).Content.Claim.Prose Claim{:0..1}: [markdown]{:1}
```

A complete ordinary RMED Claim has at least one of Formal Claim and Prose Claim. Sibling names are unique. Formal Claim contains a CFEL-labelled code fence; Prose Claim contains ordinary Markdown. A Markdown heading inside Prose Claim is part of its value, unless an applicable declaration expressly declares it as a child Property. The derived named-relation counterpart has a minimal binding Claim; it has no special exception.

## CA-R-2501

Withdraw the declaration of `Atom.Content.Claim Scope` as an applicable Property. Existing applicability text must be preserved in Prose Claim during the later migration. This withdrawal does not remove the concept of applicability or the independently resolved target Scope Unit.

## CA-R-1417, Semantics replacement

Content is the Markdown portion whose natural-language meaning generally needs interpretation. Header properties use YAML. A complete ordinary RMED Content portion has a Claim grouping with no direct value and one or both declared Formal Claim and Prose Claim children. Formal Claim contains a CFEL-labelled code fence; Prose Claim contains ordinary Markdown. Tools can extract declared Properties or parse supported formal syntax without proving all prose meaning.

One Content portion is a structured group with zero direct scalar values and independently counted child Properties. This introduces no generic Substance field. The retained Summary's word Revision means an Atom version, not a separate Revision entity.

## CA-R-2102, replacement of the RMED paragraph only

For ordinary RMED, require one Claim grouping with no direct value and one or both uniquely named Formal Claim and Prose Claim children. Formal Claim contains a CFEL-labelled code fence; Prose Claim contains ordinary Markdown. Apply the respective content rules for Concern, Analysis & Advisory, Plan and Operations, and preserve their established primary content headings.

## CA-R-2471, Formal content replacement

A Formal Claim is a declared child of an ordinary RMED Claim and contains formal content in a fenced block labelled CFEL. Formal content in an ordinary RMED Claim belongs in Formal Claim. Prose Claim contains ordinary Markdown. A heading in a Markdown value does not declare a Property by itself.

Retain the existing sibling-uniqueness rule and all other notation rules. The derived counterpart follows the ordinary Claim contract.

## CA-D-479, Claim replacement

For ordinary RMED, carry one `## Summary` and one `## Claim` as sibling Properties, optionally followed by `## Semantics` and `## Details` in that order. Claim has no direct value and contains one or both `### Formal Claim` and `### Prose Claim`, with unique sibling names. Formal Claim contains a CFEL-labelled code fence; Prose Claim contains ordinary Markdown. Omit absent optional Properties. Do not duplicate Claim in frontmatter.

Map declared headings to their Property paths with a code-fence-aware outline. Only headings admitted as children by an applicable declaration are Properties. Other headings within a Markdown value remain part of that value. A recognized Property section ends at the next recognized sibling or ancestor heading, or at the end of Main Content. Heading-like text in a fence is content. Direct value counts and dependent Property counts are independent. Retrieving a Property subtree includes its selected heading and its descendants.

Normalize recognized Property heading names to lowercase, replace spaces with underscores, and strip characters other than letters, numbers, underscore and hyphen. Reject an empty normalized key or duplicate normalized key under one parent. A flattened lookup is admissible only when unambiguous; canonical paths retain their parent chain.

Legacy layouts remain readable during migration. The existing C/A/P/O primary-content headings and their own Role-specific content rules remain applicable. A Draft may be incomplete but must satisfy the applicable complete contract before promotion.

## CA-D-495, Claim and Details replacements

A Markdown Atom Carrier must carry the Claim's applicability in its registered body content, not as a duplicate frontmatter value. For ordinary RMED, carry textual applicability in Prose Claim together with the qualified contribution; carry formal content in the CFEL fence within Formal Claim and supporting information in Details. Do not maintain a second applicability declaration in Details or frontmatter. For other Content Roles, retain applicability in their registered primary content; this rule does not change their body-section layouts.

Applicability identifies what the Claim applies to, including relevant conditions and exclusions. It does not select another structural target, change ownership, or introduce a separate Claim. A reference to the carried target is not a second authoritative copy of that target.

## CA-D-482

Retire this obsolete rule without replacement; resolve target from the active Subject.

## CA-M-228

The complete replacement Method is in its candidate carrier.

## CA-M-264, passive Subject replacement

Replace the passive Subject targeting `Atom.Content.Claim Scope` with the integrated canonical Subject targeting `Atom.Content.Claim.Prose Claim` under `CAPRMEDIO_MODEL`. Retain the Claim and remaining Subjects.

## CA-E-240, test case replacement of the first sentence

Create a Current-scope Atom with its own Scope Unit carried as the target; repeat with one GOVERNS target and with a narrower restriction and a composite restriction in its Prose Claim for ordinary RMED or the registered primary content for other roles.

Retain all other content, with “Claim Scope” in the Summary and acceptance criteria understood as textual applicability, not a Property. The test must also verify that the migrated applicability is preserved exactly in meaning and does not select or duplicate a structural target.
