---
atom_id: CA-R-2563
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2563-CORE_META_MODEL-CFEL--select-fenced-markdown-labels.md
  source_atom_id: CA-R-2563
  source_atom_revision: 2
  source_sha256: a684c024a238b6756bd6e8a1b4f0b5560d1743c190e2fefedd20d1ed6111526a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Select fenced Markdown labels

## Claim

`FENCED_LABELS(p)` selects one label per fenced code-block occurrence in one scalar Markdown value.

- Evaluate p separately for each matching bearer. Do not pool values across Atoms.
- Use the complete recursive Markdown block parse. Exclude indented code blocks.
- Preserve duplicate labels as separate occurrences. An unlabelled fence contributes an empty label.
- `FENCED_LABELS(p): [format]{:n}` requires every selected label to match the Format. The count constrains selected occurrences, including duplicates.
- The finite literal Format `[in (CFEL)]` matches only CFEL. An empty selection satisfies the Format condition but must still satisfy the count.
- Bind parsed labels through the governing Markdown Format and the existing CFEL-labelled-fence rule. No whole-info-string, token or case-normalization policy is added here.
- Missing or multiple Markdown values, incomplete parsing and unresolved or ambiguous label bindings are evaluation errors. Never replace them with an empty selection.

Selection reads Markdown value structure, not Graph Nodes or dependent Properties. CFEL body syntax is validated separately.
