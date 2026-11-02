---
atom_id: CA-M-394@9
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph/Rule
  depends_on:
  - Subject/Graph/Rule.Type
  - Subject/Graph/Rule.Applies To
  - Subject/Graph/Rule.Condition
  - Subject/Graph/Rule.Default Value
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Entity/Node/Continuant/Atom.Summary
relations: {}
version: 9
updated_at: 2026-10-24 00:38:25 +0400
tier: 1
---
# Summary

Author one formal Graph Rule and its readable Summary

## Scope

authoring an R Atom that expresses a Graph Rule, not every R Atom of Type Rule.

## Claim

to author a Graph Rule, the Author **must** express one independently replaceable rule of exactly one Graph Rule Type as formal YAML, then write its source-faithful Summary for readability.

## Details

- use R/Type: Graph Rule for the containing Atom; its Requirement Type is distinct from graph_rule_type inside the operative YAML body. Do not add graph_rule_type to the Atom's frontmatter or introduce a generic Subtype. Model Definition contracts are not Graph Rule instances merely because they describe the model.
- carry all operative applicability and constraints in the structured YAML. A formal Graph Rule has no Claim or Substance Property or section and no separate prose Scope. Summary is a navigation aid, not another authoritative statement. Semantics and Details are optional under CA-D-637; omit them when they add no useful explanation or support. Do not use them to duplicate, change or override the operative rule.
- select the registered schema for the one Graph Rule Type. Use declared fields, typed values, Subject references and formal constraints, not free-form prose pretending to be a machine-readable condition. A YAML document alone does not supply missing semantics.
- split independently replaceable rules, including rules requiring different Graph Rule Types, into separate Atoms. Do not create a list of Type values in one rule.
- retain the established Summary on update; if it must change, follow the existing new-Atom identity rule.
- author Cardinality only under CA-D-637's registered schema. Bind the declared node domain independently of edges present, preserve zero-edge cases, select direction and opposite-endpoint kinds explicitly, and use its typed minimum/maximum bounds. Do not infer Selection membership from a filtered graph or treat structural parsing as evaluation.
- use the closed Endpoint Constraint schema under CA-D-637 when the rule compares properties of both endpoints. Its `applies_to.relation_selection` value must be a full Subject string naming a source-declared Selection, and its `condition.ordering` value must be one of that schema's exact enumerated operators. For the approved RMED ordering, use the Selection defined by CA-R-2148 and the `same_scope_lower_target_tier_or_strict_ancestor` operator; do not replace these with aliases or a general-purpose expression language.
- do not invent missing Type schemas, whitelist merging, blacklist precedence, defaults or override behaviour. Report any remaining specific gap before authoring a rule that depends on it.
