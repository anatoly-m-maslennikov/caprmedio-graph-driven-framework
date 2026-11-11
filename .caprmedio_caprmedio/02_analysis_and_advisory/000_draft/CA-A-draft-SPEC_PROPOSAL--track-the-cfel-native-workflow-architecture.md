---
identity:
  atom_id: CA-A-draft
context:
  container:
    scope_unit: CA-SU-00
  role: Analysis & Advisory
  form: Spec Proposal
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Execution Control
  tier: 3
state:
  status: Draft
  version: 1
  updated_at: 2026-11-11 04:14:10 +0400
destination:
  file:
    name: CA-A-draft-SPEC_PROPOSAL--track-the-cfel-native-workflow-architecture.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory/000_draft
author: Anatoly Maslennikov
---

## Summary

Track the CFEL-native Workflow architecture

## Proposal

Tracking only. The linked standalone Draft Atoms contain the proposed architecture and its claims. This record does not duplicate or adopt those claims. All candidates remain Draft; no Current Goal, Scope Delegation, Solution, registry, directory topology or runtime is changed.

## Draft index

| Draft | Form | Proposed owner | Tier | Status |
|---|---|---|---:|---|
| [G1: Execute inspectable Workflows from formal definitions](../../CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement/draft/cfel-native-workflow-architecture/CA-R-draft-FRAMEWORK_ENGINE-GOAL--execute-inspectable-workflows-from-formal-definitions.md) | Goal | FRAMEWORK_ENGINE | 0 | Draft |
| [G2: Provide reusable internal Action implementations](../../CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/draft/cfel-native-workflow-architecture/CA-R-draft-PROGRAMMATIC-GOAL--provide-reusable-internal-action-implementations.md) | Goal | PROGRAMMATIC | 0 | Draft |
| [G3: Provide consistent public Workflow access](../../CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/draft/cfel-native-workflow-architecture/CA-R-draft-PROGRAMMATIC-GOAL--provide-consistent-public-workflow-access.md) | Goal | PROGRAMMATIC | 0 | Draft |
| [SD1: Delegate internal Tool implementations to TOOLS](../../CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/draft/cfel-native-workflow-architecture/CA-R-draft-PROGRAMMATIC-SCOPE_DELEGATION--delegate-internal-tool-implementations-to-tools.md) | Scope Delegation | PROGRAMMATIC | 3 | Draft |
| [SD2: Delegate application composition to APPS](../../CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/draft/cfel-native-workflow-architecture/CA-R-draft-PROGRAMMATIC-SCOPE_DELEGATION--delegate-application-composition-to-apps.md) | Scope Delegation | PROGRAMMATIC | 3 | Draft |
| [SD3: Delegate native Workflow execution to WORKFLOW_ENGINE](../../CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement/draft/cfel-native-workflow-architecture/CA-R-draft-APPS-SCOPE_DELEGATION--delegate-native-workflow-execution-to-workflow-engine.md) | Scope Delegation | APPS | 3 | Draft |
| [SD4: Delegate public Workflow exposure to MCP](../../CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement/draft/cfel-native-workflow-architecture/CA-R-draft-PROGRAMMATIC-SCOPE_DELEGATION--delegate-public-workflow-exposure-to-mcp.md) | Scope Delegation | PROGRAMMATIC | 3 | Draft |
| [S1: Use formal CFEL Workflow definitions as executable contracts](../../CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/05_method/draft/cfel-native-workflow-architecture/CA-M-draft-FRAMEWORK_ENGINE-SOLUTION--use-formal-cfel-workflow-definitions-as-executable-contracts.md) | Solution | FRAMEWORK_ENGINE | 0 | Draft |
| [S2: Execute formal Workflows with one generic engine](../../CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/05_method/draft/cfel-native-workflow-architecture/CA-M-draft-APPS-SOLUTION--execute-formal-workflows-with-one-generic-engine.md) | Solution | APPS | 0 | Draft |
| [S3: Expose selected Workflows as MCP Tools](../../CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method/draft/cfel-native-workflow-architecture/CA-M-draft-MCP-SOLUTION--expose-selected-workflows-as-mcp-tools.md) | Solution | MCP | 0 | Draft |
| [S4: Continue interactive Workflows in the calling session](../../CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/05_method/draft/cfel-native-workflow-architecture/CA-M-draft-FRAMEWORK_ENGINE-SOLUTION--continue-interactive-workflows-in-the-calling-session.md) | Solution | FRAMEWORK_ENGINE | 0 | Draft |
| [S5: Implement Actions through internal Tool APIs](../../CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/05_method/draft/cfel-native-workflow-architecture/CA-M-draft-TOOLS-SOLUTION--implement-actions-through-internal-tool-apis.md) | Solution | TOOLS | 0 | Draft |

