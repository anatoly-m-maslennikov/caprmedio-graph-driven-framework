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
import socket
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import patch
import uuid

APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[3]
DOCKER = APP / "docker"
TOOLS = APP.parents[1] / "201_TOOLS"
sys.path[:0] = [str(DOCKER), str(TOOLS), str(TOOLS / "VALIDATE_ATOMS"), str(Path(__file__).parent)]

from project_selection import bind_selection, resolve_project  # noqa: E402
from runtime_images import FINGERPRINT_LABEL, ImageManager, SCHEMA, SCHEMA_LABEL  # noqa: E402
from first_cut_http_security import probe_first_cut_http_security  # noqa: E402
import test_first_cut_http_docker_e2e as first_cut_http  # noqa: E402
from test_selected_workflows_docker_e2e import _structured_tool_result  # noqa: E402

ATOM_IDS = {"alpha": "CA-O-999991", "beta": "CA-O-999992"}


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
    atom_id: str

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
        atom_id = ATOM_IDS[name]
        source_ref = f"{control}/09_operations/{atom_id}--launcher-fixture.md"
        payload = (
            f"---\natom_id: {atom_id}\nstatus: Active\ncontent_role: Operations\n"
            "type: Action\nversion: 1\nupdated_at: 2026-10-09 00:00:00 +0000\n"
            f"current_scope_unit: FIXTURE\nrelations: {{}}\n---\n# Summary\n\n{marker}\n\n"
            "```toml\n[tool_binding]\nname = \"LAUNCHER_FIXTURE\"\n"
            f'entrypoint = "fixture_entrypoint.py"\naction_ids = ["{atom_id}"]\n```\n'
        ).encode("utf-8")
        (root / source_ref).write_bytes(payload)
        return cls(root.resolve(), control, marker, source_ref, hashlib.sha256(payload).hexdigest(), atom_id)

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


def _launch(fixture, token, source_root, image, *, deadline, port=None, command_receipt=None):
    remaining = deadline - time.monotonic()
    assert remaining > 30, "proof deadline exhausted before launch"
    command = [sys.executable, str(DOCKER / "runtime.py"), "--project-root", str(fixture.root),
               "--control-root", fixture.control, "--source-root", str(source_root),
               "--startup-timeout", str(min(60, remaining - 20)), "--build-timeout", "600"]
    if image is not None:
        command.extend(("--image", image, "--no-build"))
    if port is not None:
        command.extend(("--port", str(port)))
    command.append("project-mcp")
    if command_receipt is not None:
        command_receipt["argv"] = command.copy()
    environment = dict(os.environ)
    command_timeout = min(90 if image is not None else 690, remaining - 5)
    response = subprocess.run(command, env=environment, capture_output=True, text=True,
                              timeout=command_timeout, check=False)
    result = json.loads(response.stdout)
    assert isinstance(result, dict), "CLI did not return a structured result"
    assert response.returncode == (0 if result.get("readiness") is True else 1), result
    return result


async def _launch_many(fixtures, tokens, source_root, image, deadline, records=None, ports=None):
    if ports is None:
        ports = [None] * len(fixtures)
    results = await asyncio.gather(*[asyncio.to_thread(_launch, fixture, token, source_root,
        image, deadline=deadline, port=port) for fixture, token, port in zip(fixtures, tokens, ports, strict=True)], return_exceptions=True)
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
    receipts, failures = [], []
    for fixture, token in zip(fixtures, tokens, strict=True):
        selection = resolve_project(fixture.root, fixture.control)
        receipt = {"project_id": selection.instance_id, "before": [], "after": []}
        try:
            rows = backend.inspect(selection)
            receipt["before"] = [row["Id"] for row in rows]
            if not rows:
                receipt["outcome"] = "already_absent"
                continue
            identifiers = [row["Id"] for row in rows]
            record = next((row for row in records if row.get("project_id") == selection.instance_id), None)
            if record is not None and record.get("container_id"):
                assert identifiers == [record["container_id"]], "cleanup container identity changed"
            labels = rows[0]["Config"]["Labels"]
            environment = backend._environment(selection, rows[0]["Image"],
                                               labels["org.caprmedio.runtime.fingerprint"])
            command = ["docker", "compose", "--env-file", "/dev/null", "--project-name",
                       selection.compose_project, "-f", str(DOCKER / "project-mcp.compose.yaml"),
                       "down", "--timeout", "10"]
            response = subprocess.run(command, env=environment, stdout=subprocess.DEVNULL,
                                      stderr=subprocess.DEVNULL, timeout=45, check=False)
            assert response.returncode == 0, "fixture cleanup command failed"
            remaining = backend.inspect(selection)
            assert not remaining, "fixture cleanup incomplete"
            receipt["outcome"] = "removed"
        except Exception as error:
            failures.append(type(error).__name__)
            receipt["outcome"] = "failed"
        finally:
            try:
                receipt["after"] = [row["Id"] for row in backend.inspect(selection)]
            except Exception as error:
                receipt["after_inspection_failure"] = type(error).__name__
                failures.append(type(error).__name__)
            receipts.append(receipt)
    return receipts, failures


