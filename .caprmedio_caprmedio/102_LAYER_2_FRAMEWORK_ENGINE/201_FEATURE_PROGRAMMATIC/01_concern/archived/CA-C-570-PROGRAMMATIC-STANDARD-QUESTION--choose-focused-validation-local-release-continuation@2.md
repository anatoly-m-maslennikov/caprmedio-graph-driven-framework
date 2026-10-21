---
atom_id: CA-C-570
content_role: Concern
type: Question
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Resolved
priority: medium
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-P-2536, CA-P-2549, CA-P-2550, CA-O-164]
version: 2
updated_at: "2026-10-21T16:23:32Z"
---
# Summary

Choose focused-validation Local release continuation

## Concern

Should this Local release now be completed with an explicit, accurately recorded focused-validation path, or should deployment remain pending? Do not silently invent a permanent full-suite bypass or call the normal command, which automatically repeats the full suite forbidden by the latest Operator instruction.

## Evidences

The requested complete Run local-20261021-network-recovered-120901 ended failed with427modules,3806countedtests,zero skips,two failing modules; final launcher passed. Both blockers are now repaired and53focused related tests pass, including actual old11/new1 Docker modules and all29W01status cases. Exact source hashes, source review, full failed log and current focused log are retained. The Operator explicitly requested no full rerun after fixes. No existing focused/resume release binding has been admitted or executed in this increment; original0.4.4.9production remains unchanged.

## Answer

The Operator approves one explicitly recorded focused Local-release continuation through the existing PROJECT_TOOLS/release.py local entrypoint with repeatable --test-module arguments; the complete discovered suite is not rerun for this continuation. P2549 owns the exact changed/related host-module selection, source-currentness proof and focused receipt. The prior 53-test Docker/related proof is reused from .caprmedio_tmp/focused-release-repair-20261021/focused-summary.json only after the exact Engine/runtime/pyproject/uv.lock/version no-diff check; the expensive 12 Docker tests are not rerun. P2550 remains Backlog until P2549's proof, then owns the actual Local release, candidate installation and observed MCP smoke. This answers the path choice only: it does not claim a successful release, version adoption or production replacement. The complete suite remains the default, CA-O-188 public release remains full-gate, and C564 source-conformance debt remains unresolved.

## Blast radius

Only continuation of P2536's still-incomplete Local release and the meaning of its validation receipt. A selected path must preserve truthful focused-versus-full disposition, source-currentness, candidate verification, exact Project ownership and production rollback/retention safeguards. No fabricated green-suite receipt, skipped proof masquerading as pass, push or unapproved permanent release-policy change.
