---
atom_id: CA-A-1217
content_role: Analysis
type: Analysis Report
current_scope_unit: caprmedio
tier: 3
author: Anatoly Maslennikov
status: Done
version: 1
updated_at: '2026-10-24 22:52:23 +0400'
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
relations:
  analysis_for:
  - CA-P-1959
---
# Summary

Report deferred workflow conflict resolution issues

## Question

Where do the current conflict-resolution workflow definitions differ from the Operator's latest direction?

## Scope

The written RMEDO conflict workflow and its assessment, proposal, decision and Evaluation definitions. This is a source review, not a runtime test or a change to conflict-resolution methodology.

The Operator said that workflows should send all conflicts to the Operator, then explicitly deferred O updates and requested this report. Core changes and implementation are not authorized by this report.

## Approach

Read the seven Current sources below on 2026-10-24. Compare their stated behavior with the latest Operator direction. Keep decision ownership separate from permission to carry out a correction. A delegated edit is not automatically an Operator decision about which conflicting Claim should win.

## Results

### Issues

1. **Assessment can choose a winner before asking.** O005, steps 2–3, collects Global Tier and prefers higher-tier authority, then the freshest accepted Claim within those bounds. Its result can therefore classify a conflict as resolved without a new Operator decision. Global Tier is also obsolete; the current numeric Tier orders governing relations, not conflict winners.

2. **The workflow can skip its decision step.** O028 allows `assess → complete` when no unresolved conflict remains. It also allows `propose → correct` when delegation and confidence conditions hold. Combined with O005, these paths can bypass `decide` after an automatic winner was selected. Ordinary no-conflict completion is not the problem; resolving an actual conflict without the Operator is.

3. **Proposal input repeats the old precedence model.** O006, step 1, still takes Global Tier and Updated At from O005. O006 explicitly says a proposal does not authorize or perform a change; it does not itself grant permission. The issue is the inherited assessment and the surrounding workflow path.

4. **The Evaluation expects automatic winners.** E477's first three cases require higher-tier precedence or prefer the newer same-tier Claim. Those expectations would preserve the behavior the Operator now wants workflows to avoid. Its checks for coverage gaps, lost references, missing Evaluations and partial changes remain useful and should not be discarded with those expectations.

### Existing pieces and boundaries

- O007 already requests an explicit Operator decision and distinguishes approval, rejection, revision and no decision. A later workflow change can reuse it; no extra approval Atom is needed.
- R1551 reserves Principle-conflict decisions to the Operator but allows delegated resolution of other conflicts under its conditions. That is broader permission, not a requirement that every workflow use it. This report does not change R1551 or infer a new universal ban.
- R024 still describes conflict resolution through applicability tiers. This is relevant background, not authorization to reinterpret numeric Tier as conflict precedence or to rewrite this Requirement.

### Deferred follow-up

When O updates are resumed, review O005, O006, O028 and E477 together. Separate detection and proposals from the Operator's resolution, then execution of that resolution. Preserve no-conflict completion, useful coverage checks and reporting of partial effects. Do not add per-Atom approvals, a new precedence model or extra history gates.

No O, R or E source listed here was changed for this report. No runtime behavior was inspected or executed. Report completion does not mean the deferred workflow fixes are implemented.

### Sources observed

Paths identify the authoritative source files, not derived copies. Versions are observations for this report, not fixed runtime pins.

- [O005, version 19 — Assess source conflicts](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION/09_operations/CA-O-005-PROJECT_CONFIGURATION-ACTION--assess-source-conflicts.md).
- [O006, version 18 — Propose source corrections](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION/09_operations/CA-O-006-PROJECT_CONFIGURATION-ACTION--propose-source-corrections.md).
- [O007, version 17 — Obtain source correction decisions](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION/09_operations/CA-O-007-PROJECT_CONFIGURATION-ACTION--obtain-source-correction-decisions.md).
- [O028, version 21 — Resolve RMEDO conflicts without leaving gaps](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION/09_operations/CA-O-028-PROJECT_CONFIGURATION-WORKFLOW--resolve-rmedo-conflicts-without-leaving-gaps.md).
- [E477, version 20 — Validate gap-free RMEDO conflict resolution](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/003_PROJECT_CONFIGURATION/06_evaluation/CA-E-477-PROJECT_CONFIGURATION-EVAL_CASE--validate-gap-free-rmedo-conflict-resolution.md).
- [R024, version 19 — Govern Requirement conflicts by tier](../../04_requirement/CA-R-024-RULE--govern-requirement-conflicts-by-tier.md).
- [R1551, version 16 — Reserve Principle-conflict resolution to the Operator](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-1551-CORE_META_MODEL-RULE--reserve-principle-conflict-resolution-to-the-operator.md).

## TLDR

The written workflow can resolve conflicts by Tier/Updated At and bypass the Operator decision step. O007 already provides that step. O updates are deferred; the current report records the issues without applying a new conflict policy.
