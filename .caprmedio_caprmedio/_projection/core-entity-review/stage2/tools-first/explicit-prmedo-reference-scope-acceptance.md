# Explicit PRMEDO reference scope acceptance

Derived implementation evidence, 2026-10-13. Not source authority or whole-Project admission.

## Accepted private API

validate_proposed_carrier accepts optional reference_roles, a nonempty unique tuple of canonical D324 roles. Omission preserves the existing complete reference frontier and result shape. Explicit scope requires the candidate role inside it, filters admitted reference traversal, resolves every carried relation even with allow_existing_relations, rejects off-scope endpoints (including authority-record leakage), and returns an explicit finite reference_scope. It retains all finite obligations, exact source pins, placement, duplicates and currentness checks.

Independent reviewer whitelist_tests accepted the frozen +40/-5 production diff and 58/58 reference tests, including 12 independent controls. Tests cover default behavior, included/excluded malformed carriers, missing/off-scope targets, invalid scope, exact scope/parent-closure reporting, and stale source/frontier refusal. No public receiver, writer or dependency was added.

Production SHA-256: 621ebbee91717681598fc2ce621a8c88a9bf64adfe1bf01bfcc51976ae83f504.
Independent test SHA-256: f1346e18ae475f6d4c9b1f4de2ea3e079f4c132ce7f8e841c35154c305e83778.
Files: 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/proposed_carrier.py and tests/test_proposed_reference_scope_independent.py.

## Actual current-carrier admission

The producer ran real scoped calls from fresh source_context_from_project, native parse_carrier and selected-control-relative paths, with PRMEDO and default allow_existing_relations=False. All 15 direct packet endpoints resolved uniquely and remained current.

| Carrier | Actual result |
|---|---|
| M383 v2 | Refused: relates_to canonical ordering and unsupported Relation Kind |
| D632 v2 | Refused: same two gaps |
| E635 v1 | Refused: evaluation_for ordering, relates_to ordering and unsupported relates_to |
| P2307 v6 | Finite PASS, direct parent P2256; ancestor closure P2256 → P2167 → P1959 |

P2307's actual-call hash was 95728f14d1c20fdaf7c9e07d1e7fa4a24d20eab922ba9cfa2f569b84312f3d1e. Its later tracking revisions are not covered by that historical call.

The three refusals have no ordinary carrier findings; they expose genuine graph-authority gaps. check_graph_extended.py requires a source-bound canonical comparator and exact Relation Kind admission. D268 v12 requires deterministic canonical order but does not specify the comparator. No ordering or relation gate was bypassed. The scoped lookup no longer fails merely because deferred C/A has unsupported legacy carriers; a required off-scope dependency still refuses.

## Retained gates

This closes P2331's explicit scope mechanism, not TOML implementation or its full source admission. Resolve the relation-authority gaps separately. C/A migration, runtime activation, live writes and Core Subject/content migration remain excluded.
