# CA-E-677@30
# CA-E-794@5
"""Opt-in real-project reproduction of the mixed update/delete batch in C712."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import tempfile
import time
import unittest
from uuid import uuid4

import test_workbench_live_canary as lifecycle
from workbench_live_canary_support import (
    LiveCanaryError, atom_carrier, authority_path, copy_declaration_tree,
    declaration_target, current_atom_id_exists, remove_owned_file, request, scope_authority,
    validate_atom_carrier, validate_declaration_tree, write_scope_declaration,
)


class WorkbenchLiveMixedCanary(unittest.TestCase):
    def test_current_project_mixed_update_delete_batch(self) -> None:  # noqa: C901 - explicit live-write safety phases
        helper = lifecycle.WorkbenchLiveCanary()
        root, url, dry_run = helper._configuration()
        control = lifecycle.control_root(root)
        declarations = lifecycle.read_scope_unit_declarations(root, control)
        project_name = helper._project_name(control)
        scope, _, _, _ = helper._scenario(root, declarations, token=uuid4().hex[:10].upper())
        parent = authority_path(declarations, root, lifecycle.PARENT_SCOPE)
        authority = scope_authority(parent, scope)
        declaration = declaration_target(parent, scope)
        self.assertFalse(authority.exists())
        self.assertFalse(declaration.exists())
        ids = [f"CA-R-{900000000 + uuid4().int % 99999999}" for _ in range(12)]
        ids[-2:] = [value.replace("CA-R-", "CA-M-") for value in ids[-2:]]
        self.assertEqual(len(set(ids)), 12)
        self.assertFalse(any(current_atom_id_exists(root, value) for value in ids))
        paths = [authority / ("04_requirement" if index < 10 else "05_method") / f"{value}-mixed-canary.md"
                 for index, value in enumerate(ids)]
        drafts = [path.parent / "draft" / f"{value}@2-draft-mixed-canary.md"
                  for path, value in zip(paths[-2:], ids[-2:])]
        endpoint = url + f"{lifecycle.WORKBENCH_PATH}/{project_name}/run"
        status_url = url + f"{lifecycle.WORKBENCH_PATH}/{project_name}/status"
        selection = ",".join(f"'{value}'" for value in ids)
        query = ('SELECT "header.identity.atom_id", status_group, "header.state.version" '
                 f'FROM atoms WHERE "header.identity.atom_id" IN ({selection}) ORDER BY 1, 2')
        expected = sorted([[value, "Current", 1] for value in ids] + [[value, "Draft", 2] for value in ids[-2:]])
        owned: dict[Path, str] = {}
        report: dict[str, object] = {"project": str(root), "dry_run": dry_run, "scope": scope.name}
        output = lifecycle.REPORT_DIRECTORY / "mixed-latest.json"
        output.parent.mkdir(parents=True, exist_ok=True)

        def write(path: Path, raw: str) -> None:
            if path in owned:
                self.assertEqual(owned[path], hashlib.sha256(path.read_bytes()).hexdigest())
            else:
                self.assertFalse(path.exists())
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(raw, encoding="utf-8")
            validate_atom_carrier(path)
            owned[path] = hashlib.sha256(path.read_bytes()).hexdigest()

        def carrier(value: str, version: int, path: Path, *, draft: bool = False) -> str:
            text = atom_carrier(value, version, scope=scope, destination=path, root=root)
            if value.startswith("CA-M-"):
                text = text.replace("role: Requirement", "role: Method").replace("form: Declaration", "form: Decision")
            if draft:
                text = text.replace(f"ref_id: {value}", f"ref_id: {value}@{version}-draft").replace("status: Active", "status: Draft")
            return text

        def wait(rows: list[list[object]], *, idle: bool = False) -> float:
            started = time.monotonic()
            last: object = None
            while time.monotonic() - started < 90:
                code, payload = request(endpoint, method="POST", payload={"sql": query, "result_delivery": "inline"})
                last = payload
                if code == 200 and isinstance(payload, dict) and payload.get("rows") == rows:
                    if not idle:
                        return time.monotonic() - started
                    code, state = request(status_url, method="POST", payload={})
                    if code == 200 and state.get("syncing") is False:
                        return time.monotonic() - started
                time.sleep(0.2)
            self.fail(f"mixed canary did not reach expected rows: {last!r}")

        try:
            with tempfile.TemporaryDirectory(dir=output.parent) as temporary:
                staged_root = Path(temporary) / "project"
                staged_root.mkdir()
                staged_control = copy_declaration_tree(root, control, declarations, staged_root)
                staged_parent = authority_path(declarations, staged_root, lifecycle.PARENT_SCOPE)
                write_scope_declaration(declaration_target(staged_parent, scope), scope, project_name)
                self.assertIn(scope.name, validate_declaration_tree(staged_root, staged_control).by_name)
                for index, path in enumerate(paths):
                    candidate = Path(temporary) / path.name
                    candidate.write_text(carrier(ids[index], 1, path), encoding="utf-8")
                    validate_atom_carrier(candidate)
                for value, path in zip(ids[-2:], drafts):
                    candidate = Path(temporary) / path.name
                    candidate.write_text(carrier(value, 2, path, draft=True), encoding="utf-8")
                    validate_atom_carrier(candidate)
            if dry_run:
                report["outcome"] = "preflight_validated_no_source_write"
                return
            authority.mkdir()
            owned[declaration] = write_scope_declaration(declaration, scope, project_name)
            helper._wait_for_rows(endpoint, helper._scope_query(scope.scope_unit_id),
                                  [[scope.name, scope.scope_unit_id, lifecycle.PARENT_SCOPE, 1]], present=True)
            started = time.monotonic()
            for value, path in zip(ids, paths):
                write(path, carrier(value, 1, path))
            for value, path in zip(ids[-2:], drafts):
                write(path, carrier(value, 2, path, draft=True))
            wait(expected)
            report["create_visibility_s"] = round(time.monotonic() - started, 3)
            started = time.monotonic()
            for value, path in zip(ids[:10], paths[:10]):
                write(path, carrier(value, 2, path))
            for path in paths[-2:] + drafts:
                remove_owned_file(path, owned.pop(path))
            wait([[value, "Current", 2] for value in sorted(ids[:10])], idle=True)
            report["mixed_visibility_s"] = round(time.monotonic() - started, 3)
            report["updated_current"] = 10
            report["deleted_current_methods"] = 2
            report["deleted_method_drafts"] = 2
            report["outcome"] = "passed"
        except Exception as error:
            report.update(outcome="failed", error=str(error))
            raise
        finally:
            cleanup_errors = []
            for path, digest in tuple(owned.items()):
                if path != declaration:
                    try:
                        remove_owned_file(path, digest)
                    except (OSError, LiveCanaryError) as error:
                        cleanup_errors.append(str(error))
            if authority.exists():
                for directory in sorted((p for p in authority.rglob("*") if p.is_dir()),
                                        key=lambda p: len(p.parts), reverse=True) + [authority]:
                    try:
                        directory.rmdir()
                    except OSError as error:
                        cleanup_errors.append(str(error))
            if declaration in owned:
                try:
                    remove_owned_file(declaration, owned[declaration])
                except (OSError, LiveCanaryError) as error:
                    cleanup_errors.append(str(error))
            if not dry_run and not cleanup_errors:
                try:
                    wait([])
                    helper._wait_for_rows(endpoint, helper._scope_query(scope.scope_unit_id), [], present=False)
                except (AssertionError, LiveCanaryError) as error:
                    cleanup_errors.append(str(error))
            if cleanup_errors:
                report.update(cleanup_errors=cleanup_errors, outcome="cleanup_failed")
            output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
            self.assertEqual([], cleanup_errors, "mixed canary cleanup failed; see its report")



if __name__ == "__main__":
    unittest.main()
