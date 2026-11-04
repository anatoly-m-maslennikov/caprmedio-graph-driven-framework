---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Step Run.Agentic Step Execution Context
  passive:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action).Execution Kind'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Step Run
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
version: 19
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-R-2521
  - CA-R-1527@21
  - CA-R-2465
atom_id: CA-E-495
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-495-CORE_META_MODEL-EVAL_CASE--validate-action-kinds-and-step-contexts.md
  source_atom_id: CA-E-495
  source_atom_revision: 19
  source_sha256: bd67de991dfb53e31b0c79499ad79bad07d2bf83b41845e4c0c20ebb4569dedc
  original_relations_sha256: 0e037e86c7c29169ac144d5338987d631ee62c6dcfc5849c80d229423350217f
---
## Summary

Validate Action kinds and Step contexts

## Claim

### Prose Claim


Action Execution Kind **and** Agentic Step Execution Context.


the Evaluation **must** check that Action Execution Kind **and** Agentic Step Execution Context remain distinct **and** support reuse **without** duplicate definitions.

## Details

- a Programmatic Action interacts with the Operator through code **without** AI judgment: accept Programmatic classification.
- code delegates the declared responsibility's judgment **to** an AI Agent: require Agentic classification rather than classifying by the surrounding code.
- two Steps invoke the same Agentic Action **in** Integrated **and** Isolated contexts with valid bindings: accept the shared Action identity **and** distinct invocation contexts.
- one Workflow mixes Programmatic, Integrated Agentic, **and** Isolated Agentic Steps: accept **without** a Workflow-wide context classification.
- missing **or** unavailable required context: block execution admission; do **not** silently select a substitute **or** classify a well-formed definition as malformed merely because a worker is unavailable.
- a Tool call appears inside an Agentic leaf Step Run: retain **`=1`** declared Action **and** its **`=1`** Action Run for that Step rather than inferring another Step from the call.
- choosing Isolated grants additional permission, suppresses required Operator input, **or** permits concurrent mutations automatically: reject.

use definition fixtures **and** invocation evidence. these checks do **not** claim that an executor Implementation has been tested.
