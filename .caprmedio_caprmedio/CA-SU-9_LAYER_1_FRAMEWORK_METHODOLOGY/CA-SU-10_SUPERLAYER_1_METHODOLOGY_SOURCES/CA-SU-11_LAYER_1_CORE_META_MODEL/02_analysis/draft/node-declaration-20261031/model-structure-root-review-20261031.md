# MODEL and PROJECT STRUCTURE — 2026-10-31

The two Primary Node kinds are declared in CAPRMEDIO's self-describing MODEL. Named roots are their instances. A consumer MODEL is optional and may override any inherited rule locally; unchanged inherited Declarations are reused. Ownership is evaluated per effective MODEL.

Core Meta-Model contains the Atoms defining CAPRMEDIO's MODEL. PROJECT STRUCTURE describes Scope Structure, Aspects and further declared components. ENGINE Scope does not widen automatically through MODEL inheritance.

[MODEL Declaration](../../../04_requirement/draft/node-declaration-20261031/primary-expansion/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-model.md) · [PROJECT STRUCTURE Declaration](../../../04_requirement/draft/node-declaration-20261031/primary-expansion/CA-R-draft-CORE_META_MODEL-DECLARATION--declare-project-structure.md) · [Architecture decision](declaration-expansion/model-structure-root-decision.json) · [Independent review](declaration-expansion/model-structure-root-review.json)

The bounded review and Draft structure checks pass:108 Drafts,27 Primary and47 Property Declarations. The separately recorded Scope Unit Navigation Number withdrawal is preserved. All750 snapshotted Current Core Requirements and Current Epic38 are unchanged.

MODEL inheritance Relation naming, effective MODEL selection and override binding remain open. No promotion, source migration, directory move, parser or runtime implementation was performed.
