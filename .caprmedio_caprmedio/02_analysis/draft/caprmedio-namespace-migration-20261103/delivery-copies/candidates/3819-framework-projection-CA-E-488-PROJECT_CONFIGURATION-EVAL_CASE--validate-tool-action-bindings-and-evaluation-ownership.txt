---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Package
  passive:
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - CAPRMEDIO <+ STRUCTURE <+ Entity/Object/Continuant/Selection//Methodology Sources
  - CAPRMEDIO <+ MODEL <+ Scope Unit
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Operations)
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Evaluation)
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Traceability
version: 25
updated_at: 2026-11-02 18:35:20 +0400
relations:
  evaluation_for:
  - CA-R-1515
  - CA-R-1800
  - CA-R-1517
  - CA-R-1518
atom_id: CA-E-488
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 4
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/06_evaluation/CA-E-488-PROJECT_CONFIGURATION-EVAL_CASE--validate-tool-action-bindings-and-evaluation-ownership.md
  source_atom_id: CA-E-488
  source_atom_revision: 25
  source_sha256: 95d69093f079e28c4070d4d2f66af5a7d8e2cef448300d2f40feea60ef16fd1d
  original_relations_sha256: e06ebb6b9927438ff6a5af45051efe79945ea1a9a4585f67c5bf0d4ba08e6062
---
## Summary

Validate Tool Action bindings and Evaluation ownership

## Claim scope

a CAPRMEDIO Tool's methodology binding **and** Evaluation responsibility.

## Claim

the Evaluation of a CAPRMEDIO Tool's methodology binding **must** check the canonical Action owner, binding cardinality, **and** division of Evaluation responsibility under CA-R-1515-PROJECT_CONFIGURATION-RULE--keep-canonical-actions-and-workflows-in-methodology, CA-R-1800-PROJECT_CONFIGURATION-RULE--bind-every-tool-to-one-methodology-action, CA-R-1517-PROJECT_CONFIGURATION-RULE--keep-tool-operational-authority-outside-its-own-subtree, **and** CA-R-1518-PROJECT_CONFIGURATION-RULE--separate-methodology-and-tool-evaluation-responsibilities.

## Details

### Cases and expected results

- the Tool implements **`=1`** resolvable applicable Action owned by a methodology source outside the Tool's subtree: pass the binding check.
- the Tool has **`=0`** **or** **`>1`** implemented Action bindings, an unresolved definition, **or** a copied operational definition owned by the Tool: fail.
- an implementation reference targets an O Atom owned by the Tool's Scope Unit **or** a descendant: fail. a methodology Evaluation checking its own O definition **must not** fail this Tool-only containment rule.
- Tool Evaluations check the Tool's realization of its Action while methodology Evaluations check the operational definitions: pass the responsibility check.
- a Tool Evaluation independently owns Action **or** Workflow definition-validity rules: fail for misplaced authority; invoking an existing methodology check does **not** transfer that authority.
- a Workflow **contains** an unresolved Step Action **or** an unbounded retry loop: report the defect against the methodology definition through its methodology Evaluation, rather than silently repairing the Workflow inside the Tool's specification.

report binding conformance separately from actual Implementation results. valid ownership **and** references alone **must not** be reported as proof that the Tool works **or** that **all** indirect cycles are absent.
