---
atom_id: CA-A-1191
content_role: Analysis
type: Analysis Report
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Done
author: Anatoly Maslennikov
version: 1
updated_at: 2026-10-15 23:27:39 +0400
subjects:
  governs: Lineage Impact Analysis
  depends_on:
  - Atom
  - Atom/Revision
relations:
  relates_to:
  - CA-M-284
---
# Summary

Review lineage impact of CA-M-284 version 14 to 15

## Question

What is the impact state of the exact CA-M-284@14 to CA-M-284@15 tier-authority repair?

## Scope

The changed Method and its current non-archived source-reference frontier, plus stable-ID runtime/configuration consumers in `_projection/programmatic-method-tier-fix/consumers.json`. Not a global graph or runtime-conformance review.

## Approach

Change class: `semantic_revision`, not replacement. Previous Local/Global Tier was uncarried/unresolved, despite legacy CORE filename tokens. New explicit authoring disposition: PROGRAMMATIC General/global7 and Claim Target Scope Unit PROGRAMMATIC under D482. Exact Summary, complete Claim, applicability, supporting clauses, Subjects and necessary relations remain. No independently replaceable Claim is extracted, narrowed or transferred. Required metadata/headings, admitted Implementation Method Type/canonical filename, and retired-field removal are accompanying lossless carrier repairs.

Responsible Operator: Anatoly Maslennikov. The Operator explicitly requested these three tier repairs, possible splits and a projection rebuild, with a 95% confidence floor. Session: `codex:01a01cb4-e15e-78d1-9084-766bf6b0cd63`. Codex used bounded direct-file continuation; no MCP mutation Run, Draft-history admission or Journal-completeness check is claimed.

Authority: M272@14; R659@21/R1431@12/R660@17/R1669@18; R1432@13; R1633@22/R1037@14; R1667@21/R1767@19/D404@9; D276@18/D479@8. Confidence: 96%.

M389 owns the validated read-only Settings boundary and immutable derived snapshot; M387/M392 own canonical ownership and effect separation. D365/R1683 separately own currentness/Journal judgments. This complete Reader contract specializes those premises.

Exactly two full-contract realization witnesses: An in-process typed Reader library; a centralized Reader service with typed clients. Both return actual values, selected Project, physical path, raw digest and schema marker without Journal/currentness decisions.

Changed shared-contract witness preserving Core: Make physical-path output optional with an otherwise exact recoverable source binding; that changes this General contract without changing Core ownership or read-only boundaries.

The contract constrains applicable Standard construction, checks, Delivery, Plans, Operations and Implementation across Content Roles, not a role-filtered population. These are classification witnesses, not tested runtime realizations. Repeating a higher-tier foundation does not require another Core identity; no split is needed.

## Results

### Exact parent revisions

- Previous: `CA-M-284@14`, `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/archive/CA-M-284-PROGRAMMATIC-CORE-METHOD--read-engine-settings-through-one-shared-boundary@14.md`, SHA-256 `511958b7bb1701039215209b3be552a4b25485c48d56d19fab10c5a95564ed98`.
- New: `CA-M-284@15`, `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-284-PROGRAMMATIC-GENERAL-IMPLEMENTATION_METHOD--read-engine-settings-through-one-shared-boundary.md`, SHA-256 `f49dd59b4874074fd6fca548aa3f7a1a7f7babe090dd52496c8f14d7714342bc`.
- Exact predecessor bytes retained. Verification reconstructs Summary/Scope/Claim/Details from the old title/lead/applicability/supporting sections: every substantive clause remains, with only headings, governed metadata and filename changed.
- M281/M284 retain their M110 parent; no same-tier Method prohibition was found, and Requirement-specific R829 is not generalized. M110 retains Project M261 parent coverage. This does not resolve the pre-existing cross-scope validator/model tension.

### Examined child revisions and dispositions

