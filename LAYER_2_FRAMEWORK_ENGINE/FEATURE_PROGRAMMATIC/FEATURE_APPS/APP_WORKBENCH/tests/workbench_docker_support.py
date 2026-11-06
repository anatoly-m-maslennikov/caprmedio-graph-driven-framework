# CA-E-676@9
"""Small standard-library helpers shared by Workbench Docker E2E tests."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import socket
import subprocess
import tomllib
from typing import Any
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from uuid import UUID


def free_port() -> int:
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        return int(probe.getsockname()[1])


def project_name(control_root: Path) -> str:
    settings_path = control_root / "caprmedio_project_settings.toml"
    settings = tomllib.loads(settings_path.read_text(encoding="utf-8"))
    return settings["project"]["name"]


def request(url: str, *, method: str = "GET", payload: dict | None = None) -> tuple[int, dict | str]:
    body = None if payload is None else json.dumps(payload).encode()
    target = Request(url, data=body, method=method, headers={"content-type": "application/json"})
    try:
        with urlopen(target, timeout=60) as response:  # noqa: S310 -- loopback test server
            data = response.read().decode()
            return response.status, json.loads(data) if response.headers.get_content_type() == "application/json" else data
    except HTTPError as error:
        with error:
            data = error.read().decode()
        return error.code, json.loads(data) if data else {}


def container_memory_metrics(name: str) -> tuple[str, dict[str, int], int | None]:
    for events_path in ("/sys/fs/cgroup/memory.events", "/sys/fs/cgroup/memory/memory.events"):
        result = subprocess.run(
            ["docker", "exec", name, "cat", events_path],
            capture_output=True, text=True, check=False,
        )
        if result.returncode != 0:
            continue
        events = {}
        for line in result.stdout.splitlines():
            key, _, value = line.partition(" ")
            if key and value:
                try:
                    events[key] = int(value)
                except ValueError:
                    pass
        peak_result = subprocess.run(
            ["docker", "exec", name, "cat", events_path.replace("memory.events", "memory.peak")],
            capture_output=True, text=True, check=False,
        )
        peak = int(peak_result.stdout.strip()) if peak_result.returncode == 0 else None
        return events_path, events, peak
    raise AssertionError("Workbench container did not expose cgroup memory.events")


def is_uuid7(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = UUID(value)
    except ValueError:
        return False
    return parsed.version == 7 and str(parsed) == value


def assert_saved(
    case: unittest.TestCase, value: dict[str, Any], *, url: str, workbench_path: str, kind: str, sql: str,
) -> None:
    identifier = value.get("saved_query_id")
    case.assertTrue(is_uuid7(identifier), identifier)
    case.assertEqual(kind, value.get("kind"))
    case.assertEqual(sql, value.get("sql"))
    case.assertIsInstance(value.get("saved_at"), str)
    case.assertEqual(f"{url}{workbench_path}?query={identifier}", value.get("saved_query_url"))


def assert_legacy_saved(
    case: unittest.TestCase, value: dict[str, Any], *, url: str, workbench_path: str,
    identifier: str, kind: str, sql: str,
) -> None:
    case.assertEqual(identifier, value.get("saved_query_id"))
    case.assertEqual(kind, value.get("kind"))
    case.assertEqual(sql, value.get("sql"))
    case.assertEqual(f"{url}{workbench_path}?query={identifier}", value.get("saved_query_url"))


def assert_saved_journal(case: unittest.TestCase, journal_state: Path, *saved: dict[str, Any]) -> None:
    paths = sorted(journal_state.glob("workbench-saved-items-*-part-*.ndjson"))
    case.assertTrue(paths, "saved items must use the configured Journal root")
    records = [json.loads(line) for path in paths for line in path.read_text(encoding="utf-8").splitlines()]
    for value in saved:
        matching = [record for record in records if record["saved_query_id"] == value["saved_query_id"]]
        case.assertEqual(1, len(matching), value)
        record = matching[0]
        case.assertEqual(value["kind"], record["kind"])
        case.assertEqual(value["sql"], record["sql"])
        case.assertEqual(value.get("name"), record.get("name"))
        case.assertIsInstance(record["saved_at"], str)


def journal_snapshot(journal_state: Path) -> dict[str, str]:
    return {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest()
        for path in journal_state.glob("workbench-saved-items-*-part-*.ndjson")
    }


def assert_journal_unchanged(case: unittest.TestCase, journal_state: Path, before: dict[str, str]) -> None:
    case.assertEqual(before, journal_snapshot(journal_state))


def assert_not_saved(case: unittest.TestCase, value: dict[str, Any]) -> None:
    for key in ("saved_query_id", "saved_query_url", "saved_at"):
        case.assertNotIn(key, value)


def assert_legacy_files_unchanged(
    case: unittest.TestCase, workbench_state: Path, legacy_hashes: dict[str, str],
) -> None:
    directory = workbench_state / "saved_queries"
    case.assertEqual(
        legacy_hashes,
        {path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in directory.iterdir()},
    )