def _available_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as probe:
        probe.bind(("127.0.0.1", 0))
        return int(probe.getsockname()[1])


def _compose_services(selection, token, row):
    """Observe only this selected Project's compose service names."""
    from project_mcp_backend import ProjectMcpBackend
    backend = ProjectMcpBackend(build_if_missing=False)
    labels = row["Config"]["Labels"]
    environment = backend._environment(selection, row["Image"], labels["org.caprmedio.runtime.fingerprint"])
    command = ["docker", "compose", "--env-file", "/dev/null", "--project-name", selection.compose_project,
               "-f", str(DOCKER / "project-mcp.compose.yaml"), "ps", "--all", "--format", "json"]
    response = subprocess.run(command, env=environment, capture_output=True, text=True, timeout=45, check=False)
    assert response.returncode == 0, "compose status failed"
    rows = [json.loads(line) for line in response.stdout.splitlines() if line.strip()]
    services = {item.get("Service") for item in rows if isinstance(item, dict)}
    assert services == {"mcp-http"}, rows
    return sorted(services)


def _collision_diagnostic(rows):
    """Classify a failed explicit-port start without accepting a host remap."""
    assert isinstance(rows, list)
    if not rows:
        return "DOCKER_START_FAILED", []
    assert len(rows) == 1, "collision created more than one selected runtime"
    observed = []
    for row in rows:
        assert isinstance(row, dict)
        state = row.get("State")
        assert isinstance(state, dict)
        health = state.get("Health")
        assert isinstance(health, dict)
        network = row.get("NetworkSettings")
        assert isinstance(network, dict)
        ports = network.get("Ports")
        assert isinstance(ports, dict) and set(ports) == {"8092/tcp"}
        assert ports["8092/tcp"] == [], "collision created a host publisher"
        assert state.get("Status") == "running" and health.get("Status") == "healthy"
        observed.append({"container_id": row.get("Id"), "state": state.get("Status"),
                         "health": health.get("Status"), "ports": {"8092/tcp": ports["8092/tcp"]}})
    return "DOCKER_PUBLICATION_FAILED", observed


def _bounded_collision_observed(rows):
    """Safe failure receipt: identity, lifecycle state, and publisher counts only."""
    if not isinstance(rows, list):
        return [{"shape": type(rows).__name__}]
    observed = []
    for row in rows[:2]:
        if not isinstance(row, dict):
            observed.append({"shape": type(row).__name__})
            continue
        state = row.get("State") if isinstance(row.get("State"), dict) else {}
        health = state.get("Health") if isinstance(state.get("Health"), dict) else {}
        network = row.get("NetworkSettings") if isinstance(row.get("NetworkSettings"), dict) else {}
        ports = network.get("Ports") if isinstance(network.get("Ports"), dict) else {}
        observed.append({"container_id": row.get("Id"), "state": state.get("Status"),
                         "health": health.get("Status"), "ports": {
                             key: len(value) if isinstance(value, list) else "invalid"
                             for key, value in ports.items() if isinstance(key, str)}})
    return observed


def _assert_collision_refusal(result, expected):
    assert result["condition"] == expected, result
    assert result["readiness"] is False and "url" not in result, result