The keys G1–G3, SD1–SD4 and S1–S5 are local tracking labels, not Atom IDs. The identity-free Drafts receive stable identities only through their applicable adoption process. Companion links identify candidate relationships; formal governing relations and their ordering must be completed before Current adoption.

## Adoption checklist

- [ ] Review the actual Draft claims for one contribution each, duplication, Role/Form, Scope, Tier and exact Subject admission.
- [ ] Resolve Core executable-CFEL declarations and the native Decision exception to leaf RUNS rules; declare the candidate RUN/RETURN/input/output constructs and validate references/branch outputs before any executable exposure.
- [ ] Adopt needed direct-parent Scope Delegation amendments before relying on new Method / Solution permissions. Allocate a fresh WORKFLOW_ENGINE Scope Unit identity only when its declaration and required Goal/structure are accepted; do not reuse retired CA-SU-2.
- [ ] Add the appropriate governing relations after stable identities exist, and verify Tier-0 ordering instead of treating the requested tier as automatic permission.
- [ ] Reconcile affected Current MCP registration and Step/carrier contracts before replacing them. The Current registry is not silently reinterpreted by these Drafts.
- [ ] Create role-appropriate Evaluations for the accepted changes before implementation. Keep source adoption, implementation, isolated tests, image build and live acceptance as separate results.
- [ ] Keep workflow-engine implementation and SQL UPDATE deferred until separately authorized. Existing SQL UPDATE proposals, the read-only working image and its live acceptance are outside this Draft package.

## Solution admission checks

Each row remains an unchecked adoption gate. Current permission does not establish governing-relation order.

| Draft | Containing Scope Unit | Exact Main Subject | Method / Solution permission | Tier-0 governing order |
|---|---|---|---|---|
| S1 | FRAMEWORK_ENGINE (CA-SU-14) | `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control` | [ ] Current CA-R-2653 permits this Role/Form; verify exact Subject at adoption | [ ] Unresolved: add and verify governing relations and ordering |
| S2 | APPS (CA-SU-20) | `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control` | [ ] Current CA-R-2659 does not permit Method / Solution; requires SD2 adoption and exact Subject verification | [ ] Unresolved: add and verify governing relations and ordering |
| S3 | MCP (CA-SU-21) | `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts` | [ ] Current CA-R-2660 permits this Role/Form; verify exact Subject at adoption | [ ] Unresolved: add and verify governing relations and ordering |
| S4 | FRAMEWORK_ENGINE (CA-SU-14) | `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts` | [ ] Current CA-R-2653 permits this Role/Form; verify exact Subject at adoption | [ ] Unresolved: add and verify governing relations and ordering |
| S5 | TOOLS (CA-SU-16) | `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts` | [ ] Current CA-R-2655 grants no Solution; requires SD1 adoption and exact Subject verification | [ ] Unresolved: add and verify governing relations and ordering |

## Source context and tracking

Relevant current contracts include CA-R-3000, CA-R-3002, CA-R-3006, CA-R-2125, CA-R-2132, CA-R-2464, CA-R-2465, CA-R-2639, CA-R-2616, CA-R-1800, CA-R-3013, CA-M-506, CA-D-704, CA-E-798, CA-R-1107 and CA-R-1114. These references identify review inputs; they are not copied specifications.

Current discovery behavior remains the Operator's all-control-root Current/Draft filename discovery with first-loaded duplicate and later-copy issue diagnostics, without a new path or version preference. Current schema/model regeneration on every image build remains in force. This proposal does not change that behavior or turn its tracking text into a model Declaration.

Preparation occurred outside the repository. Publication requires a released source-write hold and verified final file creation; neither source adoption nor runtime activation follows from publication. The package contains no Current source edit, source migration, installed implementation, image or deployment result. The annotation about indentation is captured by the actual CFEL Method Draft S1.
