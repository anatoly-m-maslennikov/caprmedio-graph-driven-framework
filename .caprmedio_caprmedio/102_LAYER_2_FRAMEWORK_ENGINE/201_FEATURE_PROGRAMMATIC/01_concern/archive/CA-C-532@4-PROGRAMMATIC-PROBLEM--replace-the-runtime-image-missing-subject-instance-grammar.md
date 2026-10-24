---
atom_id: CA-C-532@4
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Archived
priority: high
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2401, CA-P-2433]
version: 4
updated_at: "2026-10-20T16:01:28.000Z"
---
# Summary

Replace the runtime image missing Subject instance grammar

## Concern

The running MCP uses an older immutable image that lacks the already-fixed approved // Subject instance separator. The checkout accepts the required grammar, but the normal61-target Subject staging call stopped at its first item. Deployment and the stopped stage's disposition remain separate gates.

## Evidences

The retained response for subject-stage-701e46e3e11bbd6611c32becd8c7352ce2d1cb04dec3cf978bbabad9226f3413 records completed0, inspection_required=true and ordinal1 CA-R-1574, with Subject separators require non-empty components for Entity/Node/Continuant/Term//Type. No canonical source was changed by that attempt.

Read-only image/container metadata binds port56317 and image sha256:a44ad0918f82e27ea705c9676acedcf5131a84be019b8299945012389dba0859 to source head9fc7a3e6e872ae7d12f8762cec1ebb16fcad9ed6. The matching retained runtime parser SHA256 is2a177b602ffd834e266a83b2a6d891241290990d0457950a6ac6edabe9dcad17; it splits separators one character at a time. Current parser6b377172306c9a6aa662f8436885aeee51922e9980606d08d70b0dc2273c0329 fromaf81d978cd09087fe4395f0844b942648f7f547d accepts the exact first item and12frozen notation tests pass. No protected-container exec, endpoint probe, replay or lifecycle effect was performed by the diagnosis.

Exact paths, hashes, entrypoint chain and limits: .caprmedio_tmp/mcp-audit-20261020/continuation/installed-subject-parser/report.md. The Operator expressly approved replacement AFTER isolatedtests pass, then expressly approved the normal full localrelease including all current changes and Git checkpoints. No execution receipt or readiness is implied; production remains unchanged at this checkpoint.

## Blast radius

Approved // Subjects cannot be staged by the observed installed package. No parser rewrite is needed solely for this failure. Build and verify a fresh immutable candidate and pass isolated tests before any separately authorized, coordinated production replacement. Do not auto-replay, reset or cancel the stopped inspection-required stage; its reconciliation needs exact retained-state inspection.

### Resolution checkpoint

The approved release proof `.caprmedio_tmp/mcp-audit-20261020/continuation/local-release-verified-20261020.json` and canonical receipt `.caprmedio_runtime/simple_local_release/reports/local-20261020-current-target-parser-repair-1521.md` record version `0.4.4.8`, 410 modules, 3680 tests, zero skips/failures and a passing final isolated launcher. Healthy container `b1676bbd01e451f6bf5b32237bdc0d44147dbcc7f9da43638ca8de724a939d44` serves port `56317`; the prior container is absent and its old image was removed by the approved release. Parser SHA `6b377172306c9a6aa662f8436885aeee51922e9980606d08d70b0dc2273c0329` was verified in the released package and container. This resolves the old-runtime-image grammar blocker only; no historical batch replay, public release or full capability claim is inferred.
