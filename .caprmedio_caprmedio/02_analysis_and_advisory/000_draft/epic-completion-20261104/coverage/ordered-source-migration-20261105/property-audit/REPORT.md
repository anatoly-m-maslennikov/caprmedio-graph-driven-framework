# Final live Header checks

The fresh census contains 4,669 native carriers: 4,412 Current-path and 257 Draft-path. All 4,669 passed the present-key order check: declared Header keys come first in order and unlisted extras follow. All had no empty or null Header properties, and no Relation list contained null.

Ref ID matches the explicit identity, status and version formula in 4,463 carriers; no mismatch was found. The remaining 206 have insufficient or invalid identity/status evidence: 177 lack explicit ID or status, and 29 have unallocated or invalid IDs. They require separate resolution.

Fifty-five Relation-list strings in 35 carriers do not match the normal Atom-ID spelling. They are listed separately as domain-review leads, not automatically classified as invalid. This check does not establish target existence or endpoint admissibility.

The exact pinned snapshot, path-level results and limitations are in final-header-check.json. One source changed during an initial scan; a fresh snapshot and recheck completed with no drift.
