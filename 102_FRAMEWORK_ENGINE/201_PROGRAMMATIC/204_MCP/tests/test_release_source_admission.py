"""Current D572@36 source-admission derivation tests; no manifest writes."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch


MCP = Path(__file__).resolve().parents[1]
REPOSITORY = MCP.parents[2]
sys.path.insert(0, str(MCP))

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


AUTHORITY_REF = admission_module.AUTHORITY_REF


def all_pins(record: dict[str, object]) -> list[dict[str, object]]:
    return [record["acceptance_frontier"], record["workflow"],
            *[pin for row in record["ordered_steps"] for pin in (row["step"], row["action"])],
            *record["ordered_actions"], *record["rmed_frontier"]]


class ReleaseSourceAdmissionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        authority = REPOSITORY / AUTHORITY_REF
        actual = authority.read_bytes()
        pin = admission_module.AUTHORITY_PIN
        if (hashlib.sha256(actual).hexdigest() != pin["digest"]
                or admission_module._metadata(actual) != (pin["atom_id"], pin["version"])):
            raise AssertionError("current D572 does not match the active parser source pin")
        cls.expected = derive_release_source_admission(REPOSITORY)
        cls.private_carriers: list[dict[str, str]] = []

    @staticmethod
    def copy_sources(root: Path) -> None:
        relative_paths = {AUTHORITY_REF,
                          *[pin["source_path"] for pin in all_pins(ReleaseSourceAdmissionTest.expected)]}
        for relative in relative_paths:
            target = root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPOSITORY / relative, target)
        for relative in (admission_module._OPERATIONS_ROOT,
                         *admission_module._RMED_ROOTS.values(),
                         *admission_module._TOOLS_RMED_ROOTS.values()):
            (root / relative).mkdir(parents=True, exist_ok=True)
        for filename in ("project_structure.toml", "caprmedio_project_settings.toml"):
            source = REPOSITORY / ".caprmedio_caprmedio" / filename
            target = root / ".caprmedio_caprmedio" / filename
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)

    def setUp(self) -> None:
        temporary = REPOSITORY / ".caprmedio_tmp/tests/release-source-admission"
        temporary.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=temporary, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.copy_sources(self.root)
        self.record = derive_release_source_admission(self.root)
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

    def test_current_authority_derives_current_ten_phase_record(self) -> None:
        before = self.snapshot()
        self.assertEqual(self.expected, self.record)
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


if __name__ == "__main__":
    unittest.main()
