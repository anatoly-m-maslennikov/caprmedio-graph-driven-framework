# Contained Atom target discovery — acceptance

Derived verification record. Not Core authority or live execution approval.

## Scope

CA-P-2317: private read-only inventory for an explicit source-pinned P/O parent. It returns deterministic parent-before-child targets with explicit own metadata and immediate containment. Relations do not establish containment. Current canonical history selects the greatest validated Version; older revisions and historical parent bundles are excluded. Final Archived targets remain eligible. Unknown placements, duplicate current identities, ambiguous versions, orphan directories, stale sources and malformed newer candidates refuse.

## Evidence

Author and independent suites: 21 tests PASS. Separate independent execution: 11 tests PASS (6.995 seconds). Independent connected-code review PASS. Two regressions had observed failing baselines before fixes: an orphan child directory and an invalid higher-version carrier hiding a contained target. Tests cover nested P/O, empty containers, all-status/history selection, outside references, stale parent/context and no writes (effect denial and byte/inode/mode/mtime ledgers).

Final SHA-256, rechecked by root:

- contained_atom_targets.py: af5f9ffa9954c19476beabc8e3773cce78fa5907336ef4ea89d1fda31e5c35c9
- tests/test_contained_atom_targets.py: e61058ada62ddb8da31ad2ae86fc954213da147408284a9f55260e62c5022261
- tests/test_contained_atom_targets_independent.py: 319a151385947bb57e69b6586300f3bcddb1893257abd37afba3f1ef349ff323

Files live under 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/.

## Boundaries

No public receiver, lifecycle action, cascade, live migration or runtime activation was executed. P2318 must rediscover/rebind after preceding actions, not retain a stale inventory as an execution promise. Separate P2322 boundary-consumer integration was present during testing and has its own acceptance; this receipt does not accept or publish those shared changes. Legacy noncanonical archive migration remains deferred.
