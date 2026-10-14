"""Historical D572@36 source-admission parser regressions; no manifest writes."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
REPOSITORY = MCP.parents[2]
RELEASE_ROOT = MCP.parent / "201_TOOLS/RELEASE_VERSION"
RELEASE_TESTS = RELEASE_ROOT / "tests"
for location in (MCP, RELEASE_ROOT, RELEASE_TESTS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import release_source_admission as admission_module  # noqa: E402
from release_source_admission import (  # noqa: E402
    ReleaseSourceAdmissionError,
    derive_release_graph_admission,
    derive_release_route_graph,
    derive_release_source_admission,
    resolve_current_source_pin,
    validate_release_source_admissions,
)
from selected_routes import canonical_digest  # noqa: E402
from full_suite_golden.control_fixture import copy_control_closure  # noqa: E402


AUTHORITY_REF = admission_module.AUTHORITY_REF
AUTHORITY_GOLDEN = (
    Path(__file__).with_name("release_source_admission_golden") / "ca_d_572_v36.md"
)


def all_pins(record: dict[str, object]) -> list[dict[str, object]]:
    return [record["acceptance_frontier"], record["workflow"],
            *[pin for row in record["ordered_steps"] for pin in (row["step"], row["action"])],
            *record["ordered_actions"], *record["rmed_frontier"]]


class ReleaseSourceAdmissionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        authority = AUTHORITY_GOLDEN
        if authority.is_symlink() or not authority.is_file():
            raise AssertionError("D572@36 golden fixture is unavailable")
        actual = authority.read_bytes()
        pin = admission_module.AUTHORITY_PIN
        if (hashlib.sha256(actual).hexdigest() != pin["digest"]
                or admission_module._metadata(actual) != (pin["atom_id"], pin["version"])):
            raise AssertionError("D572@36 golden bytes do not match the legacy parser source pin")
        cls.legacy_authority = actual
        cls.legacy_authority_mode = authority.stat().st_mode & 0o777
        cls.expected: dict[str, object] | None = None
        cls.private_carriers: list[dict[str, str]] = []

    @classmethod
    def copy_sources(cls, root: Path) -> None:
        """Materialize the closed golden controls, then substitute D572@36 only."""
        copy_control_closure(REPOSITORY, root)
        target = root / AUTHORITY_REF
        if target.is_symlink() or not target.is_file():
            raise AssertionError("golden control fixture did not materialize the D572 authority path")
        target.write_bytes(cls.legacy_authority)
        target.chmod(cls.legacy_authority_mode)

    def setUp(self) -> None:
        temporary = REPOSITORY / ".caprmedio_tmp/tests/release-source-admission"
        temporary.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temporary, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.copy_sources(self.root)
        self.record = derive_release_source_admission(self.root)
        if self.expected is None:
            type(self).expected = copy.deepcopy(self.record)
        else:
            self.assertEqual(self.expected, self.record)
        self.graph = derive_release_route_graph(self.root)
        self.route = {"route": "release_version", **copy.deepcopy(self.graph)}
        self.manifest = {"routes": [self.route], "release_source_admissions": [copy.deepcopy(self.record)]}

    def snapshot(self) -> dict[str, str | None]:
        return {path.relative_to(self.root).as_posix():
                hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
                for path in self.root.rglob("*")}

    def refused(self, manifest: object) -> None:
        before = self.snapshot()
        with self.assertRaises(ReleaseSourceAdmissionError):
            validate_release_source_admissions(self.root, manifest)
        self.assertEqual(before, self.snapshot(), "rejected admission mutated Project evidence")

    def test_archived_authority_derives_legacy_ten_phase_record(self) -> None:
        before = self.snapshot()
        self.assertEqual(self.record, derive_release_source_admission(self.root))
        self.assertEqual(self.record["workflow"], self.record["acceptance_frontier"])
        self.assertEqual(10, len(self.record["ordered_steps"]))
        self.assertEqual(
            ["CA-O-170", "CA-O-175", "CA-O-185", "CA-O-176", "CA-O-186",
             "CA-O-182", "CA-O-184", "CA-O-172", "CA-O-173", "CA-O-178"],
            [row["step"]["atom_id"] for row in self.record["ordered_steps"]],
        )
        self.assertEqual(34, len(self.record["rmed_frontier"]))
        self.assertIs(True, self.record["mutation_capable"])
        self.assertEqual([], self.record["native_action_calls"])
        self.assertEqual(before, self.snapshot())

    def test_current_record_and_source_derived_graph_validate_without_writes(self) -> None:
        before = self.snapshot()
        route, admission = derive_release_graph_admission(self.root)
        self.assertEqual(self.record, admission)
        self.assertEqual("CA-O-170", route["entry_step"])
        self.assertEqual(10, len(route["on_result"]))
        self.assertEqual([self.record], validate_release_source_admissions(self.root, self.manifest))
        self.assertEqual(before, self.snapshot())

    def test_derivation_scans_each_registered_root_once_without_cross_call_cache(self) -> None:
        before = self.snapshot()
        scanner = admission_module._scan_current_source_root
        with patch.object(admission_module, "_scan_current_source_root", wraps=scanner) as scan:
            self.assertEqual(self.record, derive_release_source_admission(self.root))
            # Operations plus the Project Tools and reusable Tools roots for
            # each of the four RMED roles; every one is scanned once.
            self.assertEqual(9, scan.call_count)
        with patch.object(admission_module, "_scan_current_source_root", wraps=scanner) as scan:
            self.assertEqual([self.record], validate_release_source_admissions(self.root, self.manifest))
            self.assertEqual(9, scan.call_count)
        source = self.root / self.record["workflow"]["source_path"]
        original = source.read_bytes()
        try:
            source.write_bytes(original + b"\nfresh derivation bytes\n")
            with patch.object(admission_module, "_scan_current_source_root", wraps=scanner) as scan:
                refreshed = derive_release_source_admission(self.root)
                self.assertEqual(9, scan.call_count)
            self.assertNotEqual(self.record["workflow"]["digest"], refreshed["workflow"]["digest"])
        finally:
            source.write_bytes(original)
        self.assertEqual(before, self.snapshot())

    def test_stale_or_missing_current_workflow_refuses_before_manifest_admission(self) -> None:
        source = self.root / self.record["workflow"]["source_path"]
        original = source.read_bytes()
        source.write_bytes(original + b"\nchanged\n")
        self.refused(self.manifest)
        source.write_bytes(original)
        source.unlink()
        self.refused(self.manifest)

    def test_stale_or_missing_current_rmed_source_refuses_before_manifest_admission(self) -> None:
        source = self.root / self.record["rmed_frontier"][0]["source_path"]
        original = source.read_bytes()
        source.write_bytes(original + b"\nchanged\n")
        self.refused(self.manifest)
        source.write_bytes(original)
        source.unlink()
        self.refused(self.manifest)

    def test_duplicate_or_wrong_registered_source_refuses(self) -> None:
        source = self.root / self.record["workflow"]["source_path"]
        duplicate = source.with_name("duplicate-current-o164.md")
        shutil.copyfile(source, duplicate)
        with self.assertRaisesRegex(ReleaseSourceAdmissionError, "missing or ambiguous"):
            resolve_current_source_pin(self.root, "CA-O-164", role="Operations", operation_type="Workflow")
        duplicate.unlink()
        original = source.read_text(encoding="utf-8")
        source.write_text(original.replace("type: Workflow", "type: Action", 1), encoding="utf-8")
        with self.assertRaisesRegex(ReleaseSourceAdmissionError, "wrong registered role"):
            resolve_current_source_pin(self.root, "CA-O-164", role="Operations", operation_type="Workflow")

    def test_authority_or_route_structural_drift_refuses_without_writes(self) -> None:
        authority = self.root / AUTHORITY_REF
        original = authority.read_bytes()
        authority.write_bytes(original + b"\nchanged\n")
        self.refused(self.manifest)
        authority.write_bytes(original)
        route = copy.deepcopy(self.route)
        route["ordered_steps"] = route["ordered_steps"][::-1]
        self.refused({"routes": [route], "release_source_admissions": [self.record]})

    def test_fifteen_route_manifest_needs_no_release_authority(self) -> None:
        actual = json.loads((REPOSITORY / ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json").read_text())
        actual["routes"] = actual["routes"][:15]
        actual.pop("release_source_admissions", None)
        actual["source_freshness"]["selected_binding_digest"] = canonical_digest(actual["routes"])
        unsigned = {key: value for key, value in actual.items() if key != "canonical_manifest_sha256"}
        actual["canonical_manifest_sha256"] = canonical_digest(unsigned)
        (self.root / AUTHORITY_REF).unlink()
        self.assertEqual([], validate_release_source_admissions(self.root, actual))


class RegisteredSourceOwnerTest(unittest.TestCase):
    """Disposable source owners; no live Release authority or manifest needed."""

    def setUp(self) -> None:
        temporary = REPOSITORY / ".caprmedio_tmp/tests/release-source-owners"
        temporary.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temporary)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.owners = {name: f".caprmedio_caprmedio/authoring/{name}"
                       for name in ("TOOLS", "PROJECT_TOOLS", "CONNECTOR_TOOLS", "TOOL_WORKFLOWS")}
        for owner in self.owners.values():
            for folder in ("04_requirement", "05_method", "06_evaluation", "07_delivery", "09_operations"):
                (self.root / owner / folder).mkdir(parents=True)
        (self.root / ".caprmedio_caprmedio/09_operations").mkdir()
        (self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").write_text(
            '[project]\nname = "fixture"\n[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
        )
        settings = self.root / ".caprmedio_caprmedio/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
        settings.parent.mkdir()
        settings.write_text("[authority_modes]\ndefault = 'casual'\n")
        self.write_structure()

    def write_structure(self, extra: str = "") -> None:
        text = ('schema_version = 1\n\n[[scope_units]]\nscope_unit_name = "FRAMEWORK_ENGINE"\n'
                'parent = "PROJECT"\nscope_unit_type = "Ordered"\nscope_unit_label = "LAYER"\n'
                'structural_level = 1\nlocal_order = 2\nnavigational_order_number = 2\n'
                'authority_path = ".caprmedio_caprmedio/authoring"\ndelivery_path = "native"\n\n'
                '[[scope_units]]\nscope_unit_name = "PROGRAMMATIC"\nparent = "FRAMEWORK_ENGINE"\n'
                'scope_unit_type = "Unordered"\nscope_unit_label = "FEATURE"\nstructural_level = 2\n'
                'navigational_order_number = 1\nauthority_path = ".caprmedio_caprmedio/programmatic"\n'
                'delivery_path = "native/programmatic"\n\n')
        text += "\n".join(
            f'[[scope_units]]\nscope_unit_name = "{name}"\nparent = "PROGRAMMATIC"\n'
            'scope_unit_type = "Unordered"\nscope_unit_label = "FEATURE"\nstructural_level = 3\n'
            f'navigational_order_number = {index}\nauthority_path = "{owner}"\n'
            f'delivery_path = "native/{name}"\n' for index, (name, owner) in enumerate(self.owners.items(), 1)
        )
        (self.root / ".caprmedio_caprmedio/project_structure.toml").write_text(text + extra)

    def source(self, owner: str, atom_id: str, *, role: str = "Delivery", folder: str = "07_delivery",
               operation_type: str | None = None, status: str = "Active") -> Path:
        path = self.root / self.owners[owner] / folder / f"{atom_id}--source.md"
        text = (f"---\natom_id: {atom_id}\nversion: 2\ncontent_role: {role}\n"
                f"current_scope_unit: {owner}\nstatus: {status}\n")
        if operation_type is not None:
            text += f"type: {operation_type}\n"
        path.write_text(text + "---\n# Summary\n\nFixture source\n")
        return path

    def test_resolves_each_rebuilt_owner_and_reopens_exact_current_pin(self) -> None:
        for owner, atom_id in (("CONNECTOR_TOOLS", "CA-D-625"), ("TOOL_WORKFLOWS", "CA-D-425")):
            with self.subTest(owner=owner):
                source = self.source(owner, atom_id)
                pin = resolve_current_source_pin(self.root, atom_id, role="Delivery")
                self.assertEqual({"atom_id": atom_id, "version": 2,
                                  "source_path": source.relative_to(self.root).as_posix(),
                                  "digest": hashlib.sha256(source.read_bytes()).hexdigest()}, pin)
                source.write_bytes(source.read_bytes() + b"changed\n")
                with self.assertRaisesRegex(ReleaseSourceAdmissionError, "source pin is stale"):
                    admission_module._read_pin(self.root, pin)

    def test_declared_owner_path_supersedes_hardcoded_location(self) -> None:
        source = self.source("TOOLS", "CA-D-999")
        old = self.root / admission_module._TOOLS_RMED_ROOTS["deliveries"] / source.name
        old.parent.mkdir(parents=True)
        shutil.copyfile(source, old)
        pin = resolve_current_source_pin(self.root, "CA-D-999", role="Delivery")
        self.assertEqual(source.relative_to(self.root).as_posix(), pin["source_path"])

    def test_exact_active_history_never_becomes_current(self) -> None:
        source = self.source("CONNECTOR_TOOLS", "CA-D-625")
        historical_bytes = source.read_bytes()
        original = historical_bytes.replace(b"version: 2", b"version: 3", 1)
        source.write_bytes(original)
        expected = resolve_current_source_pin(self.root, "CA-D-625", role="Delivery")
        for relative in ("archive/prior@2.md", "archived/prior@2.md", "prior@2.md", "archived/prior.md"):
            with self.subTest(relative=relative):
                historical = source.parent / relative
                historical.parent.mkdir(exist_ok=True)
                historical.write_bytes(historical_bytes)
                self.assertEqual(expected, resolve_current_source_pin(self.root, "CA-D-625", role="Delivery"))
                self.assertEqual(historical_bytes, historical.read_bytes())
                source.unlink()
                with self.assertRaisesRegex(ReleaseSourceAdmissionError, "missing or ambiguous"):
                    resolve_current_source_pin(self.root, "CA-D-625", role="Delivery")
                source.write_bytes(original)
                historical.unlink()

    def test_history_does_not_hide_actual_current_duplicates(self) -> None:
        source = self.source("CONNECTOR_TOOLS", "CA-D-625")
        original = source.read_bytes()
        source.with_name("prior@2.md").write_bytes(original)
        for name in ("duplicate.md", "duplicate@preview.md", "duplicate@0.md", "duplicate@01.md"):
            with self.subTest(name=name):
                duplicate = source.with_name(name)
                duplicate.write_bytes(original)
                with self.assertRaisesRegex(ReleaseSourceAdmissionError, "missing or ambiguous"):
                    resolve_current_source_pin(self.root, "CA-D-625", role="Delivery")
                duplicate.unlink()

    def test_invalid_project_structure_schema_refuses_without_source_changes(self) -> None:
        source = self.source("CONNECTOR_TOOLS", "CA-D-625")
        before = source.read_bytes()
        structure = self.root / ".caprmedio_caprmedio/project_structure.toml"
        original = structure.read_text()
        for text in (original.removeprefix("schema_version = 1\n"),
                     original.replace("schema_version = 1", "schema_version = 99", 1),
                     original.replace("schema_version = 1", "schema_version = true", 1),
                     'unknown = "value"\n' + original, "schema_version = 1\n"):
            with self.subTest(schema=text.splitlines()[0]):
                structure.write_text(text)
                with self.assertRaisesRegex(ReleaseSourceAdmissionError, "registration is invalid"):
                    resolve_current_source_pin(self.root, "CA-D-625", role="Delivery")
                self.assertEqual(before, source.read_bytes())

    def test_invalid_declaration_body_and_tree_refuse_without_source_changes(self) -> None:
        source = self.source("CONNECTOR_TOOLS", "CA-D-625")
        original_source = source.read_bytes()
        structure = self.root / ".caprmedio_caprmedio/project_structure.toml"
        original = tomllib.loads(structure.read_text())
        cases = []
        for field, value in (("scope_unit_type", True), ("scope_unit_type", ["Unordered"]),
                             ("structural_level", 0), ("navigational_order_number", True),
                             ("scope_unit_label", True), ("unexpected_authority", True)):
            document = copy.deepcopy(original)
            row = next(row for row in document["scope_units"] if row["scope_unit_name"] == "CONNECTOR_TOOLS")
            row[field] = value
            cases.append(document)
        missing = copy.deepcopy(original)
        next(row for row in missing["scope_units"] if row["scope_unit_name"] == "CONNECTOR_TOOLS").pop("delivery_path")
        cases.append(missing)
        undeclared_parent = copy.deepcopy(original)
        undeclared_parent["scope_units"] = [row for row in undeclared_parent["scope_units"]
                                           if row["scope_unit_name"] != "PROGRAMMATIC"]
        cases.append(undeclared_parent)
        for document in cases:
            with self.subTest(document=document):
                lines = ["schema_version = 1"]
                for row in document["scope_units"]:
                    lines += ["", "[[scope_units]]"]
                    lines += [f"{field} = {json.dumps(value)}" for field, value in row.items()]
                structure.write_text("\n".join(lines) + "\n")
                before = structure.read_bytes()
                with self.assertRaisesRegex(ReleaseSourceAdmissionError, "registration is invalid"):
                    resolve_current_source_pin(self.root, "CA-D-625", role="Delivery")
                self.assertEqual(original_source, source.read_bytes())
                self.assertEqual(before, structure.read_bytes())

    def test_operations_resolve_registered_workflow_owner(self) -> None:
        source = self.source("TOOL_WORKFLOWS", "CA-O-030", role="Operations", folder="09_operations",
                             operation_type="Action")
        pin = resolve_current_source_pin(self.root, "CA-O-030", role="Operations", operation_type="Action")
        self.assertEqual(source.relative_to(self.root).as_posix(), pin["source_path"])
        with self.assertRaisesRegex(ReleaseSourceAdmissionError, "wrong registered role"):
            resolve_current_source_pin(self.root, "CA-O-030", role="Operations", operation_type="Step")

    def test_terminal_slash_preserves_one_binding_and_duplicate_owner_refuses(self) -> None:
        source = self.source("CONNECTOR_TOOLS", "CA-D-625")
        expected = resolve_current_source_pin(self.root, "CA-D-625", role="Delivery")
        self.owners["CONNECTOR_TOOLS"] += "/"
        self.write_structure()
        structure = self.root / ".caprmedio_caprmedio/project_structure.toml"
        before = structure.read_bytes()
        self.assertEqual(expected, resolve_current_source_pin(self.root, "CA-D-625", role="Delivery"))
        self.assertEqual(before, structure.read_bytes())
        self.assertEqual(expected["digest"], hashlib.sha256(source.read_bytes()).hexdigest())
        self.owners["TOOLS"] = self.owners["CONNECTOR_TOOLS"].removesuffix("/")
        self.write_structure()
        with self.assertRaisesRegex(ReleaseSourceAdmissionError, "registration is invalid"):
            resolve_current_source_pin(self.root, "CA-D-625", role="Delivery")

    def test_duplicate_current_owner_or_registration_refuses(self) -> None:
        self.source("CONNECTOR_TOOLS", "CA-D-625")
        duplicate = self.source("TOOLS", "CA-D-625")
        with self.assertRaisesRegex(ReleaseSourceAdmissionError, "missing or ambiguous"):
            resolve_current_source_pin(self.root, "CA-D-625", role="Delivery")
        duplicate.unlink()
        self.write_structure('\n[[scope_units]]\nscope_unit_name = "CONNECTOR_TOOLS"\n'
                             'parent = "PROGRAMMATIC"\nauthority_path = ".caprmedio_caprmedio/other"\n')
        with self.assertRaisesRegex(ReleaseSourceAdmissionError, "registration is invalid"):
            resolve_current_source_pin(self.root, "CA-D-625", role="Delivery")

    def test_wrong_scope_role_and_inactive_source_refuse(self) -> None:
        source = self.source("CONNECTOR_TOOLS", "CA-D-625")
        original = source.read_text()
        for before, after, diagnostic in (
            ("current_scope_unit: CONNECTOR_TOOLS", "current_scope_unit: TOOLS", "wrong registered scope"),
            ("content_role: Delivery", "content_role: Method", "wrong registered role"),
            ("status: Active", "status: Archived", "missing or ambiguous"),
        ):
            with self.subTest(after=after):
                source.write_text(original.replace(before, after))
                with self.assertRaisesRegex(ReleaseSourceAdmissionError, diagnostic):
                    resolve_current_source_pin(self.root, "CA-D-625", role="Delivery")

    def test_unregistered_scope_is_not_an_authority_fallback(self) -> None:
        self.owners["OTHER"] = ".caprmedio_caprmedio/authoring/OTHER"
        (self.root / self.owners["OTHER"] / "07_delivery").mkdir(parents=True)
        self.source("OTHER", "CA-D-625")
        self.write_structure()
        with self.assertRaisesRegex(ReleaseSourceAdmissionError, "missing or ambiguous"):
            resolve_current_source_pin(self.root, "CA-D-625", role="Delivery")

    def test_unsafe_registered_owner_or_symlink_refuses(self) -> None:
        source = self.source("CONNECTOR_TOOLS", "CA-D-625")
        original_owner = self.owners["CONNECTOR_TOOLS"]
        for owner in ("../outside", ".caprmedio_caprmedio/_projection/copy",
                      ".caprmedio_caprmedio/000_CAPRMEDIO_framework/copy"):
            with self.subTest(owner=owner):
                self.owners["CONNECTOR_TOOLS"] = owner
                self.write_structure()
                with self.assertRaises(ReleaseSourceAdmissionError):
                    resolve_current_source_pin(self.root, "CA-D-625", role="Delivery")
        self.owners["CONNECTOR_TOOLS"] = original_owner
        self.write_structure()
        source.unlink()
        source.symlink_to(self.source("TOOLS", "CA-D-999"))
        with self.assertRaisesRegex(ReleaseSourceAdmissionError, "symlink"):
            resolve_current_source_pin(self.root, "CA-D-625", role="Delivery")
        source.unlink()
        source.parent.rmdir()
        source.parent.symlink_to(self.root / self.owners["TOOLS"] / "07_delivery", target_is_directory=True)
        with self.assertRaisesRegex(ReleaseSourceAdmissionError, "symlink"):
            resolve_current_source_pin(self.root, "CA-D-625", role="Delivery")

    def test_unmaterialized_optional_owners_do_not_create_authority(self) -> None:
        shutil.rmtree(self.root / self.owners["CONNECTOR_TOOLS"])
        source = self.source("PROJECT_TOOLS", "CA-D-999")
        pin = resolve_current_source_pin(self.root, "CA-D-999", role="Delivery")
        self.assertEqual(source.relative_to(self.root).as_posix(), pin["source_path"])
        with self.assertRaisesRegex(ReleaseSourceAdmissionError, "missing or ambiguous"):
            resolve_current_source_pin(self.root, "CA-D-625", role="Delivery")
        shutil.rmtree(self.root / self.owners["TOOLS"] / "07_delivery")
        with self.assertRaisesRegex(ReleaseSourceAdmissionError, "source root is unavailable"):
            resolve_current_source_pin(self.root, "CA-D-999", role="Delivery")


if __name__ == "__main__":
    unittest.main()
