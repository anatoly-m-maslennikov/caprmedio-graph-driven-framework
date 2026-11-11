# Workflow responsibility Draft

[Place and Reuse Workflow Definitions](../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft/workflow-responsibilities/CA-R-draft-CORE_META_MODEL-RULE--place-and-reuse-workflow-definitions.md) records the responsibility split and cross-scope Step composition.

The [Current Workflow model Declarations](../../../.caprmedio_tmp/workflow-kinds-20261103/README.md) declare `Workflow/(.Purpose := Runtime)` (CA-R-2734) and `Workflow/(.Purpose := Project)` (CA-R-2735), with the supporting `Workflow.Purpose` Declaration (CA-R-2733) and Workflow parent CA-R-2464 Version 5. Both selections use the same Steps, Substeps and Actions. Purpose does not determine the definition's owning Scope Unit.

- Core: reusable business Workflow meaning.
- Engine: technical Workflows and execution implementation.
- Project: Local/Public Release and other project-specific orchestration.
- Project Steps may call Methodology or Engine Workflows; the callee keeps its owner.

Status: the placement Rule remains Draft; the four Workflow model Declarations were promoted on 2026-11-04. The separate Scope Unit.Scope / R Scope Definition proposal is pending the question about existing non-Project Goals. No runtime change is applied here.
