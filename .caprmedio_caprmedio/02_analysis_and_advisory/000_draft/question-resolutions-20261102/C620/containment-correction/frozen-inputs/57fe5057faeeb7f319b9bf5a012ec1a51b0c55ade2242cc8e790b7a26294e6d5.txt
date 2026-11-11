---
subjects:
  active: Entity/Aspect/Engineering/Architecture/Component Structure
  passive:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - Package
  - Atom/(.Role := Operations)
  - Entity/Object/Continuant/Package/Project Implementation
  - Atom/(.Role := Evaluation)
  - Entity/Object/Continuant/Selection//Methodology Sources
  - Atom.Content
  - Atom/(.Role := Requirement)
version: 26
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-R-1514
atom_id: CA-E-487
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Evaluation
form: Eval Case
---
## Summary

Validate Workflow-independent Implementation specifications

## Claim scope

the Evaluation of a CAPRMEDIO implementation Spec.

## Claim

the Evaluation of a CAPRMEDIO implementation Spec **must** reject dependence on a production Workflow under CA-R-1514-PROJECT_CONFIGURATION-RULE--keep-implementation-specifications-independent-of-production-workflows.

## Cases and expected results

- the same RMED is satisfied by Implementations produced with different Workflows **or** **without** a formally defined Workflow: neither production choice is a failure by itself.
- an ordinary implementation Requirement delegates a required behavior **to** an O definition outside the permitted exceptions: fail for incomplete RMED authority.
- an implementation Spec requires a particular production Workflow as the condition for conformity: fail for coupling the result **to** its production procedure.
- a Tool's RMED refers **to** the methodology Action it implements under CA-R-1800-PROJECT_CONFIGURATION-RULE--bind-every-tool-to-one-methodology-action **and** CA-R-1517-PROJECT_CONFIGURATION-RULE--keep-tool-operational-authority-outside-its-own-subtree: this permitted realization reference is **not** a production-Workflow dependency.
- a methodology Evaluation checks an Action **or** Workflow definition under CA-R-1518-PROJECT_CONFIGURATION-RULE--separate-methodology-and-tool-evaluation-responsibilities: this permitted evaluation target is **not** a production-Workflow dependency.
- a generic executor consumes different applicable Workflow definitions as inputs while its RMED fully specifies their interpretation under CA-R-1519-CORE_META_MODEL-RULE--require-conforming-workflow-execution: accept this boundary; reject an attempt **to** treat a particular production Workflow as necessary for executor conformity.
- changing a valid Workflow input changes the executed behavior **without** requiring a copied Workflow policy **in** the executor Spec: this is input interpretation, **not** incomplete implementation authority.

identify the exact Claim, reference, **and** violated boundary. incomplete evidence **must not** be reported as a pass.
