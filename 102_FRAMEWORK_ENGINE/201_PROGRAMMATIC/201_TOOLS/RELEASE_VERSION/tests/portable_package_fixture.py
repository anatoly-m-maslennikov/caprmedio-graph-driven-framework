"""Physical D596/D602 fixture inputs for private portable-package tests."""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = RELEASE_ROOT.parents[1]
EXPORT_ROOT = RELEASE_ROOT.parent / "COMPILE_APPLICABLE_METHODOLOGY"
for _path in (TOOLS_ROOT, RELEASE_ROOT, EXPORT_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

import methodology_export as exporter  # noqa: E402
from release_compilation import build_preflight_validated_candidate, compile_sealed_methodology_export  # noqa: E402
from release_handoff import CANONICAL_SOURCE_RELATIVE, bind_sealed_methodology_export  # noqa: E402
from release_portable_contract import (  # noqa: E402
    build_sealed_portable_compilation,
    collect_portable_source_snapshot,
)
from source_catalog_admission import (  # noqa: E402
    TrustedSourceAdmissionInvocation,
    admit_package_sources,
)


def digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def atom(atom_id: str, *, version: int) -> bytes:
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "status: Active\n"
        f"version: {version}\n"
        "updated_at: 2026-10-09 00:00:00 +0000\n"
        "relations: {}\n"
        "---\n"
        f"# {atom_id}\n\nfixture claim\n"
    ).encode()


