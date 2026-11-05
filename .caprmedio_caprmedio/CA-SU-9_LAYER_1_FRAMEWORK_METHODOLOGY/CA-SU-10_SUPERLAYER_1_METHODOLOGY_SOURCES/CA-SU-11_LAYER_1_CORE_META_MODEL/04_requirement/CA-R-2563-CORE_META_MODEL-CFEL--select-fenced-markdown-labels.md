---
atom_id: CA-R-2563
ref_id: CA-R-2563
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2563-CORE_META_MODEL-RULE--select-fenced-markdown-labels.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Select fenced Markdown labels

## Claim

### Prose Claim


`FENCED_LABELS(p)` selects one label per fenced code-block occurrence in one scalar Markdown value.

- Evaluate p separately for each matching bearer. Do not pool values across Atoms.
- Use the complete recursive Markdown block parse. Exclude indented code blocks.
- Preserve duplicate labels as separate occurrences. An unlabelled fence contributes an empty label.
- `FENCED_LABELS(p): [format]{:n}` requires every selected label to match the Format. The count constrains selected occurrences, including duplicates.
- The finite literal Format `[in (CFEL)]` matches only CFEL. An empty selection satisfies the Format condition but must still satisfy the count.
- Bind parsed labels through the governing Markdown Format and the existing CFEL-labelled-fence rule. No whole-info-string, token or case-normalization policy is added here.
- Missing or multiple Markdown values, incomplete parsing and unresolved or ambiguous label bindings are evaluation errors. Never replace them with an empty selection.

Selection reads Markdown value structure, not Graph Nodes or dependent Properties. CFEL body syntax is validated separately.
