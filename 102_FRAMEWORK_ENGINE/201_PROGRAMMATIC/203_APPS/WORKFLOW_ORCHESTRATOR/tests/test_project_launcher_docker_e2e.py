"""Opt-in, retained two-Project HTTP launcher proof; no Workflow worker.

Unit discovery exercises fixture metadata only.  Real Docker effects require
the explicit command-line runner and CAPRMEDIO_PROJECT_LAUNCHER_DOCKER_E2E=1.
Each group owns at most two containers and has a fifteen-minute deadline.
"""
from __future__ import annotations

import argparse
import asyncio
from contextlib import AsyncExitStack
from dataclasses import dataclass
import hashlib
import json
import os
from pathlib import Path
import secrets
import subprocess
import sys
import tempfile
import time
import unittest
import uuid

APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[3]
DOCKER = APP / "docker"
TOOLS = APP.parents[1] / "201_TOOLS"
sys.path[:0] = [str(DOCKER), str(TOOLS), str(TOOLS / "VALIDATE_ATOMS"), str(Path(__file__).parent)]

from project_selection import bind_selection, resolve_project  # noqa: E402
from runtime_images import ImageManager  # noqa: E402
from first_cut_http_security import probe_first_cut_http_security  # noqa: E402
import test_first_cut_http_docker_e2e as first_cut_http  # noqa: E402
from test_selected_workflows_docker_e2e import _structured_tool_result  # noqa: E402

ATOM_ID = "CA-O-999999"


