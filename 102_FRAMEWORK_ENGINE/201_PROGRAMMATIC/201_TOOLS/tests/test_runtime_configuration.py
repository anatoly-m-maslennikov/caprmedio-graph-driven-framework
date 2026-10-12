"""Synthetic coverage for target-owned runtime TOML configuration."""

from __future__ import annotations

import errno
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


TOOLS_ROOT = Path(__file__).resolve().parents[1]
if str(TOOLS_ROOT) not in sys.path:
    sys.path.insert(0, str(TOOLS_ROOT))
TESTS_ROOT = Path(__file__).resolve().parent
if str(TESTS_ROOT) not in sys.path:
    sys.path.insert(0, str(TESTS_ROOT))

from framework_package import assemble_framework_package  # noqa: E402
from installation_transaction import installation_publication_lock  # noqa: E402
from runtime_configuration import (  # noqa: E402
    RUNTIME_CONFIGURATION_RELATIVE,
    RuntimeConfigurationError,
    ensure_runtime_configuration,
    read_admitted_runtime_default,
    read_runtime_configuration,
)
import runtime_configuration as configuration_library  # noqa: E402
from source_admission_fixture import write_source_admission_receipt  # noqa: E402


def _sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _tree_sha(path: Path) -> str:
    rows = [
        {
            "path": member.relative_to(path).as_posix(),
            "sha256": hashlib.sha256(member.read_bytes()).hexdigest(),
            "mode": member.stat().st_mode & 0o777,
        }
        for member in sorted(path.rglob("*"))
        if member.is_file() and not member.is_symlink()
    ]
    return hashlib.sha256(
        json.dumps(rows, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


class RuntimeConfigurationTests(unittest.TestCase):
    """Every fixture uses a physically assembled, content-addressed package."""

    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="caprmedio-runtime-configuration-")).resolve()
        self.source = self.root / "source"
        self.releases = self.root / "releases"
        self.project = self.root / "project"
        self.project.mkdir()
        self.default_member = "defaults/runtime-config.toml"
        self.default_bytes = b"# package-supplied default\n[transport]\nendpoint = 'fixture'\n"
        self._seed_package_compiler_closure()
        self._write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", b"tool = 'fixture'\n")
        self._write("methodology/active/001_CORE_META_MODEL/04_requirement/CA-R-001--fixture.md", b"# active methodology\n")
        self._write(
            "methodology/active/003_PROJECT_CONFIGURATION/05_method/CA-M-001--fixture.md",
            b"# configuration methodology\n",
        )
        self._write("methodology/support/CA-D-001--fixture.md", b"# declared support\n")
        self._write("SKILLS/ca/SKILL.md", b"# ca\n")
        self._write(self.default_member, self.default_bytes)
        self._write("pyproject.toml", b"[project]\nname = 'fixture'\nversion = '0.1.0'\n")
        self._write("uv.lock", b"version = 1\n")
        self._write("version.toml", b"[framework]\nversion = '0.1.0'\n")
        self._write_catalog()
        self.package = assemble_framework_package(self.source, self.releases)

    def _write(self, relative: str, payload: bytes, *, mode: int = 0o644) -> Path:
        target = self.source / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        target.chmod(mode)
        return target

    def _seed_package_compiler_closure(self) -> None:
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
            canonical = TOOLS_ROOT / relative
            self._write(
                f"102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/{relative}",
                canonical.read_bytes(),
                mode=canonical.stat().st_mode & 0o777,
            )

    def _write_catalog(self) -> None:
        source_rows = (
            ("core-engine", "core", "102_FRAMEWORK_ENGINE"),
            ("core-methodology", "methodology", "methodology/active/001_CORE_META_MODEL"),
            ("project-configuration", "configuration", "methodology/active/003_PROJECT_CONFIGURATION"),
            ("declared-support", "support", "methodology/support"),
        )
        descriptors = tuple(
            sorted(
                (
                    {
                        "identity": identity,
                        "kind": kind,
                        "revision": _tree_sha(self.source / relative),
                        "sha256": _tree_sha(self.source / relative),
                        "visibility": "public",
                        "selection_default": False,
                        "path": relative,
                    }
                    for identity, kind, relative in source_rows
                ),
                key=lambda descriptor: descriptor["identity"],
            )
        )
        receipt = write_source_admission_receipt(self.source, descriptors)
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
        self._write("catalog.toml", ("\n".join(lines) + "\n").encode("utf-8"))

    def _lock(self):
        return installation_publication_lock(
            self.project,
            target_context_sha256=_sha256("project"),
            owner_run_id="runtime-config",
            operation="installation",
            command_sha256=_sha256("command"),
            timeout_seconds=0,
        )

    @property
    def config_path(self) -> Path:
        return self.project / RUNTIME_CONFIGURATION_RELATIVE

    def test_absent_configuration_creates_exact_admitted_default_under_lock(self) -> None:
        with self._lock() as lock:
            result = ensure_runtime_configuration(
                self.project, self.package, default_member=self.default_member, lock=lock
            )
            lock.release("completed")

        self.assertEqual(result.state, "created")
        self.assertEqual(self.config_path.read_bytes(), self.default_bytes)
        self.assertEqual(result.configuration.payload, self.default_bytes)
        self.assertEqual(self.config_path.stat().st_mode & 0o777, 0o600)

    def test_shared_admitted_default_reader_is_read_only(self) -> None:
        result = read_admitted_runtime_default(self.package, default_member=self.default_member)
        self.assertEqual(result.payload, self.default_bytes)
        self.assertEqual(result.sha256, hashlib.sha256(self.default_bytes).hexdigest())
        self.assertFalse(self.config_path.parent.exists())

    def test_existing_bytes_and_comments_are_preserved_without_a_creation_lock(self) -> None:
        original = b"# target-owned comment\n[transport]\nendpoint = 'target'\n"
        self.config_path.parent.mkdir()
        self.config_path.write_bytes(original)

        result = ensure_runtime_configuration(self.project, self.package, default_member=self.default_member)

        self.assertEqual(result.state, "preserved")
        self.assertEqual(self.config_path.read_bytes(), original)
        self.assertEqual(result.configuration.payload, original)

    def test_malformed_or_schema_incompatible_target_returns_blocked_migration_needed(self) -> None:
        self.config_path.parent.mkdir()
        malformed = b"[unclosed\n"
        self.config_path.write_bytes(malformed)
        malformed_result = ensure_runtime_configuration(self.project, self.package, default_member=self.default_member)
        self.assertEqual((malformed_result.state, malformed_result.reason), ("blocked", "migration-needed"))
        self.assertEqual(self.config_path.read_bytes(), malformed)

        incompatible = b"[other]\nvalue = 'target'\n"
        self.config_path.write_bytes(incompatible)

        def authority_schema(document: dict[str, object]) -> None:
            if set(document) != {"transport"}:
                raise ValueError("authority schema changed")

        schema_result = read_runtime_configuration(self.project, validator=authority_schema)
        self.assertEqual((schema_result.state, schema_result.reason), ("blocked", "migration-needed"))
        self.assertEqual(self.config_path.read_bytes(), incompatible)

    def test_creation_failure_leaves_no_target_configuration(self) -> None:
        with self._lock() as lock:
            with patch.object(configuration_library.os, "link", side_effect=PermissionError("publication denied")):
                with self.assertRaises(RuntimeConfigurationError) as raised:
                    ensure_runtime_configuration(
                        self.project, self.package, default_member=self.default_member, lock=lock
                    )
            self.assertEqual(raised.exception.code, "runtime-config-publish-failed")
            self.assertFalse(self.config_path.exists())
            self.assertEqual(list(self.config_path.parent.glob(".config-stage-*.toml")), [])
            lock.release("blocked")

    def test_raced_target_is_preserved_instead_of_replaced(self) -> None:
        target_bytes = b"# written by competing publisher\n[transport]\nendpoint = 'raced'\n"
        original_link = configuration_library.os.link

        def publish_competing_target(*args, **kwargs):
            self.config_path.write_bytes(target_bytes)
            return original_link(*args, **kwargs)

        with self._lock() as lock:
            with patch.object(configuration_library.os, "link", side_effect=publish_competing_target):
                result = ensure_runtime_configuration(
                    self.project, self.package, default_member=self.default_member, lock=lock
                )
            lock.release("completed")

        self.assertEqual(result.state, "preserved")
        self.assertEqual(self.config_path.read_bytes(), target_bytes)

    def test_symlink_target_and_private_default_metadata_are_refused(self) -> None:
        self.config_path.parent.mkdir()
        outside = self.root / "outside.toml"
        outside.write_bytes(self.default_bytes)
        try:
            self.config_path.symlink_to(outside)
        except OSError as error:  # pragma: no cover - host capability guard.
            self.skipTest(f"symlinks unavailable in synthetic fixture: {error}")
        with self.assertRaises(RuntimeConfigurationError) as symlink:
            read_runtime_configuration(self.project)
        self.assertEqual(symlink.exception.code, "runtime-config-path-unsafe")

        self.config_path.unlink()
        with self.assertRaises(RuntimeConfigurationError) as private_member:
            ensure_runtime_configuration(self.project, self.package, default_member=".env.toml")
        self.assertEqual(private_member.exception.code, "runtime-config-default-invalid")

    def test_project_root_symlink_ancestor_is_refused_before_any_runtime_read(self) -> None:
        actual_parent = self.root / "actual-parent"
        actual_project = actual_parent / "project"
        actual_project.mkdir(parents=True)
        alias = self.root / "parent-alias"
        try:
            alias.symlink_to(actual_parent, target_is_directory=True)
        except OSError as error:  # pragma: no cover - host capability guard.
            self.skipTest(f"symlinks unavailable in synthetic fixture: {error}")

        with self.assertRaises(RuntimeConfigurationError) as raised:
            read_runtime_configuration(alias / "project")
        self.assertEqual(raised.exception.code, "runtime-config-project-unsafe")

    def test_ancestor_swap_after_validation_cannot_open_external_configuration(self) -> None:
        holder = self.root / "project-holder"
        project = holder / "project"
        project.mkdir(parents=True)
        outside_holder = self.root / "outside-holder"
        outside_config = outside_holder / "project" / RUNTIME_CONFIGURATION_RELATIVE
        outside_config.parent.mkdir(parents=True)
        outside_bytes = b"[outside]\nvalue = 'must not be read'\n"
        outside_config.write_bytes(outside_bytes)
        validated = configuration_library._project_root(project)
        original_open = configuration_library.os.open
        observed_holder_open = False

        def swapped_ancestor_open(path, *args, **kwargs):
            nonlocal observed_holder_open
            if path == holder.name:
                observed_holder_open = True
                # Model the O_NOFOLLOW failure produced when this validated
                # directory is atomically replaced by an external symlink.
                raise OSError(errno.ELOOP, "validated ancestor was replaced by a symlink")
            if path == RUNTIME_CONFIGURATION_RELATIVE.name:
                raise AssertionError("external runtime configuration must not be opened")
            return original_open(path, *args, **kwargs)

        with patch.object(configuration_library, "_project_root", return_value=validated):
            with patch.object(configuration_library.os, "open", side_effect=swapped_ancestor_open):
                with self.assertRaises(RuntimeConfigurationError) as raised:
                    read_runtime_configuration(project)
        self.assertEqual(raised.exception.code, "runtime-config-project-unsafe")
        self.assertTrue(observed_holder_open)
        self.assertEqual(outside_config.read_bytes(), outside_bytes)

    def test_default_symlink_race_is_refused_before_its_target_is_read(self) -> None:
        default_path = self.package.root / self.default_member
        outside = self.root / "outside-default.toml"
        outside.write_bytes(b"[outside]\nvalue = 'not package bytes'\n")
        original_open = configuration_library.os.open
        swapped = False

        def race_open(path, *args, **kwargs):
            nonlocal swapped
            if path == default_path.name and not swapped:
                swapped = True
                default_path.unlink()
                default_path.symlink_to(outside)
            return original_open(path, *args, **kwargs)

        with patch.object(configuration_library.os, "open", side_effect=race_open):
            with self.assertRaises(RuntimeConfigurationError) as raised:
                ensure_runtime_configuration(self.project, self.package, default_member=self.default_member)
        self.assertEqual(raised.exception.code, "runtime-config-default-invalid")
        self.assertFalse(self.config_path.exists())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
