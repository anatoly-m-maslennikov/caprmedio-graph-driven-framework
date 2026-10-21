---
atom_id: CA-C-547
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Resolved
priority: high
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2401, CA-P-2478]
version: 2
updated_at: "2026-10-20T20:10:17.734Z"
---
# Summary

Resolve selected lifecycle Current carrier failures

## Concern

Independent P2478 regression acceptance passes Draft promotion golden 22/22 and Atom operation cohort 30/30, but the broader selected lifecycle cohort has 18 errors and one failure across 48 tests. Do not describe the combined portfolio as green or infer a deployed incident from this isolated source/fixture check.

## Evidences

The 18 errors report CurrentAtomLocatorError, Atom identity does not resolve to exactly one current carrier, wrapped as complete-carrier-invalid. The model contradiction case expects model-forged but receives complete-carrier-invalid. No source/test edit occurred during acceptance. Frozen production SHA-256: atom_operations.py 4d25dae0e7efb8e6d36755902af1ae11178d18a982f54d6a926e7aa71d11d31e; lifecycle_intents.py 457e77c536a4330918bd53bd0004bd58973048c31035172c12e9eb2e2355c83c.

Exact pre-extraction HEAD reproduction and fixture Current-identity diagnosis are pending. This evidence does not yet establish a regression, a fixture-only cause, or permission to weaken the locator/complete-carrier guard. No production port, MCP effect, Docker, release, deployment or replay was involved.

## Blast radius

The selected-lifecycle functional acceptance gate is not passing. Preserve frozen-corpus isolation, exact source pins, authority closure and strict carrier validation. Identify the exact missing or ambiguous identity and compare the unchanged HEAD baseline before preparing a bounded correction. Existing full-release and runtime status remain separate.

### Resolution checkpoint

P2488 added only the missing frozen D288/D378 support-carrier overlay to shared test setup, with SHA-256 verification and no live Atom dependency. Exact HEAD reproduced all previous 48-case/9-case failures before correction. Independent final-hash reruns now pass 48/48 selected lifecycle and 9/9 version-history cases. This resolves the bounded fixture cause, not runtime adoption, all release gates or unrelated typing debt. Final fixture SHA-256 79925d47d09c43a524bab2cb0928460e0dad308b009029743a3db6059daf92be; lifecycle 568516545c8bbd870d9022d157bcdb6382a394da46420458251cd341a7aff4ea. No production guard was weakened.
