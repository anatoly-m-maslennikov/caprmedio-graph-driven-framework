"""Synthetic read-only proofs for installed MCP package admission."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
TESTS = Path(__file__).resolve().parent
if str(TESTS) not in sys.path:
    sys.path.insert(0, str(TESTS))

from installed_mcp_binding import (  # noqa: E402
    MCP_FILES,
    InstalledMcpBindingError,
    _compose_contract,
    admit_installed_mcp_binding,
)
from framework_package import (  # noqa: E402
    VerifiedFrameworkPackage,
    assemble_framework_package,
    provide_installation_package_evidence,
    verify_framework_package,
)
from installation_context import TargetProjectContext as InstallationTargetProjectContext  # noqa: E402
from installation_transaction import InstallationPublicationLock  # noqa: E402
from source_admission_fixture import write_source_admission_receipt  # noqa: E402


IMAGE = "a" * 64
GATE = "b" * 64
SETTINGS = "c" * 64
STRUCTURE = "d" * 64
REGISTRY = "e" * 64
VERSION_PAYLOAD = b'[framework]\nversion = "1.2.3"\n'


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _compose() -> bytes:
    return b'''services:
  mcp-http:
    image: ${CAPRMEDIO_IMAGE:?An admitted immutable image is required}
    init: true
    read_only: true
    cap_drop: [ALL]
    security_opt: [no-new-privileges:true]
    restart: "no"
    stop_grace_period: 10s
    tmpfs: ["/tmp:size=128m,mode=1777"]
    pids_limit: 128
    mem_limit: 512m
    cpus: 1
    command: [mcp-http]
    environment:
      CAPRMEDIO_RUNTIME_NAMESPACE: docker
      CAPRMEDIO_CONTROL_ROOT: ${CAPRMEDIO_CONTROL_ROOT:?Selected control root is required}
      CAPRMEDIO_PROJECT_INSTANCE_ID: ${CAPRMEDIO_PROJECT_INSTANCE_ID:?Selected identity is required}
      CAPRMEDIO_HOST_PROJECT_ROOT: ${CAPRMEDIO_PROJECT_ROOT:?Selected Project root is required}
    labels:
      org.caprmedio.project: ${CAPRMEDIO_PROJECT_INSTANCE_ID}
      org.caprmedio.runtime.fingerprint: ${CAPRMEDIO_RUNTIME_FINGERPRINT:?Image fingerprint is required}
      org.caprmedio.service: mcp-http
      org.caprmedio.control_root: ${CAPRMEDIO_CONTROL_ROOT}
      org.caprmedio.host_project_root: ${CAPRMEDIO_PROJECT_ROOT}
    volumes:
      - type: bind
        source: ${CAPRMEDIO_PROJECT_ROOT}
        target: /project
    ports: ["127.0.0.1:${CAPRMEDIO_MCP_HTTP_PORT:-}:8092"]
    healthcheck:
      test: [CMD, python, -c, "import json,urllib.request; assert json.load(urllib.request.urlopen('http://127.0.0.1:8092/health',timeout=3))['ready'] is True"]
      interval: 2s
      timeout: 5s
      retries: 25
      start_period: 3s
'''


class InstalledMcpBindingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        (self.root / ".caprmedio_fixture").mkdir()
        self.package_number = 0
        self.verified = self._package()
        self.context = InstallationTargetProjectContext(
            mode="bootstrap",
            target_project_identity="fixture-project",
            control_child_relpath=".caprmedio_fixture",
            settings_sha256=SETTINGS,
            project_structure_sha256=STRUCTURE,
            registry_sha256=REGISTRY,
            repository_identity=False,
            root_locator="fixture-project",
            package_evidence=provide_installation_package_evidence(self.verified.root),
        )
        self.context_sha256 = self._write_context()
        self.lock = InstallationPublicationLock(
            self.root,
            target_context_sha256=self.context_sha256,
            owner_run_id="installed-mcp-binding-fixture",
            operation="binding-fixture",
            command_sha256="f" * 64,
        ).acquire()
        self.addCleanup(self._release_lock)
        self._write_selectors()

    def _release_lock(self) -> None:
        if self.lock.active:
            self.lock.release("blocked")

    def _package(self, *, compose_payload: bytes | None = None,
                 omit: str | None = None) -> VerifiedFrameworkPackage:
        self.package_number += 1
        source = self.root / ".package_sources" / str(self.package_number)
        payloads: dict[str, bytes] = {
            "pyproject.toml": b"[project]\nname = 'fixture'\n",
            "uv.lock": b"version = 1\n",
            "version.toml": VERSION_PAYLOAD,
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py": b"# package core\n",
            "methodology/active/CA-R-001--fixture.md": b"# active methodology\n",
            "methodology/support/CA-D-001--fixture.md": b"# declared support\n",
            "SKILLS/ca/SKILL.md": b"# ca\n",
            "defaults/framework.toml": b"[defaults]\nname = 'fixture'\n",
        }
        for relative in MCP_FILES:
            payloads[relative] = b"# exact package-owned carrier\n"
        payloads[MCP_FILES[-1]] = _compose() if compose_payload is None else compose_payload
        if omit is not None:
            payloads.pop(omit)
        for relative, payload in payloads.items():
            target = source / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)
            target.chmod(0o644)
        self._write_catalog(source)
        package = assemble_framework_package(source, self.root / ".caprmedio_install/releases")
        return verify_framework_package(package.root)

    def _write_catalog(self, source: Path) -> None:
        records = (
            ("core", "core", "102_FRAMEWORK_ENGINE"),
            ("methodology", "methodology", "methodology/active"),
            ("support", "support", "methodology/support"),
        )
        descriptors = tuple(
            {
                "identity": identity,
                "kind": kind,
                "revision": self._tree_digest(source / relative),
                "sha256": self._tree_digest(source / relative),
                "visibility": "public",
                "selection_default": False,
                "path": relative,
            }
            for identity, kind, relative in records
        )
        receipt = write_source_admission_receipt(source, descriptors)
        lines = ["schema_version = 1", ""]
        for descriptor in descriptors:
            lines.extend(
                [
                    f"[source.{descriptor['identity']}]",
                    f'kind = "{descriptor["kind"]}"',
                    f'revision = "{descriptor["revision"]}"',
                    f'sha256 = "{descriptor["sha256"]}"',
                    f'admission_receipt_sha256 = "{receipt.sha256}"',
                    f'visibility = "{descriptor["visibility"]}"',
                    "selection_default = false",
                    f'path = "{descriptor["path"]}"',
                    "",
                ]
            )
        catalog = source / "catalog.toml"
        catalog.write_text("\n".join(lines), encoding="utf-8")
        catalog.chmod(0o644)

    @staticmethod
    def _tree_digest(root: Path) -> str:
        rows = [
            {"path": path.relative_to(root).as_posix(), "sha256": _digest(path.read_bytes()),
             "mode": path.stat().st_mode & 0o777}
            for path in sorted(root.rglob("*"), key=lambda candidate: candidate.as_posix())
            if path.is_file()
        ]
        return _digest(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode("utf-8"))

    def _write_context(self) -> str:
        payload = self.context.with_digest_toml()
        digest = self.context.sha256
        target = self.root / ".caprmedio_runtime/installation/contexts" / f"{digest}.toml"
        target.parent.mkdir(parents=True)
        target.write_bytes(payload)
        target.chmod(0o644)
        return digest

    def _write_selectors(self, *, catalog_sha256: str | None = None,
                         context_sha256: str | None = None,
                         release_relpath: str | None = None,
                         lock_generation: str | int | None = None) -> None:
        selector = self.root / ".caprmedio_install/current.toml"
        selector.parent.mkdir(parents=True, exist_ok=True)
        selector.write_text(
            "schema_version = 1\n"
            f'package_manifest_sha256 = "{self.verified.manifest_digest}"\n'
            f'release_relpath = "{release_relpath or "releases/" + self.verified.manifest_digest}"\n'
            'framework_version = "1.2.3"\n'
            f'version_toml_sha256 = "{_digest(VERSION_PAYLOAD)}"\n'
            f'source_catalog_sha256 = "{catalog_sha256 or self.verified.source_catalog_sha256}"\n'
            f'full_gate_receipt_sha256 = "{GATE}"\n'
            f'image_digest = "{IMAGE}"\n',
            encoding="utf-8",
        )
        runtime = self.root / ".caprmedio_runtime/installation/current.toml"
        runtime.parent.mkdir(parents=True, exist_ok=True)
        runtime.write_text(
            "schema_version = 1\n"
            f'package_manifest_sha256 = "{self.verified.manifest_digest}"\n'
            f'target_project_context_sha256 = "{context_sha256 or self.context_sha256}"\n'
            "state_generation = 1\n"
            f"installation_lock_generation = {json.dumps(self.lock.lock_generation if lock_generation is None else lock_generation)}\n"
            f'image_digest = "{IMAGE}"\n',
            encoding="utf-8",
        )

    def _admit(self):
        return admit_installed_mcp_binding(
            self.root, self.verified, target_context_sha256=self.context_sha256,
        )

    def test_admits_only_exact_installed_bundle_context_and_loopback_profile(self) -> None:
        binding = self._admit()
        self.assertEqual(self.verified.manifest_digest, binding.package_manifest_sha256)
        self.assertEqual(self.verified.source_catalog_sha256, binding.source_catalog_sha256)
        self.assertEqual(self.context_sha256, binding.target_context.sha256)
        self.assertEqual(".caprmedio_fixture", binding.target_context.control_child_relpath)
        self.assertEqual(self.verified.root / MCP_FILES[0], binding.mcp_http_server)
        self.assertEqual(self.verified.root / MCP_FILES[-1], binding.compose_file)
        self.assertEqual("127.0.0.1", binding.loopback_host)
        self.assertEqual("/mcp", binding.loopback_path)
        self.assertTrue(binding.anonymous)
        self.assertTrue(binding.readonly_container)
        self.assertEqual((128, "512m", 1), (binding.pids_limit, binding.memory_limit, binding.cpu_limit))
        self.assertEqual(_digest((self.root / ".caprmedio_install/current.toml").read_bytes()), binding.package_selector_sha256)
        self.assertEqual(_digest((self.root / ".caprmedio_runtime/installation/current.toml").read_bytes()), binding.runtime_selector_sha256)

    def test_admits_context_self_digest_and_actual_installation_lock_generation(self) -> None:
        context_path = self.root / ".caprmedio_runtime/installation/contexts" / f"{self.context_sha256}.toml"
        runtime_selector = self.root / ".caprmedio_runtime/installation/current.toml"

        self.assertEqual(self.context.with_digest_toml(), context_path.read_bytes())
        self.assertIn(
            f'installation_lock_generation = "{self.lock.lock_generation}"',
            runtime_selector.read_text(encoding="utf-8"),
        )
        self.assertTrue(self.lock.active)
        self._admit()

    def test_refuses_tampered_or_unknown_context_fields_and_non_lock_generation(self) -> None:
        context_path = self.root / ".caprmedio_runtime/installation/contexts" / f"{self.context_sha256}.toml"
        original = context_path.read_bytes()
        context_path.write_bytes(original.replace(
            f'target_project_context_sha256 = "{self.context_sha256}"'.encode("utf-8"),
            b'target_project_context_sha256 = "f"',
        ))
        with self.assertRaisesRegex(InstalledMcpBindingError, "context") as raised:
            self._admit()
        self.assertEqual("target-context-mismatch", raised.exception.code)

        context_path.write_bytes(original + b'unknown = "forged"\n')
        with self.assertRaisesRegex(InstalledMcpBindingError, "schema is not closed") as raised:
            self._admit()
        self.assertEqual("target-context-invalid", raised.exception.code)

        context_path.write_bytes(original)
        self._write_selectors(lock_generation=1)
        with self.assertRaisesRegex(InstalledMcpBindingError, "installation_lock_generation") as raised:
            self._admit()
        self.assertEqual("runtime-selector-invalid", raised.exception.code)

    def test_refuses_checkout_or_other_foreign_package_even_when_its_inventory_is_typed(self) -> None:
        checkout = self.root / "checkout"
        checkout.mkdir()
        foreign = VerifiedFrameworkPackage(
            self.verified.manifest_digest, checkout, self.verified.inventory, self.verified.framework_version,
            self.verified.version_toml_sha256, self.verified.source_catalog_sha256,
        )
        with self.assertRaisesRegex(InstalledMcpBindingError, "selected installed release") as raised:
            admit_installed_mcp_binding(self.root, foreign, target_context_sha256=self.context_sha256)
        self.assertEqual("installed-package-foreign", raised.exception.code)

    def test_refuses_tampered_or_symlinked_package_carriers(self) -> None:
        carrier = self.verified.root / MCP_FILES[0]
        carrier.write_bytes(b"tampered\n")
        with self.assertRaisesRegex(InstalledMcpBindingError, "package carrier differs") as raised:
            self._admit()
        self.assertEqual("installed-package-tampered", raised.exception.code)

        carrier.write_bytes(b"# exact package-owned carrier\n")
        target = self.verified.root / "retained-target"
        target.write_bytes(b"not a package route\n")
        carrier.unlink()
        carrier.symlink_to(target)
        with self.assertRaisesRegex(InstalledMcpBindingError, "symlink") as raised:
            self._admit()
        self.assertEqual("installed-package-tampered", raised.exception.code)

    def test_refuses_a_manifest_consistent_package_missing_a_required_mcp_carrier(self) -> None:
        self.verified = self._package(omit=MCP_FILES[0])
        self._write_selectors()
        with self.assertRaisesRegex(InstalledMcpBindingError, "omits required MCP carrier") as raised:
            self._admit()
        self.assertEqual("installed-package-missing", raised.exception.code)

    def test_refuses_stale_catalog_and_context_selector_mismatch(self) -> None:
        self._write_selectors(catalog_sha256="f" * 64)
        with self.assertRaisesRegex(InstalledMcpBindingError, "catalog digest is stale") as raised:
            self._admit()
        self.assertEqual("catalog-digest-stale", raised.exception.code)

        self._write_selectors(context_sha256="f" * 64)
        with self.assertRaisesRegex(InstalledMcpBindingError, "another target context") as raised:
            self._admit()
        self.assertEqual("target-context-mismatch", raised.exception.code)

    def test_refuses_selector_traversal_undesignated_route_and_unbounded_transport(self) -> None:
        self._write_selectors(release_relpath="releases/../checkout")
        with self.assertRaisesRegex(InstalledMcpBindingError, "release path is not canonical") as raised:
            self._admit()
        self.assertEqual("installed-selector-mismatch", raised.exception.code)

        self._write_selectors()
        with self.assertRaisesRegex(InstalledMcpBindingError, "not designated") as raised:
            admit_installed_mcp_binding(
                self.root, self.verified, target_context_sha256=self.context_sha256, route="development-checkout",
            )
        self.assertEqual("mcp-route-undesignated", raised.exception.code)

        payload = _compose().replace(
            b'"127.0.0.1:${CAPRMEDIO_MCP_HTTP_PORT:-}:8092"', b'"0.0.0.0:8092:8092"'
        )
        self.verified = self._package(compose_payload=payload)
        self._write_selectors()
        with self.assertRaisesRegex(InstalledMcpBindingError, "transport is not the anonymous loopback route") as raised:
            self._admit()
        self.assertEqual("mcp-compose-invalid", raised.exception.code)

    def test_refuses_extra_or_relaxed_compose_metadata_without_loading_an_env_file(self) -> None:
        def validate(payload: bytes) -> InstalledMcpBindingError:
            folder = self.root / ".compose_metadata" / _digest(payload)
            compose = folder / MCP_FILES[-1]
            compose.parent.mkdir(parents=True, exist_ok=True)
            compose.write_bytes(payload)
            with self.assertRaises(InstalledMcpBindingError) as raised:
                _compose_contract(folder)
            return raised.exception

        inserted = (
            b"privileged: true",
            b"network_mode: host",
            b"pid: host",
            b"devices: [/dev/null]",
            b"cap_add: [SYS_ADMIN]",
            b"env_file: [fixture.env]",
            b"secrets: [fixture]",
            b"configs: [fixture]",
            b"networks: [fixture]",
        )
        for addition in inserted:
            with self.subTest(addition=addition):
                payload = _compose().replace(b"    init: true\n", b"    init: true\n    " + addition + b"\n")
                error = validate(payload)
                self.assertEqual("mcp-compose-invalid", error.code)
                self.assertIn("service schema is not closed", str(error))

        for before, after in (
            (b"    init: true", b"    init: false"),
            (b'    restart: "no"', b'    restart: "always"'),
            (b"    stop_grace_period: 10s", b"    stop_grace_period: 1s"),
            (b"        target: /project", b"        target: /other"),
        ):
            with self.subTest(before=before):
                self.assertEqual("mcp-compose-invalid", validate(_compose().replace(before, after)).code)


if __name__ == "__main__":
    unittest.main()
