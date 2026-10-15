# Unordered relation targets acceptance

Derived implementation evidence, 2026-10-13. Not source authority or whole-Project admission.

## Source decision

The Operator chose unordered relation targets. D268 v13 removes mandatory canonical ordering; target order is nonsemantic. It preserves nonempty unique canonical references, owning Atom, direction, endpoint and Relation Kind obligations. Independent reviewer connector_binding_review accepted the exact change and v12 predecessor archive.

Current D268 SHA-256: `eba35171683bf9219f32d264cc3eaff985bd7939817114135c3a04faccf8df96`.
Predecessor SHA-256: `2afc204f59d90286345c9f4b5f74f8fcf2b8b40b992ab5aca734b0ad53e46335`.

## Implementation and checks

The shared relation parser removes only the eleven-line ordering-authority gap. The two current validator manifests and two literal source fixtures bind D268 v13. The current README no longer claims that ordering blocks admission. Historical receipts and legacy consumer pins were not rewritten.

Independent reviewer whitelist_tests verified 24 complete-carrier permutation cases, covering typed evaluation_for and generic depends_on under default and finite PRMEDO scope. All failed on the old ordering gap with the new source pins; all pass after the deletion. Four independent tests passed. Input metadata and carrier bytes remain unchanged. Empty lists, within-kind duplicates, missing or noncanonical targets, unsupported and inverse kinds, wrong endpoint roles, and stale or missing authority still refuse. The author's focused suite passed 53 tests.

Production `check_graph_extended.py` SHA-256: `6f6003272c1e1b6b8c6e0781664d471016c44ce90dff5aeca85eea5e4783c857`.
Independent `test_relation_target_order_independent.py` SHA-256: `c68e857cba01223ca4cfa452478d024586c20038468eef2496c31d739bb503c6`.

## Separate limits

The full VALIDATE_ATOMS suite passed 338 tests. Discovery and module import preceded P2334's separate one-line change; this is P2333 evidence, not a claim that this run tested that later change. Command: `PYTHONDONTWRITEBYTECODE=1 UV_CACHE_DIR=.caprmedio_tmp/cache/uv TMPDIR="$PWD/.caprmedio_tmp" uv run --offline --no-project --python 3.14 --with pydantic==2.13.5 --with PyYAML==6.0.3 python -B -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/tests`.

Actual finite PRMEDO admission rechecks returned zero ordering gaps: M383 v2, D632 v2 and E635 v1 each have only one unsupported relations.relates_to gap and no ordinary findings. P2307 v7 passed, with parent closure P2256 → P2167 → P1959; its checked hash was `2c5cb165260c34612cca1312dac3e92608ae27f4f1008394c0221b07aa6fe48c`. All four input pins were revalidated. Later Plan tracking updates are not covered by that historical check.

This does not admit the undeclared relates_to kind in the TOML packet. A distinct preexisting cross-kind lookup-identity duplication was found and is tracked by P2334; this receipt does not accept its fix. No source-list sorting, new relation kind, live publication, C/A migration or Core Subject/content migration is included.