async def _prove_group(parent, group, source_root, image, deadline, evidence):
    from project_mcp_backend import ProjectMcpBackend
    fixtures = _fixtures(parent, group)
    tokens = [None, None]
    baseline = [fixture.snapshot() for fixture in fixtures]
    records = evidence["launches"] = []
    backend = ProjectMcpBackend(build_if_missing=False)
    harness = first_cut_http.FirstCutHttpDockerEndToEnd("test_six_workflows_over_authenticated_http_mcp")
    failure = None
    try:
        if image is None:
            prebuild = ImageManager(source_root, timeout=600)
            identity = prebuild.identity()
            catalogue = prebuild._run((
                "docker", "image", "ls", "--quiet", "--no-trunc",
                "--filter", f"label={SCHEMA_LABEL}={SCHEMA}",
                "--filter", f"label={FINGERPRINT_LABEL}={identity.fingerprint}",
            ))
            if catalogue.strip():
                raise AssertionError("missing-image proof refused: compatible source image already exists")
            build_contract = {}
            alpha = await asyncio.to_thread(_launch, fixtures[0], tokens[0], source_root, None,
                                            deadline=deadline, command_receipt=build_contract)
            assert "--image" not in build_contract["argv"] and "--no-build" not in build_contract["argv"]
            assert alpha["condition"] == "READY_STARTED", alpha
            assert alpha["fingerprint"] == identity.fingerprint, alpha
            assert isinstance(alpha.get("image_id"), str), alpha
            assert prebuild._inspect(alpha["image_id"], identity) == alpha["image_id"]
            image = alpha["image_id"]
            records.append(alpha)
            evidence["build_default"] = {
                "prelaunch_matching_image": False,
                "launcher_argv": build_contract["argv"],
                "returned_image_id": image,
                "source_fingerprint": identity.fingerprint,
            }
        else:
            alpha = await asyncio.to_thread(_launch, fixtures[0], tokens[0], source_root, image,
                                            deadline=deadline)
            records.append(alpha)
        assert alpha["condition"] == "READY_STARTED", alpha
        beta_port = _available_port()
        assert beta_port != alpha["port"], "ephemeral selection collided with the live dynamic publication"
        beta = await asyncio.to_thread(_launch, fixtures[1], tokens[1], source_root, image,
                                       deadline=deadline, port=beta_port)
        records.append(beta)
        launches = [alpha, beta]
        assert all(row["condition"] == "READY_STARTED" for row in launches), launches
        for field in ("project_id", "container_id", "port", "url"):
            assert launches[0][field] != launches[1][field], {"colliding_field": field}
        for fixture, row, token in zip(fixtures, launches, tokens, strict=True):
            selection = resolve_project(fixture.root, fixture.control)
            assert row["project_id"] == selection.instance_id and row["project_root"] == str(fixture.root), row
            inspected = await asyncio.to_thread(backend.inspect, selection)
            assert len(inspected) == 1 and inspected[0]["Mounts"][0]["Source"] == str(fixture.root), inspected
            evidence.setdefault("compose_services", {})[fixture.marker] = _compose_services(selection, token, inspected[0])
        repeat = await _launch_many(fixtures, tokens, source_root, image, deadline,
                                    ports=[None, beta_port])
        concurrent = await _launch_many([fixtures[0]] * 2, [tokens[0]] * 2, source_root, image, deadline,
                                        ports=[None, None])
        for row, original in [(repeat[0], launches[0]), (repeat[1], launches[1]),
                              *((row, launches[0]) for row in concurrent)]:
            assert row["condition"] == "READY_REUSED", row
            assert all(row[key] == original[key] for key in ("container_id", "port", "project_id")), row
        mismatch = await asyncio.to_thread(_launch, fixtures[1], tokens[1], source_root, image,
                                           deadline=deadline, port=alpha["port"])
        assert mismatch["condition"] == "RUNTIME_MISMATCH", mismatch
        evidence.update(repeated=repeat, concurrent=concurrent)
        async with AsyncExitStack() as stack:
            sessions = [await stack.enter_async_context(harness._http_session(row["url"], None))
                        for row, token in zip(launches, tokens, strict=True)]
            reads, security = [], []
            for index, ((session, metadata), fixture, row, token) in enumerate(zip(
                    sessions, fixtures, launches, tokens, strict=True)):
                names = {tool.name for tool in (await session.list_tools()).tools}
                security.append(await asyncio.to_thread(probe_first_cut_http_security, row["url"], None,
                    list_tools=lambda _url, _token: names,
                    recording_boundary=lambda: [item.snapshot() for item in fixtures]))
                read = _structured_tool_result(await session.call_tool("get_execution_context", {"request": {"id": fixture.atom_id}}))
                definition = read["definition"]
                assert read["context_complete"] and definition["source_path"] == fixture.source_ref, read
                assert definition["sha256"] == fixture.source_sha256 and fixture.marker in definition["content"], read
                foreign = await session.call_tool("get_execution_context", {
                    "request": {"id": fixtures[1 - index].atom_id}})
                assert foreign.is_error, foreign
                reads.append(read)
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
        beta_cleanup, beta_cleanup_failures = await asyncio.to_thread(
            _cleanup, [fixtures[1]], [tokens[1]], records)
        assert not beta_cleanup_failures, {"cleanup_failures": beta_cleanup_failures}
        historical_beta_id = beta["container_id"]
        beta_selection = resolve_project(fixtures[1].root, fixtures[1].control)
        records[:] = [row for row in records if row.get("project_id") != beta_selection.instance_id]
        occupied = await asyncio.to_thread(_launch, fixtures[1], tokens[1], source_root, image,
                                           deadline=deadline, port=alpha["port"])
        alpha_rows = await asyncio.to_thread(backend.inspect, resolve_project(fixtures[0].root, fixtures[0].control))
        assert len(alpha_rows) == 1 and alpha_rows[0]["Id"] == alpha["container_id"], alpha_rows
        alpha_publishers = alpha_rows[0]["NetworkSettings"]["Ports"]["8092/tcp"]
        assert alpha_publishers == [{"HostIp": "127.0.0.1", "HostPort": str(alpha["port"])}], alpha_rows
        failed_beta_rows = await asyncio.to_thread(backend.inspect, beta_selection)
        evidence["collision_observed"] = _bounded_collision_observed(failed_beta_rows)
        evidence["occupied_result"] = occupied
        expected_collision, _collision_shape = _collision_diagnostic(failed_beta_rows)
        _assert_collision_refusal(occupied, expected_collision)
        failed_cleanup, failed_cleanup_failures = await asyncio.to_thread(
            _cleanup, [fixtures[1]], [tokens[1]], records)
        assert not failed_cleanup_failures, {"cleanup_failures": failed_cleanup_failures}
        assert not await asyncio.to_thread(backend.inspect, beta_selection)
        evidence["port_cases"] = {"dynamic_started": alpha["port"], "explicit_started": beta_port,
                                  "explicit_reused": repeat[1]["port"], "mismatch": mismatch,
                                  "occupied_refusal": occupied, "historical_beta_container_id": historical_beta_id,
                                  "pre_occupied_cleanup": beta_cleanup,
                                  "failed_resource_cleanup": failed_cleanup}
        anonymous_reuse = await asyncio.to_thread(_launch, fixtures[0], None, source_root, image,
                                                  deadline=deadline)
        assert anonymous_reuse["condition"] == "READY_REUSED" and anonymous_reuse["readiness"] is True, anonymous_reuse
        assert all(anonymous_reuse[key] == alpha[key] for key in ("url", "container_id", "port", "project_id")), anonymous_reuse
        assert [item.snapshot() for item in fixtures] == baseline, "read/security/reload changed authority or Journal"
        evidence["anonymous_readiness_reuse"] = anonymous_reuse
    except BaseException as error:
        failure = error
        raise
    finally:
        receipts, cleanup_failures = await asyncio.to_thread(_cleanup, fixtures, tokens, records)
        evidence["cleanup_receipts"] = receipts
        evidence["cleanup_failures"] = cleanup_failures
        if failure is None:
            assert not cleanup_failures, {"cleanup_failures": cleanup_failures}
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
                definition = Service(fixture.root).context(Context(id=fixture.atom_id))["definition"]
                with self.assertRaisesRegex(ValueError, "Unknown or ambiguous capability"):
                    Service(fixture.root).context(Context(id=fixtures[1 if fixture is fixtures[0] else 0].atom_id))
            self.assertEqual(fixture.source_ref, definition["source_path"])
            self.assertEqual(fixture.source_sha256, definition["sha256"])
        self.assertNotEqual(fixtures[0].source_sha256, fixtures[1].source_sha256)

    def test_default_build_launch_allows_the_bounded_build_window(self):
        parent = ROOT / ".caprmedio_tmp" / "launcher-epic-1829" / "fixture-checks"
        parent.mkdir(parents=True, exist_ok=True)
        fixture = _fixtures(Path(tempfile.mkdtemp(dir=parent)), "same-repository")[0]
        receipt = {}
        response = {"readiness": False, "condition": "BUILD_FAILED"}
        with patch("subprocess.run", return_value=subprocess.CompletedProcess([], 1, json.dumps(response), "")) as run:
            result = _launch(fixture, "fixture-token", ROOT, None,
                             deadline=time.monotonic() + 900, command_receipt=receipt)
        self.assertEqual("BUILD_FAILED", result["condition"])
        self.assertNotIn("--image", receipt["argv"])
        self.assertNotIn("--no-build", receipt["argv"])
        self.assertGreater(run.call_args.kwargs["timeout"], 600)
        self.assertLessEqual(run.call_args.kwargs["timeout"], 690)

    def test_absent_cleanup_has_one_scoped_receipt(self):
        import project_mcp_backend
        parent = ROOT / ".caprmedio_tmp" / "launcher-epic-1829" / "fixture-checks"
        parent.mkdir(parents=True, exist_ok=True)
        fixture = _fixtures(Path(tempfile.mkdtemp(dir=parent)), "same-repository")[0]

        class Backend:
            def __init__(self, **_kwargs):
                pass

            def inspect(self, _selection):
                return []

        with patch.object(project_mcp_backend, "ProjectMcpBackend", Backend):
            receipts, failures = _cleanup([fixture], ["fixture-token"], [])
        self.assertEqual([], failures)
        self.assertEqual(1, len(receipts))
        self.assertEqual("already_absent", receipts[0]["outcome"])
        self.assertEqual([], receipts[0]["after"])

    def test_retained_n_failure_receipt_is_not_completed(self):
        parent = ROOT / ".caprmedio_tmp" / "launcher-epic-1829" / "fixture-checks"
        parent.mkdir(parents=True, exist_ok=True)
        scratch = Path(tempfile.mkdtemp(dir=parent))
        attempt = scratch / "attempt"

        async def prove(_parent, _group, _source, _image, _deadline, evidence):
            evidence["build_default"] = {"returned_image_id": "sha256:" + "a" * 64}

        def make_attempt(**_kwargs):
            attempt.mkdir()
            return str(attempt)

        module = sys.modules[__name__]
        with patch.dict(os.environ, {"CAPRMEDIO_PROJECT_LAUNCHER_DOCKER_E2E": "1"}), \
                patch.object(module, "_snapshot", side_effect=[{"N": "before"}, {"N": "after"}]), \
                patch.object(module, "_prove_group", prove), \
                patch.object(tempfile, "mkdtemp", side_effect=make_attempt):
            with self.assertRaisesRegex(AssertionError, "root N state changed"):
                main(["--scratch", str(scratch), "--group", "two-repositories", "--build-missing"])
        report = json.loads((attempt / "result.json").read_text(encoding="utf-8"))
        self.assertEqual("failed", report["status"])
        self.assertEqual("AssertionError", report["failure_type"])
        self.assertFalse(report["retained_N"]["equal"])

    def test_collision_diagnostics_distinguish_start_and_publication_failures(self):
        self.assertEqual("DOCKER_START_FAILED", _collision_diagnostic([])[0])
        stopped = [{"Id": "beta-stopped", "State": {"Status": "exited"},
                    "NetworkSettings": {"Ports": {"8092/tcp": []}}}]
        with self.assertRaises(AssertionError):
            _collision_diagnostic(stopped)
        unpublished = [{"Id": "beta-unpublished", "State": {"Status": "running", "Health": {"Status": "healthy"}},
                        "NetworkSettings": {"Ports": {"8092/tcp": []}}}]
        code, observed = _collision_diagnostic(unpublished)
        self.assertEqual("DOCKER_PUBLICATION_FAILED", code)
        self.assertEqual([], observed[0]["ports"]["8092/tcp"])

    def test_collision_diagnostic_rejects_a_silent_host_remap(self):
        remapped = [{"Id": "beta-remapped", "State": {"Status": "running", "Health": {"Status": "healthy"}},
                     "NetworkSettings": {"Ports": {"8092/tcp": [{"HostIp": "127.0.0.1", "HostPort": "54321"}]}}}]
        with self.assertRaisesRegex(AssertionError, "host publisher"):
            _collision_diagnostic(remapped)

    def test_collision_diagnostic_rejects_multiple_or_other_target_publications(self):
        healthy = {"State": {"Status": "running", "Health": {"Status": "healthy"}},
                   "NetworkSettings": {"Ports": {"8092/tcp": []}}}
        with self.assertRaisesRegex(AssertionError, "more than one"):
            _collision_diagnostic([{**healthy, "Id": "beta-one"}, {**healthy, "Id": "beta-two"}])
        other_target = {**healthy, "Id": "beta-other", "NetworkSettings": {"Ports": {
            "8092/tcp": [], "8093/tcp": [{"HostIp": "127.0.0.1", "HostPort": "54322"}],
        }}}
        with self.assertRaises(AssertionError):
            _collision_diagnostic([other_target])

    def test_collision_refusal_rejects_a_wrong_code_or_url(self):
        with self.assertRaises(AssertionError):
            _assert_collision_refusal({"condition": "DOCKER_START_FAILED", "readiness": False,
                                       "url": "http://127.0.0.1:1/mcp"}, "DOCKER_START_FAILED")
        with self.assertRaises(AssertionError):
            _assert_collision_refusal({"condition": "DOCKER_START_FAILED", "readiness": False},
                                       "DOCKER_PUBLICATION_FAILED")


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
    failure = None
    retained_failure = None
    try:
        if args.image is not None:
            report["image_id"] = ImageManager(args.source_root, timeout=600).resolve(explicit_id=args.image)
        groups = ("two-repositories", "same-repository") if args.group == "all" else (args.group,)
        for index, group in enumerate(groups):
            entry = {"group": group, "status": "running"}
            report["groups"].append(entry)
            parent = attempt / group
            parent.mkdir()
            deadline = (started if index == 0 else time.monotonic()) + 900
            asyncio.run(_prove_group(parent, group, args.source_root, report.get("image_id"), deadline, entry))
            if report.get("image_id") is None:
                built = entry.get("build_default", {}).get("returned_image_id")
                assert isinstance(built, str), entry
                report["image_id"] = built
        report["status"] = "completed"
    except BaseException as error:
        failure = error
        report.update(status="failed", failure_type=type(error).__name__)
        raise
    finally:
        try:
            retained_after = _snapshot(ROOT, (".caprmedio_install", ".caprmedio_runtime/framework"))
            report["retained_N"] = {"equal": retained == retained_after,
                                    "before": retained, "after": retained_after}
        except BaseException as error:
            report["retained_N"] = {"equal": False, "snapshot_failure": type(error).__name__}
            retained_failure = error
        if not report["retained_N"]["equal"] and failure is None:
            report.update(status="failed", failure_type=(type(retained_failure).__name__
                                                          if retained_failure else "AssertionError"))
        (attempt / "result.json").write_text(json.dumps(report, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        print(json.dumps({"result": str(attempt / "result.json"), "status": report.get("status"),
                          "image_id": report.get("image_id")}, sort_keys=True))
        if failure is None and retained_failure is not None:
            raise retained_failure
        if failure is None and not report["retained_N"]["equal"]:
            raise AssertionError("root N state changed")


if __name__ == "__main__":
    main()
