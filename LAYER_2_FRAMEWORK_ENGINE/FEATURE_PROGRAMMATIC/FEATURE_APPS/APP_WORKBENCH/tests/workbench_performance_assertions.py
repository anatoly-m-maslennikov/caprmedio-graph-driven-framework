# CA-E-677@16
# CA-E-780@7
"""State oracle for the disposable Workbench performance fixture."""

from __future__ import annotations

import json
from collections.abc import Callable
from unittest import TestCase

from workbench_performance_fixture import (
    BASE_REFERENCE,
    BATCH_COUNT,
    BATCH_PREFIX,
    FIXTURE_ATOM_COUNT,
    expected_claim,
    PerformanceFixture,
    batch_ids,
)


Rows = Callable[[str], list[dict[str, object]]]
Scalar = Callable[[str], object]
RelationCount = Callable[..., int]
STABLE_EDGE_COUNT = FIXTURE_ATOM_COUNT - 6


def _json(value: object) -> dict[str, list[dict[str, object]]]:
    if isinstance(value, str):
        value = json.loads(value)
    if not isinstance(value, dict):
        raise AssertionError(f"expected JSON object, got {value!r}")
    return value


def assert_performance_batch(
    case: TestCase,
    fixture: PerformanceFixture,
    rows: Rows,
    scalar: Scalar,
    relation_count: RelationCount,
    *,
    version: int,
    scope_id: str,
    scope_name: str,
    suffix: str,
    expected_total: int,
    batch_present: bool = True,
    content_changed: bool = False,
    content_version: int = 1,
    absent_scope_name: str | None = None,
) -> None:
    """Prove source rows and their direct/derived graph edges are exact."""
    counts = rows(
        "SELECT count(*) AS total, count(DISTINCT reference) AS distinct_references\nFROM atoms\n;"
    )[0]
    case.assertEqual(expected_total, counts["total"], counts)
    case.assertEqual(expected_total, counts["distinct_references"], counts)
    batch = rows(
        'SELECT reference, "header.state.version", "header.context.container.scope_unit"\n'
        '  ,"header.context.scope_unit_name", "relative_path"\n'
        '  ,"header.destination.file.name", "header.destination.file.path", "header.relations"\n'
        '  ,"content.summary" AS content_summary\n'
        '  ,"content.claim.prose_claim" AS content_claim\n'
        "FROM atoms\n"
        f"where reference LIKE '{BATCH_PREFIX}%'\n"
        "ORDER BY reference\n;"
    )
    if not batch_present:
        _assert_absent(case, rows, relation_count, batch, expected_total)
        return
    expected_ids = batch_ids()
    case.assertEqual(expected_ids, {str(row["reference"]) for row in batch})
    case.assertEqual(BATCH_COUNT, len(batch))
    expected_directory = fixture.relative(fixture.batch_directory)
    for row in batch:
        atom_id = str(row["reference"])
        path = fixture.batch_directory / f"{atom_id}-{suffix}.md"
        case.assertEqual(version, row["header.state.version"], row)
        case.assertEqual(scope_id, row["header.context.container.scope_unit"], row)
        case.assertEqual(scope_name, row["header.context.scope_unit_name"], row)
        case.assertEqual(expected_directory, row["relative_path"], row)
        case.assertEqual(path.name, row["header.destination.file.name"], row)
        case.assertEqual(fixture.relative(path.parent), row["header.destination.file.path"], row)
        case.assertEqual(f"Index representative Atom {atom_id}.", row["content_summary"])
        relations = _json(row["header.relations"])
        case.assertEqual(
            [{"kind": "Atom", "reference": BASE_REFERENCE, "derived": False}],
            relations.get("IS_BLOCKED_BY"),
        )
        case.assertEqual(
            [{"kind": "Scope Unit", "reference": scope_name, "derived": False}],
            relations.get("IS_CONTAINED_BY"),
        )
        content = str(row["content_claim"])
        case.assertEqual(expected_claim(atom_id, content_version, changed=content_changed), content)
        case.assertEqual(
            content_changed,
            "This version records a real content update for delta indexing." in content,
        )
        case.assertIn(f"{atom_id} represents", content)
    _assert_present_graph(
        case, rows, scalar, relation_count, expected_ids, scope_id, scope_name, absent_scope_name
    )


def _assert_absent(
    case: TestCase,
    rows: Rows,
    relation_count: RelationCount,
    batch: list[dict[str, object]],
    expected_total: int,
) -> None:
    case.assertEqual([], batch, batch)
    base = rows(f'SELECT "header.relations"\nFROM atoms\nwhere reference = \'{BASE_REFERENCE}\'\n;')
    case.assertEqual(1, len(base), base)
    derived = _json(base[0]["header.relations"]).get("BLOCKS", [])
    case.assertFalse({str(item["reference"]) for item in derived} & batch_ids())
    scope_rows = rows(
        "SELECT relations\nFROM scope_units\nwhere scope_unit_id IN ('TEST-SU-1', 'TEST-SU-2')\n;"
    )
    for scope_row in scope_rows:
        contained = _json(scope_row["relations"]).get("CONTAINS", [])
        case.assertFalse({str(item["reference"]) for item in contained} & batch_ids())
    _assert_graph_counts(case, relation_count, 0)


def _assert_present_graph(
    case: TestCase,
    rows: Rows,
    scalar: Scalar,
    relation_count: RelationCount,
    expected_ids: frozenset[str],
    scope_id: str,
    scope_name: str,
    absent_scope_name: str | None,
) -> None:
    base = rows(f'SELECT "header.relations"\nFROM atoms\nwhere reference = \'{BASE_REFERENCE}\'\n;')
    case.assertEqual(1, len(base), base)
    derived = {
        str(item["reference"])
        for item in _json(base[0]["header.relations"]).get("BLOCKS", [])
        if item == {"kind": "Atom", "reference": item.get("reference"), "derived": True}
    }
    case.assertTrue(expected_ids <= derived)
    scope_rows = rows(
        "SELECT name, scope_unit_id, relations\nFROM scope_units\n"
        "where scope_unit_id IN ('TEST-SU-1', 'TEST-SU-2')\nORDER BY scope_unit_id\n;"
    )
    case.assertEqual(2, len(scope_rows), scope_rows)
    by_scope_id = {str(row["scope_unit_id"]): row for row in scope_rows}
    case.assertEqual(scope_name, by_scope_id[scope_id]["name"])
    if absent_scope_name is not None:
        case.assertEqual(
            0, scalar(f"SELECT count(*) FROM scope_units where name = '{absent_scope_name}';")
        )
    contained = {
        str(item["reference"])
        for item in _json(by_scope_id[scope_id]["relations"]).get("CONTAINS", [])
        if item == {"kind": "Atom", "reference": item.get("reference"), "derived": True}
    }
    case.assertTrue(expected_ids <= contained)
    other_scope_id = "TEST-SU-2" if scope_id == "TEST-SU-1" else "TEST-SU-1"
    other = {
        str(item["reference"])
        for item in _json(by_scope_id[other_scope_id]["relations"]).get("CONTAINS", [])
        if item == {"kind": "Atom", "reference": item.get("reference"), "derived": True}
    }
    case.assertFalse(expected_ids & other)
    _assert_graph_counts(case, relation_count, BATCH_COUNT)


def _assert_graph_counts(case: TestCase, relation_count: RelationCount, batch_size: int) -> None:
    expected = STABLE_EDGE_COUNT + batch_size
    case.assertEqual(expected, relation_count("IS_BLOCKED_BY", target=BASE_REFERENCE))
    case.assertEqual(expected, relation_count("BLOCKS", source=BASE_REFERENCE))
