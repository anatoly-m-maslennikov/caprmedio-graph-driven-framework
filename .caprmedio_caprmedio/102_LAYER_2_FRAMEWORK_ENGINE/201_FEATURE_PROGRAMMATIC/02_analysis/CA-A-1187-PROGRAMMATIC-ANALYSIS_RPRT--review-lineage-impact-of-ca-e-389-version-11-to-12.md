---
atom_id: CA-A-1187
content_role: Analysis
type: Analysis Report
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Done
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-15 22:40:50 +0400"
llm_session_ids: ["codex:01a01cb4-e15e-78d1-9084-766bf6b0cd63"]
subjects:
  governs: "Lineage Impact Analysis"
  depends_on: ["Atom", "Atom/Revision"]
relations:
  relates_to: [CA-E-389]
---
# Summary

Review lineage impact of CA-E-389 version 11 to 12

## Scope

One changed parent: CA-E-389@11 to CA-E-389@12. This Analysis does not declare runtime or behavioral test completion.

## Conclusion

The examined current-source-reference frontier reaches a fixed point after the stated dependent update, if any. Existing malformed carriers, undeclared Scope Units and disputed Claims recorded by the RED review remain held; this conclusion grants none of their dependent gates permission to run.

## Change classification and authority

Change class: `semantic_revision`, because Local/Global Tier changes normative applicability while the same complete primary Claim and exact Summary remain recognizable. This is not carrier-only recoding and not replacement of the existing Claim. Core6 to General7 with byte-identical complete acceptance specification. Newly admitted Core invariants CA-E-637/CA-E-638 are entailed by the prior specifications; no independently replaceable Claim is removed from the existing identity.

Responsible Operator: Anatoly Maslennikov. The Operator requested the same active-RED tier review and explicitly selected Core/General separation for E389/E536. Codex performed the bounded direct-file continuation; no MCP Run or earlier Draft admission is claimed.

Session: `codex:01a01cb4-e15e-78d1-9084-766bf6b0cd63`.

## Exact parent revisions

- Previous: `CA-E-389@11`, `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/archive/CA-E-389-PROGRAMMATIC-CORE-EVAL_APPROACH--combine-complementary-software-behavior-evidence@11.md`, SHA-256 `b72379418548f3dab5a33b3315baac188f5d52d631f7ea10d960e50b4fb147c3`.
- New: `CA-E-389@12`, `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-389-PROGRAMMATIC-GENERAL-EVAL_APPROACH--combine-complementary-software-behavior-evidence.md`, SHA-256 `4f21ae74c2f07bca6b78d7b79070804afba10d2b851a15fbae7efbd70fd68d23`.
- Verification: previous bytes retained exactly; complete bodies compare byte-for-byte equal. Only tier, Version/time and the corresponding current filename differ.

## Expected impact radius

Current admitted source references to this exact parent identity in `.caprmedio_caprmedio`, with archive/archived/Draft/evidence/projection/completed-work carriers excluded. Review also considered the exhaustive 313-Atom current Active PROGRAMMATIC RED frontier and the live scope/tier rules; no global ownership, missing target, historical receipt or runtime repair is inferred.

The reference scan is not a generated graph or a runtime conformance proof. Historical-only references are retained rather than retargeted. No production Python/JSON implementation consumer of the three changed Evaluation IDs was found.

## Examined child revisions and dispositions

