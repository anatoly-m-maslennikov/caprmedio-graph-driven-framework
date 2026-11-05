---
atom_id: CA-A-1303
ref_id: CA-A-1303
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Entity
tier: 3
status: Done
version: 3
updated_at: 2026-11-02 15:49:28 +0400
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Qualify Operation Types and declare Relation Subject notation

## Operations Type structure

```text
Atom/Content Role: Operations
	/Type: Workflow
		>{1+}Type: Step
			>{0+}Type: Sub-step
	/Type: Action
```

Workflow, Step, Sub-step and Action identify qualified Operations Atom Types, not free-standing primary kinds with the same bare names. Each contained target retains the Operations Content Role qualification; > expresses containment, not subtype inheritance from Workflow or Step. Action remains a separately reusable Type.

A leaf Step calls an Action or Workflow with bindings. A Step containing Sub-steps makes no call of its own. Sub-steps remain Action-only leaves. The settled counts and permitted Workflow-call recursion remain unchanged.

## Relation Definition Type

Reserve R/Type: Relation Definition for defining named reusable Relation Types. Their short Subject notation is carried in content.notation_for_subject as a fenced code block under ## Notation for subject. Require that field when the definition provides an admitted short Subject operator; Relation Types without a dedicated shorthand can use the general ((RELATION_TYPE)) form.

This is distinct from the R/Entity Definition describing the Relation structure itself and from R/Term Definition for Term meanings. The glyph notation does not replace the required prose Claim or change direct/inverse meanings.

## Organization versus classification

Design and the other listed aspect kinds are Aspects, so use / rather than organizational membership. The proposed Graph Syntax branch structurally contains Relation, Format and Cardinality. No remaining organizational-membership use of :: is required by the latest classification candidate; the symbol is not needed in this candidate. Preserve its older definitions as historical preparation until the planned migration reconciles them. No Current operator rule is retired by this proposal edit.

## State

Candidate A1302 is updated and a Relation Definition Type Draft is prepared. The two prepared named Relation Definitions are reclassified without changing their Summaries or claimed meanings. Their general notation does not acquire an invented shorthand. Current sources and runtime remain unchanged.
