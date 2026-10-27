---
subjects:
  governs: Subject
atom_id: CA-R-2006@7
content_role: Requirement
type: Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
version: 7
updated_at: 2026-10-25 17:32:27 +0400
author: Anatoly Maslennikov
relations: {}
tier: 1
---
# Summary

Define Subject Target Roots

## Scope

canonical Subject paths in this model.

## Claim

Bare Subject is the valid umbrella. Every more-specific canonical Subject path starts at Subject and then enters exactly one root branch: Graph Node, Graph Relation, or Graph Rule. Graph Node contains the canonical target hierarchy. Domain and Engineering each have Continuant and Occurrent child branches; Documentation, Product, and UX are also current Graph Node branches, and that set is expandable. Graph Relation names relation topics and Graph Rule names graph-constraint topics.

## Details

Graph Node is a Subject-path branch, not a new Entity, Carrier, intermediate Subject object, or target identity. Product names what the project produces; Domain names the concepts and things it works with; Engineering names how it is built, stored, and operated. Branch assignment distinguishes modeled work in Domain (Action, Step, and Workflow Run) from technical runtime in Engineering (Session and tool/app runtimes). Other Engineering policy or pure topics may remain directly under Engineering; no target acquires a temporal classification merely from this taxonomy. UX names the MCP interface and health-page appearance; it does not reclassify backend Engineering or MCP topics wholesale. Documentation retains its topic meaning.

Subject branch, Content Role and Local Scope Unit are independent. A Requirement about a product can live at Project scope without making Project its Subject. A topic need not be an independently carried object. A Scope Unit path is not automatically a Subject path.