def _snapshot(root: Path, names) -> dict[str, str]:
    files = []
    for name in names:
        directory = root / name
        files.extend(directory.rglob("*") if directory.is_dir() else [directory])
    result = {}
    for path in files:
        if path.name == ".env" or path.name.startswith(".env.") or path.name.endswith(".env"):
            raise AssertionError("protected file in proof boundary")
        if path.is_symlink():
            raise AssertionError("symlink in proof boundary")
        if path.is_file() and path.suffix not in {".pyc", ".pyo"}:
            result[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result


@dataclass(frozen=True)
class ProjectFixture:
    root: Path
    control: str
    marker: str
    source_ref: str
    source_sha256: str

    @classmethod
    def create(cls, root: Path, name: str, marker: str):
        root.mkdir(parents=True)
        control = ".caprmedio_" + name
        authority = root / control
        (authority / "09_operations").mkdir(parents=True)
        (authority / "_journal").mkdir()
        (authority / "caprmedio_project_settings.toml").write_text(
            f'[project]\nname = "{name}"\n[paths]\ncontrol_root = "{control}"\n'
            f'journal_root = "{control}/_journal"\nprojection_root = "{control}/_projection"\n'
            'runtime_root = ".caprmedio_runtime"\ntemporary_root = ".caprmedio_tmp"\n',
            encoding="utf-8",
        )
        (authority / "project_structure.toml").write_text(
            'schema_version = 1\n[[scope_units]]\nscope_unit_name = "FIXTURE"\n'
            f'authority_path = "{control}/09_operations"\n', encoding="utf-8",
        )
        (root / "fixture_entrypoint.py").write_text('"""Read-only fixture source carrier."""\n', encoding="utf-8")
        source_ref = f"{control}/09_operations/{ATOM_ID}--launcher-fixture.md"
        payload = (
            f"---\natom_id: {ATOM_ID}\nstatus: Active\ncontent_role: Operations\n"
            "type: Action\nversion: 1\nupdated_at: 2026-10-09 00:00:00 +0000\n"
            f"current_scope_unit: FIXTURE\nrelations: {{}}\n---\n# Summary\n\n{marker}\n\n"
            "```toml\n[tool_binding]\nname = \"LAUNCHER_FIXTURE\"\n"
            f'entrypoint = "fixture_entrypoint.py"\naction_ids = ["{ATOM_ID}"]\n```\n'
        ).encode("utf-8")
        (root / source_ref).write_bytes(payload)
        return cls(root.resolve(), control, marker, source_ref, hashlib.sha256(payload).hexdigest())

    def snapshot(self):
        return _snapshot(self.root, (self.control, "fixture_entrypoint.py"))


def _fixtures(parent: Path, group: str) -> list[ProjectFixture]:
    if group == "two-repositories":
        roots = [parent / "repo-a" / "project", parent / "repo-b" / "project"]
        for root in roots:
            (root.parent / ".git").mkdir(parents=True)
    else:
        repository = parent / "repo-multi"
        (repository / ".git").mkdir(parents=True)
        roots = [repository / "projects" / "alpha", repository / "projects" / "beta"]
    return [ProjectFixture.create(root, name, f"{group}: {name} authority")
            for root, name in zip(roots, ("alpha", "beta"), strict=True)]


def _launch(fixture, token, source_root, image, *, deadline):
    remaining = deadline - time.monotonic()
    assert remaining > 30, "proof deadline exhausted before launch"
    command = [sys.executable, str(DOCKER / "runtime.py"), "--project-root", str(fixture.root),
               "--control-root", fixture.control, "--source-root", str(source_root),
               "--image", image, "--no-build", "--startup-timeout", str(min(60, remaining - 20)),
               "--build-timeout", "600", "project-mcp"]
    environment = dict(os.environ, CAPRMEDIO_MCP_HTTP_SECRET_TOKEN=token)
    response = subprocess.run(command, env=environment, capture_output=True, text=True,
                              timeout=min(90, remaining - 10), check=False)
    assert token not in response.stdout and token not in response.stderr, "CLI rendered a bearer token"
    result = json.loads(response.stdout)
    assert isinstance(result, dict), "CLI did not return a structured result"
    assert response.returncode == (0 if result.get("readiness") is True else 1), result
    return result


async def _launch_many(fixtures, tokens, source_root, image, deadline, records=None):
    results = await asyncio.gather(*[asyncio.to_thread(_launch, fixture, token, source_root,
        image, deadline=deadline) for fixture, token in zip(fixtures, tokens, strict=True)], return_exceptions=True)
    if records is not None:
        records.extend(row for row in results if isinstance(row, dict))
    for row in results:
        if isinstance(row, BaseException):
            raise row
    return results


def _cleanup(fixtures, tokens, records):
    """Remove only resources attributed to retained disposable Project roots."""
    from project_mcp_backend import ProjectMcpBackend
    backend = ProjectMcpBackend(build_if_missing=False)
    failures = []
    for fixture, token in zip(fixtures, tokens, strict=True):
        selection = resolve_project(fixture.root, fixture.control)
        try:
            rows = backend.inspect(selection)
            if not rows:
                continue
            identifiers = [row["Id"] for row in rows]
            record = next((row for row in records if row.get("project_id") == selection.instance_id), None)
            if record is not None and record.get("container_id"):
                assert identifiers == [record["container_id"]], "cleanup container identity changed"
            labels = rows[0]["Config"]["Labels"]
            environment = backend._environment(selection, rows[0]["Image"],
                                               labels["org.caprmedio.runtime.fingerprint"], token)
            command = ["docker", "compose", "--env-file", "/dev/null", "--project-name",
                       selection.compose_project, "-f", str(DOCKER / "project-mcp.compose.yaml"),
                       "down", "--timeout", "10"]
            response = subprocess.run(command, env=environment, stdout=subprocess.DEVNULL,
                                      stderr=subprocess.DEVNULL, timeout=45, check=False)
            assert response.returncode == 0 and not backend.inspect(selection), "fixture cleanup incomplete"
        except Exception as error:
            failures.append(type(error).__name__)
    assert not failures, {"cleanup_failures": failures}


async def _prove_group(parent, group, source_root, image, deadline, evidence):
    from project_mcp_backend import ProjectMcpBackend
    fixtures = _fixtures(parent, group)
    tokens = [secrets.token_urlsafe(32), secrets.token_urlsafe(32)]
    baseline = [fixture.snapshot() for fixture in fixtures]
    records = evidence["launches"] = []
    backend = ProjectMcpBackend(build_if_missing=False)
    harness = first_cut_http.FirstCutHttpDockerEndToEnd("test_six_workflows_over_authenticated_http_mcp")
    try:
        launches = await _launch_many(fixtures, tokens, source_root, image, deadline, records)
        assert all(row["condition"] == "READY_STARTED" for row in launches), launches
        for field in ("project_id", "container_id", "port", "url"):
            assert launches[0][field] != launches[1][field], {"colliding_field": field}
        for fixture, row in zip(fixtures, launches, strict=True):
            selection = resolve_project(fixture.root, fixture.control)
            assert row["project_id"] == selection.instance_id and row["project_root"] == str(fixture.root), row
            inspected = await asyncio.to_thread(backend.inspect, selection)
            assert len(inspected) == 1 and inspected[0]["Mounts"][0]["Source"] == str(fixture.root), inspected
        repeat = await _launch_many(fixtures, tokens, source_root, image, deadline)
        concurrent = await _launch_many([fixtures[0]] * 2, [tokens[0]] * 2, source_root, image, deadline)
        for row, original in [(repeat[0], launches[0]), (repeat[1], launches[1]),
                              *((row, launches[0]) for row in concurrent)]:
            assert row["condition"] == "READY_REUSED", row
            assert all(row[key] == original[key] for key in ("container_id", "port", "project_id")), row
        evidence.update(repeated=repeat, concurrent=concurrent)
        async with AsyncExitStack() as stack:
            sessions = [await stack.enter_async_context(harness._http_session(row["url"], token))
                        for row, token in zip(launches, tokens, strict=True)]
            reads, security = [], []
            for index, ((session, metadata), fixture, row, token) in enumerate(zip(
                    sessions, fixtures, launches, tokens, strict=True)):
                names = {tool.name for tool in (await session.list_tools()).tools}
                security.append(await asyncio.to_thread(probe_first_cut_http_security, row["url"], token,
                    list_tools=lambda _url, _token: names, continuation_session_id=metadata.session_id,
                    recording_boundary=lambda: [item.snapshot() for item in fixtures]))
                read = _structured_tool_result(await session.call_tool("get_execution_context", {"request": {"id": ATOM_ID}}))
                definition = read["definition"]
                assert read["context_complete"] and definition["source_path"] == fixture.source_ref, read
                assert definition["sha256"] == fixture.source_sha256 and fixture.marker in definition["content"], read
                reads.append(read)
                from first_cut_http_security import _urllib_status
                assert await asyncio.to_thread(_urllib_status, row["url"].replace("/mcp", "/health"),
                    {"Authorization": "Bearer " + tokens[1 - index]}) == 401
                refused = _structured_tool_result(await session.call_tool("create_atom", {"request": {"operation_route": "create_atom", "request_id": "unconfigured"}}))
                assert refused.get("disposition") in {"blocked", "rejected"}, refused
            request_id = str(uuid.uuid4())
            receipt_paths = [resolve_project(item.root, item.control).reload_state / f"{request_id}.json" for item in fixtures]
            assert receipt_paths[0] != receipt_paths[1] and not any(path.exists() for path in receipt_paths)
            receipts = await asyncio.gather(*[session.call_tool("reload_mcp_implementation", {
                "request": {"operation": "reload", "request_id": request_id}}) for session, _metadata in sessions])
            receipts = [_structured_tool_result(item) for item in receipts]
            for receipt, path in zip(receipts, receipt_paths, strict=True):
                assert receipt["outcome"] == "unchanged" and not receipt["diagnostics"], receipt
                assert json.loads(path.read_text(encoding="utf-8")) == receipt
            evidence.update(reads=reads, security=security, reload_receipts=receipts,
                            reload_receipt_paths=[str(path) for path in receipt_paths])
        refused = await asyncio.to_thread(_launch, fixtures[0], tokens[1], source_root, image, deadline=deadline)
        assert refused["condition"] == "READINESS_FAILED" and "url" not in refused, refused
        assert [item.snapshot() for item in fixtures] == baseline, "read/security/reload changed authority or Journal"
        evidence["readiness_refusal"] = refused
    finally:
        await asyncio.to_thread(_cleanup, fixtures, tokens, records)
    assert time.monotonic() < deadline, "fifteen-minute proof deadline exceeded"
    evidence["status"] = "completed"


class ProjectLauncherFixtureTests(unittest.TestCase):
    def test_nested_projects_have_valid_distinct_selected_authority(self):
        from capability_discovery.service import Service, Context
        parent = ROOT / ".caprmedio_tmp" / "launcher-epic-1829" / "fixture-checks"
        parent.mkdir(parents=True, exist_ok=True)
        fixtures = _fixtures(Path(tempfile.mkdtemp(dir=parent)), "same-repository")
        for fixture in fixtures:
            selection = resolve_project(fixture.root, fixture.control)
            self.assertFalse((fixture.root / ".git").exists())
            with bind_selection(selection):
                definition = Service(fixture.root).context(Context(id=ATOM_ID))["definition"]
            self.assertEqual(fixture.source_ref, definition["source_path"])
            self.assertEqual(fixture.source_sha256, definition["sha256"])
        self.assertNotEqual(fixtures[0].source_sha256, fixtures[1].source_sha256)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=ROOT)
    parser.add_argument("--scratch", type=Path, required=True)
    parser.add_argument("--group", choices=("two-repositories", "same-repository", "all"), default="all")
    images = parser.add_mutually_exclusive_group(required=True)
    images.add_argument("--image")
    images.add_argument("--build-missing", action="store_true")
    args = parser.parse_args(argv)
    if os.environ.get("CAPRMEDIO_PROJECT_LAUNCHER_DOCKER_E2E") != "1":
        parser.error("real Docker proof requires CAPRMEDIO_PROJECT_LAUNCHER_DOCKER_E2E=1")
    scratch = args.scratch.resolve(strict=True)
    assert args.scratch.is_absolute() and not args.scratch.is_symlink() and scratch.is_dir()
    assert scratch.is_relative_to(ROOT / ".caprmedio_tmp") and scratch != ROOT / ".caprmedio_tmp"
    attempt = Path(tempfile.mkdtemp(prefix="launcher-proof-", dir=scratch))
    report = {"schema": "caprmedio.project_launcher_docker_e2e.v1", "attempt": str(attempt), "groups": []}
    retained = _snapshot(ROOT, (".caprmedio_install", ".caprmedio_runtime/framework"))
    started = time.monotonic()
    class RecordedImages(ImageManager):
        def _run(self, argv, **kwargs):
            report.setdefault("image_commands", []).append(list(argv))
            return super()._run(argv, **kwargs)
    try:
        manager = RecordedImages(args.source_root, timeout=600)
        report["image_id"] = manager.resolve(explicit_id=args.image, build_if_missing=args.build_missing)
        if args.build_missing:
            assert sum(command[:2] == ["docker", "build"] for command in report["image_commands"]) == 1, "missing-image case did not build exactly once"
        groups = ("two-repositories", "same-repository") if args.group == "all" else (args.group,)
        for index, group in enumerate(groups):
            entry = {"group": group, "status": "running"}
            report["groups"].append(entry)
            parent = attempt / group
            parent.mkdir()
            deadline = (started if index == 0 else time.monotonic()) + 900
            asyncio.run(_prove_group(parent, group, args.source_root, report["image_id"], deadline, entry))
        assert retained == _snapshot(ROOT, (".caprmedio_install", ".caprmedio_runtime/framework")), "root N state changed"
        report["status"] = "completed"
    except BaseException as error:
        report.update(status="failed", failure_type=type(error).__name__)
        raise
    finally:
        (attempt / "result.json").write_text(json.dumps(report, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"result": str(attempt / "result.json"), "status": report.get("status"),
                          "image_id": report.get("image_id")}, sort_keys=True))


if __name__ == "__main__":
    main()
