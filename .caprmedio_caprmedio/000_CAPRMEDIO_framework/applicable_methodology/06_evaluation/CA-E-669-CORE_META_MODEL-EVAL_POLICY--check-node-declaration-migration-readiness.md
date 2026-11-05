---
atom_id: CA-E-669
ref_id: CA-E-669
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Node
tier: 3
status: Active
version: 4
updated_at: 2026-11-02 17:54:42 +0400
carrier_destination:
  file:
    name: CA-E-669-CORE_META_MODEL-EVAL_POLICY--check-node-declaration-migration-readiness.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-669-CORE_META_MODEL-EVAL_POLICY--check-node-declaration-migration-readiness.md
  source_atom_id: CA-E-669
  source_atom_revision: 4
  source_sha256: 6aa807e323a9944d0fe9604e5b02b0f563431f5788f5b7a82c1f534533a41c1d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Check Node Declaration migration readiness

## Claim

### Prose Claim


A migration packet passes only when its selected Node inventory, predecessor dispositions, governing sources and consumer changes are explicit and independently reviewed. Reject incomplete or contradictory coverage; a prepared Draft is not an adopted Declaration.

## Details

Check the proposed governing Drafts and exact selected source versions in the selected effective MODEL. Resolve explicit local overrides first. The following checklist states CAPRMEDIO's base rules; an explicit override changes the corresponding criterion in that MODEL:

- Declaration is Requirement/Form: Declaration, with the R prefix; Role and Form remain separate. Every declared member of (Node, Node/**, .**) has exactly one effective Current Declaration after MODEL override resolution and each such Declaration has one matching active Subject. Count only that Form, not all RMED addressing the Node. Drafts and archives do not add Current owners.
- A Node Declaration states its normative constraints in its Claim, preferring admitted formal notation and using prose where existing notation cannot express a constraint without a single-use extension. The Node Claim explicitly forbids IS_PROPERTY_OF cycles, including self-loops; no dedicated acyclicity predicate is required. A repetitive prose Claim or Semantics is not mandatory. CFEL retains a Claim and may have Semantics. Unchanged inherited Properties reuse their original Declaration. Explicit local MODEL replacements are selected in that MODEL; the base remains unchanged. Effective inherited rules do not create new declaration responsibilities.
- Each effective Relation whitelist resolves its inherited permissions, directions, endpoints and both cardinalities. Reject unlisted Relations, contradictory refinements, Property bearer cycles, multiple bearers, Property narrowing/instantiation and direct Primary Node values.
- Preserve / narrowing and // instantiation for Primary Nodes, . Property access, +>/<+ composition and >|/|< classification. Check branch selectors, condition versus conclusion, and independent value/dependent-name domains and counts. Reject withdrawn .. syntax. Accept := in Subject addresses for allowed value and condition together; Formal Claims retain separate : and = meanings. Full Formal Claims do not belong in Subjects.
- Each Workflow has at least one Step; each Step has one Workflow. Each Step exclusively RUNS exactly one Action, RUNS exactly one Workflow, or contains at least one Substep and RUNS neither an Action nor a Workflow. A Step's Action or Workflow mode receives parameters only from previous Step outputs, enclosing Workflow Run input, or values fixed by that Step. Each Substep has one Step and RUNS exactly one Action. Actions allow zero or more Step/Substep callers; Workflows allow zero or more Step callers. Use IS_CONTAINED_BY with derived CONTAINS and Container: yes/no. Reverse views do not duplicate authored facts; a RUNS binding does not prove execution.
- Verify scalar-only, child-only and mixed Properties in YAML and Markdown, including one child with two values versus two child keys, skipped heading levels and fenced heading-like text. Undecided defaults or lossless retrieval policies block their affected acceptance cases.
- Verify Role/Form and active/passive carrier migration and all actual schema, parser, graph-builder, SDK/workflow and fixture consumers together. Check ENGINE permissions against its effective declared Scope under the selected MODEL. A local MODEL does not automatically widen that Scope; an explicit override is evaluated normally. Target Scope does not expand authority.
- Check that HAS_VALUE binds instance Property literals without declaring value Nodes; exact new Subject bindings and any incomplete whitelist before adopting affected rules. Establish replacement Declaration coverage and repair references before retiring the corresponding Node Definitions. Do not blanket-retire Terms, Carrier or CFEL.

Report Draft consistency, source adoption, parser conformance, graph reconstruction and runtime admission separately, with reproducible evidence. This Evaluation Draft neither performs those checks nor records a passing result.

### Review phases

The current model review checks declarations, notation and constraints using examples. Review and migration of actual Workflow, Step, Substep and Action instances are deferred. Record model-review findings separately from later instance/implementation migration readiness; do not fail the bounded model review merely because deferred instance review has not run, or report migration readiness on the strength of model review alone.

### CFEL v2 checks

- Separate expressions use semicolons.
- Formal blocks in Claim use the CFEL label.
- Claim has no separate Formal Claim heading.
- Content values use markdown.
- Values follow colon.
- Property occurrence precedes colon.
- Immediate dependent names use *.
- Recursive dependent names use **.
- Name counts are separate from value counts.
- Sibling names are unique.
