# Current Core Subject mapping preparation — CA-P-1972

This is read-only preparation for CA-P-1966, after CA-P-1963. It does not change Core, map Subjects, adopt grammar or replace the captured review. The grammar exception remains unanswered.

## Inputs

Read the current CORE_META_MODEL authority_path from project_structure.toml. Select original Active Requirement, Method, Evaluation, Delivery and Operations carriers there, with current_scope_unit CORE_META_MODEL. Record excluded roles/lifecycle copies and every invalid or mismatched source separately. Preserve malformed selected sources for review; do not repair or hide them. The two already observed invalid Updated At values are findings, not permission to fix them.

Pin the Structure, frozen candidate, consolidated review and every current source used. The captured snapshot remains at a971d0e00c33c779f485fc8cad63194894d440fb. Current and captured evidence must stay separate. An old pin does not bind a current file merely because the ID matches.

## Inventory and batches

The one-off support/inventory_current_subjects.py reads current files, never writes authority and defaults to preview. Explicit --persist creates derived outputs only; refuse a different existing output. Use the existing strict carrier parser, not a new reusable Tool or a repair framework.

current-subjects.inventory.json contains schema_version, non_authoritative=true, source_migration/native_admission=not_performed, exact input pins, selected_sources, excluded_sources, diagnostics and occurrences. Each source has relative_path, full-file SHA-256, Atom ID, Version, role, owner, status and Updated At text/type. Each occurrence has occurrence_id (relative path plus exact subjects.governs or subjects.depends_on[index]), source path/ID/Version/hash, field, index and exact old value. Do not propose a new value or infer slash meaning. Invalid values remain explicit findings; valid fields from a source with another metadata finding still appear but are quarantined from execution.

Keep all occurrences of a source together. Stable lexical batches own at most 20 selected sources and 120 occurrences. An oversized source requires further decomposition before review. Every selected source, including malformed ones, belongs to exactly one batch; every occurrence belongs to exactly one batch. Batch inputs contain exact source/occurrence rows and inventory/input hashes. current-subjects.batches.json records their paths, hashes and counts.

Root creates the bounded review Plans and one integration Plan under CA-P-1966 after inventory verification. A review leaf reads the current Main Content for its assigned sources, compares the frozen candidate/review without refreshing them, and returns one row per occurrence: unchanged/proposed/unresolved, explicit old value, nullable proposed value, confidence, evidence spans/hashes, preserved distinctions and specific remaining question. No source write or deletion. Below 90%, do not invent a replacement. Work exceeding 15 minutes is decomposed. Integration must verify all input pins, exact coverage, no overlap and all unresolved findings. Preparation alone does not finish the mapping Epic.

## Independent checks and ownership

- Inventory worker owns only its support script and create-only inventory/batch outputs.
- Verifier owns support/verify_current_inventory.py and its isolated tests. Enumerate current sources independently, reconstruct expected occurrences without importing the producer, compare all pins and exact batch coverage. Removing or corrupting an occurrence must fail. Scratch belongs under .caprmedio_tmp.
- Snapshot-comparison worker owns only support/compare_current_snapshot.py and current-snapshot.delta.json. Verify immutable Git pins and compare current bytes, Subjects and Main Content with captured bytes by ID. This is a byte/evidence reuse report, not a semantic mapping. Changes require fresh live evidence; equality does not authorize migration.
- Root owns this contract, Plan atoms, shared integration and all Git changes. No worker edits Core, captured outputs, another lane, runtime, MCP, FPF or Git state. Workers are not alone in the worktree.

The required preparation check is current-source/batch coverage with exact pins and independently rejected wrong data. The pre-existing native registry path failure is not silently repaired or treated as passing. Native admission, grammar changes, accepted graph, sealed migration approval and application remain later gates.
