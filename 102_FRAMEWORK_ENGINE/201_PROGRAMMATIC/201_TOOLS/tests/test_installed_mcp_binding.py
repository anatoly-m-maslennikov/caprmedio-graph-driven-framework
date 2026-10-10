"""Synthetic read-only proofs for installed MCP package admission."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import shutil
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
    _package_ca_skill,
    _compose_contract,
    admit_candidate_mcp_binding,
    admit_installed_mcp_binding,
)
from framework_package import (  # noqa: E402
    VerifiedFrameworkPackage,
    assemble_framework_package,
    provide_installation_package_evidence,
    read_verified_binding_projections,
    verify_framework_package,
)
import framework_package as package_library  # noqa: E402
from installation_context import TargetProjectRequest, bind_target_project_context  # noqa: E402
from installation_transaction import InstallationPublicationLock  # noqa: E402
from source_admission_fixture import write_source_admission_receipt  # noqa: E402
from target_methodology_selection import FRAMEWORK_INSTANCE_SETTINGS_RELATIVE  # noqa: E402


IMAGE = "a" * 64
GATE = "b" * 64
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
        self.control = self.root / ".caprmedio_fixture"
        self.control.mkdir()
        self.package_number = 0
        self.verified = self._package()
        self._write_target_controls()
        self._bind_context(mode="bootstrap")
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
                 omit: str | None = None,
                 extra_payloads: dict[str, bytes] | None = None,
                 binding_count: int = 0) -> VerifiedFrameworkPackage:
        self.package_number += 1
        source = self.root / ".package_sources" / str(self.package_number)
        payloads: dict[str, bytes] = {
            "pyproject.toml": b"[project]\nname = 'fixture'\n",
            "uv.lock": b"version = 1\n",
            "version.toml": VERSION_PAYLOAD,
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py": b"# package core\n",
            "methodology/active/001_CORE_META_MODEL/04_requirement/CA-R-001--fixture.md": b"# active methodology\n",
            "methodology/support/CA-D-001--fixture.md": b"# declared support\n",
            "SKILLS/ca/SKILL.md": b"# ca\n",
            "defaults/framework.toml": b"[defaults]\nname = 'fixture'\n",
        }
        for relative in MCP_FILES:
            payloads[relative] = b"# exact package-owned carrier\n"
        payloads[MCP_FILES[-1]] = _compose() if compose_payload is None else compose_payload
        if extra_payloads is not None:
            payloads.update(extra_payloads)
        if omit is not None:
            payloads.pop(omit)
        for relative, payload in payloads.items():
            target = source / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)
            target.chmod(0o644)
        binding_atoms = self._binding_frontier(source, count=binding_count)
        self._write_catalog(source)
        package = assemble_framework_package(
            source,
            self.root / ".caprmedio_install/releases",
            binding_atoms=binding_atoms,
        )
        return verify_framework_package(package.root)

    def _write_catalog(self, source: Path) -> None:
        records = [
            ("core", "core", "102_FRAMEWORK_ENGINE"),
            ("methodology", "methodology", "methodology/active/001_CORE_META_MODEL"),
            ("support", "support", "methodology/support"),
        ]
        if (source / "methodology" / "bindings").is_dir():
            records.append(("tool-bindings", "binding", "methodology/bindings"))
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
    def _binding_frontier(source: Path, *, count: int) -> tuple[dict[str, object], ...]:
        """Build canonical D561 projection fixtures for schema-2 reopening."""

        if count not in {0, 2}:
            raise AssertionError("fixture supports only empty or two-pin binding frontiers")
        codec = package_library._methodology_export_module()
        rows: list[dict[str, object]] = []
        for suffix in ("901", "902")[:count]:
            atom_id = f"CA-D-{suffix}"
            source_path = (
                ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/fixture/"
                f"07_delivery/{atom_id}--binding.md"
            )
            source_payload = (
                "---\n"
                f"atom_id: {atom_id}\n"
                "content_role: Delivery\n"
                "current_scope_unit: TOOLS\n"
                "status: Active\n"
                "author: fixture\n"
                "version: 1\n"
                "relations:\n"
                "  delivery_for: [CA-R-001]\n"
                "---\n"
                f"# {atom_id}\n\n"
                "```toml\n"
                "[tool_binding]\n"
                f'name = "FIXTURE_{suffix}"\n'
                'entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"\n'
                f'mcp_name = "fixture_{suffix}"\n'
                f'action_ids = ["CA-O-{suffix}"]\n'
                "```\n"
            ).encode("utf-8")
            record = {
                "atom_id": atom_id,
                "version": 1,
                "source_path": source_path,
                "sha256": _digest(source_payload),
            }
            binding = codec.BindingAtom(source_path, atom_id, 1, record["sha256"])
            target = source / "methodology" / "bindings" / source_path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(codec.binding_projection_bytes(source_payload, binding))
            target.chmod(0o644)
            rows.append(record)
        return tuple(rows)

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
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        target.chmod(0o644)
        return digest

    def _write_target_controls(self) -> None:
        (self.control / "caprmedio_project_settings.toml").write_text(
            "[project]\n"
            'name = "fixture-project"\n\n'
            "[paths]\n"
            'control_root = ".caprmedio_fixture"\n',
            encoding="utf-8",
        )
        (self.control / "project_structure.toml").write_text(
            "schema_version = 1\nscope_units = []\n", encoding="utf-8"
        )
        (self.control / "operators_registry.toml").write_text("operators = []\n", encoding="utf-8")
        framework_settings = self.control.joinpath(*FRAMEWORK_INSTANCE_SETTINGS_RELATIVE.parts)
        framework_settings.parent.mkdir(parents=True, exist_ok=True)
        framework_settings.write_text("# canonical fixture Framework Instance Settings\n", encoding="utf-8")

    def _bind_context(self, *, mode: str) -> None:
        evidence = provide_installation_package_evidence(self.verified.root)
        self.context = bind_target_project_context(
            TargetProjectRequest(
                target_root=self.root,
                control_child=self.control.name,
                mode=mode,
                target_project_identity="fixture-project",
                settings_path=self.control / "caprmedio_project_settings.toml",
                project_structure_path=self.control / "project_structure.toml",
                operators_registry_path=self.control / "operators_registry.toml",
                repository_identity=False,
                root_locator="fixture-project",
                package_root=self.verified.root,
                package_evidence=evidence,
            )
        )
        self.context_sha256 = self._write_context()

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
        self.assertEqual(
            (("SKILLS/ca/SKILL.md", _digest(b"# ca\n"), 0o644),),
            tuple((member.path, member.sha256, member.mode) for member in binding.package_ca_skill),
        )
        self.assertEqual("127.0.0.1", binding.loopback_host)
        self.assertEqual("/mcp", binding.loopback_path)
        self.assertTrue(binding.anonymous)
        self.assertTrue(binding.readonly_container)
        self.assertEqual((128, "512m", 1), (binding.pids_limit, binding.memory_limit, binding.cpu_limit))
        self.assertEqual(_digest((self.root / ".caprmedio_install/current.toml").read_bytes()), binding.package_selector_sha256)
        self.assertEqual(_digest((self.root / ".caprmedio_runtime/installation/current.toml").read_bytes()), binding.runtime_selector_sha256)

    def test_admits_schema_two_empty_binding_frontier_without_a_fallback(self) -> None:
        manifest = (self.verified.root / "manifest.toml").read_text(encoding="utf-8")
        self.assertIn("schema_version = 2\n", manifest)
        self.assertIn("binding_atoms = []\n", manifest)
        self.assertEqual((), self.verified.binding_atoms)
        self.assertEqual((), read_verified_binding_projections(self.verified))
        self._admit()

    def test_reopens_schema_two_binding_frontier_for_installed_and_candidate_admission(self) -> None:
        self.verified = self._package(binding_count=2)
        self._bind_context(mode="adopt")
        self._write_selectors()

        self.assertEqual(["CA-D-901", "CA-D-902"], [atom.atom_id for atom in self.verified.binding_atoms])
        self.assertEqual(2, len(read_verified_binding_projections(self.verified)))
        installed = self._admit()
        package_selector = (self.root / ".caprmedio_install/current.toml").read_bytes()
        runtime_selector = (self.root / ".caprmedio_runtime/installation/current.toml").read_bytes()
        candidate = admit_candidate_mcp_binding(
            self.root,
            self.verified,
            target_context_sha256=self.context_sha256,
            prospective_package_selector=package_selector,
            prospective_runtime_selector=runtime_selector,
        )
        self.assertEqual(self.verified.manifest_digest, installed.package_manifest_sha256)
        self.assertEqual(self.verified.manifest_digest, candidate.package_manifest_sha256)

    def test_reopens_historical_schema_one_without_binding_projection_or_conversion(self) -> None:
        current = (self.verified.root / "manifest.toml").read_bytes()
        historical = current.replace(b"schema_version = 2\n", b"schema_version = 1\n", 1).replace(
            b"binding_atoms = []\n\n", b"", 1,
        )
        historical_root = self.verified.root.parent / _digest(historical)
        shutil.copytree(self.verified.root, historical_root)
        (historical_root / "manifest.toml").write_bytes(historical)
        self.verified = verify_framework_package(historical_root)
        self._bind_context(mode="adopt")
        self._write_selectors()

        self.assertEqual((), self.verified.binding_atoms)
        self.assertEqual((), read_verified_binding_projections(self.verified))
        self._admit()

    def test_refuses_missing_extra_or_unknown_package_manifest_schemas(self) -> None:
        manifest = self.verified.root / "manifest.toml"
        original = manifest.read_bytes()
        malformed = (
            original.replace(b"binding_atoms = []\n\n", b"", 1),
            original.replace(
                b"binding_atoms = []\n",
                b"binding_atoms = []\nmanifest_binding_atoms = []\n",
                1,
            ),
            original.replace(b"schema_version = 2\n", b"schema_version = 99\n", 1),
        )
        for payload in malformed:
            with self.subTest(payload=payload[:80]):
                manifest.write_bytes(payload)
                with self.assertRaises(InstalledMcpBindingError) as raised:
                    self._admit()
                self.assertEqual("installed-package-tampered", raised.exception.code)
                manifest.write_bytes(original)

    def test_refuses_missing_canonical_ca_skill_even_when_another_skill_member_exists(self) -> None:
        self.verified = self._package(
            omit="SKILLS/ca/SKILL.md",
            extra_payloads={"SKILLS/ca/other.md": b"# not the canonical entrypoint\n"},
        )
        self._write_selectors()

        with self.assertRaises(InstalledMcpBindingError) as raised:
            self._admit()
        self.assertEqual("package-ca-skill-missing", raised.exception.code)

    def test_refuses_non_skill_row_and_keeps_only_ca_subtree(self) -> None:
        with self.assertRaises(InstalledMcpBindingError) as raised:
            _package_ca_skill({
                "SKILLS/ca/SKILL.md": {"role": "engine", "sha256": "a" * 64, "mode": 0o644},
            })
        self.assertEqual("package-ca-skill-invalid", raised.exception.code)

    def test_admits_exact_prospective_selectors_without_live_selector_publication(self) -> None:
        package_selector = (self.root / ".caprmedio_install/current.toml").read_bytes()
        runtime_selector = (self.root / ".caprmedio_runtime/installation/current.toml").read_bytes()
        (self.root / ".caprmedio_install/current.toml").unlink()
        (self.root / ".caprmedio_runtime/installation/current.toml").unlink()

        binding = admit_candidate_mcp_binding(
            self.root, self.verified, target_context_sha256=self.context_sha256,
            prospective_package_selector=package_selector,
            prospective_runtime_selector=runtime_selector,
        )

        self.assertEqual(_digest(package_selector), binding.package_selector_sha256)
        self.assertEqual(_digest(runtime_selector), binding.runtime_selector_sha256)
        self.assertEqual(self.verified.manifest_digest, binding.package_manifest_sha256)
        self.assertFalse((self.root / ".caprmedio_install/current.toml").exists())

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
        self._bind_context(mode="adopt")
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
