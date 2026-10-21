---
atom_id: CA-M-394
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
global_tier: 9
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Entity/Graph Rule
  depends_on:
  - Entity/Graph Rule.Type
  - Entity/Graph Rule.Applies To
  - Entity/Graph Rule.Condition
  - Entity/Graph Rule.Default Value
  - Entity/Node/Continuant/Atom.Substance
  - Entity/Node/Continuant/Atom.Summary
relations: {}
version: 4
updated_at: "2026-10-20 13:33:10 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/05_method/CA-M-394-CORE_META_MODEL-CORE--author-one-formal-graph-rule-and-its-readable-summary.md
  source_atom_id: CA-M-394
  source_atom_revision: 4
  source_sha256: d6e7149d13d3f2cb1a4752ff107f9c3bbcbc136a6943768a862f198569b91d5f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
- do not invent missing Type schemas, whitelist merging, blacklist precedence, defaults, override behaviour or a general-purpose expression language. Report the specific gap before authoring a rule that depends on it.
