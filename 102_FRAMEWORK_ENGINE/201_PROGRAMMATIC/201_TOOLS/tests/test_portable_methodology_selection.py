"""Fast catalog-selection checks for package Methodology material rows."""

from __future__ import annotations

from dataclasses import replace
import hashlib
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
TESTS = Path(__file__).resolve().parent
TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
if str(TESTS) not in sys.path:
    sys.path.insert(0, str(TESTS))

from framework_package import PackageInventoryRow, VerifiedFrameworkPackage, assemble_framework_package  # noqa: E402
import portable_methodology_installation as delivery  # noqa: E402
import artifact_metadata  # noqa: E402
from source_admission_fixture import write_source_admission_receipt  # noqa: E402


class PortableMethodologySelectionTests(unittest.TestCase):
    def _package(self, rows: tuple[tuple[str, str, str, bytes], ...]) -> tuple[VerifiedFrameworkPackage, tuple[tuple[str, dict[str, str]], ...], tuple[object, ...]]:
        root = Path(tempfile.mkdtemp(prefix="caprmedio-portable-methodology-selection-"))
        inventory: list[PackageInventoryRow] = []
        records: list[tuple[str, dict[str, str]]] = []
        pins: list[object] = []
        for identity, kind, path, payload in rows:
            target = root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(payload)
            target.chmod(0o640)
            digest = hashlib.sha256(payload).hexdigest()
            inventory.append(PackageInventoryRow(path, digest, 0o640, "methodology"))
            record = {
                "kind": kind,
                "revision": "r1",
                "sha256": digest,
                "admission_receipt_sha256": "a" * 64,
                "path": path,
            }
            records.append((identity, record))
            pins.append(SimpleNamespace(identity=identity, **record))
        package = VerifiedFrameworkPackage("b" * 64, root, tuple(inventory), "1.2.3", "c" * 64, "d" * 64)
        return package, tuple(records), tuple(pins)

    def _admitted_package(
        self,
        *,
        compiler_bytes: bytes | None,
        dependency_overrides: dict[Path, bytes] | None = None,
        omit_dependency: Path | None = None,
    ) -> VerifiedFrameworkPackage:
        """Build a real content-addressed package, retaining its fixture root."""

        base = Path(tempfile.mkdtemp(prefix="caprmedio-portable-methodology-compiler-", dir=TEST_TEMP_ROOT)).resolve()
        source, releases = base / "source", base / "releases"

        def write(relative: str, payload: bytes, mode: int = 0o644) -> None:
            carrier = source / relative
            carrier.parent.mkdir(parents=True, exist_ok=True)
            carrier.write_bytes(payload)
            carrier.chmod(mode)

        if compiler_bytes is not None:
            write(delivery.PACKAGE_COMPILER_RELATIVE.as_posix(), compiler_bytes, 0o755)
        else:
            write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", b"tool = 'fixture'\n", 0o755)
        package_tools = Path("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS")
        for _name, relative, _is_package in delivery._PACKAGE_COMPILER_DEPENDENCIES:
            if relative == omit_dependency:
                continue
            payload = (dependency_overrides or {}).get(relative)
            if payload is None:
                payload = (TOOLS / relative.relative_to(package_tools)).read_bytes()
            write(relative.as_posix(), payload, 0o644)
        write("methodology/active/001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", b"# core\n")
        write("methodology/support/CA-D-001--support.md", b"# support\n")
        write("SKILLS/ca/SKILL.md", b"# ca\n")
        write("defaults/framework.toml", b"[defaults]\nname = 'fixture'\n")
        write("pyproject.toml", b"[project]\nname = 'fixture'\nversion = '0.1.0'\n")
        write("uv.lock", b"version = 1\n")
        write("version.toml", b"[framework]\nversion = '0.1.0'\n")

        def tree_sha(relative: str) -> str:
            root = source / relative
            if root.is_file():
                return hashlib.sha256(root.read_bytes()).hexdigest()
            rows = [
                {
                    "path": member.relative_to(root).as_posix(),
                    "sha256": hashlib.sha256(member.read_bytes()).hexdigest(),
                    "mode": member.stat().st_mode & 0o777,
                }
                for member in sorted(root.rglob("*"))
                if member.is_file()
            ]
            return hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

        descriptors = tuple(
            {
                "identity": identity,
                "kind": kind,
                "revision": tree_sha(relative),
                "sha256": tree_sha(relative),
                "visibility": "public",
                "selection_default": False,
                "path": relative,
            }
            for identity, kind, relative in (
                ("core-engine", "core", "102_FRAMEWORK_ENGINE"),
                ("core-methodology", "methodology", "methodology/active/001_CORE_META_MODEL"),
                ("declared-support", "support", "methodology/support"),
            )
        )
        receipt = write_source_admission_receipt(source, descriptors)
        lines = ["schema_version = 1", ""]
        for descriptor in descriptors:
            lines.extend((
                f"[source.{descriptor['identity']}]",
                f'kind = "{descriptor["kind"]}"',
                f'revision = "{descriptor["revision"]}"',
                f'sha256 = "{descriptor["sha256"]}"',
                f'admission_receipt_sha256 = "{receipt.sha256}"',
                'visibility = "public"',
                "selection_default = false",
                f'path = "{descriptor["path"]}"',
                "",
            ))
        write("catalog.toml", ("\n".join(lines) + "\n").encode())
        return assemble_framework_package(source, releases)

    def test_unselected_extension_configuration_rows_are_excluded_but_selected_rows_are_kept(self) -> None:
        package, records, pins = self._package((
            ("method", "methodology", "methodology/active/001_CORE_META_MODEL/04_requirement/one.md", b"one\n"),
            ("config", "configuration", "methodology/active/003_PROJECT_CONFIGURATION/05_method/two.md", b"two\n"),
        ))

        only_method = delivery._selected_members(package, records, ("method",), pins)
        both = delivery._selected_members(package, records, ("method", "config"), pins)

        self.assertEqual(["method"], [member.identity for member in only_method])
        self.assertEqual(["method", "config"], [member.identity for member in both])

    def test_overlapping_or_unadmitted_material_rows_are_refused_before_selection(self) -> None:
        path = Path("methodology/active/001_CORE_META_MODEL/04_requirement/one.md")
        overlap = (
            ("tree", {"kind": "methodology", "path": "methodology/active/001_CORE_META_MODEL"}),
            ("file", {"kind": "methodology", "path": path.as_posix()}),
        )
        with self.assertRaises(delivery.PortableMethodologyInstallationError) as overlapping:
            delivery._material_descriptor(overlap, path, {"methodology"})
        self.assertEqual("portable-methodology-row-overlap", overlapping.exception.code)

        with self.assertRaises(delivery.PortableMethodologyInstallationError) as unadmitted:
            delivery._material_descriptor((("other", {"kind": "methodology", "path": "methodology/active/other"}),), path, {"methodology"})
        self.assertEqual("portable-methodology-row-unadmitted", unadmitted.exception.code)

    def test_direct_target_selection_requires_the_typed_context_tuple(self) -> None:
        context = SimpleNamespace(methodology_source_identities=("core-methodology", "extension-a"))
        self.assertEqual(
            ("core-methodology", "extension-a"),
            delivery._target_methodology_identities(context),
        )
        with self.assertRaises(delivery.PortableMethodologyInstallationError) as missing:
            delivery._target_methodology_identities(SimpleNamespace(methodology_source_identities=["core-methodology"]))
        self.assertEqual("portable-methodology-target-selection-missing", missing.exception.code)

    def test_direct_projection_relates_to_the_prospective_installed_package_not_private_package_root(self) -> None:
        package, _records, _pins = self._package((
            ("method", "methodology", "methodology/active/001_CORE_META_MODEL/04_requirement/one.md", b"one\n"),
        ))
        member = delivery._SourceMember(
            identity="method",
            kind="methodology",
            package_path=Path("methodology/active/001_CORE_META_MODEL/04_requirement/one.md"),
            source_relative=Path("001_CORE_META_MODEL/04_requirement/one.md"),
            payload=b"one\n",
            sha256=hashlib.sha256(b"one\n").hexdigest(),
            mode=0o640,
        )
        root = Path("/prospective/project")
        relation = delivery._prospective_source_relation(
            root,
            Path(".caprmedio_project/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"),
            package,
            member,
            SimpleNamespace(role_directory="04_requirement"),
        )
        self.assertIn(f".caprmedio_install/releases/{package.manifest_digest}/methodology/active/", relation)
        self.assertNotIn(package.root.as_posix(), relation)

    def test_admitted_package_compiler_is_loaded_from_package_not_current_checkout_and_tamper_refuses(self) -> None:
        current_bytes = Path(delivery.compiler.__file__).read_bytes()
        package_bytes = current_bytes + b"\n# package-only compiler revision\n"
        package = self._admitted_package(compiler_bytes=package_bytes)

        package_compiler, binding = delivery.open_admitted_package_compiler(package)
        self.assertEqual(delivery.PACKAGE_COMPILER_RELATIVE.as_posix(), binding.path)
        self.assertEqual(hashlib.sha256(package_bytes).hexdigest(), binding.sha256)
        self.assertEqual((package.root / delivery.PACKAGE_COMPILER_RELATIVE).as_posix(), package_compiler.__file__)
        self.assertNotEqual(hashlib.sha256(current_bytes).hexdigest(), binding.sha256)
        self.assertTrue(callable(package_compiler.projection_bytes))
        reopened_compiler, reopened_binding = delivery.reopen_admitted_package_compiler(package, binding)
        self.assertEqual(binding, reopened_binding)
        self.assertEqual(package_compiler.__file__, reopened_compiler.__file__)

        carrier = package.root / delivery.PACKAGE_COMPILER_RELATIVE
        carrier.write_bytes(package_bytes + b"# tampered\n")
        with self.assertRaises(delivery.PortableMethodologyInstallationError) as tampered:
            delivery.open_admitted_package_compiler(package)
        self.assertEqual("portable-methodology-package-compiler-invalid", tampered.exception.code)

    def test_admitted_package_compiler_loads_its_closed_dependency_bytes_not_current_modules(self) -> None:
        compiler_bytes = Path(delivery.compiler.__file__).read_bytes() + (
            b"\n\ndef package_late_identity():\n"
            b"    from artifact_metadata import atom_identifier\n"
            b"    return atom_identifier('ordinary.md')\n"
            b"\ndef package_stdlib_identity():\n"
            b"    import json\n"
            b"    return json.dumps({'stable': True}, sort_keys=True, separators=(',', ':'))\n"
            b"\ndef package_missing_fromlist():\n"
            b"    from VALIDATE_ATOMS import unknown_child\n"
            b"    return unknown_child\n"
        )
        metadata_relative = Path("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/artifact_metadata.py")
        package_metadata = (TOOLS / "artifact_metadata.py").read_bytes()
        original = b'return name.removesuffix(".md").split("--", 1)[0]'
        self.assertIn(original, package_metadata)
        package_metadata = package_metadata.replace(original, b'return "PKG-SENTINEL"', 1)
        package = self._admitted_package(
            compiler_bytes=compiler_bytes,
            dependency_overrides={metadata_relative: package_metadata},
        )

        path_before = tuple(sys.path)
        historic_metadata = sys.modules["artifact_metadata"]
        with (
            patch.object(artifact_metadata, "atom_identifier", return_value="CURRENT-SENTINEL"),
            patch.dict(sys.modules, {"json": SimpleNamespace(dumps=lambda *_args, **_kwargs: "CURRENT-N-JSON")}),
        ):
            package_compiler, _binding = delivery.open_admitted_package_compiler(package)
            self.assertEqual("PKG-SENTINEL", package_compiler.derive_atom_id(Path("ordinary.md"), ""))
            # This import occurs only after open() restored ambient modules.
            self.assertEqual("PKG-SENTINEL", package_compiler.package_late_identity())
            self.assertEqual('{"stable":true}', package_compiler.package_stdlib_identity())
        self.assertEqual(path_before, tuple(sys.path))
        self.assertIs(historic_metadata, sys.modules["artifact_metadata"])
        with patch.dict(
            sys.modules,
            {f"{package_compiler.__package__}.unknown_child": SimpleNamespace(value="ambient")},
        ):
            with self.assertRaises(delivery.PortableMethodologyInstallationError) as missing_child:
                package_compiler.package_missing_fromlist()
        self.assertEqual("portable-methodology-package-compiler-dependency-unadmitted", missing_child.exception.code)

    def test_admitted_package_compiler_refuses_an_unadmitted_local_dependency(self) -> None:
        package = self._admitted_package(
            compiler_bytes=Path(delivery.compiler.__file__).read_bytes(),
            omit_dependency=Path("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/artifact_metadata.py"),
        )
        with self.assertRaises(delivery.PortableMethodologyInstallationError) as missing:
            delivery.open_admitted_package_compiler(package)
        self.assertEqual("portable-methodology-package-compiler-dependency-missing", missing.exception.code)

    def test_unadmitted_package_compiler_is_refused(self) -> None:
        package = self._admitted_package(compiler_bytes=None)
        with self.assertRaises(delivery.PortableMethodologyInstallationError) as missing:
            delivery.open_admitted_package_compiler(package)
        self.assertEqual("portable-methodology-package-compiler-missing", missing.exception.code)

    def test_legacy_materializer_uses_context_selection_not_package_availability_summary(self) -> None:
        package, records, pins = self._package((
            ("core", "methodology", "methodology/active/001_CORE_META_MODEL/04_requirement/core.md", b"core\n"),
            ("extension-selected", "extension", "methodology/active/002_INSTALLED_EXTENSIONS/a/r1/04_requirement/a.md", b"selected\n"),
            ("extension-unselected", "extension", "methodology/active/002_INSTALLED_EXTENSIONS/b/r1/04_requirement/b.md", b"unselected\n"),
            ("configuration", "configuration", "methodology/active/003_PROJECT_CONFIGURATION/05_method/config.md", b"configuration\n"),
        ))
        target_context = SimpleNamespace(
            package_evidence=SimpleNamespace(
                # Availability deliberately includes an alternative extension.
                selected_source_identities=("core", "extension-selected", "extension-unselected", "configuration"),
                source_pins=pins,
            ),
            methodology_source_identities=("core", "extension-selected", "configuration"),
            sha256="1" * 64,
        )
        current = SimpleNamespace(package=package, target_context=target_context)
        captured: dict[str, object] = {}

        class StopBeforeStage(Exception):
            pass

        def stop_stage(*args: object, **kwargs: object) -> object:
            captured["members"] = args[4]
            captured["compiler_module"] = kwargs["compiler_module"]
            captured["compiler_sha256"] = kwargs["compiler_sha256"]
            raise StopBeforeStage

        package_compiler = object()
        compiler_binding = delivery.PackageCompilerBinding(
            package.manifest_digest,
            delivery.PACKAGE_COMPILER_RELATIVE.as_posix(),
            "e" * 64,
            0o644,
        )

        with (
            patch.object(delivery, "_reopen_preparation", return_value=current),
            patch.object(delivery, "_rebind_target_context", return_value=target_context),
            patch.object(delivery, "_lock", return_value=None),
            patch.object(delivery, "_context_paths", return_value=(package.root, Path("authoring"), Path("output"))),
            patch.object(delivery, "_catalog", return_value=records),
            patch.object(delivery, "open_admitted_package_compiler", return_value=(package_compiler, compiler_binding)),
            patch.object(delivery, "_selected_candidates", return_value=([], "2" * 64)),
            patch.object(delivery, "_stage", side_effect=stop_stage),
        ):
            with self.assertRaises(StopBeforeStage):
                delivery.materialize_portable_methodology(object(), object(), lock=object())  # type: ignore[arg-type]

        self.assertEqual(
            ["configuration", "core", "extension-selected"],
            sorted(member.identity for member in captured["members"]),
        )
        self.assertIs(package_compiler, captured["compiler_module"])
        self.assertEqual(compiler_binding.sha256, captured["compiler_sha256"])

    def _historical_export(self) -> Path:
        """Create a canonical, sealed-export-shaped root delivery fixture."""

        root = Path(tempfile.mkdtemp(prefix="caprmedio-portable-methodology-prior-export-"))
        source_path = "001_CORE_META_MODEL/04_requirement/one.md"
        payload = b"---\natom_id: CA-R-001\nrevision: 1\n---\ntext\n"
        digest = hashlib.sha256(payload).hexdigest()
        atom = {"atom_id": "CA-R-001", "sha256": digest, "source_path": source_path, "version": 1}
        exporter = delivery._exporter()
        frontier = exporter._frontier_digest(exporter._atom_records([atom], "fixture.active"))
        frozen: dict[str, object] = {
            "active_frontier": [atom],
            "active_frontier_sha256": frontier,
            "catalog_pins": [],
            # Root-delivery replacement accepts canonical historical v1
            # evidence.  A v2 manifest also has a mandatory Project binding.
            "schema": exporter.LEGACY_FROZEN_SCHEMA,
            "selected_atoms": [atom],
            "source_root": "/retained/methodology-source",
            "source_tree_sha256": "b" * 64,
            "support_inventory": [],
        }
        frozen["sha256"] = hashlib.sha256(delivery._canonical_json(frozen)).hexdigest()
        atoms = [{**atom, "destination_path": source_path, "digest": digest}]
        inventory: dict[str, object] = {
            "atoms": atoms,
            "atom_count": 1,
            "catalog_pins": [],
            "catalog_pin_count": 0,
            "frozen_manifest": frozen,
            "frozen_manifest_sha256": frozen["sha256"],
            "logical_delivery_root": "methodology",
            "schema": exporter.SCHEMA,
            "support": [],
            "support_count": 0,
        }
        inventory["inventory_sha256"] = hashlib.sha256(delivery._canonical_json(inventory)).hexdigest()
        carrier = root / source_path
        carrier.parent.mkdir(parents=True)
        carrier.write_bytes(payload)
        carrier.chmod(0o644)
        (root / "methodology-export-inventory.json").write_bytes(delivery._canonical_json(inventory) + b"\n")
        return root

    @staticmethod
    def _rewrite_inventory(root: Path, mutate: object) -> None:
        inventory = json.loads((root / "methodology-export-inventory.json").read_text(encoding="utf-8"))
        mutate(inventory)
        inventory.pop("inventory_sha256", None)
        inventory["inventory_sha256"] = hashlib.sha256(delivery._canonical_json(inventory)).hexdigest()
        (root / "methodology-export-inventory.json").write_bytes(delivery._canonical_json(inventory) + b"\n")

    def test_prior_export_inventory_requires_exporter_rows_counts_and_frozen_manifest(self) -> None:
        valid = self._historical_export()
        self.assertEqual(
            ["001_CORE_META_MODEL/04_requirement/one.md", "methodology-export-inventory.json"],
            [record.path for record in delivery._prior_source_export_inventory(valid)],
        )

        for label, mutate in (
            ("count", lambda inventory: inventory.__setitem__("atom_count", 0)),
            ("metadata", lambda inventory: inventory["atoms"][0].__setitem__("metadata", "forged")),
            (
                "frozen-schema",
                lambda inventory: self._rewrite_frozen_schema(inventory),
            ),
            (
                "v2-without-project-binding",
                lambda inventory: self._rewrite_frozen_v2_without_project_binding(inventory),
            ),
        ):
            with self.subTest(label=label):
                root = self._historical_export()
                self._rewrite_inventory(root, mutate)
                with self.assertRaises(delivery.PortableMethodologyInstallationError) as refused:
                    delivery._prior_source_export_inventory(root)
                self.assertEqual("portable-methodology-source-export-not-owned", refused.exception.code)

    def test_direct_reopener_refuses_forged_preparation_facts_before_any_publication(self) -> None:
        """A self-consistent caller object is never an alternate input authority."""

        source = delivery.PreparedTargetMethodologySource(
            identity="core-methodology",
            kind="methodology",
            package_path="methodology/active/001_CORE_META_MODEL/04_requirement/one.md",
            source_view_path="001_CORE_META_MODEL/04_requirement/one.md",
            sha256="a" * 64,
            mode=0o644,
        )
        payload = b"projected\n"
        file = delivery.PreparedTargetMethodologyFile(
            path="04_requirement/one.md", sha256=hashlib.sha256(payload).hexdigest(), mode=0o644, payload=payload,
        )
        expected = delivery.PreparedTargetMethodologyPublication(
            package_manifest_sha256="b" * 64,
            source_catalog_sha256="c" * 64,
            target_project_context_sha256="d" * 64,
            gate_receipt_sha256="e" * 64,
            selected_source_identities=("core-methodology",),
            compiler_sha256="f" * 64,
            compiler_frontier_sha256="1" * 64,
            source_view_sha256="2" * 64,
            authoring_source_sha256="3" * 64,
            source_members=(source,),
            files=(file,),
            manifest_bytes=b"canonical-preparation\n",
            manifest_sha256="4" * 64,
        )
        forged = (
            replace(expected, files=()),
            replace(expected, files=(replace(file, payload=b"forged\n", sha256=hashlib.sha256(b"forged\n").hexdigest()),)),
            replace(expected, manifest_bytes=b"forged-manifest\n", manifest_sha256="5" * 64),
            replace(expected, source_members=(replace(source, source_view_path="forged.md"),)),
            replace(expected, compiler_frontier_sha256="6" * 64),
        )
        with patch.object(delivery, "_prepare_target_methodology_publication", return_value=expected):
            for value in forged:
                with self.subTest(value=value):
                    with self.assertRaises(delivery.PortableMethodologyInstallationError) as refused:
                        delivery.reopen_prepared_target_portable_methodology_publication(
                            object(),  # type: ignore[arg-type]
                            value,
                            package=object(),  # type: ignore[arg-type]
                            target_context=object(),  # type: ignore[arg-type]
                            prospective_selector=object(),  # type: ignore[arg-type]
                        )
                    self.assertEqual("portable-methodology-target-prepared-stale", refused.exception.code)

        with self.assertRaises(delivery.PortableMethodologyInstallationError) as raw:
            delivery.reopen_prepared_target_portable_methodology_publication(
                object(),  # type: ignore[arg-type]
                object(),  # type: ignore[arg-type]
                package=object(),  # type: ignore[arg-type]
                target_context=object(),  # type: ignore[arg-type]
                prospective_selector=object(),  # type: ignore[arg-type]
            )
        self.assertEqual("portable-methodology-target-prepared-untrusted", raw.exception.code)

    @staticmethod
    def _rewrite_frozen_schema(inventory: dict[str, object]) -> None:
        frozen = inventory["frozen_manifest"]
        assert isinstance(frozen, dict)
        frozen["schema"] = "caprmedio.methodology_export.frozen.invalid"
        frozen.pop("sha256", None)
        frozen["sha256"] = hashlib.sha256(delivery._canonical_json(frozen)).hexdigest()
        inventory["frozen_manifest_sha256"] = frozen["sha256"]

    @staticmethod
    def _rewrite_frozen_v2_without_project_binding(inventory: dict[str, object]) -> None:
        frozen = inventory["frozen_manifest"]
        assert isinstance(frozen, dict)
        frozen["schema"] = delivery._exporter().FROZEN_SCHEMA
        frozen.pop("sha256", None)
        frozen["sha256"] = hashlib.sha256(delivery._canonical_json(frozen)).hexdigest()
        inventory["frozen_manifest_sha256"] = frozen["sha256"]


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