```json
[
  {
    "examined_revision": "CA-C-184@4",
    "path": ".caprmedio_caprmedio/01_concern/CA-C-184-QUESTION--what-settings-sources-and-provenance-must-the-shared-reader-cover.md",
    "sha256": "50f689022dc6a623a063c684237f61daf5ab7dda619653182d4677d6f0c102da",
    "disposition": "compatible",
    "basis": "Stable ID remains valid; historical observations are retained, not made current authority. No runtime tier/version/digest pin was found.",
    "resulting_revision": null,
    "recursive_result": "stop: unchanged or content-equivalent reference; complete Method contract preserved"
  },
  {
    "examined_revision": "CA-A-925@1",
    "path": ".caprmedio_caprmedio/02_analysis/CA-A-925-ANALYSIS_RPRT--harvest-the-whole-third-partition-draft-review-report.md",
    "sha256": "e1178f292986d89e899c1ddbb0fd67965ecc97a099689e4c86a94d126e4a1f92",
    "disposition": "compatible",
    "basis": "Stable ID remains valid; historical observations are retained, not made current authority. No runtime tier/version/digest pin was found.",
    "resulting_revision": null,
    "recursive_result": "stop: unchanged or content-equivalent reference; complete Method contract preserved"
  },
  {
    "examined_revision": "CA-P-2354@3",
    "path": ".caprmedio_caprmedio/03_plan/18-CA-P-1959-EPIC--improve-entity-model-stage-2/30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/39-CA-P-2280-TASK--implement-complete-configuration-read/01-CA-P-2300-TASK--bind-complete-configuration-read-to-receiving-context/done/01-CA-P-2354-TASK--align-settings-inspection-schema-and-source.md",
    "sha256": "889dff791a879893c015ef27afea4ad11a7d7492def4aea7a533dc1040c81403",
    "disposition": "compatible",
    "basis": "Stable ID remains valid; historical observations are retained, not made current authority. No runtime tier/version/digest pin was found.",
    "resulting_revision": null,
    "recursive_result": "stop: unchanged or content-equivalent reference; complete Method contract preserved"
  },
  {
    "examined_revision": "CA-C-276@3",
    "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/01_concern/CA-C-276-FRAMEWORK_ENGINE-QUESTION--how-should-the-shared-settings-reader-draft-be-reconciled.md",
    "sha256": "d48b817367b12c041131ef4f73d61287e4e3164642fd6be767a7048b829f8ed8",
    "disposition": "compatible",
    "basis": "Stable ID remains valid; historical observations are retained, not made current authority. No runtime tier/version/digest pin was found.",
    "resulting_revision": null,
    "recursive_result": "stop: unchanged or content-equivalent reference; complete Method contract preserved"
  },
  {
    "examined_revision": "CA-M-389@2",
    "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-389-PROGRAMMATIC-CORE--pass-validated-configuration-through-one-shared-boundary.md",
    "sha256": "83cf8d0fb3a4b637b95ed8b7d24464030ae6815a5f5e29ea062b68d7bc56381d",
    "disposition": "compatible",
    "basis": "Stable ID remains valid; historical observations are retained, not made current authority. No runtime tier/version/digest pin was found.",
    "resulting_revision": null,
    "recursive_result": "stop: unchanged or content-equivalent reference; complete Method contract preserved"
  },
  {
    "examined_revision": "CA-E-454@5",
    "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/archive/CA-E-454-PROGRAMMATIC-QA_CASE--use-one-settings-reader-across-engine-software@5.md",
    "sha256": "8964fed68dec1582d62dc7d05bba7688c973b687da96d994e683e78b1741fd18",
    "disposition": "update_required",
    "basis": "Same full Claim/stable identity; current-reference repair or separately reviewed whole-contract Method tier repair only.",
    "resulting_revision": {
      "revision": "CA-E-454@6",
      "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-454-PROGRAMMATIC-QA_CASE--use-one-settings-reader-across-engine-software.md",
      "sha256": "c0520b6918b5fbded7968239ca9719731358c548ab704e679b3380f4d34a46ec"
    },
    "recursive_result": "compatible: resulting reference-only revision or complete-contract Method revision preserves this parent contract; no further semantic propagation"
  }
]
```

### Recursive result and fixed point

All examined branches are unchanged-compatible or reach the pinned content-equivalent reference repair/complete-contract Method revision. Five Evaluation links target canonical current Method filenames. D250's filename-qualified M281 token is normalized to the same stable ID. No behavioral Claim, concrete test or runtime consumer changes. Runtime/configuration references are stable-ID only and remain unchanged. The compact Methods projection is regenerated from current sources; historical archives, observations and Journal pins remain historical.

No successor or blocking Concern was needed for this delta. Unrelated legacy metadata/Subjects and retained Project-parent modeling tension are not pronounced valid. This conclusion covers the examined reference frontier, not full validator, graph, live MCP or runtime acceptance.

## TLDR

General/global7; unchanged identity and complete policy; no Core split. Exact predecessor, current-reference repairs and regenerated non-authoritative projection are retained. Source-preservation/metadata/link checks and independent Method/projection review passed; no full runtime suite or graph/MCP reload was run.