```json
[
  {
    "examined_child": "CA-A-978@1",
    "path": ".caprmedio_caprmedio/02_analysis/CA-A-978-ANALYSIS_RPRT--harvest-the-final-tool-policy-follow-up.md",
    "sha256": "06d55972890a022ce18d5e93e368a64850d41ed10ddb0a9d5b91fc8009a846af",
    "disposition": "compatible",
    "basis": "Stable-ID reference retains the same complete portfolio/canary acceptance specification; historical observations remain observations. No current path, frozen-version or Core-only binding is changed.",
    "resulting_revision": null,
    "recursive_result": "stop: child unchanged"
  },
  {
    "examined_child": "CA-A-1075@2",
    "path": ".caprmedio_caprmedio/02_analysis/CA-A-1075-ANALYSIS_RPRT--reconcile-implementation-and-functional-runtime-guarantees.md",
    "sha256": "25cf631e5749a6cf5f63bfa541b011a81512c0e1288d1db631dd5ae88993f7e3",
    "disposition": "compatible",
    "basis": "Stable-ID reference retains the same complete portfolio/canary acceptance specification; historical observations remain observations. No current path, frozen-version or Core-only binding is changed.",
    "resulting_revision": null,
    "recursive_result": "stop: child unchanged"
  },
  {
    "examined_child": "CA-P-2281@2",
    "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/03_plan/02-CA-P-2281-FRAMEWORK_ENGINE-EPIC--implement-rmed-guided-engine-workflow.md",
    "sha256": "b1ea39a55f843e13eb4ebe97c6c83de36cd754c13aa930f1d0b02597ef068d36",
    "disposition": "compatible",
    "basis": "Stable-ID reference retains the same complete portfolio/canary acceptance specification; historical observations remain observations. No current path, frozen-version or Core-only binding is changed.",
    "resulting_revision": null,
    "recursive_result": "stop: child unchanged"
  },
  {
    "examined_child": "CA-E-637@1",
    "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/06_evaluation/CA-E-637-PROGRAMMATIC-CORE-EVAL_APPROACH--require-observable-evidence-for-behavioral-acceptance.md",
    "sha256": "7591a1a808599240ee21a945b3c8fc2c457fe0bc0491c82086ebdc40d53b39e9",
    "disposition": "compatible",
    "basis": "Stable-ID reference retains the same complete portfolio/canary acceptance specification; historical observations remain observations. No current path, frozen-version or Core-only binding is changed.",
    "resulting_revision": null,
    "recursive_result": "stop: child unchanged"
  },
  {
    "examined_child": "CA-M-285@13",
    "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/archive/CA-M-285-PROGRAMMATIC--select-software-evaluation-techniques-by-failure-mode@13.md",
    "sha256": "ea8701cf82a1a6318034073f24668b72e95c9a5b7a2b9553d40b157b9a0bcf0f",
    "disposition": "update_required",
    "basis": "Old Core filenames and tier-only description required explicit Core invariant plus retained General criteria bindings. Same aggregate acceptance contract is preserved.",
    "resulting_revision": "CA-M-285@14",
    "result_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/05_method/CA-M-285-PROGRAMMATIC--select-software-evaluation-techniques-by-failure-mode.md",
    "result_sha256": "7758edf1da83e8d4c553bedb524fb9d623cb4292915b649bcfb751f123dfebbd",
    "recursive_result": "compatible: referenced criteria remain exact prior bodies; the Method adds no policy, gate or test quota. Retained source-reference consumers remain valid under the equivalent combined policy."
  },
  {
    "examined_child": "CA-P-2286@2",
    "path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/03_plan/02-CA-P-2281-FRAMEWORK_ENGINE-EPIC--implement-rmed-guided-engine-workflow/05-CA-P-2286-FRAMEWORK_ENGINE-TASK--compile-the-evaluation-policies.md",
    "sha256": "dc240399e8260ea53e7345e54d9e5f90374c9517d2319e80a27771ec4cac98c5",
    "disposition": "compatible",
    "basis": "Stable-ID reference retains the same complete portfolio/canary acceptance specification; historical observations remain observations. No current path, frozen-version or Core-only binding is changed.",
    "resulting_revision": null,
    "recursive_result": "stop: child unchanged"
  }
]
```

## Recursive result and fixed-point boundary

Every examined branch is either unchanged-compatible or reaches the explicitly recorded compatible resulting Method Revision. No replacement identity or automatic execution/retry was introduced. No new blocking Concern was needed for these changed branches; unrelated pre-existing review holds remain separate and unresolved.

The LIA records its conclusion and source evidence, not evidence of its own correctness. Independent source review and byte/hash/link checks are separate verification. Full tests, live gates, graph compilation, MCP refresh, publication and runtime validation are outside this conclusion.

## Sources

CA-R-1432, CA-R-1633, CA-R-1037, CA-R-1029, CA-R-1632, CA-R-1032, CA-R-1033, CA-R-1038, CA-R-1039 and CA-R-1497; current tier definitions CA-R-659/CA-R-1431/CA-R-660/CA-R-794. Frozen review frontier: `.caprmedio_caprmedio/_projection/programmatic-red-tier-review/inventory.json`.
