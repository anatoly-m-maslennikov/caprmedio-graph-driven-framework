# Scope Unit Declaration source check

The native Current source scan found **46 active Scope Unit Declaration Atoms**: one Project root and 45 non-root declarations. All 45 non-root sources declare exactly one Scope Unit ID; nine are ordered and 36 unordered. Atom IDs and Scope Unit IDs are unique within this scan. No per-source field inconsistency was detected.

The root CA-R-2640 declares the Project name and does not directly state an ID or ordering. Canonical Current R2524@3 in CA-SU-11 supplies the inherited no-ID, unordered and no-order-number rules. Its exact path and hash are pinned in the inventory.

The 2026-10-31 cutover recorded 44 sources, 43 non-root IDs and nine ordered. CA-R-2682 is no longer Current and has an archive; The additional distinct native Current declarations are CA-R-2730 (WORKBENCH, CA-SU-43), CA-R-2763 (WORKBENCH_BACKEND, CA-SU-45), and CA-R-2764 (WORKBENCH_FRONTEND, CA-SU-46). The net count is +2. All 43 surviving original sources have changed hashes. Their earlier bytes match the namespace-migration preimages; direct comparison shows their only differences are the Subject namespace and Formal Claim / instance-block wrapping, ignoring blank-line formatting. This is a source-text comparison, not a runtime check.

[inventory.json](inventory.json) records every Current path, hash, ID, subject, declared fields and per-source historical comparison. Historical aggregate digest was not recomputed. No test, reader, projection, runtime or release validation was performed.

All 46 counted paths were checked against the old `000_CAPRMEDIO_framework` tree and `applicable_methodology` copies; none is included. Current status establishes source inclusion, not independent approval or runtime activation.

The owner subsequently updated CA-R-2763 from version 2 to version 3. Its current source hash was refreshed; its declared Subject, ID, name and order fields remain unchanged. All 46 source hashes matched at this check. The previous review pin remains in the inventory.
