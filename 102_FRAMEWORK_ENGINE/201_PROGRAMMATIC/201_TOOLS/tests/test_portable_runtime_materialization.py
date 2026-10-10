"""Synthetic coverage for the inert portable runtime command-stage fragment."""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
for candidate in (TOOLS, Path(__file__).resolve().parent):
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

from framework_package import (  # noqa: E402
    assemble_framework_package,
    provide_installation_package_evidence,
)
from installation_context import TargetProjectRequest, bind_target_project_context  # noqa: E402
from installation_transaction import InstallationPublicationLock  # noqa: E402
import portable_runtime_materialization as materialization  # noqa: E402
from portable_runtime_materialization import (  # noqa: E402
    PortableRuntimeMaterializationError,
    RuntimeCommandStageRequest,
    stage_runtime_command,
)
from source_admission_fixture import write_source_admission_receipt  # noqa: E402


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _tree_sha(path: Path) -> str:
    rows = [
        {
            "path": member.relative_to(path).as_posix(),
            "sha256": _sha256(member.read_bytes()),
            "mode": member.stat().st_mode & 0o777,
        }
        for member in sorted(path.rglob("*"))
        if member.is_file() and not member.is_symlink()
    ]
    return _sha256(json.dumps(rows, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8"))


def _canonical_digest(value: object) -> str:
    return _sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")
    )


class PortableRuntimeMaterializationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.base = Path(tempfile.mkdtemp(dir=TEST_TEMP_ROOT)).resolve()
        self.target = self.base / "target"
        self.target.mkdir()
        self.package = self._package()
        self.package_evidence = provide_installation_package_evidence(self.package.root)
        self.target, self.control = self._target()
        self.context = self._context()
        self._write_context()
        self._write_package_selector()
        self.path_one = self.base / "path-one"
        self.path_two = self.base / "path-two"
        self.home = self.base / "home"
        for directory in (self.path_one, self.path_two, self.home):
            directory.mkdir()

    def _write(self, root: Path, relative: str, payload: bytes, *, mode: int = 0o644) -> None:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
        path.chmod(mode)

    def _seed_package_compiler_closure(self, source: Path) -> None:
        """Seal the actual compiler and every locally imported dependency."""

        for relative in (
            "COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py",
            "project_runtime.py",
            "project_selection.py",
            "artifact_metadata.py",
            "VALIDATE_ATOMS/validate_atoms_workers/__init__.py",
            "VALIDATE_ATOMS/validate_atoms_workers/read_io.py",
            "VALIDATE_ATOMS/validate_atoms_workers/settings.py",
        ):
            canonical = TOOLS / relative
            self._write(
                source,
                f"102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/{relative}",
                canonical.read_bytes(),
                mode=canonical.stat().st_mode & 0o777,
            )

    def _target(self) -> tuple[Path, Path]:
        target = self.base / "target"
        control = target / ".caprmedio_target"
        control.mkdir(parents=True)
        self._write(
            control,
            "caprmedio_project_settings.toml",
            b'[project]\nname = "target"\n\n[paths]\ncontrol_root = ".caprmedio_target"\n',
        )
        self._write(control, "project_structure.toml", b"schema_version = 1\nscope_units = []\n")
        self._write(control, "operators_registry.toml", b"operators = []\n")
        configuration = next(pin for pin in self.package_evidence.source_pins if pin.identity == "project-configuration")
        self._write(
            control,
            "000_CAPRMEDIO_framework/caprmedio_framework_settings.toml",
            (
                "[methodology.configuration]\n"
                "identity = \"project-configuration\"\n"
                f"revision = \"{configuration.revision}\"\n"
            ).encode("utf-8"),
        )
        return target, control

    def _package(self):
        source = self.base / "source"
        releases = self.target / ".caprmedio_install" / "releases"
        self._seed_package_compiler_closure(source)
        self._write(
            source,
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/runtime_entry.py",
            b"print('fixture runtime')\n",
            mode=0o755,
        )
        self._write(source, "methodology/active/001_CORE_META_MODEL/04_requirement/CA-R-001--fixture.md", b"# active\n")
        self._write(
            source,
            "methodology/active/003_PROJECT_CONFIGURATION/05_method/CA-M-001--fixture.md",
            b"# configuration\n",
        )
        self._write(source, "methodology/support/CA-D-001--fixture.md", b"# support\n")
        self._write(source, "SKILLS/ca/SKILL.md", b"# ca\n")
        self._write(source, "SKILLS/ca/helper.py", b"print('not an engine entrypoint')\n")
        self._write(source, "defaults/runtime-config.toml", b"schema_version = 1\n")
        self._write(source, "pyproject.toml", b"[project]\nname = 'fixture'\nversion = '0.1.0'\n")
        self._write(source, "uv.lock", b"version = 1\n")
        self._write(source, "version.toml", b"[framework]\nversion = '0.1.0'\n")
        descriptors = tuple(
            sorted(
                (
                    {
                        "identity": identity,
                        "kind": kind,
                        "revision": _tree_sha(source / relative),
                        "sha256": _tree_sha(source / relative),
                        "visibility": "public",
                        "selection_default": False,
                        "path": relative,
                    }
                    for identity, kind, relative in (
                        ("core-engine", "core", "102_FRAMEWORK_ENGINE"),
                        ("core-methodology", "methodology", "methodology/active/001_CORE_META_MODEL"),
                        ("project-configuration", "configuration", "methodology/active/003_PROJECT_CONFIGURATION"),
                        ("declared-support", "support", "methodology/support"),
                    )
                ),
                key=lambda descriptor: descriptor["identity"],
            )
        )
        receipt = write_source_admission_receipt(source, descriptors)
        catalog = ["schema_version = 1", ""]
        for descriptor in descriptors:
            catalog.extend(
                (
                    f"[source.{descriptor['identity']}]",
                    f'kind = "{descriptor["kind"]}"',
                    f'revision = "{descriptor["revision"]}"',
                    f'sha256 = "{descriptor["sha256"]}"',
                    f'admission_receipt_sha256 = "{receipt.sha256}"',
                    'visibility = "public"',
                    "selection_default = false",
                    f'path = "{descriptor["path"]}"',
                    "",
                )
            )
        self._write(source, "catalog.toml", ("\n".join(catalog) + "\n").encode("utf-8"))
        return assemble_framework_package(source, releases)

    def _context(self):
        return bind_target_project_context(
            TargetProjectRequest(
                target_root=self.target,
                control_child=self.control.name,
                mode="bootstrap",
                target_project_identity="target",
                settings_path=self.control / "caprmedio_project_settings.toml",
                project_structure_path=self.control / "project_structure.toml",
                operators_registry_path=self.control / "operators_registry.toml",
                repository_identity=False,
                root_locator="fixtures/target",
                package_root=self.package.root,
                package_evidence=self.package_evidence,
            )
        )

    def _write_context(self) -> None:
        path = self.target / ".caprmedio_runtime" / "installation" / "contexts" / f"{self.context.sha256}.toml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(self.context.with_digest_toml())

    def _write_package_selector(self) -> None:
        path = self.target / ".caprmedio_install" / "current.toml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "\n".join(
                (
                    "schema_version = 1",
                    f'package_manifest_sha256 = "{self.package.manifest_digest}"',
                    f'release_relpath = "releases/{self.package.manifest_digest}"',
                    f'framework_version = "{self.package.framework_version}"',
                    f'version_toml_sha256 = "{self.package.version_toml_sha256}"',
                    f'source_catalog_sha256 = "{self.package.source_catalog_sha256}"',
                    f'full_gate_receipt_sha256 = "{"a" * 64}"',
                    f'image_digest = "{"b" * 64}"',
                    "",
                )
            ),
            encoding="utf-8",
        )

    def _request(self, **changes: object) -> RuntimeCommandStageRequest:
        values: dict[str, object] = {
            "package": self.package,
            "target_context": self.context,
            "state_generation": 1,
            "entrypoint": "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/runtime_entry.py",
            "fixed_arguments": ("--fixture", "ready"),
            "invocation_nonce": "fixture-nonce",
            "path_directories": (self.path_one, self.path_two),
            "home": self.home,
        }
        values.update(changes)
        return RuntimeCommandStageRequest(**values)

    def _lock(self) -> InstallationPublicationLock:
        return InstallationPublicationLock(
            self.target,
            target_context_sha256=self.context.sha256,
            owner_run_id="runtime-stage-test",
            operation="runtime-command-stage",
            command_sha256="c" * 64,
        ).acquire()

    def test_stages_exact_inert_command_environment_wrapper_and_manifest(self) -> None:
        lock = self._lock()
        self.addCleanup(lambda: lock.active and lock.release("completed"))
        stage = stage_runtime_command(self._request(), lock=lock)

        self.assertEqual(stage.root, self.target / ".caprmedio_tmp" / "installation" / "staging" / lock.lock_generation)
        self.assertEqual(stage.state_generation, 1)
        self.assertEqual(stage.package_manifest_sha256, self.package.manifest_digest)
        self.assertEqual(stage.target_project_context_sha256, self.context.sha256)
        self.assertFalse((self.target / ".caprmedio_runtime" / "config.toml").exists())
        self.assertFalse((self.target / ".caprmedio_runtime" / "installation" / "current.toml").exists())

        command_payload = stage.command_path.read_bytes()
        environment_payload = stage.environment_path.read_bytes()
        wrapper_payload = stage.wrapper_path.read_bytes()
        command = tomllib.loads(command_payload.decode("utf-8"))
        environment = tomllib.loads(environment_payload.decode("utf-8"))
        manifest = tomllib.loads(stage.manifest_path.read_text(encoding="utf-8"))
        self.assertEqual(
            set(command),
            {
                "schema_version", "package_manifest_sha256", "target_project_context_sha256", "state_generation",
                "entrypoint", "argv", "environment_sha256", "wrapper_sha256", "invocation_nonce", "command_sha256",
            },
        )
        self.assertEqual(
            command["argv"],
            [
                "uv", "run", "--locked", "--no-sync", "--no-env-file", "--project", str(self.package.root),
                "python", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/runtime_entry.py", "--fixture", "ready",
            ],
        )
        without_command_digest = {key: value for key, value in command.items() if key != "command_sha256"}
        self.assertEqual(command["command_sha256"], _canonical_digest(without_command_digest))
        self.assertEqual(set(environment), {"schema_version", "variables", "environment_sha256"})
        self.assertEqual(set(environment["variables"]), {"PATH", "HOME", "UV_PROJECT_ENVIRONMENT", "UV_CACHE_DIR"})
        self.assertEqual(environment["variables"]["PATH"], f"{self.path_one}:{self.path_two}")
        self.assertEqual(
            environment["environment_sha256"],
            _canonical_digest({key: value for key, value in environment.items() if key != "environment_sha256"}),
        )
        self.assertIn(b"#!/bin/sh\n", wrapper_payload)
        self.assertIn(b"exec env -i", wrapper_payload)
        self.assertNotIn(b"$@", wrapper_payload)
        self.assertNotIn(b".env", wrapper_payload)
        self.assertEqual(set(manifest), {"schema_version", "package_manifest_sha256", "target_project_context_sha256", "state_generation", "lock_generation", "files"})
        self.assertEqual([row["path"] for row in manifest["files"]], ["command.toml", "environment.toml", "wrapper"])
        self.assertEqual([row["mode"] for row in manifest["files"]], [0o600, 0o600, 0o700])
        self.assertEqual([row["sha256"] for row in manifest["files"]], [_sha256(command_payload), _sha256(environment_payload), _sha256(wrapper_payload)])
        for path, mode in ((stage.command_path, 0o600), (stage.environment_path, 0o600), (stage.wrapper_path, 0o700), (stage.manifest_path, 0o600)):
            self.assertEqual(path.stat().st_mode & 0o777, mode)

    def test_refuses_forwarded_environment_file_argument_before_stage_write(self) -> None:
        lock = self._lock()
        self.addCleanup(lambda: lock.active and lock.release("completed"))
        with self.assertRaisesRegex(PortableRuntimeMaterializationError, "runtime-stage-arguments-invalid"):
            stage_runtime_command(self._request(fixed_arguments=("--env-file", "forbidden")), lock=lock)
        self.assertFalse((self.target / ".caprmedio_tmp" / "installation" / "staging" / lock.lock_generation).exists())

    def test_refuses_non_native_state_generations_before_stage_write(self) -> None:
        for generation in (True, 0, -1):
            with self.subTest(generation=generation):
                lock = self._lock()
                try:
                    with self.assertRaisesRegex(PortableRuntimeMaterializationError, "runtime-stage-generation-invalid"):
                        stage_runtime_command(self._request(state_generation=generation), lock=lock)
                    self.assertFalse(
                        (self.target / ".caprmedio_tmp" / "installation" / "staging" / lock.lock_generation).exists()
                    )
                finally:
                    if lock.active:
                        lock.release("completed")

    def test_refuses_absent_or_nonconcrete_lock_before_any_stage_directory(self) -> None:
        for lock in (None, object()):
            with self.subTest(lock_type=type(lock).__name__):
                with self.assertRaisesRegex(PortableRuntimeMaterializationError, "runtime-stage-lock-required"):
                    stage_runtime_command(self._request(), lock=lock)  # type: ignore[arg-type]
        self.assertFalse((self.target / ".caprmedio_tmp").exists())

    def test_refuses_changed_selected_package_before_stage_write(self) -> None:
        (self.package.root / "uv.lock").write_bytes(b"version = 2\n")
        lock = self._lock()
        self.addCleanup(lambda: lock.active and lock.release("completed"))
        with self.assertRaisesRegex(PortableRuntimeMaterializationError, "runtime-stage-package-invalid"):
            stage_runtime_command(self._request(), lock=lock)
        self.assertFalse((self.target / ".caprmedio_tmp" / "installation" / "staging" / lock.lock_generation).exists())

    def test_refuses_changed_persisted_context_before_stage_write(self) -> None:
        context_path = self.target / ".caprmedio_runtime" / "installation" / "contexts" / f"{self.context.sha256}.toml"
        context_path.write_bytes(b"schema_version = 1\n")
        lock = self._lock()
        self.addCleanup(lambda: lock.active and lock.release("completed"))
        with self.assertRaisesRegex(PortableRuntimeMaterializationError, "runtime-stage-context-stale"):
            stage_runtime_command(self._request(), lock=lock)
        self.assertFalse((self.target / ".caprmedio_tmp" / "installation" / "staging" / lock.lock_generation).exists())

    def test_refuses_symlinked_staging_ancestor_before_stage_write(self) -> None:
        outside = self.base / "outside"
        outside.mkdir()
        (self.target / ".caprmedio_tmp").symlink_to(outside, target_is_directory=True)
        lock = self._lock()
        self.addCleanup(lambda: lock.active and lock.release("completed"))
        with self.assertRaisesRegex(PortableRuntimeMaterializationError, "runtime-stage-path-unsafe"):
            stage_runtime_command(self._request(), lock=lock)
        self.assertFalse((outside / "installation").exists())

    def test_refuses_symlinked_existing_stage_without_writing_the_redirected_tree(self) -> None:
        lock = self._lock()
        self.addCleanup(lambda: lock.active and lock.release("completed"))
        redirected = self.base / "redirected"
        redirected.mkdir()
        staging = self.target / ".caprmedio_tmp" / "installation" / "staging"
        staging.mkdir(parents=True)
        (staging / lock.lock_generation).symlink_to(redirected, target_is_directory=True)
        with self.assertRaisesRegex(PortableRuntimeMaterializationError, "runtime-stage-conflict"):
            stage_runtime_command(self._request(), lock=lock)
        self.assertFalse((redirected / "installation").exists())

    def test_package_ancestor_replacement_before_member_read_refuses_without_external_read(self) -> None:
        lock = self._lock()
        self.addCleanup(lambda: lock.active and lock.release("completed"))
        redirected = self.base / "redirected-package"
        redirected.mkdir()
        install_root = self.target / ".caprmedio_install"
        moved_install_root = self.target / ".caprmedio_install.moved"
        original_reader = materialization._read_target_regular
        replacement = {"performed": False}

        def replace_before_entrypoint(root: Path, relative: Path, **kwargs: object) -> bytes:
            if kwargs.get("label") == "entrypoint":
                try:
                    install_root.rename(moved_install_root)
                    install_root.symlink_to(redirected, target_is_directory=True)
                    replacement["performed"] = True
                except PermissionError as error:
                    self.skipTest(f"host denied package ancestor swap injection: {error}")
            return original_reader(root, relative, **kwargs)

        with patch.object(materialization, "_read_target_regular", side_effect=replace_before_entrypoint):
            try:
                stage_runtime_command(self._request(), lock=lock)
            except PortableRuntimeMaterializationError as error:
                self.assertTrue(replacement["performed"])
                self.assertEqual(error.code, "runtime-stage-entrypoint-unadmitted")
            else:
                self.assertFalse(replacement["performed"])
        self.assertFalse((redirected / "releases").exists())
        if replacement["performed"]:
            self.assertFalse((self.target / ".caprmedio_tmp").exists())

    def test_staging_parent_replacement_after_open_keeps_writes_out_of_redirected_tree(self) -> None:
        lock = self._lock()
        self.addCleanup(lambda: lock.active and lock.release("completed"))
        redirected = self.base / "redirected-stage"
        redirected.mkdir()
        staging = self.target / ".caprmedio_tmp" / "installation" / "staging"
        moved_staging = self.target / ".caprmedio_tmp" / "installation" / "staging.moved"
        original_open_stage = materialization._open_stage
        replacement = {"performed": False}

        def replace_after_parent_open(parent_fd: int, lock_generation: str) -> int:
            try:
                staging.rename(moved_staging)
                staging.symlink_to(redirected, target_is_directory=True)
                replacement["performed"] = True
            except PermissionError as error:
                self.skipTest(f"host denied staging ancestor swap injection: {error}")
            return original_open_stage(parent_fd, lock_generation)

        with patch.object(materialization, "_open_stage", side_effect=replace_after_parent_open):
            try:
                stage = stage_runtime_command(self._request(), lock=lock)
            except PortableRuntimeMaterializationError as error:
                self.assertTrue(replacement["performed"])
                self.assertEqual(error.code, "runtime-stage-reopen-failed")
            else:
                self.assertFalse(replacement["performed"])
                self.assertTrue(stage.command_path.is_file())
        self.assertFalse((redirected / lock.lock_generation / "command.toml").exists())
        if replacement["performed"]:
            self.assertTrue((moved_staging / lock.lock_generation / "command.toml").is_file())

    def test_post_write_wrapper_tamper_is_refused_by_real_reopen(self) -> None:
        lock = self._lock()
        self.addCleanup(lambda: lock.active and lock.release("completed"))
        original_write = materialization._write_new

        def write_then_tamper(directory_fd: int, name: str, payload: bytes, *, mode: int) -> None:
            original_write(directory_fd, name, payload, mode=mode)
            if name == "wrapper":
                descriptor = os.open(name, os.O_WRONLY | os.O_TRUNC | os.O_NOFOLLOW, dir_fd=directory_fd)
                try:
                    os.write(descriptor, b"#!/bin/sh\necho tampered\n")
                    os.fsync(descriptor)
                finally:
                    os.close(descriptor)

        with patch.object(materialization, "_write_new", side_effect=write_then_tamper):
            with self.assertRaisesRegex(PortableRuntimeMaterializationError, "runtime-stage-reopen-failed"):
                stage_runtime_command(self._request(), lock=lock)
        stage_root = self.target / ".caprmedio_tmp" / "installation" / "staging" / lock.lock_generation
        self.assertEqual((stage_root / "wrapper").read_bytes(), b"#!/bin/sh\necho tampered\n")

    def test_refuses_unadmitted_or_non_engine_entrypoint_before_stage_write(self) -> None:
        for entrypoint in (
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/missing.py",
            "SKILLS/ca/helper.py",
        ):
            with self.subTest(entrypoint=entrypoint):
                lock = self._lock()
                try:
                    with self.assertRaisesRegex(PortableRuntimeMaterializationError, "runtime-stage-entrypoint-unadmitted"):
                        stage_runtime_command(self._request(entrypoint=entrypoint), lock=lock)
                    self.assertFalse(
                        (self.target / ".caprmedio_tmp" / "installation" / "staging" / lock.lock_generation).exists()
                    )
                finally:
                    if lock.active:
                        lock.release("completed")

    def test_refuses_unsafe_environment_paths_before_stage_write(self) -> None:
        for changes in (
            {"path_directories": (Path("relative-path"),)},
            {"home": Path("relative-home")},
        ):
            with self.subTest(changes=changes):
                lock = self._lock()
                try:
                    with self.assertRaisesRegex(PortableRuntimeMaterializationError, "runtime-stage-environment-invalid"):
                        stage_runtime_command(self._request(**changes), lock=lock)
                    self.assertFalse(
                        (self.target / ".caprmedio_tmp" / "installation" / "staging" / lock.lock_generation).exists()
                    )
                finally:
                    if lock.active:
                        lock.release("completed")

    def test_refuses_a_different_second_stage_without_overwriting_first_bytes(self) -> None:
        lock = self._lock()
        self.addCleanup(lambda: lock.active and lock.release("completed"))
        first = stage_runtime_command(self._request(), lock=lock)
        original = {
            path.name: path.read_bytes()
            for path in (first.command_path, first.environment_path, first.wrapper_path, first.manifest_path)
        }
        with self.assertRaisesRegex(PortableRuntimeMaterializationError, "runtime-stage-conflict"):
            stage_runtime_command(self._request(fixed_arguments=("--changed",)), lock=lock)
        self.assertEqual(
            {
                path.name: path.read_bytes()
                for path in (first.command_path, first.environment_path, first.wrapper_path, first.manifest_path)
            },
            original,
        )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
