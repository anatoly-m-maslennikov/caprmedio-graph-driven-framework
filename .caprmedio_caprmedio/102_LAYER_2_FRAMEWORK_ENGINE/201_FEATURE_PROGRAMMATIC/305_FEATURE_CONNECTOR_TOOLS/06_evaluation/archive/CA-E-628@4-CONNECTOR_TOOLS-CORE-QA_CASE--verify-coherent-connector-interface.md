---
atom_id: CA-E-628@4
content_role: Evaluation
type: Eval Case
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Engineering/Connector Interface Conformance Evaluation
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Workflow
  - Subject/Domain/Node/Continuant/Governing Configuration
version: 4
updated_at: 2026-10-24 02:14:24 +0400
relations:
  evaluation_for:
  - CA-R-1936
  - CA-D-625
  relates_to:
  - CA-M-376
  - CA-D-527
  - CA-O-046
  - CA-O-047
  - CA-O-204
tier: 3
---
# Summary

Verify coherent connector interface

## Scope

Required future conformance cases for CA-R-1936, CA-M-376 and CA-D-625 across every CONNECTOR_TOOLS connector and its declared supported subset. These are test specifications, not execution or passing-test evidence.

## Claim

Every connector uses the coherent logical input/output roles and performs only its explicitly supplied mechanical operation. Workflow admission owns identity, Version/time, lifecycle and configuration/schema decisions.

## Details

1. Independently author valid query/read/create/modify requests for each connector's admitted subset and logical kinds. Require CA-D-625's exact inner keys and consistent data/current_state/effects/errors result. Reject unknown keys, unsupported operations/kinds, malformed delta, missing or conflicting target/query and unresolved authorization/context.
2. Read an Atom by explicit full ID with no pre-known Version; compare complete content and returned actual exact Version/state against independent expected state. Also test pinned and historical Read with exact supplied Version/state. Reject an ambiguous source view, unavailable target or stale pin. Verify no implicit Find or mutation.
3. Require expected current state for Modify and expected absence for Create. Supply complete workflow-selected schema/identity/lifecycle/Version metadata and delta. Verify the connector checks those bindings but never allocates another ID, supplies defaults, chooses a schema, bumps Version/time itself, archives/deletes an Atom or rewrites references.
4. Exercise one connector through different admitted adapters/consumers while preserving logical identity, request meaning and result evidence. Physical locator or internal computed occurrence position is adapter evidence, not a public target or list selector. No DB implementation is required or inferred.
5. Test malformed input, absent/ambiguous target, stale state, denied permission, invalid supplied schema evidence and backend failure. Verify the stable structured error code/message/field and actual known/unknown effects. Empty query matches and true no-op are not fabricated errors or mutation effects. Require `effect_uncertain` for every unknown effect; nonempty errors never indicate success even after a known effect. An exception-free but unverified result cannot pass with empty errors. Prove a true no-op leaves the requested state unchanged.
6. Query returns matches only; Read returns full requested content. Test unique-current-value and whole-set list deltas where supported, including missing/duplicate/ambiguous values and caller indexes. Verify every unrelated byte/state remains outside the explicit effect.
7. Under the existing selected service, independently check CA-D-527 outer parameters/target/effect/definition/currentness/authorization bindings. The logical payload neither duplicates the outer protocol nor fabricates Run/Event identities, persistence, transport admission or completion.
8. Inject an action-local effect/verification failure and retain the connector's actual known/unknown effect evidence. A composed workflow retains earlier independent successes and stops at its first failure; no cross-Atom rollback or new retry/resume is inferred.

### Acceptance and failure disposition

Compare independently authored requests, complete state/effect/error ledgers and reopened source/history observations. Fail on hidden policy choice, widened scope, lifecycle/schema bypass, false completion or stale-binding acceptance. Existing file/TOML safeguards and action-local safety remain required; stronger backend/concurrency/publication guarantees need separate proof.
