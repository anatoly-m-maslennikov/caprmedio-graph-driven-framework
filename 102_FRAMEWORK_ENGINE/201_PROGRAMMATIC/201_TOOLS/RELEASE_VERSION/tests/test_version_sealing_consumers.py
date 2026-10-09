"""Downstream consumers retain exact version-sealed package bindings."""

from __future__ import annotations

import hashlib
import shutil
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

import release_delivery  # noqa: E402
import release_image  # noqa: E402
import release_suite  # noqa: E402
from release_handoff import PackageRow  # noqa: E402
from release_packaging import RUNTIME_ROOT, _render_manifest  # noqa: E402


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _row(resource: str, source: str, destination: str, payload: bytes = b"fixture\n") -> PackageRow:
    return PackageRow(resource=resource, source_path=source, destination_path=destination, sha256=_digest(payload), mode=0o644)


class VersionSealingConsumerTests(unittest.TestCase):
    def _versioned_rows(self) -> list[PackageRow]:
        rows = [
            _row("FRAMEWORK_ENGINE", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"),
            _row("FRAMEWORK_ENGINE", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py", "FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py"),
            _row("FRAMEWORK_ENGINE", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py", "FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py"),
            _row("FRAMEWORK_ENGINE", "102_FRAMEWORK_ENGINE/202_AGENTIC/201_PROMPTS/run.md", "FRAMEWORK_ENGINE/202_AGENTIC/201_PROMPTS/run.md"),
            _row("METHODOLOGY", ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/source.md", "METHODOLOGY/sources/source.md", b"# source\n"),
            _row("METHODOLOGY", ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/_release_materialized/N/compiled.md", "METHODOLOGY/compiled/compiled.md", b"# compiled\n"),
            _row("SKILL", "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md", "SKILLS/ca/SKILL.md", b"# skill\n"),
            _row("SKILL", "102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/agents/openai.yaml", "SKILLS/ca/agents/openai.yaml", b"name: ca\n"),
        ]
        version = b'[framework]\nversion = "N"\n'
        rows.append(_row("PACKAGE_CONTROL", "version.toml", "version.toml", version))
        return sorted(rows, key=lambda row: (row.destination_path, row.source_path, row.sha256))

    def _write_versioned_package(self, root: Path, rows: list[PackageRow], *, identity: str = "N") -> tuple[Path, str]:
        package = root / RUNTIME_ROOT / "releases" / identity
        package.mkdir(parents=True)
        for row in rows:
            target = package / row.destination_path
            target.parent.mkdir(parents=True, exist_ok=True)
            payload = b'[framework]\nversion = "N"\n' if row.destination_path == "version.toml" else (
                b"# source\n" if row.destination_path.endswith("source.md") else
                b"# compiled\n" if row.destination_path.endswith("compiled.md") else
                b"# skill\n" if row.destination_path.endswith("SKILL.md") else
                b"name: ca\n" if row.destination_path.endswith("openai.yaml") else b"fixture\n"
            )
            target.write_bytes(payload)
        version_sha = _digest((package / "version.toml").read_bytes())
        (package / "manifest.toml").write_text(
            _render_manifest(identity, rows, framework_version="N", version_toml_sha256=version_sha),
            encoding="utf-8",
        )
        return package, version_sha

    def test_image_context_uses_the_versioned_manifest(self) -> None:
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as temporary:
            root = Path(temporary).resolve()
            package = root / RUNTIME_ROOT / "releases/candidate"
            package.mkdir(parents=True)
            version = b'[framework]\nversion = "N+1"\n'
            row = _row("PACKAGE_CONTROL", "version.toml", "version.toml", version)
            (package / "version.toml").write_bytes(version)
            inputs = []
            for relative, payload in (
                ("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile", b"FROM scratch\n"),
                ("pyproject.toml", b"[project]\nname='fixture'\n"),
                ("uv.lock", b"version = 1\n"),
            ):
                source = root / relative
                source.parent.mkdir(parents=True, exist_ok=True)
                source.write_bytes(payload)
                inputs.append(SimpleNamespace(source_path=relative, source_sha256=_digest(payload), source_mode=0o644, resource="IMAGE_INPUT"))
            candidate = SimpleNamespace(manifest=SimpleNamespace(
                sha256="a" * 64,
                source_inventory_rows=inputs,
                candidate_image=SimpleNamespace(dockerfile_sha256=inputs[0].source_sha256),
            ))
            compilation = SimpleNamespace(framework_version="N+1", version_toml_sha256=_digest(version))
            attempt = root / "attempt"
            attempt.mkdir()
            with (
                patch.object(release_image, "_complete_rows", return_value=("candidate", [row], b"selector")),
                patch.object(release_image, "_verify_release") as verified,
            ):
                _context, _manifest_sha = release_image._context(root, candidate, compilation, attempt)
            self.assertEqual("N+1", verified.call_args.kwargs["framework_version"])
            self.assertEqual(_digest(version), verified.call_args.kwargs["version_toml_sha256"])

    def test_versioned_n_is_accepted_as_the_next_suite_predecessor(self) -> None:
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as temporary:
            root = Path(temporary).resolve()
            rows = self._versioned_rows()
            identity = "a" * 64
            package, version_sha = self._write_versioned_package(root, rows, identity=identity)
            public = root / ".agents/skills/ca"
            public.mkdir(parents=True)
            for relative in ("SKILL.md", "agents/openai.yaml"):
                target = public / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((package / "SKILLS/ca" / relative).read_bytes())
            selector = root / ".caprmedio_runtime/framework/current.toml"
            selector.parent.mkdir(parents=True, exist_ok=True)
            selector.write_text(f'release = "{identity}"\n', encoding="utf-8")
            candidate = SimpleNamespace(authority=SimpleNamespace(executing_release=identity))
            with patch.object(release_suite, "_verify_release") as verified:
                release_suite._active_n_state(root, candidate)
            self.assertEqual("N", verified.call_args.kwargs["framework_version"])
            self.assertEqual(version_sha, verified.call_args.kwargs["version_toml_sha256"])

    def test_versioned_n_is_accepted_as_the_next_delivery_predecessor(self) -> None:
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as temporary:
            root = Path(temporary).resolve()
            rows = self._versioned_rows()
            identity = "b" * 64
            package, version_sha = self._write_versioned_package(root, rows, identity=identity)
            selector = root / ".caprmedio_runtime/framework/current.toml"
            selector.parent.mkdir(parents=True, exist_ok=True)
            selector.write_text(f'release = "{identity}"\n', encoding="utf-8")
            destination = root / "101_LAYER_1_FRAMEWORK_METHODOLOGY/sources"
            destination.parent.mkdir(parents=True)
            shutil.copytree(package / "METHODOLOGY/sources", destination)
            candidate = SimpleNamespace(authority=SimpleNamespace(executing_release=identity))
            with patch.object(release_delivery, "_verify_release") as verified:
                release_delivery._prove_predecessor(root, candidate, destination)
            self.assertEqual("N", verified.call_args.kwargs["framework_version"])
            self.assertEqual(version_sha, verified.call_args.kwargs["version_toml_sha256"])


if __name__ == "__main__":
    unittest.main()