def logical_tree_digest(root: Path) -> str:
    records = [
        {
            "path": path.relative_to(root).as_posix(),
            "sha256": digest(path.read_bytes()),
            "mode": path.stat().st_mode & 0o777,
        }
        for path in sorted(root.rglob("*"))
        if path.is_file()
    ]
    return digest(json.dumps(records, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode())


class PortablePackageFixture:
    """A retained real candidate/export/private-compilation input chain."""

    def __init__(self, *, extra_engine_members: dict[str, bytes] | None = None, admit: bool = True) -> None:
        # Keep this physical proof tree.  Managed macOS hosts can reject
        # recursive cleanup after compiler reads, and TemporaryDirectory's
        # finalizer can then stall process shutdown.
        self.root = Path(tempfile.mkdtemp(prefix="caprmedio-portable-package-")).resolve(strict=True)
        self.source = self.root / CANONICAL_SOURCE_RELATIVE
        for layer in ("001_CORE_META_MODEL", "003_PROJECT_CONFIGURATION"):
            for role in ("04_requirement", "05_method", "06_evaluation", "07_delivery", "09_operations"):
                (self.source / layer / role).mkdir(parents=True, exist_ok=True)
        (self.source / "002_INSTALLED_EXTENSIONS").mkdir()
        self._seed_project(extra_engine_members or {})
        self.run_id = "portable-fixture-run"
        self.candidate_root = self.root / ".caprmedio_tmp/release_candidates" / self.run_id
        self.candidate = self._candidate()
        self._export()
        self.export = bind_sealed_methodology_export(self.candidate, self.candidate_root)
        self.private_compilation = compile_sealed_methodology_export(self.export)
        self.source_snapshot = collect_portable_source_snapshot(
            self.candidate, self.private_compilation, candidate_run_id=self.run_id,
        )
        self.admission = self.admit_sources() if admit else None
        self.sealed = (
            build_sealed_portable_compilation(
                self.candidate, self.private_compilation, candidate_run_id=self.run_id,
            )
            if admit else None
        )

    def cleanup(self) -> None:
        """Retain managed-host fixture evidence; never mask test results."""

    def write(self, relative: str, payload: bytes, mode: int = 0o644) -> Path:
        target = self.root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        target.chmod(mode)
        return target

    def _seed_project(self, extra_engine_members: dict[str, bytes]) -> None:
        self.write(".caprmedio_caprmedio/project_structure.toml", (
            "[[scope_units]]\n"
            'scope_unit_name = "METHODOLOGY_SOURCES"\n'
            f'authority_path = "{CANONICAL_SOURCE_RELATIVE}"\n'
        ).encode())
        self.write(".caprmedio_caprmedio/caprmedio_project_settings.toml", b'[paths]\ncontrol_root = ".caprmedio_caprmedio"\n')
        self.write(f"{CANONICAL_SOURCE_RELATIVE}/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml", b"")
        self.write(f"{CANONICAL_SOURCE_RELATIVE}/003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml", b"")
        self.atom_one = self.write(f"{CANONICAL_SOURCE_RELATIVE}/001_CORE_META_MODEL/04_requirement/CA-R-001--one.md", atom("CA-R-001", version=1))
        self.atom_two = self.write(f"{CANONICAL_SOURCE_RELATIVE}/003_PROJECT_CONFIGURATION/05_method/CA-M-002--two.md", atom("CA-M-002", version=1))
        self.support = self.write(f"{CANONICAL_SOURCE_RELATIVE}/002_INSTALLED_EXTENSIONS/support.txt", b"declared support\n")
        self.write(".caprmedio_runtime/framework/current.toml", b'release = "N"\n')
        self.write("version.toml", b'[framework]\nversion = "N+1"\n')
        self.write("pyproject.toml", b"[project]\nname = 'portable-fixture'\nversion = '0.0.0'\n")
        self.write("uv.lock", b"version = 1\n")
        self.write("defaults/runtime.toml", b"[runtime]\nprofile = 'fixture'\n")
        self.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", b"tool = 'fixture'\n", 0o755)
        self.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py", b"app = 'fixture'\n")
        self.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py", b"server = 'fixture'\n")
        self.write("102_FRAMEWORK_ENGINE/202_AGENTIC/201_PROMPTS/prompt.md", b"# prompt\n")
        self.write("102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md", b"# ca\n")
        self.write("102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/agents/openai.yaml", b"name: ca\n")
        self.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile", b"FROM scratch\nCOPY pyproject.toml uv.lock ./\n")
        self.write(
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py",
            (EXPORT_ROOT / "compile_applicable_methodology.py").read_bytes(), 0o755,
        )
        for relative, payload in extra_engine_members.items():
            if not relative.startswith("102_FRAMEWORK_ENGINE/") or not isinstance(payload, bytes):
                raise ValueError("extra_engine_members must map Framework Engine paths to bytes")
            self.write(relative, payload)

    def _candidate(self):
        return build_preflight_validated_candidate(
            self.root, candidate_release="N+1",
            full_suite_environment={"runner": "fixture", "command": ["python", "-m", "unittest"], "working_directory": "."},
            candidate_image_reference="fixture:N+1",
        )[1]

    def _export(self) -> None:
        manifest = exporter.freeze_methodology_manifest(
            source_root=self.source,
            selected_atoms=[{"atom_id": "CA-R-001", "version": 1}, {"atom_id": "CA-M-002", "version": 1}],
            support_inventory=[{"path": self.support.relative_to(self.source).as_posix(), "sha256": digest(self.support.read_bytes())}],
            catalog_pins=[],
        )
        frozen = self.write("freeze/manifest.json", exporter.frozen_manifest_bytes(manifest))
        exporter.export_selected_methodology(
            source_root=self.source, frozen_manifest_path=frozen, release_candidate_root=self.candidate_root,
        )

    def admit_sources(self, *, admitter=None):
        def fixture_admitter(request):
            return TrustedSourceAdmissionInvocation(
                request.snapshot_sha256,
                "fixture-operator",
                "fixture-command:admit-package-sources",
                "fixture-action-run-001",
            )

        return admit_package_sources(
            self.root, self.source_snapshot,
            invocation_admitter=fixture_admitter if admitter is None else admitter,
        )

    def _catalog_row(self, identity: str, kind: str, value: str, path: str) -> list[str]:
        return [
            f"[source.{identity}]", f'kind = "{kind}"', f'revision = "{"a" * 40}"',
            f'sha256 = "{value}"', f'admission_receipt_sha256 = "{"b" * 64}"',
            'visibility = "public"', "selection_default = false", f'path = "{path}"', "",
        ]

    def _write_catalog(self) -> None:
        support_source = self.support
        atoms = [self.atom_one, self.atom_two]
        active_root = self.root / ".catalog-active"
        support_root = self.root / ".catalog-support"
        for root, paths in ((active_root, atoms), (support_root, [support_source])):
            for source in paths:
                target = root / source.relative_to(self.source)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(source.read_bytes())
                target.chmod(source.stat().st_mode & 0o777)
        lines = ["schema_version = 1", ""]
        lines.extend(self._catalog_row("core", "core", logical_tree_digest(self.root / "102_FRAMEWORK_ENGINE"), "102_FRAMEWORK_ENGINE"))
        lines.extend(self._catalog_row("active", "methodology", logical_tree_digest(active_root), "methodology/active"))
        lines.extend(self._catalog_row("support", "support", logical_tree_digest(support_root), "methodology/support"))
        self.write("catalog.toml", ("\n".join(lines) + "\n").encode())
