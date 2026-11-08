# CA-E-794@3
"""Opt-in live Workbench canary against the current Project only.

This is deliberately not part of the normal suite.  It needs both an explicit
current repository root and a live Workbench URL because it temporarily adds a
valid Scope Unit Declaration to the project's real source tree.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
import sys
import tempfile
import time
import tomllib
import unittest
from uuid import uuid4


REPOSITORY = Path(__file__).resolve().parents[5]
PROGRAMMATIC = REPOSITORY / "LAYER_2_FRAMEWORK_ENGINE" / "FEATURE_PROGRAMMATIC"
TOOLS = PROGRAMMATIC / "FEATURE_TOOLS"
MCP = PROGRAMMATIC / "FEATURE_MCP"
APPS = PROGRAMMATIC / "FEATURE_APPS"
TESTS = Path(__file__).resolve().parent
for location in (TOOLS, MCP, APPS, TESTS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from http_paths import HEALTH_PATH, WORKBENCH_PATH  # noqa: E402
from scope_unit_declarations import read_scope_unit_declarations  # noqa: E402
from selected_route_manifest import _configured_control_root  # noqa: E402


CANARY_FLAG = "CAPRMEDIO_LIVE_CANARY"
ROOT_FLAG = "CAPRMEDIO_LIVE_CANARY_ROOT"
URL_FLAG = "CAPRMEDIO_LIVE_CANARY_URL"
DRY_RUN_FLAG = "CAPRMEDIO_LIVE_CANARY_DRY_RUN"
PARENT_SCOPE = "WORKBENCH_BACKEND"
REPORT_DIRECTORY = REPOSITORY / ".caprmedio_tmp" / "workbench" / "live-canary"


from workbench_live_canary_support import (  # noqa: E402
    CanaryScope, LiveCanaryError, atom_carrier as _atom_carrier,
    atomic_publish as _atomic_publish, atomic_replace as _atomic_replace,
    authority_path as _authority_path, copy_declaration_tree as _copy_declaration_tree,
    declaration_target as _declaration_target, new_atom_id as _new_atom_id,
    new_scope_unit_id as _new_scope_unit_id, remove_owned_authority as _remove_owned_authority,
    remove_owned_file as _remove_owned_file, request as _request,
    scope_authority as _scope_authority, scope_carrier as _scope_carrier,
    stage_carrier as _stage_carrier, validate_declaration_tree as _validate_declaration_tree,
    validate_atom_carrier, write_scope_declaration as _write_scope_declaration,
)


class WorkbenchLiveCanary(unittest.TestCase):
    maxDiff = None

    def _configuration(self) -> tuple[Path, str, bool]:
        if os.environ.get(CANARY_FLAG) != "1":
            self.skipTest(f"set {CANARY_FLAG}=1 to permit a real Project source mutation")
        root_value, url = os.environ.get(ROOT_FLAG), os.environ.get(URL_FLAG)
        if not root_value or not url:
            raise LiveCanaryError(f"{ROOT_FLAG} and {URL_FLAG} are both required")
        root = Path(root_value).expanduser().resolve()
        if root != REPOSITORY.resolve():
            raise LiveCanaryError("live canary accepts only this current repository root")
        if not url.startswith(("http://127.0.0.1:", "http://localhost:")):
            raise LiveCanaryError("live canary accepts only an explicit loopback Workbench URL")
        return root, url.rstrip("/"), os.environ.get(DRY_RUN_FLAG) == "1"

    @staticmethod
    def _project_name(control: Path) -> str:
        settings = tomllib.loads((control / "caprmedio_project_settings.toml").read_text(encoding="utf-8"))
        name = settings.get("project", {}).get("name")
        if not isinstance(name, str) or not name:
            raise LiveCanaryError("Project Settings lacks project.name")
        return name

    @staticmethod
    def _wait_for_rows(url: str, query: str, expected: list[list[object]], *, present: bool) -> float:
        """Measure visibility only; the deadline protects the canary process, not a product SLA."""
        started = time.monotonic()
        deadline = started + 90
        last: object = None
        while time.monotonic() < deadline:
            status, payload = _request(url, method="POST", payload={"sql": query, "page_size": 10})
            last = payload
            if status == 200 and isinstance(payload, dict) and payload.get("rows") == expected:
                return round(time.monotonic() - started, 3)
            if not present and status == 200 and isinstance(payload, dict) and payload.get("rows") == []:
                return round(time.monotonic() - started, 3)
            time.sleep(0.25)
        state = "appear" if present else "disappear"
        raise LiveCanaryError(f"canary Scope Unit did not {state} before the safety deadline; last={last!r}")

    @staticmethod
    def _write_report(report: dict[str, object]) -> None:
        REPORT_DIRECTORY.mkdir(parents=True, exist_ok=True)
        staged = REPORT_DIRECTORY / f".{uuid4().hex}.tmp"
        target = REPORT_DIRECTORY / "latest.json"
        staged.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        os.replace(staged, target)

    def _assert_offline_phase(
        self, root: Path, control: Path, expected_scopes: set[str], *, absent_scopes: set[str] = frozenset(),
        atom_id: str | None = None,
    ) -> None:
        declarations = _validate_declaration_tree(root, control)
        self.assertTrue(expected_scopes <= set(declarations.by_name))
        self.assertFalse(absent_scopes.intersection(declarations.by_name))
        if atom_id is not None:
            self.assertTrue(any(path.name.startswith(f"{atom_id}-") for path in root.rglob("*.md")))

    def _offline_validate_scenario(
        self, root: Path, control: Path, declarations: object, project_name: str,
        first: CanaryScope, second: CanaryScope, renamed: CanaryScope, atom_id: str,
    ) -> None:
        """Validate every published state before the live source tree can change."""
        with tempfile.TemporaryDirectory() as temporary:
            staged_root = Path(temporary).resolve() / "project"
            staged_root.mkdir()
            staged_control = _copy_declaration_tree(root, control, declarations, staged_root)
            parent_authority = _authority_path(declarations, staged_root, PARENT_SCOPE)
            first_authority = _scope_authority(parent_authority, first)
            second_authority = _scope_authority(parent_authority, second)
            first_target = _declaration_target(parent_authority, first)
            second_target = _declaration_target(parent_authority, second)
            _write_scope_declaration(first_target, first, project_name)
            first_authority.mkdir()
            self._assert_offline_phase(staged_root, staged_control, {first.name})
            _write_scope_declaration(second_target, second, project_name)
            second_authority.mkdir()
            self._assert_offline_phase(staged_root, staged_control, {first.name, second.name})

            atom = first_authority / "04_requirement" / f"{atom_id}-canary-source.md"
            atom.parent.mkdir(parents=True, exist_ok=True)
            atom.write_text(_atom_carrier(atom_id, 1, scope=first, destination=atom, root=staged_root), encoding="utf-8")
            validate_atom_carrier(atom)
            self._assert_offline_phase(staged_root, staged_control, {first.name, second.name}, atom_id=atom_id)
            atom.write_text(_atom_carrier(atom_id, 2, scope=first, destination=atom, root=staged_root), encoding="utf-8")
            validate_atom_carrier(atom)
            renamed_atom = atom.with_name(f"{atom_id}-canary-renamed.md")
            atom.write_text(_atom_carrier(atom_id, 2, scope=first, destination=renamed_atom, root=staged_root), encoding="utf-8")
            atom.rename(renamed_atom)
            moved_atom = second_authority / "04_requirement" / renamed_atom.name
            moved_atom.parent.mkdir(parents=True, exist_ok=True)
            renamed_atom.rename(moved_atom)
            moved_atom.write_text(_atom_carrier(atom_id, 2, scope=second, destination=moved_atom, root=staged_root), encoding="utf-8")
            self._assert_offline_phase(staged_root, staged_control, {first.name, second.name}, atom_id=atom_id)

            first_updated = first.with_changes(version=2)
            _write_scope_declaration(first_target, first_updated, project_name)
            self._assert_offline_phase(staged_root, staged_control, {first.name, second.name})
            second_target.unlink()
            self._assert_offline_phase(staged_root, staged_control, {first.name}, absent_scopes={second.name})
            moved_second_authority = _scope_authority(first_authority, second)
            second_authority.rename(moved_second_authority)
            moved_atom = moved_second_authority / "04_requirement" / moved_atom.name
            moved_atom.write_text(_atom_carrier(atom_id, 2, scope=second, destination=moved_atom, root=staged_root), encoding="utf-8")
            moved_second = second.with_changes(parent=first.name, version=2)
            moved_second_target = _declaration_target(first_authority, moved_second)
            _write_scope_declaration(moved_second_target, moved_second, project_name)
            self._assert_offline_phase(staged_root, staged_control, {first.name, second.name})

            moved_second_target.unlink()
            self._assert_offline_phase(staged_root, staged_control, {first.name}, absent_scopes={second.name})
            renamed_authority = _scope_authority(first_authority, renamed)
            moved_second_authority.rename(renamed_authority)
            moved_atom = renamed_authority / "04_requirement" / moved_atom.name
            moved_atom.write_text(_atom_carrier(atom_id, 2, scope=renamed, destination=moved_atom, root=staged_root), encoding="utf-8")
            renamed_target = _declaration_target(first_authority, renamed)
            _write_scope_declaration(renamed_target, renamed, project_name)
            self._assert_offline_phase(staged_root, staged_control, {first.name, renamed.name})
            moved_atom.unlink()
            self._assert_offline_phase(staged_root, staged_control, {first.name, renamed.name})
            renamed_target.unlink()
            _remove_owned_authority(renamed_authority)
            self._assert_offline_phase(staged_root, staged_control, {first.name}, absent_scopes={renamed.name})
            first_target.unlink()
            _remove_owned_authority(first_authority)
            self._assert_offline_phase(staged_root, staged_control, set(), absent_scopes={first.name, renamed.name})

    @staticmethod
    def _scope_query(scope_id: str) -> str:
        return (
            "SELECT name, scope_unit_id, parent_name, declaration_version FROM scope_units "
            f"WHERE scope_unit_id = '{scope_id}'"
        )

    @staticmethod
    def _atom_reference_query(atom_id: str) -> str:
        return f"SELECT reference FROM atoms WHERE reference = '{atom_id}'"

    @staticmethod
    def _atom_query(atom_id: str) -> str:
        return (
            'SELECT reference, "relative path", "header.state.version" '
            ', "header.context.container.scope_unit", "header.context.scope_unit_name" '
            ', "header.destination.file.name", "header.destination.file.path" '
            f"FROM atoms WHERE reference = '{atom_id}'"
        )

    @staticmethod
    def _atom_expected(
        root: Path, atom_id: str, path: Path, scope: CanaryScope, version: int,
    ) -> list[list[object]]:
        return [[
            atom_id,
            path.parent.relative_to(root).as_posix(),
            version,
            scope.scope_unit_id,
            scope.name,
            path.name,
            path.parent.relative_to(root).as_posix(),
        ]]

    def _check_queries(self, url: str, project_name: str, queries: list[str]) -> list[object]:
        checked: list[object] = []
        for query in queries:
            status, payload = _request(
                url + f"{WORKBENCH_PATH}/{project_name}/check", method="POST", payload={"sql": query},
            )
            if status != 200:
                raise LiveCanaryError(f"Workbench query check failed: {payload!r}")
            checked.append(payload)
        return checked

    def _record_visibility(
        self, report: dict[str, object], phase: str, url: str, query: str,
        expected: list[list[object]], *, present: bool,
    ) -> None:
        latencies = report.setdefault("visibility_seconds", {})
        if not isinstance(latencies, dict):
            raise LiveCanaryError("canary report lost its visibility metrics")
        latencies[phase] = self._wait_for_rows(url, query, expected, present=present)

    @staticmethod
    def _scenario(root: Path, declarations: object, *, token: str) -> tuple[CanaryScope, CanaryScope, CanaryScope, str]:
        names = (f"CANARY_A_{token}", f"CANARY_B_{token}", f"CANARY_C_{token}")
        existing_scope_ids = {unit.scope_unit_id for unit in declarations.units}  # type: ignore[attr-defined]
        reserved_atoms: set[str] = set()
        first = CanaryScope(
            names[0], _new_scope_unit_id(existing_scope_ids), _new_atom_id(root, reserved_atoms), PARENT_SCOPE,
        )
        existing_scope_ids.add(first.scope_unit_id)
        second = CanaryScope(
            names[1], _new_scope_unit_id(existing_scope_ids), _new_atom_id(root, reserved_atoms), PARENT_SCOPE,
        )
        return first, second, second.with_changes(name=names[2], parent=first.name, version=3), _new_atom_id(root, reserved_atoms)

    def test_offline_current_project_lifecycle_is_valid(self) -> None:
        """Exercise every canary carrier transition without a service or source mutation."""
        root = REPOSITORY.resolve()
        control = _configured_control_root(root)
        control = control if control.is_absolute() else root / control
        declarations = read_scope_unit_declarations(root, control)
        first, second, renamed, atom_id = self._scenario(root, declarations, token="OFFLINE")
        self._offline_validate_scenario(
            root, control, declarations, self._project_name(control), first, second, renamed, atom_id,
        )

    def test_current_project_scope_unit_and_atom_lifecycle(self) -> None:  # noqa: C901 - explicit safety phases
        root, url, dry_run = self._configuration()
        control = _configured_control_root(root)
        control = control if control.is_absolute() else root / control
        project_name = self._project_name(control)
        try:
            declarations = read_scope_unit_declarations(root, control)
        except Exception as error:
            self._write_report({
                "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "dry_run": dry_run, "outcome": "preflight_failed_no_source_write", "error": str(error), "url": url,
            })
            raise
        if PARENT_SCOPE not in declarations.by_name:
            raise LiveCanaryError(f"current Project has no {PARENT_SCOPE} Scope Unit")

        first, second, renamed, atom_id = self._scenario(root, declarations, token=uuid4().hex[:10].upper())
        if any(scope.name in declarations.by_name for scope in (first, second, renamed)):
            raise LiveCanaryError("generated live canary Scope Unit name already exists")

        parent_authority = _authority_path(declarations, root, PARENT_SCOPE)
        first_target, second_target = (_declaration_target(parent_authority, scope) for scope in (first, second))
        first_authority, second_authority = (_scope_authority(parent_authority, scope) for scope in (first, second))
        if any(path.exists() for path in (first_target, second_target, first_authority, second_authority)):
            raise LiveCanaryError("generated live canary carrier path already exists")
        report: dict[str, object] = {
            "scope_units": [first.name, second.name, renamed.name], "scope_unit_ids": [first.scope_unit_id, second.scope_unit_id],
            "atom_id": atom_id, "parent_scope_unit": PARENT_SCOPE, "url": url, "dry_run": dry_run,
            "created_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        REPORT_DIRECTORY.mkdir(parents=True, exist_ok=True)
        staged: set[Path] = set()
        owned: dict[Path, str] = {}
        try:
            self._offline_validate_scenario(root, control, declarations, project_name, first, second, renamed, atom_id)
            health_status, health = _request(url + HEALTH_PATH)
            if health_status != 200:
                raise LiveCanaryError(f"Workbench health check failed: {health!r}")
            report["health"] = health
            queries = [self._scope_query(first.scope_unit_id), self._scope_query(second.scope_unit_id), self._atom_reference_query(atom_id)]
            report["header_layout"] = "nested; first/last fixture may rebuild observed Header columns"
            report["query_checks"] = self._check_queries(url, project_name, queries)
            if dry_run:
                report["outcome"] = "preflight_validated_no_source_write"
                return

            query_url = url + f"{WORKBENCH_PATH}/{project_name}/run"
            def publish(scope: CanaryScope, target: Path) -> None:
                candidate = _stage_carrier(REPORT_DIRECTORY, scope.atom_id, _scope_carrier(scope, project_name, "2026-11-06 00:00:00 +0000"))
                staged.add(candidate)
                _write_scope_declaration(candidate, scope, project_name)
                owned[target] = _atomic_publish(candidate, target)
                staged.discard(candidate)

            def replace_atom(path: Path, scope: CanaryScope, version: int) -> None:
                candidate = _stage_carrier(
                    REPORT_DIRECTORY, atom_id,
                    _atom_carrier(atom_id, version, scope=scope, destination=path, root=root),
                )
                staged.add(candidate)
                validate_atom_carrier(candidate)
                owned[path] = _atomic_replace(candidate, path)
                staged.discard(candidate)

            first_authority.mkdir()
            publish(first, first_target)
            self._record_visibility(report, "scope_create_first", query_url, self._scope_query(first.scope_unit_id), [[first.name, first.scope_unit_id, PARENT_SCOPE, 1]], present=True)
            second_authority.mkdir()
            publish(second, second_target)
            self._record_visibility(report, "scope_create_second", query_url, self._scope_query(second.scope_unit_id), [[second.name, second.scope_unit_id, PARENT_SCOPE, 1]], present=True)

            atom = first_authority / "04_requirement" / f"{atom_id}-canary-source.md"
            atom.parent.mkdir(parents=True, exist_ok=True)
            atom_stage = _stage_carrier(
                REPORT_DIRECTORY, atom_id,
                _atom_carrier(atom_id, 1, scope=first, destination=atom, root=root),
            )
            staged.add(atom_stage)
            validate_atom_carrier(atom_stage)
            owned[atom] = _atomic_publish(atom_stage, atom)
            staged.discard(atom_stage)
            self._record_visibility(
                report, "atom_create", query_url, self._atom_query(atom_id),
                self._atom_expected(root, atom_id, atom, first, 1), present=True,
            )
            replace_atom(atom, first, 2)
            self._record_visibility(
                report, "atom_update", query_url, self._atom_query(atom_id),
                self._atom_expected(root, atom_id, atom, first, 2), present=True,
            )
            renamed_atom = atom.with_name(f"{atom_id}-canary-renamed.md")
            atom_stage = _stage_carrier(
                REPORT_DIRECTORY, atom_id,
                _atom_carrier(atom_id, 2, scope=first, destination=renamed_atom, root=root),
            )
            staged.add(atom_stage)
            validate_atom_carrier(atom_stage)
            owned[atom] = _atomic_replace(atom_stage, atom)
            staged.discard(atom_stage)
            atom.rename(renamed_atom)
            owned[renamed_atom] = owned.pop(atom)
            self._record_visibility(
                report, "atom_rename", query_url, self._atom_query(atom_id),
                self._atom_expected(root, atom_id, renamed_atom, first, 2), present=True,
            )
            moved_atom = second_authority / "04_requirement" / renamed_atom.name
            moved_atom.parent.mkdir(parents=True, exist_ok=True)
            renamed_atom.rename(moved_atom)
            owned[moved_atom] = owned.pop(renamed_atom)
            replace_atom(moved_atom, second, 2)
            self._record_visibility(
                report, "atom_move", query_url, self._atom_query(atom_id),
                self._atom_expected(root, atom_id, moved_atom, second, 2), present=True,
            )

            first_updated = first.with_changes(version=2)
            first_stage = _stage_carrier(REPORT_DIRECTORY, first.atom_id, _scope_carrier(first_updated, project_name, "2026-11-06 00:00:00 +0000"))
            staged.add(first_stage)
            _write_scope_declaration(first_stage, first_updated, project_name)
            owned[first_target] = _atomic_replace(first_stage, first_target)
            staged.discard(first_stage)
            self._record_visibility(report, "scope_update", query_url, self._scope_query(first.scope_unit_id), [[first.name, first.scope_unit_id, PARENT_SCOPE, 2]], present=True)

            _remove_owned_file(second_target, owned.pop(second_target))
            self._record_visibility(report, "scope_move_remove_declaration", query_url, self._scope_query(second.scope_unit_id), [], present=False)
            moved_second_authority = _scope_authority(first_authority, second)
            second_authority.rename(moved_second_authority)
            moved_atom = moved_second_authority / "04_requirement" / moved_atom.name
            owned[moved_atom] = owned.pop(second_authority / "04_requirement" / moved_atom.name)
            replace_atom(moved_atom, second, 2)
            moved_second = second.with_changes(parent=first.name, version=2)
            moved_second_target = _declaration_target(first_authority, moved_second)
            publish(moved_second, moved_second_target)
            self._record_visibility(report, "scope_move_publish_declaration", query_url, self._scope_query(second.scope_unit_id), [[second.name, second.scope_unit_id, first.name, 2]], present=True)
            self._record_visibility(
                report, "atom_scope_move", query_url, self._atom_query(atom_id),
                self._atom_expected(root, atom_id, moved_atom, second, 2), present=True,
            )

            _remove_owned_file(moved_second_target, owned.pop(moved_second_target))
            self._record_visibility(report, "scope_rename_remove_declaration", query_url, self._scope_query(second.scope_unit_id), [], present=False)
            renamed_authority = _scope_authority(first_authority, renamed)
            moved_second_authority.rename(renamed_authority)
            moved_atom = renamed_authority / "04_requirement" / moved_atom.name
            owned[moved_atom] = owned.pop(moved_second_authority / "04_requirement" / moved_atom.name)
            replace_atom(moved_atom, renamed, 2)
            renamed_target = _declaration_target(first_authority, renamed)
            publish(renamed, renamed_target)
            self._record_visibility(report, "scope_rename_publish_declaration", query_url, self._scope_query(second.scope_unit_id), [[renamed.name, renamed.scope_unit_id, first.name, 3]], present=True)
            self._record_visibility(
                report, "atom_scope_rename", query_url, self._atom_query(atom_id),
                self._atom_expected(root, atom_id, moved_atom, renamed, 2), present=True,
            )

            _remove_owned_file(moved_atom, owned.pop(moved_atom))
            self._record_visibility(report, "atom_delete", query_url, self._atom_reference_query(atom_id), [], present=False)
            _remove_owned_file(renamed_target, owned.pop(renamed_target))
            self._record_visibility(report, "scope_delete_second", query_url, self._scope_query(second.scope_unit_id), [], present=False)
            _remove_owned_authority(renamed_authority)
            _remove_owned_file(first_target, owned.pop(first_target))
            self._record_visibility(report, "scope_delete_first", query_url, self._scope_query(first.scope_unit_id), [], present=False)
            _remove_owned_authority(first_authority)
            report["outcome"] = "passed"
        except Exception as error:
            report["outcome"] = "failed_after_source_publish" if owned else "preflight_failed_no_source_write"
            report["error"] = str(error)
            raise
        finally:
            for path in staged:
                path.unlink(missing_ok=True)
            for path, expected_hash in tuple(owned.items()):
                try:
                    _remove_owned_file(path, expected_hash)
                except LiveCanaryError as error:
                    report.setdefault("cleanup_errors", []).append(str(error))
            for authority in (second_authority, _scope_authority(first_authority, second), _scope_authority(first_authority, renamed), first_authority):
                try:
                    _remove_owned_authority(authority)
                except OSError as error:
                    report.setdefault("cleanup_errors", []).append(str(error))
            self._write_report(report)


if __name__ == "__main__":
    unittest.main()
