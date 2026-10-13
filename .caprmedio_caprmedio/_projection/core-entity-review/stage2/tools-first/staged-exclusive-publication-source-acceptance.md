# Staged review and exclusive publication window: source acceptance

Derived review evidence, not governing authority or runtime acceptance.

## Decision and scope

The Operator selected staged review followed by a short exclusive publication window: no manual edits, Git operations or synchronization writes to affected files, with one shared cooperative Engine lock. Outside writers that ignore the window are not excluded by this mechanism.

Four TOOL_WORKFLOWS definitions record this choice. Existing admission, effect-time metadata, exact predecessor history, restoration, truthful failure reporting and the live-write guard remain required. No implementation, new public request fields, live Core migration or stronger crash-atomic guarantee is approved by this source packet. E626 remains unchanged.

## Accepted source pins

All four sources are under `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/306_FEATURE_TOOL_WORKFLOWS/`.

| Atom | Version | SHA-256 |
| --- | --- | --- |
| CA-R-866 | 21 | `63ae03d3609dba204482f61c3eb4936632ad3f22b54e284f03fcbccb13bfaa17` |
| CA-M-371 | 9 | `c5ff4204c8cca2309fbc60e91640dbf4fe8e1bc5373b1e7d96fd235a90684d7a` |
| CA-E-304 | 20 | `bd47c0196c8720a762d6437785f30f00af8646144cba76e9eb713bae124d9398` |
| CA-O-030 | 14 | `febda2f81aecbdee01e98021a9e471b8863467d4747c735ed37b565ddc0031c5` |

Producer manifest: `.caprmedio_tmp/window-publication-source-manifest-20261013-052220.json`, SHA-256 `edb81a053d91ace83e47719582cebdf37ba2219a6733995ad60077af4e3b56d2`. This scratch manifest is supporting evidence, not required persistent authority. Exact predecessors are retained in each role's archive folder.

## Independent result

Independent reviewer `epic_carriers` returned bounded source PASS on 2026-10-13. Its 75 mechanical assertions checked fresh final hashes, exact predecessor bytes, intended full transformations, unchanged identity/Summary/Subjects/Type/relations, and Version increments of one. Semantic review preserved source/delta review versus effect-time metadata, no-op handling, API/admission/recording/restoration and live-Core boundaries. E626, D425, D527 and D531 were unchanged. No blocking source finding remained.

This is not FPF acceptance or runtime proof. The new FPF design-challenge Plan was independently validated but awaits Operator execution approval.

## Remaining gates

- Bind the exclusive window and affected frontier through actual receiving admission, not a caller Boolean.
- Define one shared Engine lock and cover all affected cooperating writers.
- Hold the lock through final revalidation, effects, readback and existing Action-local restoration.
- Independently exercise actual combined fixtures, including contention, stale sources, history collisions, failed restoration and exact no-op behavior.
- Resolve any conflict with unchanged E626 before treating the selected model as implementation-ready.
- Keep live publication guarded until the required implementation and admission evidence is accepted. Core migration remains separately gated.
